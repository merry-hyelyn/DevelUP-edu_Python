class Person:
    def __init__(self, age):
        self.age = age

    def price(self):
        if self.age <= 13:
            return 5000

        elif self.age > 13 and self.age <= 19:
            return 7000

        else:
            return 8000


def choice_movie():


menu = ["1. 영화예매", "2. 영화시간", "3. 총수입", "4. 프로그램 종료"]

while(True):
    print("메뉴를 선택해주세요")
    for i in menu:
        print(i)

    choice = int(input())

    if choice == 1:
        pass
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    else:
        break
