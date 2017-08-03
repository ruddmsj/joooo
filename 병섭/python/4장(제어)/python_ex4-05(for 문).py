#for 문은 인자로 받은 시퀀스형 객체와 이터레이션이 가능한 객체를 순차적으로 순회
#for 문 구조
#for <아이템 i> in <Sequence형 객체 s>:
#   <구문>

I = ['Apple','red',100,15.23]
for i in I:
    print(i, type(i))

#이터레이터 객체를 이용해 for문 수행

L = [10,20,30]
iterator = iter(L)
for i in iterator:
    print(i)

#반복문은 2개이상 중첩하여 사용 가능하다

for i in [1,2]:
    print("{0}+단".format(i))
    for y in [1,2,3,4,5,6,7,8,9]:
        print("{0}*{1}={2}".format(i,y,i*y))