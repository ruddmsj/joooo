#함수에서 return은 함수를 종료하고 해당 함수를 호출한 곳으로 되돌아 가게 한다
#return 은 어떠한 객체도 돌려줄 수 있으며 여러 값을 튜플로 묶어서 처리 할 수도 있다
#return을 적지 한거나 return만 적어도 함수가 종료 되며 None 객체값을 반환한다

def setValue(newValue):
    x = newValue
retval = setValue(10)
print(retval)

#함수는 한개의 객체만 반환 할수 있으며 밑의 예제는 두개의 값을 반환 하는것이 아니라 여러개의 값을 하나의 튜플 객체로
#만들어 반환 하는 것이다

def swap(a,b):
    return b,a
print(swap(1,2))
a, b = swap(1,2)
print(a,b)

def intersect(alist,blist):
    retlist =[]
    for i in alist:
        if i in blist and i not in retlist:
            retlist.append(i)
    return retlist

list1 = "강병섭"
list2 = "강아지"

print(intersect(list1,list2))