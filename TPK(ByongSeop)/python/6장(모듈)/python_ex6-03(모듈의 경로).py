#모듈 이름만으로 임포트되게 하려면 모듈 검색 경로(module search path)에 모듈 파일이 있어야 합니다

#모듈을 임포트 할대 파이썬은 다음과 같은 순서대로 모듈을 찾는다

#1. 현재 작업 디렉터리(Current Working Directory)
#2. PYTHONPATH 환경변수에 등록된 위치
#3. 표준 라이브러리 디렉터리
#sys.path에 경로를 넣어주는 것은 프로그램 동작 중에도 가능