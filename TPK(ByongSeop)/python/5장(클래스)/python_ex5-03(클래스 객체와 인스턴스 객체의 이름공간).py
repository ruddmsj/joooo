#인스턴스 객체를 통해 변수나 함수의 이름을 찾는 경우의 순서
#인스턴스 객체 영역 -> 클래스 객체 영역 -> 전역 영역
#이렇게 찾지 못할 경우 AttributeError 예외가 발생 한다


#파이썬에서는 런타임에 각 클래스와 인스턴스 이름공간에 멤버 변수를 추가하거나 삭제 할 수 있다.

class Person:
    name = "Default Name"

p1 = Person()
p2 = Person()
print("p1's name:",p1.name)
print("p2's name:",p2.name)

p1.name = "강병섭" #p1인스턴스의 'name' 속성을 변경
print("p1's name:",p1.name)
print("p2's name:",p2.name)

#인스턴스 객체 p1의 멤버 데이터 name을 "강병섭"으로 변경 하면 인스턴스 P1의 이름공간에 존재하는 name이라는 변수에 변경된 데이터 저장
#반면 p2의 멤버 데이터인 name는 변경되지 않았기 때문에 여전히 클래스의 데이터를 참조


Person.title = "New title"      #클래스 객체에 새로운 멤버 변수 title추가
print("p1's title:",p1.title)
print("p2's title:",p2.title)   #두 인스턴스 객체에서 모두 접근 가능
print("Person's title:"Person.title)    #클래스 객체에서도 접근 가능

#파이썬에서는 클래스 객체와 인스턴스 객체에 동적으로 멤버 변수를 추가/삭제 할 수 있다

p1.age = "25"       #p1객체에만 age멤버 변수를 추가
print("p1's age :",p1.age)
#print("p2's age :",p2.age)     p2객체와 상위 Person클래스에는 age 이름을 찾을수 없어서 오류 발생

#코드 작성 시 주로 발생하는 실수중 하나가 클래스 메서드 내에서 인스턴스(self)를 통하지 않고 변수에 접근하는 것
#전역 영역의 변수와 클래스의 변수의 이름이 동일한 경우 에러도 발생하지 않아 규모가 큰 프로그램에서는 이런 문제를 찾기가 쉽지 않다

str = "Not Class Member"        #전역 변수
class GString:
    str = ""                    #클래스 객체 멤버 변수
    def Set(self,msg):
        self.ste = msg
    def Print(self):
        print(str)              #self를 이용해 클래스 멤버에 접근하지 않는 경우 이름이 동일한 전역 변수에 접근해서 출력함

g = GString()
g.Set("First Message")
g.Print()

#p102 뱁잡기 다시 한번 보기