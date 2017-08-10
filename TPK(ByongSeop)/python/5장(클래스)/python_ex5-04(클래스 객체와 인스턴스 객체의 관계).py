#인스턴스 객체가 어떤 클래스로 부터 생성됬는지 확인하는 방법으로 isinstance() 내장 함수를 사용가능

#isinstance(인스턴스 객체 , 클래스 객체)

#클래스 간의 상속관계가 있는 경우에도 자식 클래스의 인스턴스 객체는 부모 클래스의 인스턴스로 평가
#클래스 객체를 정의할 때 어떠한 상속을 받지 않더라도 버전 3 이후로는 암묵적으로 object 객체를 상속받습니다  자료형 또한 object객체에서 파생

class Person:
    pass

class Bird:
    pass

class Student(Person):
    pass

p,s = Person(), Student()
print("p is instance of Person:", isinstance(p,Person))     #상속관계 판단 가능

print("s is instance of Person:", isinstance(s,Person))
print("p is instance of object:", isinstance(p,object))     #버전 3 이후로 모든 클래스는 object에서 파생됨

print("p is instance of Bird:", isinstance(p,Bird))
print("int is instance of Object:",isinstance(int,object))      #버전 3 이후 기본 자료형도 object에서 파생된