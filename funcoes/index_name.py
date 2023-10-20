import re
from urllib.parse import urlparse

def formatar_nome_indice_a_partir_url(json_url, split_condition):
    # Use a biblioteca urllib.parse para obter a parte do caminho da URL após "dadosabertos/"
    parsed_url = urlparse(json_url)
    path_after_condition = parsed_url.path.split(split_condition)[1]

    # Remova espaços
    path_cleaned = re.sub(r'%20', '_', path_after_condition)

    # tirando o .json
    path_cleaned = path_cleaned.replace(".json", "")

    # Substitua barras por underscores
    index_name = path_cleaned.replace("/", "_")
    
    return index_name
