import requests as req
from openpyxl import Workbook

wb = Workbook()
ws = wb.active
# 設定表格項目標題
title = ['產品名稱(product_name)', '價格(price)', '最低價格(price_min)', '最高價格(price_max)']
ws.append(title)

# 設定網站爬取權限(變更瀏覽器存取)
header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}

# 爬取網站每一頁的內容
for index in range(50):
    url = "https://shopee.tw/api/v4/search/search_items?by=relevancy&fe_categoryids=11041645&limit=60&newest=" + str(index) + "&order=desc&page_type=search&scenario=PAGE_CATEGORY&version=2"
    print(url)
    r = req.get(url, headers=header)

    # 轉成json格式
    root_json = r.json()

    # 用迴圈抓取items裡面的標籤
    for items in root_json['items']:
        product = []
        product.append(items['item_basic']['name'])
        # 蝦皮價格(不知道為啥)都要除以10萬
        product.append(items['item_basic']['price']/100000)
        product.append(items['item_basic']['price_min']/100000)
        product.append(items['item_basic']['price_max']/100000)

        ws.append(product)

wb.save('shopee.xlsx')