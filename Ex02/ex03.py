# 딕션어리 키-값

a = {}
a['r38'] = '빅데이터반'
a['r32'] = '풀스택반'
a['r30'] = '추가'

print(a)

d = {'basketball':5, 'soccer':3, 'baseball': 7}
print(d)

#값 추가하고싶을 때
d['volleyball'] = 6
print(d)

# 키로 값 출력
print(a['r30'])
print(a['r32'])
print(a['r38'])


#삭제는 remove, pop 둘다 동일하게 사용

#전체삭제
#1. d = {}
#2. d.clear()

# 찾기

d = {'basketball':5, 'soccer':11, 'baseball':9}
print('soccer' in d)
print('soccer' not in d)



# =============== 딕션어리의 키들을 리스트로 반환 ===================
d = {'basketball':5, 'soccer':11, 'baseball':9}
keys = d.keys()
print(keys, type(keys))

for key in keys:
    print(key)

#딕션어리의 값을 기존 vo했던것처럼 묶어서 리스트로 관리
play_list = d.items()
print(play_list,type(play_list))
print(play_list[0])


