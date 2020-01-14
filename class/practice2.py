"""
    < 특별한 메소드와 클래스 변수 >
     - __init__ : 객체 생성과 동시에 초기값 생성해주는 생성자 함수

    < 인스턴스 변수, 클래스 변수 >
     - 객체 간 변수 값 공유 X
     - self.변수이름 -> 인스턴스 변수
     - 클래스 이름.변수 이름 -> 클래스 변수, 같은 클래스 내 인스턴스 공유, 접근 ○

    < 정적 메소드, 인스턴스 메소드, 클래스 메소드 >
     - 인스턴스 메소드 : self로 인스턴스의 필드에 접근가능한 메소드
     - 정적 메소드 : self 매개변수 갖지 않는 메소드, @staticmethod로 정적 메소드임을 표시

    < 실습 >
    1. Member라는 클래스를 만들어 봅시다.
    2. setId라는 인스턴스 메소드를 만들고 아이디(id)와 비밀번호(password)를 인자로 받습니다.
    3. setId 인스턴스 메소드 내에 self를 이용하여 해당 인스턴스의 아이디와 비밀번호를 각각 변수에 저장합니다.
    4. getId라는 인스턴스 함수를 만든 뒤 호출하면 아이디와 비밀번호를 출력하도록 합니다.
"""

class Member : 
    def setId(self, id, password) :
        self.id = id
        self.password = password

    def getId(self):
        print(self.id, self.password)

mem1 = Member()
mem1.setId("goorm","goorm1")
mem1.getId()