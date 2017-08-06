#함수는 이름없이 객체만 있을 뿐이며 기본 레퍼런스를 이름이라고 말하고 있다
#파이썬에서는 이름이 없고 함수 객체만 존재하는 익명 함수를 만들 수 있다

#익명 함수(람다 함수 Lambda)는 필요한 곳 어느 곳에서나 쓰일수 있으며 return구문을 적을 수 없다
#람다 함수는 한 줄의 간단한 함수가 필요한 경우나 프로그램의 가독성을 위해 혹은 함수를 인자로 넘겨 줄때 사용

#lamda 인자 : <구문>

g = lambda x,y : x*y
print(g(2,3))
print((lambda x : x*x)(3))

def sqrt(x):
    x = x*x
    return x
a = list(map(sqrt,[1,2,3,4,5]))
b = list(map(lambda x : x**2,[1,2,3,4,5]))
print(a)
print(b)

#람다 함수는 한줄 이상의 구문을 적을 수 없지만 '\'를 이용해 여러줄을 적을 수 있다
#하지만 많이 사용하면 가독성이 떨어진다

def testLambda(t):
    t(1,2,3)
testLambda(lambda a,b,c: print("sumis ",\
                               a+b+c,"type of a",type(a),\
                               ":list object is", zip([a,b,c])))