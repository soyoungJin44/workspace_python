#1번 리스트 출력
def list():
    #파일 읽기
    file_path = "C:\\javaStudy\\workspace_python\\Ex02\\PhoneDB.txt"

    #한줄씩 읽기
    with open(file_path, "r", encoding="UTF-8") as file:
        data = file.read().strip()
        line = data.splitlines()

        for index, line in enumerate(line, start=1):
            name, hp, company = line.split(",")
            print(f"{index}. {name.strip():<6} {hp.strip():<17} {company.strip():<17}")


#2번 등록
