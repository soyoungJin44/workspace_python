code = int(input("과목번호를 입력해주세요\n"))

match code:
    case 1:
        print('R101호')
    case 2:
        print('R102호')
    case 3:
        print('R103호')
    case 4:
        print('R104호')
    case _:
        print('상담원 문의 ㄱ')