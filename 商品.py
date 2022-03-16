import json

from time import strftime,sleep

import requests


def pupu_market():
    url='https://j1.pupuapi.com/client/product/storeproduct/detail/4dcdeca2-f5a3-4be8-9e2f-e099889a23a0/b15e1173-1b43-4eb2-8055-b78cb4d3a033'
    head={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
    }
    reque=requests.get(url,headers=head)
    sold=json.loads(reque.text)
    #定义价格
    price=sold['data']['price']/100
    price=str(price)
    #定义规格
    spec=sold['data']['spec']
    spec=str(spec)
    #定义原价/折扣价（不打折）
    original_price=sold['data']['market_price']/100
    original_price=str(original_price)
    #定义详细内容
    detail=sold['data']['share_content']

    print('---------------商品:长富巴氏鲜奶221ml---------------')
    print('规格:'+spec)
    print('价格:'+price+'元')
    print('原价/折扣价:' + original_price+'元'+'/'+original_price+'元')
    print('详细内容:'+detail)

    # 异常处理
    try:
        while (True):
            nowtime = strftime('%Y' + '-' + '%m' + '-' + '%d' + ' %H:%M:%S,价格为' + price +'元')
            print(nowtime)
            sleep(3)
    except:
        print("程序结束")

if __name__ == '__main__':
    pupu_market()