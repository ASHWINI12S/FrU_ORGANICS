from flask import *
from DBM import *

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/home")
def homepage():
    return render_template("home.html")
    

@app.route("/about")
def aboutus():
    return render_template("about.html")


@app.route("/login",methods = ["POST"])
def login():
    username = request.form['username']
    password = request.form['password']

    t  =(username,password)
    user= showuser(t)
    if len(user)!= 0:
        return render_template("home.html")
    else:
        return render_template("register.html")
    

@app.route("/logout")
def logout():
    return redirect("/")

@app.route("/reg")
def register():
    return render_template("register.html")

@app.route("/emplist")
def emp_list():
    el = selectAllEmp()
    return render_template("emplist.html",elist = el)

@app.route("/addEmp",methods=["POST"])
def add_emp():
    idi= request.form["id"]
    name = request.form["name"]
    contact = request.form["contact"]
    email = request.form["email"]
    username =  request.form["username"]
    password = request.form["password"]
    
    

    t = (idi,name,contact,email,username,password)
    addEmp(t)
    
    return render_template("login.html")

@app.route("/update",methods=["POST"])
def updaterec():
    idi= request.form["id"]
    name = request.form["name"]
    contact = request.form["contact"]
    email = request.form["email"]
    username =  request.form["username"]
    password = request.form["password"]
    
    t = (name,contact,email,username,password,idi)
    updateEmp(t)

    return redirect("/emplist")
    
@app.route("/myupdate")
def showrec():
    idi=request.args.get("id")
    elist=selectEmpById(idi)
    return render_template("update.html",elist=elist)

 
@app.route("/mydelete")
def delrec():
    idi=request.args.get("id")
    deleteEmp(idi)
    return redirect("/emplist")


  


##@app.route("/login",methods=['POST'])
##def login():
##    username=request.form['username']
##    password=request.form['password']
##    t=(username,password)
##    user=showusers()
##    if t in user:
##        return render_template("home.html")
##    else:
##         return render_template("register.html")
##        


if (__name__ == "__main__"):
    app.run()
