import pymysql as p
def getConnection():
    return p.connect(host='localhost',user='root',password='',database='mkpbatch')
    
def addEmp(t):
    db=getConnection()
    sql='insert into emp values(%s,%s,%s,%s,%s,%s)'
    cr=db.cursor()
    cr.execute(sql,t)
    db.commit()
    db.close()

def showrec():
    db =  getConnection()
    cr = db.cursor()
    sql ="selct * from emp"
    cr.execute(sql)
    elist = cr.fetchall()
    db.commit()
    db.close()
    return elist

def selectAllEmp():
    db=getConnection()
    sql='select * from emp'
    cr=db.cursor()
    cr.execute(sql)
    elist=cr.fetchall()
    db.commit()
    db.close()
    return elist

def showuser(t):
    db = getConnection()
    cr = db.cursor()
    sql = "select * from emp where username =%s and password = %s"
    cr.execute(sql,t)
    elist = cr.fetchall()
    db.commit()
    db.close()
    return elist

##
##def showusers():
##    db=getConnection()
##    cr=db.cursor()
##    sql="select username,password from emp"
##    cr.execute(sql)
##    elist=cr.fetchall()
##    db.commit()
##    db.close()
##    return elist




    
    
def deleteEmp(id):
    db=getConnection()
    sql='delete from  emp where id=%s'
    cr=db.cursor()
    cr.execute(sql,id)
    db.commit()
    db.close()

def selectEmpById(id):
    db=getConnection()
    sql='select * from emp where id=%s'
    cr=db.cursor()
    cr.execute(sql,id)
    elist=cr.fetchall()
    db.commit()
    db.close()
    return elist[0]

def updateEmp(t):
    db=getConnection()
    sql='update emp set name=%s,contact=%s,email=%s,username=%s,password=%s where id=%s'
    cr=db.cursor()
    cr.execute(sql,t)
    db.commit()
    db.close()

def updatepass(username):
    db=getconnect()
    cr=db.cursor()

    sql="select * from myemp where username=%s"
    cr.execute(sql,username)

    data=cr.fetchall()
        
    db.commit()
    db.close()
    return data[0]
