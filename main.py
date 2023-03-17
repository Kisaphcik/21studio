from bs4 import BeautifulSoup
import sqlite3

db = sqlite3.connect('PC_database.db')
cur = db.cursor()
cur.execute("""CREATE TABLE data(
    name TEXT,
    price TEXT,
    link TEXT
)""")


def func(page):
    with open(f"html_DNS/{page}.html", 'r', encoding="utf8") as f:
        soup = BeautifulSoup(f, 'lxml')

        for el in soup.select(".catalog-products > .catalog-product"):
            name = el.select(".catalog-product__name > span")
            link = el.find('a').get('href')
            price = el.select(".product-buy__price-wrap > .product-buy__price")[0].text.split("₽")
            cur.execute("INSERT INTO data VALUES(?, ?, ?)", (name[0].text, price[0], f"https://www.dns-shop.ru{link}"))


for i in range(1, 13):
    func(i)

db.commit()
db.close()