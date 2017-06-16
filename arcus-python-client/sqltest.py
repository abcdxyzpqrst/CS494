import pymysql
import datetime, time, sys

def main():
    conn = pymysql.connect(host='172.17.0.7', user='arcprime', password='slzmfh719', db='sampledb', charset='utf8')
    print ("\n########## Connection Success! ##########")

    cursor = conn.cursor()
    
    query1 = "select name from Student where id=20120001"
    query2 = "select name from Student where id=20120002"
    query3 = "select name from Student where id=20120003"
    query4 = "select name from Student where id=20120004"
    query5 = "select name from Student where id=20120005"

    start_time = time.time()
    cursor.execute(query1)
    cursor.execute(query2)
    cursor.execute(query3)
    cursor.execute(query4)
    cursor.execute(query5)
    end_time = time.time()

    print ("########## MySQL Running Time ##########")
    print (end_time - start_time)
    print ("")

    return

if __name__ == "__main__":
    main()
