#range() - 수열의 생성
#내장함수 range()를 통해 수열을 얻을 수 있다

#range()원형
#range(['시작값'],'종료값', ['증가값'])
#시작값과 증가값은 입력하지 않으면 기본값으 0,1 이다

print(list(range(10))) #종료값이 있는 경우
print(list(range(5,10))) #시작값과 종료값이 있는 경우
print(list(range(10,0,-1))) #시작값과 종료값과 증가값이 있는 경우

#리스트 항목과 인데스 값을 동시에 얻는 법
#enumerate() 내장 함수를 사용

#enumerate() 원형
#enumerate('시퀀스 타입 객체',['시작값'=0])
#첫번째 인자는 이터레이션이 가능한 객체가 입력되며 두번째 인자는 인덱스의 순번이며 생략 가능 기본값은 0

L = ["apple",100,15.5]
for i in enumerate(L):
    print(i)
for i in enumerate(L,101):
    print(i)

#리스트 내장
#구조
#<표현식> for <아이텐> in <시퀀스 타입 객체> (if <조건식>)

l = [1,2,3,4,5]
l = [i ** 2 for i in l]
print(l)
t = ("강병섭", "tpk", "정보통신python")
t = [len(i) for i in t]
print(t)
d = {1:"apple", 2:"banana",3:"tomato"}
d = [i.upper() for i in d.values()]
print(d)
l = ["apple", 'tpk','kangbyongseop']
l = [i for i in l if len(i)>3]
print(l)

l1 = [1,2,3]
l2 = [4,5,6]
l3 = [x*y for x in l1 for y in l2]
print(l3)

#반복문 작성시 도움 되는 함수
#filter()는 입력받은 시퀀스형 객체 즉 이터레이션이 가능한 객체를 순회 하며 함수의 결과가 True인 경우만을 묶어 해당 이터레이터 객체를 반환

#filter() 원형
#filter(<function> | None, <이터레이션이 가능한 자료형>)

#첫번째 인자는 function은 함수의 이름으로 필터링할 방법을 제공하며 None를 쓰면 모든 아이템을 선택한다
#두번째 인자는 필터링 할 대상이다

#아무런 필터링을 안할때
L = [10,20,30]
IterL = filter(None,L)
for i in IterL:
    print("Item : {0}".format(i))

#필터링 함수를 지정했을때
def GetBiggerThan20(i):
    return i>20
L = [10,25,30]
Iterl = filter(GetBiggerThan20,L)
for i in Iterl:
    print("Item : {0}".format(i))

#람다 함수를 작성도 가능하다
L = [10,25,30]
Iterl = filter(lambda x : x>20,L)
for i in Iterl:
    print("Item : {0}".format(i))

#zip() 함수는 순회 가능한 시퀀스형 이나 이터레이터형 객체들을 결합하여 쌍으로 순회 가능한 이터레이터 객체를 얻을수 있다
x = [10,20,30]
y = [1,2,3]
xy = zip(x,y)
for i in zip(x,y):
    print("Item : {0}".format(i))
#*를 붙혀서 결합된 결과를 분리 할수도 있다
x2, y2 = zip(*xy)
print(x2,y2)

#인자의 개수가 동일 하지 않은 경우 짧은쪽을 기준으로 하고 나머지 시퀀스는 버린다
x = [1,2,3]
y = [4,5,6,7,8]
for i in zip(x,y):
    print("Item : {0}".format(i))

#시퀀스형 객체를 순회 하면서 모든값을 갱신할때 map()함수를 이용한다
#map() 형태
#map(<함수이름>, 이터레이션이 가능한 객체, ...)

#첫인자는 함수이름이 뒤에 오는 인자는 순회 가능한 인자로 filter(), zip()과 동일한 형태

L = [10,20,30]
def Add10(i):
    return i*10
for i in map(Add10,L):
    print("Item : {0}".format(i))

#효율적인 순회 방법
#시퀀스형 자료형을 순회 하면서 출력한는 방법으로
#첫번째 for문을 사용

x = ["1","2","3"]
for i in x:
    print("Item : {0}".format(i))

#두번째 문자열 내장 메소드인 join()이나 리스트 내장을 이용
print("\n".join(x))
print("\n".join(i for i in x))

import time
l = range(1000000)

t = time.mktime(time.localtime())
for i in l:
    print(i,)
t1 = time.mktime(time.localtime())-t

t = time.mktime(time.localtime())
print(",".join(str(i) for i in l))
t2 = time.mktime(time.localtime())-t

print("for 문으로 각 인자를 출력")
print("Take {0} seconds".format(t1))
print("join() 문으로 각 인자를 출력")
print("Take {0} secodns".format(t2))