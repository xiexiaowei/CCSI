import MySQLdb
import csv
conn=MySQLdb.connect(host='localhost',user ='user_name',passwd='password',db='ccsi')
cur=conn.cursor() 
#take uploading hic data for example:
for k in range(1,40):
    with open('hic-'+str(k)+'.csv', 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        T=[]
        for row in spamreader:
            t=tuple(row) #change list into tuple
            T.append(t)
        cur.executemany("insert into interaction values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", T)     
conn.commit() # must be needed before close
cur.close()
conn.close()
print 'ok'
