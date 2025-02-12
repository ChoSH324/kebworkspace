import random
drinks_foods = {"위스키": "초콜릿", "와인": "치즈", "소주": "삽겹살", "고량주": "양꼬치"}
drinks_foods_list = [["위스키","초콜릿"],["와인","치즈"],["소주","삼겹살"],["고량주","양꼬치"]]

japan_drinks_foods = {"사케": "광어회", "위스키": "낙곱새"}
japan_drinks_foods_list=[["사케","광어회"],["위스키","낙곱새"]]
drinks_foods.update(japan_drinks_foods)
drinks_foods_list.extend(japan_drinks_foods_list)
print(drinks_foods_list)

len=len(drinks_foods_list)
while True:
    print("다음 술 중에 고르세요")
    for i in range(1,len+1):
        print(f'{i}){drinks_foods_list[i-1][0]}', end = " ")
    print(f'{len+1}) 아무거나 {len+2} 종료 : ')
    menu = input()
    menu = int(menu)
    if 1<=menu<=len:
        print(f'{drinks_foods_list[menu-1][0]}에 어울리는 안주는 {drinks_foods_list[menu-1][1]} 입니다')
    elif menu == len+1:
        random_number=random.randint(0,len-1)
        print(f'{drinks_foods_list[random_number][0]}에 어울리는 안주는 {drinks_foods_list[random_number][1]} 입니다')
    elif menu == len+2:
        print(f'다음에 또 오세요')
        break