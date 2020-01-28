# 실습 내용
# 본인의 전화번호부 관리 프로그램을 만든다고 상상하며 실습을 진행해봅시다.

# 1. 초기화 메소드를 통해 'name', 'number', 'religion' 변수를 초기화합니다.
# 2. "(religion) 거주 (name):(number)"를 출력해주는 showData 메소드를 만듭니다.
# 3. 'phoneBook' 클래스로부터 상속받는 'BestFriend'라는 이름의 클래스를 만듭니다.
# 4. 'BestFriend'클래스에서 'age', 'hobby' 변수 두 개를 더 받아 초기화 메소드를 재정의 합니다.
# 5. 'age','hobby' 변수만 따로 출력하는 specialData 메소드를 만듭니다.


class phoneBook():
    def __init__(self, name, number, religion):
        self.name = name
        self.number = number
        self.religion = religion
        print("info is saved")

    def showData(self):
        print(self.religion+" 거주 "+self.name+": "+self.number)


class BestFriend(phoneBook):
    def __init__(self, name, number, religion, age, hobby):

        self.name = name
        self.number = number
        self.religion = religion
        self.age = age
        self.hobby = hobby
        print("info is saved")

    def specialData(self):
        print(self.age+"살"+", "+self.hobby+"가 취미")


user1 = phoneBook("김구름", "01011111111", "판교")
user1.showData()

friend1 = BestFriend("이에듀", "01022222222", "강남", "23", "영화보기")
friend1.showData()
friend1.specialData()
