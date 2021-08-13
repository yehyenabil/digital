from app import app
from flask import render_template,redirect ,request  ,flash,session
from flask_sqlalchemy import SQLAlchemy


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
db = SQLAlchemy(app)
app.secret_key = 'somesecretkeythatonlyishouldknow'


class contact(db.Model):

    __tablename__ = "contact"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String, nullable=False)
    message = db.Column(db.String) 
    phone = db.Column(db.String)
    bessines = db.Column(db.String) 



    def __init__(self, name, email, message,phone,bessines):
        self.name = name
        self.email = email
        self.message =(message)
        self.phone = phone
        self.bessines = bessines
        
        
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return (self.id)

    def __repr__(self):
        return '<name - {}>'.format(self.name)
class user(db.Model):

    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String) 
    phone = db.Column(db.String)
    bessines = db.Column(db.String) 



    def __init__(self, name, email, password,phone,bessines):
        self.name = name
        self.email = email
        self.password =(password)
        self.phone = phone
        self.bessines = bessines

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return (self.id)

    def __repr__(self):
        return '<name - {}>'.format(self.name)




@app.route('/',methods=["POST", "GET"])
def home_page():
    if "name" in session:
        name=session["name"]
        return  redirect(f"/{name}")
    
        
        
    return render_template('home.html')

@app.route('/forget',methods=["POST", "GET"])
def forget():
    if "name" in session:
        name=session["name"]
        return  redirect(f"/{name}")
    
        
        
    return render_template('forget.html')
        
@app.route('/home',methods=["POST", "GET"])
def home():
    if "name" in session:
        name=session["name"]
        return  redirect(f"/{name}")
    if request.method == 'POST':
        email = request.form['email']
        
        s = contact(name=None,email=email,message=None,phone=None,bessines=None)
        db.session.add(s)
        db.session.commit()
        flash("THANKS...")   
        return render_template('home.html')
      
    return render_template('home.html')
@app.route('/about',methods=["POST", "GET"])
def about():
    if "name" in session:
        name=session["name"]
        return  redirect(f"/{name}")
    if request.method == 'POST':
        email = request.form['email']
        
        s = contact(name=None,email=email,message=None,phone=None,bessines=None)
        db.session.add(s)
        db.session.commit()
        flash("THANKS...")   
        return render_template('about.html')
    return render_template('about.html')
@app.route('/post',methods=["POST", "GET"])
def post():
    if "name" in session:
        name=session["name"]
        return  redirect(f"/{name}")
    if request.method == 'POST':
        email = request.form['email']
        
        s = contact(name=None,email=email,message=None,phone=None,bessines=None)
        db.session.add(s)
        db.session.commit()
        flash("THANKS...")   
        return render_template('post.html')
    return render_template('post.html')
@app.route('/contact',methods=["POST", "GET"])
def contact1():
    if "name" in session:
        name=session["name"]
        return  redirect(f"/{name}")
    
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        bessines=request.form['bessines']
        message = request.form['message']
        
        s = contact(name=name,email=email,message=message,phone=phone,bessines=bessines)
        db.session.add(s)
        db.session.commit()

        return redirect('/home')
       

    else:
        return render_template('contact.html')
    
@app.route('/<name>',methods=["POST", "GET"])
def user1(name):
    if "name" not in session:
        return render_template('home.html')
    return render_template('user12.html',name=name)

@app.route("/login",methods=["GET", "POST"])
def login():
    if "name" in session:
        name=session["name"]
        return  redirect(f"/{name}")
    if request.method == "POST":
        uname = request.form["email"]
        passw = request.form["password"]
       
        
        login = user.query.filter_by(email=uname, password=passw).first()
        if login is not None:         
            session["name"]=login.name
            return  redirect(f"/{login.name}")
        else:
            flash("your email or password is incorrect!")   
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if "name" in session:
        name=session["name"]
        return  redirect(f"/{name}")
    if request.method == "POST":
        uname = request.form['name']
        mail = request.form['email']
        phone = request.form['phone']
        bessines = request.form['bessines']
        passw = request.form['password']
        

        register = user(name = uname,email = mail, password = passw, phone=phone,bessines=bessines)
        db.session.add(register)
        db.session.commit()
        session["name"]=register.name
        return redirect(f"/{register.name}")
    return render_template("register.html")


@app.route("/logout", methods=["GET", "POST"])
def logout1():
    session.clear()
    return render_template('home.html')



