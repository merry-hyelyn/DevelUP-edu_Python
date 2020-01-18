"""
    < 생성자 실습 >
    1. __init__을 이용하여 인스턴스를 생성할 때 아이디와 비밀번호를 입력받도록 합니다.
    2. getId라는 인스턴스 메소드를 생성하여 이 함수를 호출하면 아이디와 비밀번호를 출력하도록 합니다.
    3. Member 클래스의 인스턴스를 하나 만든 후 getId 메소드를 실행해 봅시다.
"""

class Member : 
    def __init__(self, id, password):
        self.id = id
        self.password = password

    def getId(self):
        return self.id, self.password

mem1 = Member("goormedu","goorm")
id, pw = mem1.getId()
print(id, pw)