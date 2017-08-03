#순회 도중에 break를 만나면 반복문의 내부 블록을 벗어난다

L = [1,2,3,4,5,6,7,8,9]
for i in L:
    if i>5:
        break
    print(i)

#순회 도중 continue문을 만나면 continue 이후의 반보문 내부 블록을 수행하지 않고 다음 아이템을 선택한다

L = [1,2,3,4,5,6,7,8,9]
for i in L:
    if i%2 == 0:
        continue
    print("Item:{0}".format(i))

#for나 while문에서 break로 인해 중간에 종료 되지 않고 끝까지 수행 됬을때 else블록이 수행

L = [1,2,3,4,5,6,7,8,9,10]
for i in L:
    if i%2 == 0:
        continue
    print("Item:{0}".format(i))
else:
    print("Exit without break")
print("Always this is  printed")

L = [1,2,3,4,5,6,7,8,9,10]
for i in L:
    if i%2 == 0:
        break
    print("Item:{0}".format(i))
else:
    print("Exit without break")
print("Always this is  printed")