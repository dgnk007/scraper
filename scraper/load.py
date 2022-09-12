import multi_scrap,psycopg2
items = ['laptop','t shirt','smart phone',]
data = multi_scrap.flipkartPage('laptop',1,21)
postgres_insert_query = """ INSERT INTO importflipkart (id, title, link,price) VALUES (%s,%s,%s,%s)"""
conn = psycopg2.connect(database="scraper", user='postgres', password='Axims0ft123', host='localhost', port= '5432')
cursor = conn.cursor()
for i in data:
    cursor.execute(postgres_insert_query, (i["id"],i["title"], i["link"],i["price"]))
conn.commit()
conn.close()


