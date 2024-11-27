#滙入自訂模組
import Unit0201Coffee as coffee
from shop.product import items 


#使用Unit0201Coffee 模組內的自訂函數
coffee.favorite("藝伎")
coffee.sale("美式咖啡",150,10)

print('\n------呼叫product 模組之items()--------------------')
items("美式咖啡","藝伎咖啡豆","衣索比亞咖啡豆")




