
# MySQL 8.0.28

def Connect_to_database():
    global msql_server
    print("check")

    if mysql_server == None or mysql_server.is_connected() == False:
        sip =  read_from_reg("sip").split(";")
        print(sip)
        mydb = mysql.connector.connect(
            host = sip[0],
            port = sip[1],
            user = "text something",
            password = "text something",
            charset=  "utf8",
            autocommit =True
        )
        mysql_server  = mydb
    mysql_server.ping(True)

    return mysql_server

def mysql_server_glob(sql_str ="", sql_parameter =[]):
    state = True
    sql_list=[]
    print("SQL Query", sql_str)
    mydb = Connect_to_database()

    with mydb.cursor(buffered= False, dictionary = True) as cur:
        try:
            cur.execute(sql_str, sql_parameter)
            sql_list  =cur.fetchall()
            state= True
        except mysql.connector.Error as err:
            mydb.rollback()
            print("Sql error": err)
            print("Error code": err.errno)
            state =  False
        cur.close()

        print("Global sql result = " + str(sql_list))
    return state, sql_list