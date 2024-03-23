import requests

def make_api_request(api_key, url):
    """
    Faz uma solicitação à API usando a chave de API fornecida.
    
    Args:
        api_key (str): A chave de API para autenticação.
        url (str): O URL da API.
        
    Returns:
        dict: Os dados da resposta da API em formato JSON.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lança exceção para erros de solicitação
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Erro ao fazer a solicitação à API: {e}")
        return None

