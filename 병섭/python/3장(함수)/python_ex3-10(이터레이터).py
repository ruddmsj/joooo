#리스트, 튜플, 문자열 처럼 순회 가능한 객체에는 이터레이터(iterator)라는 특별한 객체가 포함돼 있다
#이터레이터란
#순회 가능한 객체의 요소에 순서대로 접근 할 수 있는 객체 이다

#리스트 순회

for element in [1,2,3]:
    print(element)

#튜플 순회

for element in (1,2,3):
    print(element)

#사전 순회

for element in {'one':1,'two':2}:
    print(element)

#문자열 순회

for char in "123":
    print(char)

#파일 내용 순회

#for line in open("myfile.txt"):
#    print(line)

#원리는 for문에서 지정한 순회 가능한 객체에서 이터레이터 객체를 가져오며 이때 이터레이터는 첫번째 요소를 가리킨다
#그 다음에 이터레이터 안의 연산자 __next()__메서드를 실행하여 이터레이터가 가리키는 요소를 반환 한뒤 다음 요소로 이터레이터를 옮긴다
#for 구문은 StopIteration 예외를 만날때 까지 반복으로 __next()__구문 수행
#내장 함수 next()를 사용하여 실행도 가능

a = [1,2,3]
it = iter(a)
print(next(it))
print(next(it))
print(it.__next__())
print(next(it))