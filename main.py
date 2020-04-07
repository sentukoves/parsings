import sqlite3 as s

conn = s.connect("base.db")
curs = conn.cursor()

curs.execute('select * from hh')

#curs.execute("INSERT INTO hh(proff, price) VALUES ('Прог' ,150000)")
#conn.commit()
#print(curs.fetchall())


aaa = 'от 70 000 руб.'



"""
mass = curs.fetchall()
print(mass)
for i in range(len(mass)):
    if 'от' in aaa:
        print(int(str(mass[i][2]).replace("от ", "").replace(" руб.", "").replace(" ","")))
    else:
        print(mass[i][2])
"""

from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://saratov.hh.ru/search/vacancy?area=&st=searchVacancy&text=%D0%9F%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%81%D1%82&from=suggest_post")


hhs = []
prices = driver.find_elements_by_xpath('//span[@class = "bloko-section-header-3 bloko-section-header-3_lite"]')
for items in prices:
    hhs.append(items.text)
ma1=hhs[0::2]
ma2=hhs[1::2]

for i in range(len(ma2)):
    curs.execute(f"insert into hh(proff, price) VALUES ('{ma1[i]}','{ma2[i]}')")
    conn.commit()