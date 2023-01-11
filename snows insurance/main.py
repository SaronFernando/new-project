from flask import Flask,render_template, request, redirect
import utils.json_utils as json_utils

file="data/user.json"


app=Flask(__name__)
@app.route("/")
def index ():
    return render_template('main_page.html')

@app.route("/get_insurance",methods=["GET","POST"])
def register():
    return render_template("register.html")

@app.route("/register",methods=["GET","POST"])
def new_register():
    if request.method=="POST":
        name=request.form["name"]
        email=request.form["email"]
        phone=request.form["phone"]
        password=request.form["password"]
        data=json_utils.read_json(file)
        user={
            "name":name,
            "email":email,
            "phone":phone,
            "password":password,
        }
        data["user"].append(user)
        json_utils.write_json(file,data)
    return redirect("main_page.html")
            
            
                    
    
    
    

        

if __name__=="__main__"  :
    app.run(debug=True)
