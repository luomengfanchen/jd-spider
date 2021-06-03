from xl import save_data
from data import get_data
from url import get_url
from rich import print as rprint

key = input("请输入京东要搜索的关键字: ")
all_goods_data = []

for index in range(10):
    url_path = "https://search.jd.com/Search?keyword=" + key + "&page=" + str(index)

    href_url = get_url(url_path)

    rprint('[bold blue]' + '>>>第' + str(index + 1) + '页爬取中......' + '[/bold blue]')

    for item in href_url:
        all_goods_data.append(get_data(item))
    
    rprint('[bold blue]' + '>>>第' + str(index + 1) + '页内容爬取完毕!\n\n' + '[/bold blue]')

save_data(all_goods_data)