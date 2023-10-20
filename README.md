# Document Indexer para Elasticsearch

Este é um projeto que permite indexar documentos no Elasticsearch com base nas URLs fornecidas em arquivos JSON. Ele oferece flexibilidade para selecionar uma coluna específica dos dados JSON e coletar o conteúdo da URL se essa coluna contiver um link HTTP para algum documento.

## Funcionalidades

- **Coleta de Dados Personalizada**: Você pode especificar a URL do JSON, a coluna desejada e outros detalhes como o host do seu elastic.

- **Extração de Conteúdo HTTP**: O código verificará a coluna selecionada em busca de URLs HTTP e coletará todo o conteúdo desses links.

- **Indexação Automática**: Um índice no Elasticsearch será criado automaticamente com base na URL do documento. Cada URL HTTP encontrada em colunas diferentes será tratada como um documento separado e salvo no Elasticsearch.

## Requisitos

- Além das bibliotecas importadas no código que está diponivel:
- Baixar o tika-server e rodar no seu sistema.
- Ter o servidor do elasticsearch rodando na sua maquina.

## Como Usar

1. Clone o repositório.
2. Instale as bibliotecas necessárias: EXEMPLO`pip install elasticsearch requests pandas`.
3. Forneça os detalhes necessários na main.py e execute.
4. Os documentos serão indexados no Elasticsearch com base nas URLs das colunas especificadas no JSON.

# Exemplo de uso:

Vamos pegar os links de documentos do seguinte JSON:

https://sistemas.anac.gov.br/dadosabertos/regulamentacao/Normas%20Publicadas/resolucoes/2022.json
![image](https://github.com/BrandonSaraiva/indexador_elastic/assets/90096835/024fa470-c84a-4d1a-b450-83123545109f)
Aqui podemos ver que o link dos documentos se encontra na coluna outros, vamos especificar isso para o nosso código:
![image](https://github.com/BrandonSaraiva/indexador_elastic/assets/90096835/4c7f7cc7-6739-454c-afa2-e334034f4fa9)
Agora nosso código sabe qual coluna deve percorrer para acessar o link dos documentos.
---------------------------------------------------------------------------------------
Podemos ver na url de nosso json que após o /dadosabertos/ temos a descriçao do que esse json armazena, iremos informar isso ao nosso codigo para ele criar um index com essa informaçao:
![image](https://github.com/BrandonSaraiva/indexador_elastic/assets/90096835/76fc4a11-cc53-49fa-b94e-b7f60f768796)
Veja como ficou o nome do index:
![image](https://github.com/BrandonSaraiva/indexador_elastic/assets/90096835/818c057a-fc92-4d32-8282-ff381f5a445b)

------------------------------------------------------------------------------------------------------------
Dps de informar todas as informações necessárias e estar com nosso tika server e elasticsearch server rodando, podemos acompanhar o resultado de nossa indexão:
![image](https://github.com/BrandonSaraiva/indexador_elastic/assets/90096835/b0f379a4-ea1b-4ba7-bab0-ff30217c45c9)

