movies = ["Batman", "Harry Porter", "Scream", "Happy Dog"]


print("관람하실 영화를 입력해 주세요.")
for movie in movies:
    print(movie)


print("관람하실 영화를 입력해 주세요.")
choice = input()


while choice not in movies:
    print("다시 선택해 주세요.")
    choice = input()


print("관람하실 인원을 입력해 주세요.")
number = int(input())


while not((type(number) == int) & (number > 0)):
    print("인원은 양수이고 정수이어야 합니다.")
    number = int(input())

print("할인권이 있는 경우 y 입력, 없는 경우 n 을 입력해 주세요.")

coupon = input()
coupon_price = 0

if coupon == 'y':
    print("할인권의 금액:")
    coupon_price = int(input())

original_price = 12000*number
price_sum = original_price - coupon_price

print("")
print("결제 내역")
print("-------------------------")
print("인원: %d명" % number)
print("영화 제목 : {}".format(choice))
print("합산 금액 : {}원".format(original_price))
print("할인 금액 : {}원".format(coupon_price))
print("-------------------------")
print("총 결제 금액 : {}원".format(price_sum))
