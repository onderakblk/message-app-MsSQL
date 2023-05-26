import pyodbc
import connection


def login():
    print("*******************************************")
    name = input("username: ")
    pswd = input("password: ")
    conn = pyodbc.connect(connection.connection_string)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    results = cursor.fetchall()
    log = 0

    for row in results:
        if row[1] == name:
            if row[2] == pswd:
                log = 1
                break
            else:
                print("yanlis sifre")
                break
    else:
        print("yanlış kullanıcı adı")

    cursor.close()

    if log == 1:
        while True:
            print("*******************************************")
            menü = input("1-Önceden mesajlaştıklarınız\n2-Yeni mesaj\n3-Mesajları sil\n4-Çıkış\n")
            if menü == "1":
                cursor1 = conn.cursor()
                sql = 'SELECT DISTINCT buyer FROM mesage WHERE sender=?'
                value = [name,]
                cursor1.execute(sql,value)
                mesage = cursor1.fetchall()
                print("*******************************************")
                for x in mesage:
                    print(x[0])
                cursor1.close()


            elif menü == "2":
                print("*******************************************")
                user = input("Mesaj atmak istediğiniz kullanıcı: ")
                cursor6 = conn.cursor()
                cursor6.execute('SELECT * FROM users')
                resultss = cursor6.fetchall()
                log = 0

                for row in resultss:
                    if row[1] == user:
                        log=1
                else:
                    print("yanlış kullanıcı adı")
                cursor6.close()

                if log==1:
                    cursor2 = conn.cursor()
                    sql = 'SELECT * FROM mesage WHERE (sender=? and buyer=?) or (sender=? and buyer=?)'
                    value = [name,user,user,name]
                    cursor2.execute(sql,value)
                    mesagee = cursor2.fetchall()
                    print("*******************************************")
                    for y in mesagee:
                        print(f"{y[1]}: {y[3]}")
                    cursor2.close()


                    while True:
                        print("*******************************************")
                        print("Çıkmak için 'çıkış' yazınız")
                        msg = input("Ne mesaj atmak istersiniz: ")
                        if msg == "çıkış":
                            break

                        else:
                            cursor3 = conn.cursor()
                            sql = 'INSERT INTO mesage(sender, buyer, message) VALUES (?, ?, ?)'
                            valuess = [name,user,msg]
                            cursor3.execute(sql,valuess)
                            conn.commit()
                            cursor3.close()

                            cursor4 = conn.cursor()
                            sql = 'SELECT * FROM mesage WHERE (sender=? and buyer=?) or (sender=? and buyer=?)'
                            valuesss = [name,user,user,name]
                            cursor4.execute(sql,valuesss)
                            mesagee = cursor4.fetchall()
                            print("*******************************************")
                            for y in mesagee:
                                print(f"{y[1]}: {y[3]}")
                            
                            cursor4.close()
                

            elif menü == "3":
                print("*******************************************")
                print("Hangi kullanıyla olan konuşmayı silmek istersin")
                userrname = input("kullanıcı adı: ")
                cursor5 = conn.cursor()
                sql = "DELETE FROM mesage WHERE (sender=? and buyer=?) or (sender=? and buyer=?)"
                params = (userrname,name,name,userrname)
                cursor5.execute(sql,params)
                conn.commit()
                cursor5.close()
                


            elif menü == "4":
                break

            else:
                print("Hatalı işlem") 
    

    conn.close()




def insert():
    print("*******************************************")
    user = input("kullanıcı adı: ")
    pswd = input("şifre: ")
    name = input("isim: ")
    surname = input("soyisim: ")
    mail = input("email: ")
    number = input("Telefon no: ")
    print("*******************************************")
    conn = pyodbc.connect(connection.connection_string)
    cursor1 = conn.cursor()
    cursor1.execute('SELECT * FROM users')
    result = cursor1.fetchall()
    for x in result:
        if x[1] == user:
            print("Bu kullanıcı adı alınmış")
            cursor1.close()
            break
    else:
        cursor1.close()
        cursor = conn.cursor()
        sql = 'INSERT INTO users(username_, password_, name, surname, email, number) VALUES (?, ?, ?, ?, ?, ?)'
        values = [user,pswd,name,surname,mail,number]
        cursor.execute(sql,values)
        conn.commit()
 
    conn.close()

def menü1():
    while True:
        print("*******************************************")
        menü = input("1-Giriş yap\n2-Kayıt ol\n3-Çıkış\n")
        if menü == "1":
            login()

        elif menü == "2":   
            insert()
        elif menü == "3":
            break
        else:
            print("Yanlış seçim: ")

menü1()
