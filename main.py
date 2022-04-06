import requests
from bs4 import BeautifulSoup


def get_url(url):
    response = requests.get(url, headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36"})
    return response


def get_other_urls(url, added_sites):
    response = get_url(url)
    soup = BeautifulSoup(response.text, "html.parser")
    all_a = soup.find_all("a")

    sites_to_check = []
    site_name = url.split("/")[2]
    print("****************")
    print(f"Сейчас парсится {url} ...")
    added_sites.append(site_name)

    for a in all_a:
        a_url = a.get("href")

        if a_url is None:
            continue

        if "http" in a_url.split("/")[0]:
            site_name = a_url.split("/")[2]
            if site_name in added_sites:
                continue
            else:
                sites_to_check.append(a_url)
                added_sites.append(site_name)

    print("Все ссылки с этого сайта:")
    if not sites_to_check:
        print("Нету ссылок")
    else:
        for site in sites_to_check:
            print(site)
        for site in sites_to_check:
            try:
                get_other_urls(site, added_sites)
            except Exception:
                continue


def main():
    get_other_urls("https://proglib.io/p/top-20-besplatnyh-resursov-dlya-izucheniya-python-sohrani-eto-v-zakladki-2021-01-08", [])


if __name__ == '__main__':
    main()