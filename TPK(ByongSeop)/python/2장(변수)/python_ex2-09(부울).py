#부울(bool)은 참과 거짓을 나타내는 자료형이며 사용값은 True와 False이다

isRight = True
print(type(isRight))

#부울은 부울값들 간에 논리연산이나 비교연산의 결과로 사용

#비교연산자
# >, <, ==, !=, >=, <=

#논리연산자
#'and(&)'둘다 true어야 true반환, 'or(|)'둘중 하나만 true라도 true반환, 'not'반대 값 반환

#논리연산자에서 'and'의 경우 첫번째 값이 거짓이면 두번째 값을 보지 않는다
#수치를 사용 하는 경우 0은 False로 간주하고 음수를 포함한 다른 모든 값은 True로 간주한다
#문자열에서의 경우 ''(빈문자열)은 False로 간주한다

print(bool(0))
print(bool(-1))
print(bool('test'))
print(bool(''))
print(bool(None))