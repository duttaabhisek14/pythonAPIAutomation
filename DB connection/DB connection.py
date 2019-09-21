import mysql.connector
cnx = mysql.connector.connect(user='bcbsfl_app_user', password='bcbsfl_app_user',
                              host='POCWCSGCIDB1\SQL2016CI',
                              database='BCBSFL_61_Integration')

try:
   cursor = cnx.cursor()
   cursor.execute("""
      select * from mbr_enc
   """)
   result = cursor.fetchall()
   print result
finally:
    cnx.close()