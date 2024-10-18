no = int(input("단을 입력해주세요 \n"))

for i in range(1,10):
    print(f"{no} * {i} = {no*i}")


for n in range(1,10):
    for j in range(1,10):
        print(f"{n} * {j} = {n*j}")