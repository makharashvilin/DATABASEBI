import sqlite3

conn = sqlite3.connect('book_db.sqlite')
# conn.row_factory = sqlite3.Row
cursor = conn.cursor()
cursor.execute("SELECT * FROM books")


# cursor.execute("SELECT * FROM books WHERE author='William Shakespeare'")

# cursor.execute("SELECT * FROM books WHERE author='William Shakespeare' OR author='Rowling'")

# cursor.execute("SELECT * FROM books WHERE price<=20")

# results = cursor.execute("SELECT author from books").fetchall()
# res = []
# for row in results:
#     if row not in res:
#         res.append(row)
# print(res)

# cursor.execute("SELECT username FROM users WHERE balance>100")

# cursor.execute("SELECT book_id FROM purchase WHERE purchase_date<2018")



records = cursor.fetchall()
for record in records:
    print(record)
conn.commit()
