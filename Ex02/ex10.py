
'''
자바
public int plus(a,b){
    sum = a+b
    return sum;
}
'''

def plus(a,b):
    sum = a+b
    return sum

result = plus(5,3)
print(result)

'''
문자열 +  숫자 안됨 

result = plus(5,'한글')
print(result)
'''

# 정의
def my_function():
    print("hello ffff")

#사용
my_function()

#정의 
def none_function():
    pass

none_function()

#패킹 / 언패킹 구분 후 정리

#정의
def plus_print(a=0,b=0):
    print(a,b)

plus_print(3,5)
#안됨 //  정의할때 값이 안들어오면 0으로 세팅해두면됨
plus_print(3)




#정의
def plus_print(a=0, b=0):
    print(a,b)

#이름으로 매칭해준다 ,333 이런식으로 ㄴㄴ
plus_print(b=333)
plus_print(a=773)
plus_print(a=333)

#정의 갯수를 몇개를 넣던 묶여서 온다.
#매개변수를 정의할수없을때 *args
def sum_many(*args):
    #print(type(args))
    sum = 0
    for no in args:
        sum += no
        print(no)
        
    print("======================")
    print(sum)

sum_many(1)
sum_many(1,2,3)
sum_many(1,2,3,4,5,69,7,8)


def sum_mul(mode, *args):
    if mode == "sum":
        sum = 0
        for no in args:
            sum += no
        return sum
    elif mode == "mul":
        mul = 1
        for no in args:
            mul *= no
        return mul
    else:
        print("mode를 입력해주세요!")

print(sum_mul("sum",3,2))
print(sum_mul("mul",2,9))





