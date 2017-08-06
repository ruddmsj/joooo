# 리스트는 값의 나열이다
# 순서가 존재하며 여러 종류의 값을 담을 수 있다.
# 0부터 시작하는 index가 있으며 slicing도 가능

#리스트의 생성

color = ['red', 'green', 'blue']
print(color)
print(type(color))

#리스트 값 추가

color.append('black')
print(color)

#insert()를 이용해 원하는 곳에 값 삽입

color.insert(1,'white')
print(color)

#extend()를 사용하여 튜플이나 리스트의 여러값을 한번에 넣을 수 있다

color.extend(['gold', 'red'])
print(color)

#+연산자도 사용 가능하며 리스트나 튜플 같은 순회 가능한 값을 넣어야 한다
#문자열을 넣으면 쪼개져서 들어감

color += ['yellow']
print(color)
color += 'yellow'
print(color)

#값의 위치를 확인하는 index() 메소드도 지원한다
#두번째 인자로 시작점을 알려줄수도 있다

print(color.index('red'))
print(color.index('red',1))

#해당 값의 개수를 반환 하는 count()메소드와 값을 뽑아내는 pop()메소드도 제공

print(color.count('red'))
print(color.pop())
print(color.pop(1))
print(color)

#remove()는 단순히 해당값만을 삭제

color.remove('red')
print(color)

#정렬을 쉽게 하기 위해서 sort()와 역방향 정렬 reverse()메소가 제공

color.sort()
print(color)
color.reverse()
print(color)

#sort()메소드는 key값을 주어서 자신이 원하는 방식으로 정렬을 할 수 있다
#mysort() 함수는 마지막 문자를 기준으로 비교 수행 한다

def mysort(x):
    return x[-1]
color.sort(key = mysort)
print(color)
color.sort(key = mysort, reverse = True)
print(color)