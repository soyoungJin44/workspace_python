#파일 읽기

file_path = "C:\\javaStudy\\workspace_python\\Ex02\\PhoneDB.txt"

file = open(file_path, "r", encoding="UTF-8")
data = file.read()
print(data)
file.close()

#파일 한줄씩 읽기1
file = open(file_path, "r", encoding="UTF-8")
for line in file:
    print(line.strip())     #문자열 자체적으로 가지고있는 문법임. \n부분 파일에 붙어있는거 빼주는거
file.close()

#파일 읽기2 ( with문 )  close안해줘도됨. 블록이 끝나면 알아서 해줌
with open(file_path, "r", encoding="UTF-8") as file:
    data = file.read()
