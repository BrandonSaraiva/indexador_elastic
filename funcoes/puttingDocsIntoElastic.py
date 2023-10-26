import requests
import re
from tika import parser
import json
from elasticsearch import Elasticsearch

def indexar_documentos_no_elasticsearch(json_url, index_name, column_name, host):
    """Indexa documentos no Elasticsearch a partir de um arquivo JSON.

    Args:
        json_url: A URL do arquivo JSON.
        index_name: O nome do índice no Elasticsearch.
        column_name: O nome da coluna que contém os links.
        host: O host do Elasticsearch.
    """

    # Obtem o JSON do arquivo.
    response = requests.get(json_url)

    # Verifica se o JSON foi obtido com sucesso.
    if response.status_code != 200:
        print("\nFalha ao obter o JSON da URL.")
        return

    # Converte o JSON para um objeto Python.
    data = json.loads(response.content)

    # Contador de documentos indexados.
    count = 0

    # Para cada item no JSON, indexa o documento no Elasticsearch.
    for item in data:
        # Obtenha os links do item a partir da coluna fornecida.
        column_values = item.get(column_name, '')
        links = re.findall(r'href=["\'](http[s]?://[^"\']+)["\']', column_values)
        
        # checking if the column_values is a link or a list of links
        has_href = "href" in column_values
        has_http = "http" in column_values

        # in case the column_values is a direct link
        if not has_href and has_http:
            links_separates = column_values.split('\n')
            if links_separates != ['']:
                for link in links_separates:
                    # Obtenha o conteúdo do documento.
                    response = requests.get(link)

                    # Verifica se o documento foi obtido com sucesso.
                    if response.status_code != 200:
                        print("Falha ao obter o documento do link: " + link)
                        continue

                    # Extrai o texto do documento.
                    parsed = parser.from_buffer(response.content)
                    text = parsed['content']

                    # Cria um documento.
                    doc = {
                        "content": text
                    }

                    es = Elasticsearch([host])  # Especifique os hosts do Elasticsearch
                    # indexando o documento
                    response = es.index(index=index_name, body=doc)

                    # Imprimindo o resultado da indexação.
                    print(response)

                    # Verifique se o documento foi indexado com sucesso.
                    if response['result'] == 'created':
                        count += 1
                        print("\nDocumento indexado com sucesso no Elasticsearch.\n")
                        print("=--------------------------------------------------=\n")
                    else:
                        print("\n!Erro ao indexar o documento no Elasticsearch.!\n")
                        print("=--------------------------------------------------=\n")
        else:
            # Para cada link, indexa o documento no Elasticsearch.
            for link in links:
                print("eeee", link)
                # Obtenha o conteúdo do documento.
                response = requests.get(link)

                # Verifica se o documento foi obtido com sucesso.
                if response.status_code != 200:
                    print("Falha ao obter o documento do link: " + link)
                    continue

                # Extrai o texto do documento.
                parsed = parser.from_buffer(response.content)
                text = parsed['content']

                # Cria um documento.
                doc = {
                    "content": text
                }

                es = Elasticsearch([host])  # Especifique os hosts do Elasticsearch
                # indexando o documento
                response = es.index(index=index_name, body=doc)

                # Imprimindo o resultado da indexação.
                print(response)

                # Verifique se o documento foi indexado com sucesso.
                if response['result'] == 'created':
                    count += 1
                    print("\nDocumento indexado com sucesso no Elasticsearch.\n")
                    print("=--------------------------------------------------=\n")
                else:
                    print("\n!Erro ao indexar o documento no Elasticsearch.!\n")
                    print("=--------------------------------------------------=\n")

    # Imprima o total de documentos indexados.
    print("Total de documentos indexados:", count)


