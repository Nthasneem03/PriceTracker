import requests
from bs4 import BeautifulSoup

products = [
    {
        'prod_url' : 'https://www.snapdeal.com/product/apnisha-navy-blue-chiffon-saree/8070451153965737690#bcrumbLabelId:176'  ,
        'name': 'Saree',
       'target_price': 600
    },
    {
        'prod_url': 'https://www.snapdeal.com/product/amiras-indian-ethnic-wear-rayon/623589687220#bcrumbLabelId:2591',
        'name': 'Salwar set',
        'target_price':700
    },
    {
        'prod_url': 'https://www.snapdeal.com/product/kedar-fab-black-net-circular/636751463471#bcrumbLabelId:417',
        'name': 'Lehenga',
        'target_price':600
    },{
        'prod_url': 'https://www.snapdeal.com/product/hetsa-rust-cotton-blend-straight/8070451202323575926#bcrumbLabelId:4589' ,
        'name': 'Kurti Top',
        'target_price':300
    },
     {
        'prod_url': 'https://www.snapdeal.com/product/ctmtex-green-rayon-womens-anarkali/8070451198612259353' ,
        'name': 'Anarkali Top',
        'target_price':400
    }
]

def give_product_price(URL):
    headers = {
        "User_Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
    }
    page = requests.get(URL,headers=headers)
    soup = BeautifulSoup(page.content,'html.parser')
    price = soup.find(class_="payBlkBig")
    return price.getText()

result_file = open('result_file.txt','w')

try:
    for every_product in products:
        product_price_returned = give_product_price(every_product.get('prod_url'))
        print("Rupees "+ product_price_returned + "/- for " + every_product.get('name'))

        my_product_price = int(product_price_returned)

        print(my_product_price)
        if my_product_price < every_product.get('target_price'):
            print("Available at your required price")
            result_file.write(every_product.get("name") + ' -  \t' + ' Available at Target Price \t' + ' Current Price - ' + str(my_product_price) + '\n')

        else:
            print("Still at current price")

finally :
    result_file.close()




