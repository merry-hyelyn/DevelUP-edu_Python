"""
    < 클래스 상속 >
    
    < 실습 >
    Person클래스를 상속하는 클래스를 만들어 봅시다.
    1. 클래스 이름은 Student로 정합니다.
    2. Student 클래스 내에 school 이라는 변수에 "goorm school"이라고 저장합니다.
    3. Student 클래스에 Person 클래스의 aboutMe 메소드를 오버로딩하여 학생의 이름과 나이가 출력되도록 합니다.
"""

class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age
		
	def aboutMe(self):
		print("나는 부모 클래스 입니다.")
		
		
class Student(Person):

	school = "goorm school"

	def aboutMe(self):
		print(f'{self.name}\n{self.age}\n')

		
Student_ex = Student("goormy", 15)
Student_ex.aboutMe()