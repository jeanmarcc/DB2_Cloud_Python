import ibm_db

#Replace the placeholder values with your actual Db2 hostname, username, and password:
dsn_hostname = "d14b6a23-7db2-4b61-90c3-73a036873b46.c7o11g2r0m1anejc44rg.databases.appdomain.cloud" # e.g.: "54a2f15b-5c0f-46df-8954-7e38e612c2bd.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud"
dsn_uid = "d85f99e8"        # e.g. "abc12345"
dsn_pwd = "L7xTJqHBNBp9ttEy"      # e.g. "7dBZ3wWt9XN6$o0J"

dsn_driver = "{IBM DB2 ODBC DRIVER}"
dsn_database = "BLUDB"            # e.g. "BLUDB"
dsn_port = "31998"                # e.g. "32733" 
dsn_protocol = "TCPIP"            # i.e. "TCPIP"
dsn_security = "SSL"              #i.e. "SSL"
# SSLSERVERCERTIFICATE="C:\\temp\DigiCertGlobalRootCA.crt"
#DO NOT MODIFY THIS CELL. Just RUN it with Shift + Enter
#Create the dsn connection string
dsn = (
    "DRIVER={0};"
    "DATABASE={1};"
    "HOSTNAME={2};"
    "PORT={3};"
    "PROTOCOL={4};"
    "UID={5};"
    "PWD={6};"
    "SECURITY={7};"
    # "SSLSERVERCERTIFICATE={8};"
    ).format(dsn_driver, dsn_database, dsn_hostname, dsn_port, dsn_protocol, dsn_uid, dsn_pwd,dsn_security)

#print the connection string to check correct values are specified
# print(dsn)

#DO NOT MODIFY THIS CELL. Just RUN it with Shift + Enter
#Create database connection

try:
    conn = ibm_db.connect(dsn, "", "")
    print ("Connected to database: ", dsn_database, "as user: ", dsn_uid, "on host: ", dsn_hostname)

except:
    # print(vars(ibm_db))
    print ("Unable to connect: ", ibm_db.conn_errormsg() )

# Retrieve Metadata for the Database Server
server = ibm_db.server_info(conn)

# print ("DBMS_NAME: ", server.DBMS_NAME)
# print ("DBMS_VER:  ", server.DBMS_VER)
# print ("DB_NAME:   ", server.DB_NAME)


SelectQuery = "select * from MYSCHEM.HOLDING"
selectStmt = ibm_db.exec_immediate(conn, SelectQuery)
ibm_db.fetch_both(selectStmt)

while ibm_db.fetch_row(selectStmt) != False:
   print (ibm_db.result(selectStmt, "TICKER_CODE"),"---",ibm_db.result(selectStmt, "NAME"),ibm_db.result(selectStmt, "CURRENCY"))



# Now we do a call to a DB2 PROCEDURE that returns the full name of a Ticker
resultCallProc = ibm_db.callproc(conn, 'PROC_GET_NAME', ('1','?'))
print("The company name related to this ticker is: ",resultCallProc[2])

resultCallProc = ibm_db.callproc(conn, 'PROC_GET_CURRENCY', ('AQN','?'))
print("The company name related to this ticker is: ",resultCallProc[2])

try:
    conn = ibm_db.close(conn)
    print ("DB has been closed successfully\n")

except:
    print ('%n',"Unable to close Database!!!\n")
