from openpyxl import Workbook
import random

# 제품 데이터 생성 함수
def generate_product_data():
    products = []
    for i in range(100):
        product_id = i + 1
        product_name = f"제품{product_id}"
        quantity = random.randint(1, 100)
        price = round(random.uniform(10, 1000), 2)
        products.append((product_id, product_name, quantity, price))
    return products

# 제품 데이터 가져오기
product_data = generate_product_data()

# Excel 파일 생성 및 데이터 쓰기
workbook = Workbook()
sheet = workbook.active
sheet.append(["제품ID", "제품명", "수량", "가격"])

for product in product_data:
    sheet.append(product)

# 파일 저장
workbook.save(filename="c:/work/products.xlsx")
print("파일이 성공적으로 저장되었습니다.")
