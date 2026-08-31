from flask import Flask,session,render_template,redirect,request,jsonify,url_for,send_file
from flask_migrate import Migrate
from model import db,userLogin,events,registeredevents
from flask_bcrypt import Bcrypt
from sqlalchemy.exc import IntegrityError
from reportlab.pdfgen import canvas
from reportlab.lib import colors
import re
import io


app=Flask(__name__)
app.secret_key="123456"
bcrypt=Bcrypt(app)

app.config['SQLALCHEMY_DATABASE_URI']="mysql+pymysql://root:Krishnapriya22@localhost/event_management"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
db.init_app(app)
migrate=Migrate(app,db)

@app.route('/')
def home():
    return render_template('index.html',msg="")

@app.route('/adminpage')
def admin():
    return render_template("adminpage.html")

@app.route('/adminn')
def adminn():
    return render_template("adminn.html")

@app.route('/userpage')
def user():
    all_events = events.query.all()
    data=events.query.get(id)
    return render_template("userpage.html", events=all_events,data=data)

@app.route('/login',methods=['POST'])
def login():
    if request.method=='POST':
        username=request.form.get('username')
        password=request.form.get("password")
        account=userLogin.query.filter_by(username=username).first()
        if account and bcrypt.check_password_hash(account.password,password):
            session['loggedin']=True
            session['id']=account.id
            session['username']=account.username
            return jsonify({"status":"success"})
        else:
            return jsonify({
                "status":"error",
                "message":"Username doesn't exists."
            })
        
@app.route('/register',methods=["GET","POST"])
def register():
    failuremsg=''
    passwordmsg=''
    uerror=''
    if request.method=="POST":
        username=request.form.get("username")
        upattern=r'^.{8,}$'
        if not re.search(upattern,username):
            failuremsg="*username must contain 8 characters"
        email=request.form.get("email")
        contact=request.form.get("contact")
        clg=request.form.get("clg")
        dept=request.form.get("dept")
        password=request.form.get("password")
        ppattern=r'[!@#$%_&]'
        if not re.search(ppattern,password):
            passwordmsg="*password must contain one special character."
        if not failuremsg and not passwordmsg:
            hashed_password=bcrypt.generate_password_hash(password).decode('UTF-8')
            new_user=userLogin(username=username,password=hashed_password,email=email,contact=contact,collegename=clg,department=dept)
            try:
                db.session.add(new_user)
                db.session.commit()
                return redirect('/')
            except IntegrityError:
                db.session.rollback()
                uerror="Username already exists"
    return render_template("register.html",uerror=uerror,failuremsg=failuremsg,passwordmsg=passwordmsg)

@app.route('/userpage')
def userpage():
    if 'loggedin' not in session:
        return redirect('/')
    user_id=session['id']
    users=userLogin.query.filter_by(id=user_id).all()
    return render_template('userpage.html',users=users,username=session['username'])

@app.route('/adminlogin',methods=["GET","POST"])
def adminlogin():
    errormsg=''
    if request.method=="POST":
        username=request.form.get("username")
        password=request.form.get("password")
        if username=='admin' and password=='greenfield@':
            return redirect('/adminpage')
        else:
            errormsg="Invalid Credentials"
            return render_template('index.html')
    return render_template('index.html',errormsg=errormsg)

@app.route('/addevents', methods=["GET", "POST"])
def addevents():

    if request.method == "POST":

        eventname = request.form.get("eventname")
        eventdate = request.form.get("date")
        duration = request.form.get("time")
        participants = request.form.get("part")
        topics = request.form.get("topics")

        category_list = request.form.getlist("category")
        category = ",".join(category_list)

        new_events = events(eventname=eventname,eventdate=eventdate,duration=duration ,participants=participants,topics=topics,category=category)

        db.session.add(new_events)
        db.session.commit()

        return redirect('/viewevents')

    return render_template('addevent.html')

@app.route('/viewevents')
def viewevents():

    all_events = events.query.all()

    return render_template(
        'viewevents.html',
        events=all_events
    )

@app.route('/edit/<int:id>', methods=["GET", "POST"])
def edit(id):

    data = events.query.get_or_404(id)

    if request.method == 'POST':

        data.eventname = request.form['eventname']
        data.eventdate = request.form['date']
        data.duration = request.form['time']
        data.participants = request.form['part']
        data.topics = request.form['topics']

        db.session.commit()

    return redirect('/viewevents')

@app.route('/delete/<int:id>')
def delete(id):

    data = events.query.get_or_404(id)

    db.session.delete(data)
    db.session.commit()

    return redirect('/viewevents')

@app.route('/viewusers')
def viewusers():

    all_user = db.session.query(
        userLogin.username,
        userLogin.email,
        userLogin.contact,
        userLogin.collegename,
        userLogin.department
    ).all()

    return render_template(
        'viewuser.html',
        all_user=all_user
    )

@app.route('/events')
def events_filter():
    search = request.args.get("search")
    category = request.args.get("category")
    query = events.query
    if search:
        query = query.filter((events.eventname.like(f"%{search}%")))
    if category:
        query = query.filter(events.category.like(f"%{category}%"))
    events_list = query.all()
    return render_template('filterevents.html', events=events_list)

@app.route('/registerevents')
def registerevents():
    event_names = events.query.all()
    return render_template('eventregister.html',event_names=event_names)

@app.route('/userevents', methods=['GET', 'POST'])
def userevents():
    if request.method == "POST":
        if 'loggedin' not in session:
            return redirect('/')

        name = request.form.get('name')
        dept = request.form.get('dept')
        interest = request.form.get('interest')
        selected_event = request.form.getlist("selectedevent")
        selectedevent = ",".join(selected_event)

        register_events = registeredevents(
            user_id=session['id'],      
            name=name,
            dept=dept,
            interest=interest,
            selectedevent=selectedevent
        )
        db.session.add(register_events)
        db.session.commit()
        session['reg_id'] = register_events.id
        return redirect('/payment')
    return redirect('/registerevents')

@app.route('/payment')
def payment():
    return render_template("pay.html")

@app.route('/paymentsuccess')
def paymentsuccess():
    return render_template("paymentsuccess.html")

@app.route('/userregisterdevents')
def userregisteredevents():
    userregevents=registeredevents.query.all()
    return render_template('paymentreceipt.html',userregevents=userregevents)

@app.route('/receiptdownload')
def receiptdownload():
    reg_id = session.get('reg_id')
    if not reg_id:
        return redirect('/registerevents')   

    r = registeredevents.query.get(reg_id)   
    if not r:
        return redirect('/registerevents')

    buffer = io.BytesIO()
    pdf = canvas.Canvas(buffer)
    pdf.setTitle("Event Registration Receipt")

    pdf.setFillColorRGB(0.1, 0.3, 0.7)
    pdf.setFont("Helvetica-Bold", 18)
    pdf.drawCentredString(300, 750, "GreenField College of Engineering")

    y = 700
    pdf.setFillColorRGB(0.1, 0.5, 0.8)
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(80, y, "Registration Details")
    y -= 30

    pdf.setFillColorRGB(0.15, 0.15, 0.15)
    pdf.setFont("Helvetica", 11)

    pdf.drawString(80, y, f"Name: {r.name}")
    y -= 25

    pdf.drawString(80, y, f"Department: {r.dept}")
    y -= 25

    pdf.drawString(80, y, f"Selected Event: {r.selectedevent}")
    y -= 25

    pdf.setFillColorRGB(0.0, 0.55, 0.25)
    pdf.setFont("Helvetica-Bold", 11)
    pdf.drawString(80, y, "Registration fee of Rs.150 PAID SUCCESSFULLY")

    pdf.setStrokeColorRGB(0.1, 0.4, 0.8)
    pdf.line(100, y - 15, 500, y - 15)

    pdf.showPage()
    pdf.save()
    buffer.seek(0)

    return send_file(
        buffer,
        as_attachment=True,
        download_name="Event_Receipt.pdf",
        mimetype="application/pdf"
    )

@app.route('/dashboard')
def dashboard():
    total_events = events.query.count()
    registrations = registeredevents.query.all()
    total_registered_events = len(registrations)
    tech_count = 0
    nontech_count = 0
    event_registration_count = {}

    all_events = events.query.all()

    event_category = {}

    for event in all_events:
        event_category[event.eventname.strip()] = event.category.lower()

    for registration in registrations:

        if registration.selectedevent:

            selected_events = [
                e.strip()
                for e in registration.selectedevent.split(",")
                if e.strip()
            ]

            for selected_event in selected_events:

                if selected_event not in event_registration_count:
                    event_registration_count[selected_event] = 0

                event_registration_count[selected_event] += 1

                category = event_category.get(selected_event, "")

                if "non" in category and "tech" in category:
                    nontech_count += 1

                elif "tech" in category:
                    tech_count += 1

    event_names = list(event_registration_count.keys())
    event_counts = list(event_registration_count.values())
    return render_template(
        "dashboard.html",
        total_events=total_events,
        total_registered_events=total_registered_events,
        tech_count=tech_count,
        nontech_count=nontech_count,
        event_names=event_names,
        event_counts=event_counts
    )

@app.route('/logout')
def logout():
    return redirect('/')

@app.route("/myregistered")
def myregistered():
    if 'loggedin' not in session:
        return redirect("/")

    user_id = session['id']
    registrations = registeredevents.query.filter_by(user_id=user_id).all()

    registered_events = []
    for registration in registrations:
        if not registration.selectedevent:
            continue
        event_names = [e.strip() for e in registration.selectedevent.split(",") if e.strip()]
        for ename in event_names:
            event = events.query.filter_by(eventname=ename).first()
            if event:
                registered_events.append(event)

    return render_template("viewregisteredevents.html", registered_events=registered_events)