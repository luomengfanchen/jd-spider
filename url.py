import requests
import bs4

# 获取搜索页的中的商品页链接
def get_url(url_path):
    all_a_href = []

    session = requests.session()
    headers = {
        'User-Agent': 'Mozilla',
    }

    res = session.get(url_path, headers = headers)
    soup = bs4.BeautifulSoup(res.text, "html.parser")

    # 获取页面的的链接DOM
    target = soup.find_all('div', class_="p-name p-name-type-2")

    # 将链接存入数组中
    for item in target:
        all_a_href.append('https:' + item.a["href"])

    return all_a_href