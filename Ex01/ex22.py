color_list = ['red', 'yellow', 'green', 'blue']

for color in color_list:
    print(color)


#index번호 한방에 출력
for index, color in enumerate(color_list):
    if index>3:
        break
    else :
        print(index, color)