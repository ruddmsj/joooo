#파이썬에서는 모든 변수는 해당 객체의 주소를 가지고 있다.
#a=1이라고 하면은 1이라는 객체를 생성한 후 a라는 변수에 1이란 객체의 주소가 저장되는 것이다

#예를 들면
a = [1,2,3]
b = a
a[0] = 4
print(a)
print(b)
#위의 소스에서 a에는 간단한 리스트 객체가 생성 되고 b에 a의 객체가 복사 되는 것으로 생각 할수 있지만
#사실 a에는 [1,2,3]객체의 주소가 저장되는 것이며 b에는 그 주소가 복사 되는 것이다

#그래서 b에 같은 객체를 공유하지 않게 하려면 a의 값을 강제로 복사하여야 한다

a = [1,2,3]
b = a[:]
a[0] = 4
print(a,b)

#리스틍 이외의 일반적인 경우에는 copy모듈을 사용한다

#copy()함수는 주소가 복사되어 객체를 공유하는 얕은 복사
#deepcopy()함수는 객체를 공유하지 않는 깊은 복사이다

import copy
a = [1,2,3]
b = copy.copy(a)
c = copy.deepcopy(a)
a[0] = 4
print(a,b,c)

a = [1,[2,3]]
b = copy.copy(a)
c = copy.deepcopy(a)

print(a,b,c)
print(id(a), id(b), id(c))

a[1].append(4)
print(a,b,c)
print(id(a[1]), id(b[1]), id(c[1]))

