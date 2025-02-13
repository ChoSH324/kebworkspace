import random

drinks = ["위스키", "와인", "소주", "고량주"]
snacks = ["초콜릿", "치즈", "삽겹살", "양꼬치"]
prices = [50000,30000,5000,25000]

drinks.append("사케")
snacks.append("광어회")
prices.append(40000)
snacks[0] = "낙곱새"
drinks.append("데킬라")
snacks.append("소금")
prices.append(55000)

def print_menu(n):
    print(f'{drinks[n]}에 어울리는 안주는 {snacks[n]} 입니다')


def print_price(n):
    print(f'{drinks[n]}의 가격은 {snacks[n]}입니다')


# main
if len(drinks) != len(snacks) & len(snacks)!=len(prices):
    exit()

menu_list = '다음 술중에 고르세요.\n'
for i in range(len(drinks)):
    menu_list = menu_list + f'{i+1}) {drinks[i]}  '
menu_list = menu_list + f'{len(drinks)+1}) 아무거나  {len(drinks)+2}) 종료 : '

while True:
    menu = int(input(menu_list))
    if 1 <= menu <= len(drinks):
        print_menu(menu - 1)
        print_price(menu - 1)
    elif menu == len(drinks)+1:
        random_index = random.randint(0, len(drinks)-1)
        print(f'{drinks[random_index]}에 어울리는 안주는 {snacks[random_index]} 입니다')
    elif menu == len(drinks)+2:
        print(f'다음에 또 오세요')
        break