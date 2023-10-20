from funcoes.puttingDocsIntoElastic import indexar_documentos_no_elasticsearch

from funcoes.index_name import formatar_nome_indice_a_partir_url

def main():
    # Coloque aqui o URL do arquivo JSON
    json_url = "https://sistemas.anac.gov.br/dadosabertos/regulamentacao/Normas%20Publicadas/resolucoes/2022.json"

# apartir depois de qual ponto do url que voce quer pegar o nome do index
    split_point = "dadosabertos/"

# FIltrando o nome da url
    index_name = formatar_nome_indice_a_partir_url(json_url, split_point)

    # putting the index_name to lower case
    index_name = index_name.lower()

    print("\nNome do index: ", index_name);

    # Coluna que contem os links para os documentos
    column_name = "outros"

    # http do seu servid Elasticsearch
    elastic_host = "http://localhost:9200"

    # Indexando os documentos no Elasticsearch
    indexar_documentos_no_elasticsearch(json_url, index_name, column_name, elastic_host)

if __name__ == "__main__":
    main()
