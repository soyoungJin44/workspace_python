# 시퀀스형 자료형: 순서가 있는것들   // set은 해당안됨

no_list = {1, 2, 3}
print(type(no_list))

print(len(no_list))

print(2 in no_list)
print(2 not in no_list)

# set메소드 ========================== set은 방번호가 없기 때문에 n번째에 넣어야겠다 ㄴㄴ
no_list.add(4)
print(no_list)

#set에는 중복값 들어 갈 수 없다
# no_list.add(4)
# print(no_list)

no_list.remove(1)
print(no_list)

#없는값 지우라하면 remove는 오류 discard는 없다넘어감
no_list.discard(100)
print(no_list)
#no_list.remove(100)
#print(no_list)

#추가
no_list.update({888,999})
print(no_list)

#전체비우기
no_list.clear()
print(no_list)


#================ 집합 개념
s1 = {1,2,3,4,5,6,7,10}
s2 = {10,20,30}

print(type(s1), type(s2))

# < 합집합 >
#1. s3 = s1.union(s2)     :아래와 동일
s3 = s1 | s2
print(s3)

# < 교집합 >
# 1. s4 = s1.intersection(s2) 
s4 = s1 & s2
print(s4)

# < 차집합 >
#1. s5 = s1-s2
s5 = s1.difference(s2)
print(s5)

s6 = s2.difference(s1)
print(s6)