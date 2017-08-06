#파이썬에는 특별한 인자 모드가 있는데
#기본 인자 값, 키워드 인자 값, 가변 인자 리스트, 정의되지 않은 키워드 인자 처리가 있다

#기본 인자 값
#함수를 호출할 때 인자를 지정하지 않아도 기본 값이 할당하게 하는 방법
#기본 인자 값이 앞에 있으면 뒤에 기본 값이 없는 인자가 올 수 없다

def Times(a=10,b=20):
    return a*b
print(Times(),Times(5))

#키워드 인자
#변수의 이름으로 특정 인자를 전달 할 수 있다
#키워드 인자 이후에는 순서에 의한 인자 매칭을 할 수 없다 키워드 인자는 일반 인자 뒤에 위치

def connecURI(server,port):
    str = "http://"+server+":"+port
    return str
print(connecURI(port="8800",server="test.com"))
print(connecURI("test.com",port="8800"))
#print(connecURI(server="test.com",8800))  오류

#가변 인자 리스트
#인자의 개수가 정해지지 않은 가변 인자를 전달 받을 수 있다
#*를 인자 앞에 붙이며 가변 인자 리스트는 입력받은 인자를 튜플에 저장

def test(*args):
    print(type(args))
test(1,2)

def union2(*ar):
    res = []
    for item in ar:
        for i in item:
            if not i in res:
                res.append(i)
    return res
print(union2("ham","egg","spam"))

#정의되지 않은 인자 처리하기
#**를 붙이면 정의되지 않은 인자를 사전 형식으로 전달 받을 수 있다

def user(server,port,**user):
    str = "http://"+server+":"+port+"?/"
    for i in user.keys():
        str += i + "=" + user[i] +"&"
    return str
print(user("test.com","8800",id = 'tpk', password='1234'))