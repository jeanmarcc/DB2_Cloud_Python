import ibm_db

dsn_hostname = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" 
dsn_uid = "xxxxxxxx"         
dsn_pwd = "xxxxxxxxxxxxxxxx"      

dsn_driver = "{IBM DB2 ODBC DRIVER}"  #don't change this line, the driver comes along with ibm_db
dsn_database = "xxx"             
dsn_port = "xxxxx"                 
dsn_protocol = "TCPIP"            
dsn_security = "SSL"             

dsn = (
    "DRIVER={0};"
    "DATABASE={1};"
    "HOSTNAME={2};"
    "PORT={3};"
    "PROTOCOL={4};"
    "UID={5};"
    "PWD={6};"
    "SECURITY={7};"
    ).format(dsn_driver, dsn_database, dsn_hostname, dsn_port, dsn_protocol, dsn_uid, dsn_pwd,dsn_security)

print(dsn)

#
# connection to DB2
#
try:
    conn = ibm_db.connect(dsn, "", "")
    print ("Connected to database: ", dsn_database, "as user: ", dsn_uid, "on host: ", dsn_hostname)

except:
    print ("Unable to connect: ", ibm_db.conn_errormsg() )

server = ibm_db.server_info(conn)

#
# display some parameters of the db
#
print ("DBMS_NAME: ", server.DBMS_NAME)
print ("DBMS_VER:  ", server.DBMS_VER)
print ("DB_NAME:   ", server.DB_NAME)

#
# perform a simple query; table HOLDING has 3 fields: 'ticker_code', 'name' and 'currency' 
#
SelectQuery = "select * from MYSCHEM.HOLDING"
selectStmt = ibm_db.exec_immediate(conn, SelectQuery)
ibm_db.fetch_both(selectStmt)

while ibm_db.fetch_row(selectStmt) != False:
   print (ibm_db.result(selectStmt, "TICKER_CODE"),"---",ibm_db.result(selectStmt, "NAME"),ibm_db.result(selectStmt, "CURRENCY"))

#
# close the db 
#
try:
    conn = ibm_db.close(conn)
    print ("DB has been closed successfully")

except:
    print ("Unable to close Dtabase!!!")
