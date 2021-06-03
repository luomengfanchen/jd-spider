import requests
import bs4
from rich import print as rprint

def get_data(url):
    all_data = []

    session = requests.session()

    headers = {
        'User-Agent': 'Mozilla',
    }

    res = session.get(url, headers = headers)
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    target = soup.find_all('div', class_="p-parameter")

    goods = ''

    rprint('\t[bold yellow]' + '爬取: '+ url + '......'+ '[/bold yellow]')

    for item in target:
        goods = item.text.split('\n')

    for item in goods:
        if item != '' and item != '更多参数>>':
            all_data.append(item.split('：')[0].strip())
            all_data.append(item.split('：')[1].strip())

    return all_data