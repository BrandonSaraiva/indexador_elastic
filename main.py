from funcoes.puttingDocsIntoElastic import indexar_documentos_no_elasticsearch

from funcoes.index_name import formatar_nome_indice_a_partir_url

from funcoes.modal import modal_input_infos

def main():
    info = {
        "UrlJson": "https://sistemas.anac.gov.br/dadosabertos/fiscalizacao/decisoes-monocraticas-de-processos-em-segunda-instancia/2022/2022.json",

        "IndexName": "nome do index aqui",
        
        "ColumnName": "nome da coluna aqui"
    }

    infos_atts = modal_input_infos(info)
    
# FIltrando o nome da url

    # http do seu servid Elasticsearch
    elastic_host = "http do seu elastic aqui"


    # Indexando os documentos no Elasticsearch
    indexar_documentos_no_elasticsearch(infos_atts["UrlJson"], infos_atts["IndexName"], infos_atts["ColumnName"], elastic_host)

if __name__ == "__main__":
    main()
