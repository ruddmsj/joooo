#패키지란
#여러개의 모듈을 하나로 묶은 것

#일반 디렉터리는 __init__.py가 없지만 패키지의 디렉터리라면 __init_.py가 꼭 있다

#패키지를 사용할때 한가지 주의해야 할 점은 어떤 패키지를 임포트 했을 때 해당 패키지의 하위 패키지는 자동으로 임포트 되지 않는다

#패키지 안에서 패키지 안의 모듈 참조하기

#참조 할려는 모듈이 같은 디렉터리에 잇거나 하위 디렉터리에 있다면
#from 참조하려는 모듈 import *

#참조하려는 모듈이 상위 디렉터리에 있다면 상위 디렉터리부터 찾아 가야 한다 '.'을 사용
#from 상위모듈.모듈이름 import 모듈이름

#'.'을 사용해 현재 패키지와 부모 패키지를 참조 할 수 있다