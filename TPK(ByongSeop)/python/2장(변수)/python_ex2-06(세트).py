#세트는 집합과 동일하다
#리스트와 마찬가지로 값의 모임이며 순서는 없다

#세트의 생성

a = {1,2,3}
b = {3,4,5}
print(a,b)
print(type(a))

#합집합
print(a.union(b))
print(a|b)

#교집합
print(a.intersection(b))
print(a&b)

#차집합
print(a-b)