#List 容器
#串列,清單或列表
#其他語言,Array(陣列)
#串列的資料,稱為元素
#每個元素以「,」 隔開

#宣告容器
coffee=['美式','義式','拿鐵','卡布']

print(coffee)

print('\n-------狂賀台灣棒球,世界第一,以下咖啡飲品買一送一-------------')
print(coffee[0])    #索引值為0開始
print(coffee[1])
print(coffee[2])
print(coffee[3])
#print(coffee[4])   #IndexError: list index out of range,索引值超出範圍

#走訪list 元素(element)
print('\n---------走訪list 元素---------------------')
for e in coffee:
    print(e)

qty=[10,20,30,25]
total=0
print('\n1~4季銷售數量：')
for e in qty:
    total +=e
    print(e)

print("今年度咖啡的銷售總數量為 ", total ,' 萬杯')

