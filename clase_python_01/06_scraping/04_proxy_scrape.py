import concurrent.futures
import requests
import time
from pprint import pprint
from bs4 import BeautifulSoup
from config import *





def proxy_scrape():

    url = "https://api.proxyscrape.com/v4/free-proxy-list/get?request=display_proxies&proxy_format=protocolipport&format=json"
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        data = response.json()
        elite_proxies = []
        
        # for proxy in data['proxies']:
        #     if proxy.get('anonymity') == 'elite':
        #         city = proxy['ip_data'].get('city')
        #         country = proxy['ip_data'].get('country')

        #         if proxy['anonymity'] == 'elite':
        #             # elite_proxies.append(f"{proxy['ip']}:{proxy['port']}, city:{city}, country:{country}, anonymity:{proxy['anonymity']}")
        #             elite_proxies.append(f"{proxy['ip']}:{proxy['port']}")

        for p in data['proxies']:
            # Guardamos los proxies como diccionarios para mantener la información del protocolo
            if p.get('anonymity') == 'elite':
                elite_proxies.append({
                    "protocol": p['protocol'],
                    "proxy": f"{p['ip']}:{p['port']}"
                })


        # print (f"{WHITE}Proxies obtenidos: {BLUE}{len(elite_proxies)}, {YELLOW}Free Proxy List")
        # pprint(elite_proxies)
        return {"origen": "ProxyScrape:",
                "lista": elite_proxies
               }
    except requests.RequestException as e:
        print(f"Error fetching proxy list: {e}")
        return []
    except Exception as e:
        print(f"Error procesando la respuesta: {e}")
        return []
    
    for key, value in response[proxies].items():
        if value["anonymity"] == "elite":
            proxies.append(proxy)
    return {
        "origen": "ProxyScrape:",
        "lista": proxies
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

    req = proxy_scrape()
    print(f'{WHITE}Proxies obtenidos: {BLUE}{len(req["lista"])}, {req["origen"]}{RESET}')
    proxies.extend(req["lista"])

    req = free_proxie()
    print(f'{WHITE}Proxies obtenidos: {BLUE}{len(req["lista"])}, {req["origen"]}{RESET}')
    proxies.extend(req["lista"])


    # proxies = list(set(proxies))

    # Deduplicar proxies basados en la cadena 'proxy' (ip:port)
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
        print(f"{BLUE} Tiempo por proxy: {WHITE}{seconds / n_proxies_total:.2f} segundos{RESET}")

        pprint(proxies, sort_dicts=False)

        # with open("working_proxies.txt",encoding = "utf-8", mode="w") as f:
        #     f.write("\n".join(proxies))

        proxies_to_save = [f"{p['protocol']}://{p['proxy']}" for p in proxies]
        with open("working_proxies.txt", encoding="utf-8", mode="w") as f:
            f.write("\n".join(proxies_to_save))
    else:
        print(f"{RED}No se encontraron proxies válidos.{RESET}")



     
    # print(f"{GREEN}Proxies{CYAN}: {proxies}{RESET}")
    print(f"{MAGENTA}TOTAL: {n_proxies_total}{RESET}")
    print(f"{YELLOW}Tiempo total: {time.time() - start} segundos{RESET}")
