price,price2=50,65

print("美式咖啡價格：",price)
print("義式咖啡價格：",price2)

#條件式流程控制,單一條件,單一敘述, <,>,>=,<=,==
if price<price2:
    print("義式咖啡比較貴") #會執行

if price>price2:
    print("美式咖啡比較貴") #不會執行

#單一條件,多重敘述
print("--------------------------------")
if price<price2:
    print("義式咖啡比較貴")
else:
    print("美式咖啡比較貴")


print("--------------------------------")
cp=int(input("請輸入咖啡的價格:"))

#多個條件
if cp<35:
    print("趕快去搶購")
elif cp==50:
    print("讓我想想")
else:
    print("這家咖啡太貴了,呷不起")

print("\n---int()-----------------------------")
num=99.9
print("num",num)
print("num",int(num))

