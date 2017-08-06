#재귀적 함수 호출이란
#함수 내부에서 자기 자신을 호출 하는 것을 말한다

#예를 들면
def factorial(x):
    if x == 1:
        return 1
    return x*factorial(x-1)
print(factorial(10))