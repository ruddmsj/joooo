#int는 정수(integer)를 의미한다  10진수 정수로 인식
year = 2017
month = 12
print(year, month) # 2017 12

#0o = 8진수  0b = 2진수  0x = 16진수
print(0o10, 0x10, 0b10) # 8 16 2

#10 진수를 입력 받아서 원하는 진수로 변환 하는 함수
print(oct(38)) # 8진수 0o46
print(hex(38)) # 16진수 0x26
print(bin(38)) # 2진수 0b100110

#python 3형에서는 long형이 사라지고 모두 int형으로 대체
print(type(1)) # <class 'int'>
print(type(2**31)) # <class 'int'>
print(type(3.14)) # <class 'float'>
print(type(314e-2)) # <class 'float'>  314e-2 는 지수형

#복소수를 나타내는 법
x = 3-4j
print(type(x)) # <class 'complex'>
print(x.imag) # -4.0
print(x.real) # 3.0
print(x.conjugate()) # (3+4j)  conjugate() = 켤레복소수를 만드는 메소드

# 연산자 + - * / % **(거듭제곱) //(정수나누기 : 나눈후 정수 부분만을 결과로 취함)
