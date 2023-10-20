# Document Indexer for Elasticsearch

This is a project that allows you to index documents in Elasticsearch based on URLs provided in JSON files. It provides flexibility to select a specific column from the JSON data and collect the URL content if that column contains an HTTP link to some document.

## Functionalities

- **Custom Data Collection**: You can specify the JSON URL, the desired column and automate the name of the created indexes.

- **HTTP Content Extraction**: The code will scan the selected column for HTTP URLs and collect all content from those links.

- **Automatic Indexing**: An index in Elasticsearch will be automatically created based on the document URL. Each HTTP URL found in different columns will be treated as a separate document and saved in Elasticsearch.

## Requirements

- In addition to the libraries imported into the code that is available:
- Download tika-server and run it on your system.
- Have the elasticsearch server running on your machine.

## How to use

1. Clone the repository.
2. Install the necessary libraries: EXAMPLE`pip install elasticsearch requests pandas`.
3. Provide the required details in main.py and run.
4. Documents will be indexed in Elasticsearch based on the column URLs specified in the JSON.

# Example of use:

Let's get the document links from the following JSON:

https://sistemas.anac.gov.br/dadosabertos/regulamentacao/Normas%20Publicadas/resolucoes/2022.json

![image](https://github.com/BrandonSaraiva/indexador_elastic/assets/90096835/024fa470-c84a-4d1a-b450-83123545109f)

- Here we can see that the documents link is in the "outros" column, let's specify this for our code:

![image](https://github.com/BrandonSaraiva/indexador_elastic/assets/90096835/4c7f7cc7-6739-454c-afa2-e334034f4fa9)

- Now our code knows which column to scroll through to access the documents link.
---------------------------------------------------------------------------------------

- We can see in the url of our json that after /dadosabertos/ we have the description of what this json stores, we will inform our code so that it can create an index with this information:
- 
![image](https://github.com/BrandonSaraiva/indexador_elastic/assets/90096835/76fc4a11-cc53-49fa-b94e-b7f60f768796)

- See what the name of the index looks like:
![image](https://github.com/BrandonSaraiva/indexador_elastic/assets/90096835/818c057a-fc92-4d32-8282-ff381f5a445b)

------------------------------------------------------------------------------------------------------------
- After providing all the necessary information and having our tika server and elasticsearch server running, we can monitor the results of our indexing:
![image](https://github.com/BrandonSaraiva/indexador_elastic/assets/90096835/b0f379a4-ea1b-4ba7-bab0-ff30217c45c9)

