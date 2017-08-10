#연산자 중복 정의란
#사용자 정의 객체에 대해 필요한 연산자를 내장 타입과 형태와 동작이 유사하도록 재정의 하는것
#클래스 메서드로 구현 가능

#벡터나 행렬과 같은 수치 연산에서 주로 사용

#example
class GSrting:
    def __init(self, init = None):      #생성자
        self.content = init

    def __sub__(self, str):     # '-'연산자 중복 정의
        for i in str:
            self.content = self.content.replace(i,'')
        return GSrting(self.content)

    def Remove(self,str):       #Remove 메서드는 '-'연산자 중복과 동일하기에 '__sub__'를 재호출
        return self.__sub__(str)

#개발자가 명시적으로 중복하지 않은 연산자를 사용하는 경우 TypeError가 발생

#g = GSrting("abcedfg")
# g + "apple"  Error 발생

#연산자 중복을 위해 미리 정의된 메서드

#수치 연산자 p110 참조

#example
class GString:
    def __init__(self, init = None):
        self.content = init
    def __sub__(self, str):     # '-' 연산자를 중복
        for i in str:
            self.content = self.content.replace(i,'')
        return GString(self.content)
    def __abs__(self):
        return GString(self.content.upper())

    def Print(self):
        print(self.content)

g = GString("aBcdef")
g -= "def"
g.Print()
g =abs(g)
g.Print()


#더 많은 중복 연산자는 책 참조 혹은 개인 홈페이지에 개제 할 예정