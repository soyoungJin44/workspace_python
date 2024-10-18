import phone_dao as pd


print("*"*50)
print(f"*{'전화번호 관리 프로그램'.center(38)}*")
print("*"*50)

while True:
    print("\n 1.리스트".ljust(11) + "2.등록".ljust(8) + "3.삭제".ljust(8) + "4.검색".ljust(8) + "5.종료".ljust(8))
    print("-"*50)
    num = int(input(">메뉴번호:"))

    if num == 1:
        print("<1.리스트>")
        pd.list()