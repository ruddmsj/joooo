#모듈을 만든다는 것은 파일을 만든다는 뜻이다
#일반적으로 <모듈이름>.py 로 저장

#교집합, 합집합, 차집합을 계산하는 모듈 만들기
#모듈 이름은 simpleset.py로 만든다

import simpleset
print(dir(simpleset))

setA = [1,3,5,7]
setB = [2,3,4,9]

print(simpleset.union(setA,setB))
print(simpleset.intersect(setA,setB,[1,2,3]))