total_pen = int(input("전체 연필갯수를 입력해주세요: "))
total_per = int(input("전체 인원수를 입력해주세요.: "))

print(f"1인당 연필의 갯수는 {int(total_pen / total_per)} 입니다.")
print(f"나머지 갯수는 {total_pen % total_per} 입니다.")