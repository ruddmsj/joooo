#Static Method(정적 메서드)
#정적 메서드는 객체를 통하지 않고 클래스를 통해 직접 호출 할 수 있는 메서드
#이경우 메서드를 정의 할대 인스턴스 객체를 참조하는 'self'라는 인자를 선언하지 않는다

#Class Method(클래스 메서드)
#클래스 메서드의 경우 암묵적으로 첫 인자로 클래스 객체가 전달

#클래스 내에 등록하는 형식

#<호출할 메서드 이름> = staticmethod(클래스 내에 정의한 메서드 이름)
#<호출할 메서드 이름> = classmethod(클래스 내에 정의한 메서드 이름)

#예를 들면 클래스부터 생성되는 인스턴스의 개수를 관리하고 싶은 경우, 클래스 영역에서 해당 정보를 관리하는 것이 가장 효육적

#example Error 있는것
class CounterManager:
    insCount = 0
    def __init__(self):     #인스턴스 객체가 생성되면 클래스 영역의 insCount 변수 값이 증가
        CounterManager.insCount += 1
    def printInstanceCount():   #인스턴스 객체 개수 출력
        print("Instance Count: ",CounterManager.insCount)

a,b,c = CounterManager(),CounterManager(),CounterManager()
CounterManager.printInstanceCount()      #인스턴스 개수 출력
#b.printInstanceCount()              #암묵적으로 인스턴스 객체를 받기 때문에 Error 발생

#example Error 없는것
class CounterManager:
    insCount = 0
    def __init__(self):
        CounterManager.insCount += 1
    def staticPrintCount():     #정적 메서드 정의
        print("Instance Count: ", CounterManager.insCount)
    SPrintCount = staticmethod(staticPrintCount)    #정적 메서드로 등록
    def classPrintCount(cls):   #클래스 메서드 정의 (암묵적으로 첫 인자는 클래스를 받음)
        print("Instance Count:",cls.insCount)
    CPrintCount = classmethod(classPrintCount)      #클래스 메서드 등록

a,b,c = CounterManager(),CounterManager(), CounterManager()

CounterManager.SPrintCount()        #정적 메서드로 인스턴스 객체 개수를 출력
b.SPrintCount()

CounterManager.CPrintCount()        #클래스 메서드로 인스턴스 객체 개수 출력
b.CPrintCount()

#정적 메서드로 출력 하는 경우 암묵적으로 받는 첫 인자가 필요하지 않습니다

#p107~108 뱀잡기 더 공부