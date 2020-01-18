## 모듈 만들기2

-   모듈 이름 :my_module.py

```python
def three_times(a):
  return a * 3

def ten_times(a):
  return a * 10
```

-   main.py

```python
import my_module

print(my_module.three_times(10)) #=> 30
print(my_module.ten_times(10)) #=> 100
```

모듈 함수 사용 시 `my_module.three_times` 또는 `my_module.ten_times`  
==> 번거로움

-   `from 모듈이름 import 모듈함수` 를 이용하여 함수이름 호출만으로 사용가능

```python
from my_module import three_times
from my_module import ten_times

print(three_times(10)) #=> 30
print(ten_times(10)) #=> 100
```

-   모듈 내의 모든 함수를 불러올 때 : `import 모듈이름 import *`
