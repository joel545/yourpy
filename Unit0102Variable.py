#宣告變數
coffee="美式咖啡"   #coffee 變數名稱，美式咖啡 為變數的值, = 為指定或指派運算子, 將"美式咖啡"指定給coffee 變數
price=45
bean='阿拉比卡'

#----------------------------------------
#同一行,指定多個變數的值
coffee2,price2,bean2="卡布奇諾",55,'耶加雪菲'

#---------------------------------
#單一值,指定給多個變數
price3=price4=price5=60

#-------------------
#刪除變數
coffee3='義式咖啡'


print("coffee=",coffee)
print("price=",price)
print("bean=",bean)

print("------------------------")
print("coffee2=",coffee2)
print("price2=",price2)
print("bean2=",bean2)


print("------------------------")
print("price3=",price3)
print("price4=",price4)
print("price5=",price5)

print("------------------------")
print("coffee3=",coffee3)

#刪除變數
del coffee3
#print("coffee3=",coffee3) #NameError: name 'coffee3' is not defined. Did you mean: 'coffee'?,因為coffee3 已被刪除