#상속이란
#부모 클래스의 모든 속성을 자식 클래스로 물려줄 수 있다
#수현해야 하는 여러 클래스의 공통된 속성을 부모클래스에 정의 하고 각 하위 클래스에서는 그에 맞는 특화된 메서드와 데이터를 정의

#Person 클래스
class Person:
    "부모 클래스"
    def __init__(self,name,phoneNumber):
        self.name = name
        self.phoneNumber =phoneNumber

    def PrintINfo(self):
        print("Info(Name:{0}, phonNumber:{1})".format(self.name, self.phoneNumber))

    def PrintPersonData(self):
        print("Person(Name:{0}, phonNumber:{1})".format(self.name, self.phoneNumber))

#만약 1개 이상 다중 상속 받는 경우 ';'으로 구분해서 기입
#Student 클래스
class Student(Person):
    "자식 클래스"
    def __init__(self,name, phoneNumber, subject, studentID):
        self.name = name
        self.phoneNumber = phoneNumber
        self.subject = subject
        self.studentID = studentID

#확인
p = Person("강병섭","010-1932-2167")
s = Student("TPK","010-9132-2168","Computer science","1001")
print(p.__dict__)
print(s.__dict__)

#클래스 간 관계 확인은 issubclass로 확인 할 수 있다
#issubclass(자식 클래스, 부모 클래스)

print(issubclass(Student,Person))   #Person이 Student의 부모 클래스 인지 확인
print(issubclass(Person, Student))  #Student가 Person의 부모 클래스 인지 확인
print(issubclass(Person,Person))    #자기 자신은 항상 True를 반환
print(issubclass(Person,object))    #모든 클래스는 object를 암묵적으로 상속받음
print(issubclass(Student,object))
class Dog:
    pass
print(issubclass(Student,Dog))      #아무런 상속 관계도 없음
print(issubclass(Dog,object))       #Dog 클래스 역시  object를 암묵적으로 상속받음

#어떤 클래스의 부모 클래스를 알기 위해서는 __bases__속성을 사용해 알아 낼 수 있다
#이 속성은 직계 부모 클래스를 튜플로 반환

print(Person.__bases__)

#부모 클래스의 생성자 호출

class Student2(Person):
    "자식 클래스2"
    def __init__(self, name, phoneNumber, subject, studentID):
        Person.__init__(self, name, phoneNumber)    #명시적으로 Person 생성자를 호출
        self.subject = subject
        self.studentID = studentID

#메서드 추가하기

class Student3(Person):
    "자식 클래스3"
    def __init__(self,name, phoneNumber, subject, studentID):
        Person.__init__(self, name, phoneNumber)
        self.subject = subject
        self.studentID = studentID
    def PrintStudentData(self):     #새로운 메서드 추가
        print("Student3(Subject: {0}, studentID: {1}".format(self.subject, self.studentID))

s = Student3("강병섭", "010-9132,2167", "computer science", "1002")
s.PrintPersonData()
s.PrintStudentData()
print(s.__dict__)

#메서드 재정의 하기(Method Overriding)

class Student4(Person):
    "자식 클래스4"
    def __init__(self,name, phoneNumber, subject, studentID):
        Person.__init__(self, name, phoneNumber)
        self.subject = subject
        self.studentID = studentID
    def PrintStudentData(self):
        print("Student3(Subject: {0}, studentID: {1}".format(self.subject, self.studentID))

    def PrintINfo(self):
        print("Info(Name: {0}, PhoneNumber:{1}".format(self.name,self.phoneNumber))
        print("Info(Subject: {0}, StudetID: {1}".format(self.subject,self.studentID))

s = Student4("강병섭", "010-9132-2167", "Data Science", "1004")
s.PrintINfo()

#파이썬에서의 메서드 재정의는 단순히 주 메서드의 이름만 같으면 된다
#이유는 이름공간의 속성 정보가 내부적으로 사전 형식으로 관리 되고 있기 때문이다
#즉 키값인 메서드 이름만 같으면 부모 클래스의 메서드 대신에 자식 클래스의 메서드를 호출

#Person Student4  인스턴스 객체를 PersonList 리스트에 입력한후 각각에 대해 동일한 인터페이스인 PrintInfo()를 호출

p = Person("Tim", "010")
s = Student4("강병섭4", "010-9132-2167", "Data science", "1005")
PersonList = [p,s]

for item in PersonList:
    item.PrintINfo()

#메서드 확장하기

class Student5:
    "자식 클래스5"
    def __init__(self,name, phoneNumber, subject, studentID):
        Person.__init__(self, name, phoneNumber)
        self.subject = subject
        self.studentID = studentID
    def PrintStudentData(self):
        print("Student3(Subject: {0}, studentID: {1}".format(self.subject, self.studentID))

    def PrintINfo(self):
        Person.PrintINfo(self)
        print("Info(Subject: {0}, StudetID: {1}".format(self.subject,self.studentID))

#클래스 상속과 이름공간
#상속 관계 검색의 원칙(Principle of the inheritance search)
#인스턴스 객체 영역 -> 클래스 객체 간 상속을 통한 영역(자식 클래스 영역 -> 부모 클래스 영역) -> 전역 영역

#즉 클래스의 상속 관계에서 속성의 이름을 검색할 때 개별적으로 독립된 영역을 가지고 있는 클래스 간의 상속 관계 순서로 이름을 찾는다

#자식 클래스가 상속 받은 멤버 메서드에 대해 재정의 하지 않거나 멤버 데이터에  새로운 값을 할당 하지 않는 경우
#자식 클래스 내부의 이름공간에 해당 데이터와 메서드를 위한 저장 공간을 생성 하는 대신  단순히 부모 클래스의 이름공간에 존재하는 데이터를 참조

#다중 상속

class Tiger:
    def Jump(self):
        print("호랑이처럼 멀리 점프하기")
    def Cry(self):
        print("호랑이 어흥")

class Lion:
    def Bite(self):
        print("사자처럼 한입에 꿀꺽하기")
    def Cry(self):
        print("사자 으르렁")

class Liger(Tiger,Lion):
    def Play(self):
        print("라이거만의 사육사와 재미잇게 놀기")

l = Liger()
l.Bite()
l.Jump()
l.Play()
l.Cry() #Tiger의 Cry가 호출되는 이유는 Liger클래스 선언무에 상속 받는 순서가 Tiger 클래스 부터 시작 됬기 때문이다

#다양한 상속 구조에서 메서드의 이름을 찾는 순서는 __mro__에 튜플로 정의돼 있다

#super()를 이용한 상위 클래스의 메서드 호출

#Animal 클래스의 생성자가 두번 호출
class Animal:
    def __init__(self):
        print("Animal __init__()")
class Tiger(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Tiger __init__()")
    def Jump(self):
        print("호랑이처럼 멀리 점프하기")
    def Cry(self):
        print("호랑이 어흥")

class Lion(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Lion __init__()")
    def Bite(self):
        print("사자처럼 한입에 꿀꺽하기")
    def Cry(self):
        print("사자 으르렁")

class Liger(Tiger,Lion):
    def __init__(self):
        Tiger.__init__(self)
        Lion.__init__(self)
        print("Liger __init__()")
    def Play(self):
        print("라이거만의 사육사와 재미잇게 놀기")

l = Liger()

#Animal 클래스의 생성자가 한번 호출

class Animal:
    def __init__(self):
        print("Animal __init__()")
class Tiger(Animal):
    def __init__(self):
        super().__init__()
        print("Tiger __init__()")
    def Jump(self):
        print("호랑이처럼 멀리 점프하기")
    def Cry(self):
        print("호랑이 어흥")

class Lion(Animal):
    def __init__(self):
        super().__init__()
        print("Lion __init__()")
    def Bite(self):
        print("사자처럼 한입에 꿀꺽하기")
    def Cry(self):
        print("사자 으르렁")

class Liger(Tiger,Lion):
    def __init__(self):
        super().__init__()
        print("Liger __init__()")
    def Play(self):
        print("라이거만의 사육사와 재미잇게 놀기")

l = Liger()

#Ligerdml super() 메서드를 호출 하는 경우
#super(Liger, self).__init__() 같이 명시적으로 클래스의 이름과 인스턴스 객체를 인자로 전달해서 호출 가능