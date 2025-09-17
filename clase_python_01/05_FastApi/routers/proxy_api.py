from fastapi import APIRouter


import requests
import time
from bs4 import BeautifulSoup
import concurrent.futures
from pprint import pprint

# Definición de colores ANSI
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"
RESET = "\033[0m"


# Headers para las peticiones
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}


router = APIRouter(prefix="/proxy",
                   tags=["proxy"],
                   responses={404: {"message": "No encontrado"}})








def proxy_scrape():
    url = "https://api.proxyscrape.com/v4/free-proxy-list/get?request=display_proxies&proxy_format=protocolipport&format=json"
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        data = response.json()
        elite_proxies = []
        
        for p in data['proxies']:
            if p.get('anonymity') == 'elite':
                elite_proxies.append({
                    "protocol": p['protocol'],
                    "proxy": f"{p['ip']}:{p['port']}"
                })

        return {
            "origen": "ProxyScrape:",
            "lista": elite_proxies
        }

    except requests.RequestException as e:
        print(f"Error fetching proxy list: {e}")
        return {
            "origen": "ProxyScrape:",
            "lista": []
        }
    except Exception as e:
        print(f"Error procesando la respuesta: {e}")
        return {
            "origen": "ProxyScrape:", 
            "lista": []
        }


def free_proxie():

    r = requests.get("https://free-proxy-list.net/", headers=HEADERS, timeout=10)

    soup = BeautifulSoup(r.text, "html.parser")
    lines = soup.find("tbody").find_all("tr")
    proxies = []
    for line in lines:
        values = line.find_all("td")
        # print(values)
        proxy_ip = values[0].text
        proxy_port = values[1].text
        proxy_country = values[3].text
        proxy_anonymity = values[4].text
        proxy_https = values[6].text     



        if proxy_anonymity == "elite proxy":
            # # proxy = f'{proxy_ip}:{proxy_port}, country: {proxy_country}'
            # proxy = f'{proxy_ip}:{proxy_port}'
            # proxies.append(proxy)

            protocol = "https" if proxy_https == "yes" else "http"
            proxies.append({
                "protocol": protocol,
                "proxy": f'{proxy_ip}:{proxy_port}'
            })
    # print (f"{WHITE}Proxies obtenidos: {BLUE}{len(proxies)}, {YELLOW}Free Proxy List{RESET}")
    # pprint(proxies)

    return {
        "origen": "Free Proxy List:",
        "lista": proxies
    }
    # return print(proxies)

def proxie_to_list():
    proxies = []

    # Obtener proxies de ProxyScrape
    req = proxy_scrape()
    if isinstance(req, dict) and "lista" in req:  # Verificar que req sea un diccionario válido
        print(f'{WHITE}Proxies obtenidos: {BLUE}{len(req["lista"])}, {req["origen"]}{RESET}')
        proxies.extend(req["lista"])
    else:
        print(f'{RED}Error obteniendo proxies de ProxyScrape{RESET}')

    # Obtener proxies de Free Proxy List
    req = free_proxie()
    if isinstance(req, dict) and "lista" in req:  # Verificar que req sea un diccionario válido
        print(f'{WHITE}Proxies obtenidos: {BLUE}{len(req["lista"])}, {req["origen"]}{RESET}')
        proxies.extend(req["lista"])
    else:
        print(f'{RED}Error obteniendo proxies de Free Proxy List{RESET}')

    # Deduplicar proxies
    unique_proxies = {}
    for p in proxies:
        unique_proxies[p['proxy']] = p
    
    proxies = list(unique_proxies.values())
    return proxies

def try_proxies(proxy_info, url):
    output = {
        "proxy": proxy_info['proxy'],
        "timeout": None,
        "response": None
    }
    try:
        protocol = proxy_info['protocol']
        proxy_str = proxy_info['proxy']
    
        proxies = {
            "http": f"{protocol}://{proxy_str}",
            "https": f"{protocol}://{proxy_str}"
        }
        start_time = time.time()

        response = requests.get(url, proxies=proxies, timeout=5)
        output["timeout"] = time.time() - start_time
        output["response"] = response.status_code

    except requests.exceptions.RequestException as e:
        output["response"] = str(e.__class__.__name__)
    return output


def filter_proxies(proxies):
    working_proxies = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        # for proxy in proxies:
        #     futures.append(executor.submit(try_proxies, proxy, "https://httpbin.org/ip"))

        for proxy_info in proxies:
            futures.append(executor.submit(try_proxies, proxy_info, "https://httpbin.org/ip"))


        for future in concurrent.futures.as_completed(futures):
            res = future.result()
            if res["response"] == 200:
                # working_proxies[proxy] = res["timeout"]
                # print(f"{GREEN}Proxy {proxy} is working, response time: {res['timeout']:2f} seconds{RESET}")
                original_proxy_info = next((p for p in proxies if p['proxy'] == res['proxy']), None)
                if original_proxy_info:
                    working_proxy = {
                        "proxy": res["proxy"],
                        "protocol": original_proxy_info['protocol'],
                        "timeout": res['timeout']
                    }
                    working_proxies.append(working_proxy)
                    print(f"{GREEN}Proxy {res['proxy']} ({original_proxy_info['protocol']}) is working, response time: {res['timeout']:.2f} seconds{RESET}")
            else:
                # print(f"{RED}Proxy {proxy} failed, response: {res['response']}{RESET}")
                print(f"{RED}Proxy {res['proxy']} failed, response: {res['response']}{RESET}")  
    if working_proxies:
        #working_proxies = dict(sorted(working_proxies.items(), key=lambda item: item[1]))

        working_proxies = sorted(working_proxies, key=lambda item: item['timeout'])
    return working_proxies
    



if __name__ == "__main__":
    start = time.time()
    print(f"{BLUE}Iniciando la recolección de proxies...{RESET}")
    proxies = proxie_to_list()
    n_proxies_total = len(proxies)
    print(f'{BLUE}Probando {WHITE} {n_proxies_total} {BLUE} proxies...{RESET}')
    proxies = filter_proxies(proxies)
    n_proxies_total = len(proxies)
    print(f'{GREEN}Proxies válidos encontrados: {n_proxies_total}{RESET}')

    if n_proxies_total > 0:
        print(f'{CYAN}Proxies válidos: {n_proxies_total}{RESET}')
        seconds = time.time() - start
        print(f"{YELLOW}Tiempo total: {seconds:.2f} segundos{RESET}")
        print(f"{BLUE} Tiempo por proxy: {WHITE}{seconds / n_proxies_total:.2f} segundos{BLUE}")

        pprint(f'{proxies} {RESET}', sort_dicts=False)

        # with open("working_proxies.txt",encoding = "utf-8", mode="w") as f:
        #     f.write("\n".join(proxies))

        # proxies_to_save = [f"{p['protocol']}://{p['proxy']}" for p in proxies]
        # with open("working_proxies.txt", encoding="utf-8", mode="w") as f:
        #     f.write("\n".join(proxies_to_save))
    else:
        print(f"{RED}No se encontraron proxies válidos.{RESET}")



     
    # print(f"{GREEN}Proxies{CYAN}: {proxies}{RESET}")
    print(f"{MAGENTA}TOTAL: {n_proxies_total}{RESET}")
    print(f"{YELLOW}Tiempo total: {time.time() - start} segundos{RESET}")



@router.get("/")
async def proxies():
    proxies = proxie_to_list()
    n_proxies_total = len(proxies)
    working_proxies = filter_proxies(proxies)
    n_proxies_working = len(working_proxies)

    if n_proxies_working > 0:
        return {
            "total_proxies": n_proxies_total,
            "working_proxies": n_proxies_working,
            "proxies": working_proxies
        }
    else:
        return {
            "total_proxies": n_proxies_total,
            "working_proxies": 0,
            "proxies": []
        }