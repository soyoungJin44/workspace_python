print("튜플 기본")

#[] : 리스트 (등록, 수정, 삭제 가능)
test_list = [1, 12, 123, 1234]
print(type(test_list))

#() : 튜플 (static같은느낌. 한번 만들면 수정불가함. 읽기만 가능)
t = (1, 2, 3, 4)
print(type(t))

#수정불가, 읽기는 가능함 tset

print(t[0], t[1], t[2])
print(t[1:3])
print(t[:])    #튜플전체 

print(t*2)


print(t+(100,200,300))
print(t)
print(3 in t)
print(len(t))

print("튜플 생성>>>>>>>>>>>")
t = (1,2,3,4)
tt = 100,200,300  #기본으로 튜플형으로 만들어진다.

print(type(tt))

#숫자가 1개일 때에는 그냥 숫자(자료형:int)로 생성된다.
p = (1)
print(type(p))
#뒤에 , 를 찍어주면 값이 1개여도 튜플로 생성할수있다.
p = (1 ,)
print(type(p))

t = ('apple', 'banana', 10, 20)

#튜플은 수정할수 없기때문에 오류 나옴
#t[0] = 'mango'
#print(t)









