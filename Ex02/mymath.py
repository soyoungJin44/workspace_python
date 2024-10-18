pi = 3.14

def plus(a,b):      #더하기
    return a + b

def minus(a,b):     #빼기
    return a-b

def multi(a,b):     #곱하기
    return a*b

def div(a,b):       #나누기
    return a/b

def area_circle(r): #원의넓이
    return pi * (r**2)


#직접실행 
# :본인이실행하면 main으로 나오고 다른곳에서 부르면 파일명이 나온다.

print(__name__)

if __name__ == "__main__":
    print("======================")
    print(plus(5,3))
    print(minus(7,1))