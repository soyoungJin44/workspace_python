num = input('숫자를 입력해주세요\n')
print(num, type(num))
int_num = int(num)

if int_num>0:
    print('0보다 큰 수 입니다.')
elif int_num<0:
    print('0보다 작습니다.')
else:
    print('0 입니다.')

print('=========================================')
num1 = input('숫자를 입력해주세요\n')
int_num1 = int(num1)

if int_num1%2==0:
    print('짝수입니다.')
elif int_num1%2==1:
    print('홀수입니다.')
else:
    print('0입니다.')


num2 = input('과목번호를 입력해주세요\n')
int_num2 = int(num2)

if int_num2==1:
    print('R101호 입니다.')
elif int_num2==2:
    print('R102호 입니다.')
elif int_num2==3:
    print('R103호 입니다.')
elif int_num2==4:
    print('R104호 입니다.')
else:
    print('상담원에게 문의하세요.')




