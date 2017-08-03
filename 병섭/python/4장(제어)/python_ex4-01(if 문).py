#if 문은 기본적으로 조건을 평가해 그 결과에 따라 수행 여부를 결정
#if 문 구조
#if <조건식>:
#   <구문>

#2개 이상의 조건을 처리하려면 elif를
#어떠한 조건에도 만족하지 않으면 else 를 사용한다

#예제

score = int(input(('Input Score:')))

if 90 <= score <= 100:
    grade = 'A'
elif 80 <= score < 90:
    grade = 'B'
elif 70 <= score < 80:
    grade = 'C'
elif 60 <= score <70:
    grade = 'D'
else:
    grade = 'F'

print("Grade is " +grade)