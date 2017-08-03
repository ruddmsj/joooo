#파이썬에서 인자는 레퍼런스를 이용해 전달
#함수의 인자는 호출자 내부 객체의 레퍼런스 이다

#호출자가 전달하는 변수가 변경 가능한 변수(Mutable)일 때와 변경이 불가능한 변수(Immutable)일때 내부에서 처리하는 방식이 달라
#call by reference와는 다르다

#변경 불가능한 변수 일때(ex 정수형 변수)
a = 10
b = 20

def sum1(x,y):
    return x+y
print(sum1(a,b))

x = 10
def sum2(x,y):
    x=1
    return x+y
print(sum2(x,b))
print(x)

#변경 가능한 변수 일때(ex 리스트)

def change(x):
    x[0] = 'h'
word = ['j','a','m']
change(word)
print(word)

#변경 가능한 객체의 값을 바꾸면 그 객체를 참조하는 다른 레퍼런스도 영향을 받게 된다