import requests
import bs4
from rich import print as rprint

# 爬取商品页数据
def get_data(url):
    all_data = []

    session = requests.session()

    headers = {
        'User-Agent': 'Mozilla',
    }

    res = session.get(url, headers = headers)
    soup = bs4.BeautifulSoup(res.text, "html.parser")

    # 获取商品详情的数据DOM
    target = soup.find_all('div', class_="p-parameter")

    goods = ''

    rprint('\t[bold yellow]' + '爬取: '+ url + '......'+ '[/bold yellow]')

    # 将每组数据分割存入数组中
    for item in target:
        goods = item.text.split('\n')

    # 将数据键值对保存
    for item in goods:
        # 去除空数据
        if item != '' and item != '更多参数>>':
            # 保存键
            all_data.append(item.split('：')[0].strip())
            # 保存值
            all_data.append(item.split('：')[1].strip())

    return all_data