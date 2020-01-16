## 모듈 만들기1

#### import

-   다른 파일에 있는 함수를 현재 사용 중인 파일에 포함하기 위한 함수

#### 예시

-   모듈로 사용하기 위한 calculator.py 를 생성한다.

```python
#file 이름 : calculator.py

def add(a, b):
  return(a + b)

def sub(a, b):
  return(a - b)

def mul(a, b):
  return(a * b)

def div(a, b):
  return(a / b)

def mod(a, b):
  return(a % b)
```

-   main.py 에 모듈로 사용하기 위해 생성한 calculator.py 를 import 한다.

```python
import calcultor

add_result = calculator.add(10,2)
sub_result = calculator.sub(10,2)
mul_result = calculator.mul(10,2)
div_result = calculator.div(10,2)
mod_result = calculator.mod(10,2)

print(add_result)  #=> 12
print(sub_result)  #=> 8
print(mul_result)  #=> 20
print(div_result)  #=> 5
print(mod_result)  #=> 0
```

**calculator.py 와 main.py 의 위치는 동일해야 한다!**
