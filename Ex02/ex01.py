test_list = [1, 12, 123, 1234]
print(test_list[0], test_list[3])
print(test_list[-1])

str = 'First Strint'
print(str[1:4])

print(test_list[2:3])

#갯수 알아내기  len()
print(len(test_list))

print((test_list *2)[3])
print(test_list)

print(test_list + [100, 200, 300])
print(test_list)

print(13 in test_list)

print("==== 리스트 삭제 ====")

# [] 번째 값 삭제. 바로 반영됨
del(test_list[0])
print(test_list)

# [] 번째 값 수정. 바로 반영됨
test_list[0] = 20
test_list[0] = 'apple'
print(test_list)

b_list = ['apple', 'banana', 10, 20]
print(b_list)

# -- 2번째에 있는 값을 꺼내서, 이 값을 넣어주세요.
b_list[2] = b_list[2] + 90
print(b_list)

test_list = [1, 12, 123, 1234]
print(test_list)
#(0번부터 2개)
test_list[0:2] = [888, 999]
print(test_list)

#2개값이 변경되는게 아니라 0번부터 2개의 값이 777로 변경된다.
test_list[0:2] = [777]
print(test_list)


print("================ 슬라이드를 통한 삽입 ===================")
a = [1, 12, 123, 1234]

a[1:1] = ['a', 'b']
print(a)


#슬라이싱 문법. 방 번호가 같으면 추가 [3:3]
# //list메소드 사용
print("=================== 리스트 메소드 사용")

a = [1, 12, 123, 'hello', 3.14, 1000]
print(a)

# <추가>

#제일 마지막으로 추가됨 (1개만 가능)
a.append('진')
print(a)

#내가 원하는곳에 값 추가
a.insert(2,'영')
print(a)

#여러개의 값을 추가할 때 (값 뒤로 들어감)
a.extend([6, 7, 8])
print(a)

# <삭제>

#1000을 지워줘
a.remove(1000)
print(a)

# 방번호 해당값 지워줘
a.pop(6)
print(a)

#pop안에 비워두면 마지막값을 지워줌 
a.pop()
print(a)

print("=================== 리스트 메소드 사용2")

#b에 12가 몇개있는지
b = [1, 12,12, 123, 1234]
print(b.count(12))

#순서 뒤집기
b.reverse()
print(b)

#정렬
b.sort()   #오름차순
print(b)
b.sort(reverse=True)   #내림차순
print(b)

#값으로 index 번호 찾기
print(b.index(1))

