import pickle
from webbrowser import get
from flask import Flask, request, make_response, redirect, url_for,session,logging,request, flash, abort
from flask.templating import render_template
#from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
import sklearn
import numpy as np

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dbase1.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

app.secret_key = 'randomstringapapun'


class user(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        nama_penanggung = db.Column(db.String(80))
        emails = db.Column(db.String(120))
        password = db.Column(db.String(80))
        prov = db.Column(db.String(80))
        kota = db.Column(db.String(80))
        kec = db.Column(db.String(80))
        desa = db.Column(db.String(80))
        status = db.Column(db.String(20))
        idm = db.Column(db.Float)
        iks = db.Column(db.Float)
        ike = db.Column(db.Float)
        ikl = db.Column(db.Float)

class dt_desa(db.Model):
    id_dt = db.Column(db.Integer, primary_key=True)
    stat_dt = db.Column(db.String(20))
    # idm_dt = db.Column(db.Float)
    # iks_dt = db.Column(db.Float)
    # ike_dt = db.Column(db.Float)
    # ikl_dt = db.Column(db.Float)
    col_e = db.Column(db.Integer)
    col_f = db.Column(db.Integer)
    col_g = db.Column(db.Integer)
    col_h = db.Column(db.Integer)
    col_i = db.Column(db.Integer)
    col_j = db.Column(db.Integer)
    col_k = db.Column(db.Integer)
    col_l = db.Column(db.Integer)
    col_m = db.Column(db.Integer)
    col_n = db.Column(db.Integer)
    col_o = db.Column(db.Integer)
    col_p = db.Column(db.Integer)
    col_q = db.Column(db.Integer)
    col_r = db.Column(db.Integer)
    col_s = db.Column(db.Integer)
    col_t = db.Column(db.Integer)
    col_u = db.Column(db.Integer)
    col_v = db.Column(db.Integer)
    col_w = db.Column(db.Integer)
    col_x = db.Column(db.Integer)
    col_y = db.Column(db.Integer)
    col_z = db.Column(db.Integer)
    col_aa = db.Column(db.Integer)
    col_ab = db.Column(db.Integer)
    col_ac = db.Column(db.Integer)
    col_ad = db.Column(db.Integer)
    col_ae = db.Column(db.Integer)
    col_af = db.Column(db.Integer)
    col_ag = db.Column(db.Integer)
    col_ah = db.Column(db.Integer)
    col_ai = db.Column(db.Integer)
    col_aj = db.Column(db.Integer)
    col_ak = db.Column(db.Integer)
    col_al = db.Column(db.Integer)
    col_am = db.Column(db.Integer)
    col_an = db.Column(db.Integer)
    col_ao = db.Column(db.Integer)
    col_ap = db.Column(db.Integer)
    col_aq = db.Column(db.Integer)
    col_ar = db.Column(db.Integer)
    col_as = db.Column(db.Integer)
    col_at = db.Column(db.Integer)
    col_au = db.Column(db.Integer)
    col_av = db.Column(db.Integer)
    col_aw = db.Column(db.Integer)
    col_ax = db.Column(db.Integer)
    col_ay = db.Column(db.Integer)
    


@app.route('/')
def index():
    flash('Silahkan Masuk atau Daftarkan Desa Anda','info')
    return render_template('index.html')

@app.route('/dash/<email>')
def dash(email):
    getdt = user.query.filter_by(emails=email).first_or_404() 
    if getdt is None:
        return render_template('index.html')   
    return render_template('dash.html', showdt=getdt)

@app.route("/login",methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if request.form['email'] == '' or request.form['passwd'] == '' :
            abort(401)

        session['email'] = request.form["email"]
        paswd = request.form["passwd"]
        
        getdt = user.query.filter_by(emails=session['email'], password=paswd).first_or_404()
        if getdt is not None:
            flash('Login Berhasil dilakukan','success')
            return redirect(url_for("dash", email=getdt.emails))
        else :
            flash('Gagal Melakukan Login','error')
            return render_template("login.html")
    return render_template("login.html")

@app.route('/registrasi', methods=["GET", "POST"])
def regis():
    db.create_all()
    if request.method == "POST":
        des_id = request.form["id_desa"]
        penang = request.form["nama_penang"]
        email = request.form["email"]
        paswd = request.form["passwd"]
        provin = request.form["provinsi"]
        kot = request.form["kota"]
        kece = request.form["kecem"]
        des = request.form["nam_desa"]
       
        register = user(id=des_id,nama_penanggung = penang, emails= email, password = paswd,
                         prov = provin, kota = kot, kec= kece, desa = des, 
                         status = None, idm=None, iks=None, ike=None, ikl=None)
        db.session.add(register)
        db.session.commit()
        flash('Data Desa sudah ditambahkan','success')
        return redirect(url_for("login"))
    return render_template("regis.html")

@app.route('/predict/<ides>', methods=['GET', 'POST'])
def predict(ides):
    
    getdt = user.query.filter_by(id=ides).first_or_404()
    if request.method == 'POST':
        with open("decitree.pkl", 'rb') as r:
            mod = pickle.load(r)
        des_id = getdt.id
        
        col1 = int(request.form["s1"])
        col2 = int(request.form["s2"])
        col3 = int(request.form["s3"])
        col4 = int(request.form["s4"])
        col5 = int(request.form["s5"])
        col6 = int(request.form["s6"])
        col7 = int(request.form["s7"])
        col8 = int(request.form["s8"])
        col9 = int(request.form["s9"])
        col10 = int(request.form["s10"])
        col11 = int(request.form["s11"])
        col12 = int(request.form["s12"]) 
        col13 = int(request.form["s13"])
        col14 = int(request.form["s14"])
        col15 = int(request.form["s15"])
        col16 = int(request.form["s16"])
        col17 = int(request.form["s17"])
        col18 = int(request.form["s18"])
        col19 = int(request.form["s19"])
        col20 = int(request.form["s20"]) 
        col21 = int(request.form["s21"])
        col22 = int(request.form["s22"])
        col23 = int(request.form["s23"])
        col24 = int(request.form["s24"])
        col25 = int(request.form["s25"])
        col26 = int(request.form["s26"])
        col27 = int(request.form["s27"])
        col28 = int(request.form["s28"]) 
        col29 = int(request.form["s29"])
        col30 = int(request.form["s30"])
        col31 = int(request.form["s31"])
        col32 = int(request.form["s32"])

        col33 = int(request.form["e1"])
        col34 = int(request.form["e2"])
        col35 = int(request.form["e3"])
        col36 = int(request.form["e4"])
        col37 = int(request.form["e5"])
        col38 = int(request.form["e6"])
        col39 = int(request.form["e7"])
        col40 = int(request.form["e8"])
        col41 = int(request.form["e9"])
        col42 = int(request.form["e10"])
        col43 = int(request.form["e11"])
        col44 = int(request.form["e12"])

        col45 = int(request.form["l1"])
        col46 = int(request.form["l2"])
        col47 = int(request.form["l3"])

        state = np.array((col1,col2,col3,col4,col5,col6,col7,col8,col9,col10, col11, col12,  col13, col14, col15, col16, col17, col18, col19, col20,  col21, col22, col23, col24, col25, col26, col27, col28,  col29, col30, col31,col32,col33,col34,col35,col36,col37,col38,col39,col40,col41,col42,col43,col44,col45,col46,col47))
        state = np.reshape(state,(1,-1))

        status = mod.predict(state)
        if status == 1:
            statusDesa = "Maju"
        elif status == 2:
            statusDesa = "Mandiri" 
        elif status == 3:
            statusDesa = "Sangat Tertinggal" 
        elif status == 4:
            statusDesa = "Tertinggal" 
        else:
            statusDesa = "Berkembang" 
        
        getdt.status = statusDesa
        getdt.iks = (col1+col2+col3+col4+col5+col6+col7+col8+col9+col10+col11+col12+col13+col14+col15+col16+col17+col18+col19+col20+col21+col22+col23+col24+col25+col26+col27+col28+col29+col30+col31+col32)/175
        getdt.ike = (col33+col34+col35+col36+col37+col38+col39+col40+col41+col42+col43+col44)/60
        getdt.ikl = (col45+col46+col47)/15
        getdt.idm = (getdt.iks+getdt.ike+getdt.ikl)/3
        dt_status_desa = dt_desa(id_dt=des_id, stat_dt=statusDesa, col_e=col1, col_f=col2, col_g=col3, col_h=col4, col_i=col5, 
                                col_j=col6, col_k=col7, col_l=col8, col_m=col9, col_n=col10, col_o=col11, col_p=col12, col_q=col13, 
                                col_r=col14, col_s=col15, col_t=col16, col_u=col17, col_v=col18, col_w=col19, col_x=col20, col_y=col21, 
                                col_z=col22, col_aa=col23, col_ab=col24, col_ac=col25, col_ad=col26, col_ae=col27, col_af=col28, col_ag=col29,
                                col_ah=col30, col_ai=col31, col_aj=col32, col_ak=col33, col_al=col34, col_am=col35, col_an=col36, col_ao=col37, 
                                col_ap=col38, col_aq=col39, col_ar=col40, col_as=col41, col_at=col42, col_au=col43, col_av=col44, col_aw=col45, 
                                col_ax=col46, col_ay=col47)
        db.session.add(dt_status_desa)
        db.session.commit()
        flash('Status Desa Berhasil Ditentukan','success')
        return redirect(url_for("dash", email=getdt.emails))
    return render_template("quest.html", showdt=getdt)

@app.route('/editdesa/<ides>', methods=['GET','POST'])
def editdesa(ides):

    getdt = user.query.filter_by(id=ides).first_or_404()
    if request.method == 'POST':
        getdt.nama_penanggung = request.form["nama_penang"]
        getdt.emails = request.form["email"]
        getdt.password = request.form["passwd"]
        getdt.prov = request.form["provinsi"]
        getdt.kota = request.form["kota"]
        getdt.kec = request.form["kecem"]
        getdt.desa = request.form["nam_desa"]
        db.session.commit()
        flash("Update Profile Desa Success!")
        return redirect(url_for("dash", email=getdt.emails))
    
    flash("Update failure!")
    return render_template('edtdesa.html', showdt=getdt)
    
@app.route('/logout')
def logout():
    flash('Terima Kasih sudah Bekerja dengan Baik, we PROUD', 'info')
    session.pop('username', None)
    return redirect(url_for('index'))    


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)