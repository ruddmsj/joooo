#파이썬에서는 api문서를 찾아 볼 필요 없이 help함ㅅ로 어떤 값을 매개변수로 받는지 어떤 값을 반환 하는지 알수 있다

#print 함수의 document를 요청

help(print)

#자신이 만든 함수에서도 help를 사용할 수 있다

def plus(a,b):
    return a+b

help(plus)

#생성한 함수에 대해서 더 자세한 설명을 넣고 싶다면 __doc__속성을 이용하면 된다
#__doc__속성에 설명을 직접 적을 수도 있지만 함수가 시작하는 부분에 "", """를 이용해서 설명을 석으면 함수 객체가 생성 될때
#자동으로 적은 내용이 저장

def factorial(x):
    """Return the factorial of n, an exact integar >=0,
    factorial(6)"""
    if x == 1:
        return 1
    return x*factorial(x-1)
help(factorial)