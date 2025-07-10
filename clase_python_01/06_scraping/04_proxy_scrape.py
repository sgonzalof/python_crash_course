import requests


def list_proxies():
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"}
    url = "https://api.proxyscrape.com/v4/free-proxy-list/get?request=display_proxies&proxy_format=protocolipport&format=text"
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        proxies = response.text.splitlines()
        return proxies
    except requests.RequestException as e:
        print(f"Error fetching proxy list: {e}")
        return []
    


def extract_elite_proxies():
    elite_proxies = []
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"}
    url = "https://api.proxyscrape.com/v4/free-proxy-list/get?request=get_proxies&skip=0&proxy_format=protocolipport&format=json&limit=15"
    response = requests.get(url, headers=headers, timeout=10)
    datos = response.json()
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        datos = response.json()
        for key, value in datos["proxies"].items():
            if value["annonymity"] == "elite":
                elite_proxies.append(f"{value['protocol']}://{value['ip']}:{value['port']}")
    except requests.RequestException as e:
        print(f"Error fetching elite proxy list: {e}")
    return elite_proxies


print(extract_elite_proxies())