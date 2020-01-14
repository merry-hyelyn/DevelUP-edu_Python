"""
클래스와 객체 - 실습1
# 1. Customer라는 클래스를 만듭니다.
# 2. id를 입력값으로 받는 info라는 인스턴스(객체) 메소드를 선언하여 사용자의 id를 출력하도록 코드를 작성합니다.
# 3. Customer 클래스의 객체를 만든 뒤 welcome 변수의 내용을 출력합니다.
# 4. 마지막으로 info 메소드를 호출항 id에 "goorm"을 입력하여 출력해봅시다.
"""
class Customer: 
    welcome = "반갑습니다"

    def info(self, id):
        self.id = id
        print(self.id)

person = Customer()
print(person.welcome)
person.info(input())