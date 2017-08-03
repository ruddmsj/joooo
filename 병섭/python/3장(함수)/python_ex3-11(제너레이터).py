#제너레이터(generators)는 이터레이너(iterator)를 만드는 간단하고도 강력한 도구이다
#함수와 비슷하게 생겼지만 return대신에 yield를 사용

#함수의 동작 원리는 함수가 호출 되면 지역변수와 코드가 스택에 적재되고 코드를 실행
#함수가 끝나면 결과를 호출한 곳에 넘겨주고 함수 객체는 스택에서 사라진다

#제너레이터는 yield라 적힌 곳에서 잠시 멈추고 호출한 곳에 값을 전달
#호출한 곳에서 next()함수를 실행하면 제네레이터는 중단된 위치로부터 다시 시작하며
#제너레이터는 중단된 위치로 부터 모든 데이터와 마지막에 실행된 명령문을 유지하고 있다

#예제

def reverse(data):
    for index in range(len(data)-1,-1,-1):
        yield data[index]

for char in reverse('golf'):
    print(char)

a = [1,2,3,4,5,6,7,8,9]
print(sum(a))
b = (i for i in range(10))
print(b)
print(sum(b))

#enumerate는 파이썬 만의 독특한 내장 함수로써 순회 가능한 객체로 부터 인덱스 값과 요소 값을 모두 반환 한다

def Fibonaci():
    a,b = 0,1
    while 1:
        yield a
        a, b = b, a+b
for i, ret in enumerate(Fibonaci()):
    if i<20: print(i,ret)
    else :break