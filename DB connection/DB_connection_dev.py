import pyodbc
conn = pyodbc.connect('DSN=jiva_61sp_dev;UID=jiva_dev_user;PWD=J!va_6ev_user;')
# 'Trusted_Connection=yes;')
cursor = conn.cursor()
result = cursor.execute('SELECT top 1 mbr_idn FROM mbr with (nolock) order by 1 desc')
print(result.fetchone())