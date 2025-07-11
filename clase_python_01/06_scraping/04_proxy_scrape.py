import requests
import time
from pprint import pprint
from bs4 import BeautifulSoup


HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
    }

def list_proxies_proxyscrape():

    url = "https://api.proxyscrape.com/v4/free-proxy-list/get?request=get_proxies&skip=0&proxy_format=protocolipport&format=json"
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        proxies = response.text.splitlines()
        return proxies
    except requests.RequestException as e:
        print(f"Error fetching proxy list: {e}")
        return []
    


def free_proxie_list():
    r = requests.get("https://free-proxy-list.net/", headers=HEADERS, timeout=10)

    soup = BeautifulSoup(r.text, "html.parser")
    lines = soup.find("tbody").find_all("tr")
    proxies = []
    for line in lines:
        values = line.find_all("td")
        # print(values)
        proxy_ip = values[0].text
        proxy_port = values[1].text
        proxy_type = values[4].text

        if proxy_type == "elite proxy":
            proxy = f'{proxy_ip}:{proxy_port}'
            proxies.append(proxy)

    return {
        "origen": "Free Proxy List:",
        "lista": proxies
    }






print(free_proxie_list())