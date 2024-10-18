print("#패킹과 언패킹============")


'''
z01 = 10
z02 = 20
z03 = 'python'

t = [z01, z02, z03]
print(t)
'''

t = 10,20,'python'      #튜플로 묶어서 변수에 할당.
print(t)

print(t[0])         #꺼내기 가능
print(t[1])

item01 = t[0]
item02 = t[1]
item03 = t[2]

print(item01, item02, item03)

print(type(t))

a_list = list(t)
print(type(a_list))
print(a_list)

# ============ 튜플 => set 으로 변형
print(">>>>>>>>>>>>>>>>>>>")
t = (1,2,3)
# print(t)

s_set = set(t)
print(s_set)




