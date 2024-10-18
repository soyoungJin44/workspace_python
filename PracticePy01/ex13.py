total = input("전체금액을 입력해주세요: ")

re = total[:-3] + '00'
print(f"실제 지불금액은 {re}원 입니다.")