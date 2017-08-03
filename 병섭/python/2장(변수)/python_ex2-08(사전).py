#사전(Dictionary)은 키와 값의 쌍으로 구정되어 있다
#키를 이용해 값을 가져올 수 있으며 인덱스는 지원하지 않고 없는 키를 사용하면 에러가 난다

#사전의 정의

d = dict(a=1,b=3,c=5)
print(d,type(d))

color = {"apple":"red", "banana":"yellow"}
print(color,type(color))
print(color["apple"])

#사전에 새로운 값 추가 및 변경

color["cheery"] = "red"
print(color)
color["apple"] = "green"
print(color)

#사전의 내용을 얻을라면 items(), keys(), values()를 사용하면 된다

#items()는 사전의 모든 키와 값을 튜플로 묶어서 반환

for i in color.items():
    print(i)

for x,y in color.items():
    print(x,y)

#keys()는 사전의 키만을 반환

for i in color.keys():
    print(i)

#values()는 사전의 값만을 반환

for i in color.values():
    print(i)

#사전의 반환 값을 리스트로 받고 싶을때

x = list(color.keys())
print(x, type(x))

#del()를 사용하여 하나씩 삭제 할 수도 있고 clear()를 사용하여 한번에 삭제도 가능

print(color)
del color['cheery']
print(color)
color.clear()
print(color)

#다음과 같이 자료형을 섞어서 사용도 가능하다

x = {'age':40.5, 'job':[1,2,3], 'name':{'kim':2,'cho':1}}
y = [1,2,3,('green'),{'apple':'red'}]
print(x)
print(y)