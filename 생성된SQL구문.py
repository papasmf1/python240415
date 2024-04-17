import sqlite3
import random
import string

class ProductDatabase:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS products (
                            id INTEGER PRIMARY KEY,
                            name TEXT,
                            price REAL
                            )''')
        self.conn.commit()

    def insert_product(self, name, price):
        self.cur.execute('''INSERT INTO products (name, price) VALUES (?, ?)''', (name, price))
        self.conn.commit()

    def update_product_price(self, product_id, new_price):
        self.cur.execute('''UPDATE products SET price = ? WHERE id = ?''', (new_price, product_id))
        self.conn.commit()

    def delete_product(self, product_id):
        self.cur.execute('''DELETE FROM products WHERE id = ?''', (product_id,))
        self.conn.commit()

    def select_product_by_id(self, product_id):
        self.cur.execute('''SELECT * FROM products WHERE id = ?''', (product_id,))
        return self.cur.fetchone()

    def generate_random_string(self, length=6):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for i in range(length))

    def generate_sample_data(self, num_samples=100):
        for _ in range(num_samples):
            name = self.generate_random_string()
            price = random.uniform(100, 1000)
            self.insert_product(name, price)

# 예제로 사용할 데이터베이스 파일명
db_name = 'products.db'

# 데이터베이스 객체 생성
product_db = ProductDatabase(db_name)

# 샘플 데이터 생성
product_db.generate_sample_data()

# 제품 조회 예제
product_id = 1
print("Product with ID", product_id, ":", product_db.select_product_by_id(product_id))

# 제품 가격 업데이트 예제
product_db.update_product_price(product_id, 500)
print("Updated product with ID", product_id, ":", product_db.select_product_by_id(product_id))

# 제품 삭제 예제
product_db.delete_product(product_id)
print("Deleted product with ID", product_id)

# 연결 종료
product_db.conn.close()
