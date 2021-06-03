import requests
import bs4

def get_url(url_path):
    all_a_href = []

    session = requests.session()
    headers = {
        'User-Agent': 'Mozilla',
    }

    res = session.get(url_path, headers = headers)
    soup = bs4.BeautifulSoup(res.text, "html.parser")

    target = soup.find_all('div', class_="p-name p-name-type-2")

    # target = soup.find_all('div', class_="p-price")
    # for item in target:
    #     print(item.i.text)

    for item in target:
        all_a_href.append('https:' + item.a["href"])

    return all_a_href