## 오류예외 처리하기

#### 방법

-   try ~ except

```python
try:
    실행할 코드

except 에러이름 as 메세지변수:
    에러발생 시 실행할 코드
```

-   try ~ else

```python
try:
    실행할 코드

except 에러이름 as 메세지변수:
    에러발생 시 실행할 코드

else:
    에러가 없을 때 실행하는 코드
```

-   try ~ finally

```python
try:
    실행할 코드

except 에러이름 as 메세지 변수:
    에러발생 시 실행할 코드

else:
    에러가 없을 때 실행하는 코드

finally:
    try 문 실행 후 '무조건' 실행하는 코드
```

finally 코드는 try 문의 오류 여부와 상관없이 **무조건** 실행
