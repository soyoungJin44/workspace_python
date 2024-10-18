price = float(input("상품가격: "))
pay = float(input("받은금액: "))
vat_rate = 0.10

print("===========================")
print(f"받은돈: {pay}")
print(f"상품가격: {price}")
print(f"부가세: {price*vat_rate}")
print(f"거스름돈: {pay-price}")