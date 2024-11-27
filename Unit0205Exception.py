'''
例外
Exception
'''

import os

i=10
print(f'i={i}')

#j=10
#print(f'j={j}') #NameError: name 'j' is not defined

#print('hello')  #若前述發生Error, 此行不會執行

#Exception 區塊
try:
    print(f'j={j}')
except:
    print("變數未定義!!")

print("hello")

#----------------------------------
#os.mkdir("myfolder")   #建立資料夾

try:
    os.rmdir("myfolder")    #刪除資料夾
    print("myfolder 資料夾已被刪除")
except:
    print("找不到myfolder 資料夾")


print("hello2")