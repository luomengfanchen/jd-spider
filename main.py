from xl import save_data
from data import get_data
from url import get_url
from rich import print as rprint

# 获取搜索的关键字
key = input("请输入京东要搜索的关键字: ")
all_goods_data = []

# 爬取前十页的数据
for index in range(10):
    url_path = "https://search.jd.com/Search?keyword=" + key + "&page=" + str(index)

    # 获取商品页链接
    href_url = get_url(url_path)

    rprint('[bold blue]' + '>>>第' + str(index + 1) + '页爬取中......' + '[/bold blue]')

    # 将爬取的数据放入数组中
    for item in href_url:
        all_goods_data.append(get_data(item))
    
    rprint('[bold blue]' + '>>>第' + str(index + 1) + '页内容爬取完毕!\n\n' + '[/bold blue]')

# 将数据保存到excel表格中
save_data(all_goods_data)