#튜플은 리스트와 유사하지만 리스트와 달리 ()로 묶어서 표현 하며 읽기 전용이다
#제공되는 함수가 적은 반면 속도가 빠르다

#튜플의 생성

a = (1,2,3)
print(a,type(a))

#튜플이 제공하는 함수는 count()와 index()정도이다
#swap예제를 다음과 같이 쉽게 할 수 있다

a,b = (1,2)
print(a,b)
a,b = b,a
print(a,b)

#리스트, 세트, 튜플은 다음과 같이 생성자 list(),tuple(),set()로 서로서로 언제든지 변환이 가능하다

a = set((1,2,3))
print(a,type(a))
b = list(a)
print(b, type(b))
c = tuple(b)
print(c, type(c))
d = set(c)
print(d, type(d))

#이 모든 자료형들은 in 연산자를 사용 할 수 있다

print(1 in a)
print(2 in b)
print(3 in c)
print(4 in a)
