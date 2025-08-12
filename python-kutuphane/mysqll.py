import mysql.connector


conn=mysql.connector.connect(
    host= "localhost",
    user= "root",
    password= "",
    database= "pythonsql"
)
cursor=conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT)")
cursor.execute("INSERT INTO users (name, age) VALUES ('John', 25)") ## cursor.execute mysql komutlarını çalıştırır
conn.commit()
cursor.close()
conn.close()

)