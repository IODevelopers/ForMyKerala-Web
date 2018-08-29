import os
import sys
import json
from datetime import datetime
import time
from functools import wraps
import requests
from flask import Flask ,render_template, redirect, url_for, session, request, logging


app = Flask(__name__)


def is_logged_in(f):	# Function for implementing security and redirection
	@wraps(f)
	def wrap(*args,**kwargs):
		if 'logged_in' in session:
			return f(*args, **kwargs)
		else:
			return redirect(url_for('login'))
	return wrap	# A wrap is a concept that is used to check for authorisation of a request

def is_admin_logged_in(f):    # Function for implementing security and redirection
    @wraps(f)
    def wrap(*args,**kwargs):
        if 'admin_logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect(url_for('home'))
    return wrap # A wrap is a concept that is used to check for authorisation of a request


@app.route('/', methods=['GET','POST']) #landing page
def home():
    try:
        if session['logged_in'] == True:
            return redirect(url_for('dashvolunteer'))
    except:
        return render_template("index.html")


@app.route('/accept/<string:timeindex>',methods=['GET','POST'])
def accept(timeindex):
    print(timeindex)
    timeindexlist = timeindex.split('&')
    if timeindexlist[1] == 'null':
        return redirect(url_for('dashvolunteer'))
    url = 'https://e7i3xdj8he.execute-api.ap-south-1.amazonaws.com/Dev/verification/request'
    data = {'TimeIndex':timeindexlist[0],'PhoneNumber':timeindexlist[1]}
    headers = {'content-type': 'application/json'}
    r=requests.post(url, data=json.dumps(data), headers=headers)
    data = r.json()
    return redirect(url_for('dashvolunteer'))

@app.route('/accept1/<string:timeindex>',methods=['GET','POST'])
def accept1(timeindex):
    print(timeindex)
    timeindexlist = timeindex.split('&')
    if timeindexlist[1] == 'null':
        return redirect(url_for('dashvolunteer'))
    url = 'https://e7i3xdj8he.execute-api.ap-south-1.amazonaws.com/Dev/verification/donations'
    data = {'TimeIndex':timeindexlist[0],'PhoneNumber':timeindexlist[1]}
    headers = {'content-type': 'application/json'}
    r=requests.post(url, data=json.dumps(data), headers=headers)
    data = r.json()
    print(data)
    return redirect(url_for('dashvolunteer'))

@app.route('/acceptadmin/<string:timeindex>',methods=['GET','POST'])
@is_admin_logged_in 
def acceptadmin(timeindex):
    print(timeindex)
    timeindexlist = timeindex.split('&')
    if timeindexlist[1] == 'null':
        return redirect(url_for('verifyrequests'))
    url = 'https://e7i3xdj8he.execute-api.ap-south-1.amazonaws.com/Dev/verification/request'
    data = {'TimeIndex':timeindexlist[0],'PhoneNumber':'Admin'}
    headers = {'content-type': 'application/json'}
    r=requests.post(url, data=json.dumps(data), headers=headers)
    data = r.json()
    return redirect(url_for('verifyrequests'))

@app.route('/acceptadmin1/<string:timeindex>',methods=['GET','POST'])
@is_admin_logged_in 
def acceptadmin1(timeindex):
    print(timeindex)
    timeindexlist = timeindex.split('&')
    if timeindexlist[1] == 'null':
        return redirect(url_for('verifydonors'))
    url = 'https://e7i3xdj8he.execute-api.ap-south-1.amazonaws.com/Dev/verification/donations'
    data = {'TimeIndex':timeindexlist[0],'PhoneNumber':'Admin'}
    headers = {'content-type': 'application/json'}
    r=requests.post(url, data=json.dumps(data), headers=headers)
    data = r.json()
    print(data)
    return redirect(url_for('verifydonors'))

@app.route('/commentadmin/<string:timeindex>',methods=['GET','POST'])
def commentadmin(timeindex):
    print(timeindex)
    timeindexlist = timeindex.split('&')
    if timeindexlist[1] == 'null':
        return redirect(url_for('verifyrequests'))
    url = 'https://e7i3xdj8he.execute-api.ap-south-1.amazonaws.com/Dev/requests/add-comment'
    data = {'TimeIndex':timeindexlist[0],'Comments':timeindexlist[1]}
    headers = {'content-type': 'application/json'}
    r=requests.post(url, data=json.dumps(data), headers=headers)
    data = r.json()
    print(data)
    return redirect(url_for('verifyrequests'))

@app.route('/commentadmin1/<string:timeindex>',methods=['GET','POST'])
def commentadmin1(timeindex):
    print(timeindex)
    timeindexlist = timeindex.split('&')
    if timeindexlist[1] == 'null':
        return redirect(url_for('verifydonors'))
    url = 'https://e7i3xdj8he.execute-api.ap-south-1.amazonaws.com/Dev/donors/add-comment'
    data = {'TimeIndex':timeindexlist[0],'Comments':timeindexlist[1]}
    headers = {'content-type': 'application/json'}
    r=requests.post(url, data=json.dumps(data), headers=headers)
    data = r.json()
    print(data)
    print("I'm Here")
    return redirect(url_for('verifydonors'))

@app.route('/closeadmin1/<string:timeindex>',methods=['GET','POST'])
def closeadmin1(timeindex):
    print(timeindex)
    url = 'https://e7i3xdj8he.execute-api.ap-south-1.amazonaws.com/Dev/requests/close-request'
    data = {'TimeIndex':timeindex}
    headers = {'content-type': 'application/json'}
    r=requests.post(url, data=json.dumps(data), headers=headers)
    data = r.json()
    print(data)
    print("I'm Here1")
    return redirect(url_for('verifyrequests'))

@app.route('/admin-home', methods=['GET','POST']) #landing page admin 
@is_admin_logged_in 
def admin_home():
    return render_template("admin-home.html")









@app.route('/comment/<string:timeindex>',methods=['GET','POST'])
def comment(timeindex):
    print(timeindex)
    timeindexlist = timeindex.split('&')
    if timeindexlist[1] == 'null':
        return redirect(url_for('dashvolunteer'))
    url = 'https://e7i3xdj8he.execute-api.ap-south-1.amazonaws.com/Dev/requests/add-comment'
    data = {'TimeIndex':timeindexlist[0],'Comments':timeindexlist[1]}
    headers = {'content-type': 'application/json'}
    r=requests.post(url, data=json.dumps(data), headers=headers)
    data = r.json()
    print(data)
    return redirect(url_for('dashvolunteer'))

@app.route('/comment1/<string:timeindex>',methods=['GET','POST'])
def comment1(timeindex):
    print(timeindex)
    timeindexlist = timeindex.split('&')
    if timeindexlist[1] == 'null':
        return redirect(url_for('dashvolunteer'))
    url = 'https://e7i3xdj8he.execute-api.ap-south-1.amazonaws.com/Dev/donors/add-comment'
    data = {'TimeIndex':timeindexlist[0],'Comments':timeindexlist[1]}
    headers = {'content-type': 'application/json'}
    r=requests.post(url, data=json.dumps(data), headers=headers)
    data = r.json()
    print(data)
    print("I'm Here")
    return redirect(url_for('dashvolunteer'))

@app.route('/close1/<string:timeindex>',methods=['GET','POST'])
def close1(timeindex):
    print(timeindex)
    url = 'https://e7i3xdj8he.execute-api.ap-south-1.amazonaws.com/Dev/requests/close-request'
    data = {'TimeIndex':timeindex}
    headers = {'content-type': 'application/json'}
    r=requests.post(url, data=json.dumps(data), headers=headers)
    data = r.json()
    print(data)
    print("I'm Here1")
    return redirect(url_for('dashvolunteer'))


@app.route('/auth1/<string:timeindex>',methods=['GET','POST'])
def auth1(timeindex):
    print(timeindex)
    url = 'https://e7i3xdj8he.execute-api.ap-south-1.amazonaws.com/Dev/volunteer/authorize'
    data = {'TimeIndex':timeindex}
    headers = {'content-type': 'application/json'}
    r=requests.post(url, data=json.dumps(data), headers=headers)
    data = r.json()
    print(data)
    print("I'm Here1")
    return redirect(url_for('verifyvolunteer'))

@app.route('/deauth1/<string:timeindex>',methods=['GET','POST'])
def deauth1(timeindex):
    print(timeindex)
    url = 'https://e7i3xdj8he.execute-api.ap-south-1.amazonaws.com/Dev/volunteer/deauthorize'
    data = {'TimeIndex':timeindex}
    headers = {'content-type': 'application/json'}
    r=requests.post(url, data=json.dumps(data), headers=headers)
    data = r.json()
    print(data)
    print("I'm Here1")
    return redirect(url_for('verifyvolunteer'))



@app.route('/delete1/<string:timeindex>',methods=['GET','POST'])
@is_admin_logged_in 
def delete1(timeindex):
    print(timeindex)
    timeindexlist = timeindex.split('&')
    if timeindexlist[1] == 'null':
        return redirect(url_for('verifyrequests'))
    url = 'https://e7i3xdj8he.execute-api.ap-south-1.amazonaws.com/Dev/admin/deleterequest'
    data = {'TimeIndex':timeindexlist[0],'PhoneNumber':timeindexlist[1]}
    headers = {'content-type': 'application/json'}
    r=requests.post(url, data=json.dumps(data), headers=headers)
    data = r.json()
    print(data)
    return redirect(url_for('verifyrequests'))

@app.route('/delete2/<string:timeindex>',methods=['GET','POST'])
@is_admin_logged_in 
def delete2(timeindex):
    print(timeindex)
    timeindexlist = timeindex.split('&')
    if timeindexlist[1] == 'null':
        return redirect(url_for('verifydonors'))
    url = 'https://e7i3xdj8he.execute-api.ap-south-1.amazonaws.com/Dev/admin/deletedonor'
    data = {'TimeIndex':timeindexlist[0],'PhoneNumber':timeindexlist[1]}
    headers = {'content-type': 'application/json'}
    r=requests.post(url, data=json.dumps(data), headers=headers)
    data = r.json()
    print(data)
    return redirect(url_for('verifydonors'))











@app.route('/feedback', methods=['GET','POST']) #landing page
def feedback():
    if request.method =="POST":
        name = request.form['name']
        phone = request.form['phone']
        familymembers = request.form['members']
        situation = request.form['situation']
        reccomendations = request.form['reccomendations']
        items = request.form['items123']
        url="https://e7i3xdj8he.execute-api.ap-south-1.amazonaws.com/Dev/feedback"
        data = {'Name':name,'PhoneNumber':phone,'FamilyMembers':familymembers,'Situation':situation,'Reccomendations':reccomendations,'Items':items,'Platform':"Web"}
        print(data)
        headers = {'content-type': 'application/json'}
        r=requests.post(url, data=json.dumps(data), headers=headers)
        data = r.json()
        message="We have recieved your request"
        return render_template("feedback.html", message=message)
    return render_template("feedback.html")

@app.route('/login', methods=['GET','POST']) #landing page
def login():
    if request.method =="POST":
        phone = request.form['phone']
        url= "https://e7i3xdj8he.execute-api.ap-south-1.amazonaws.com/Dev/volunteer/login"
        data = {'PhoneNumber':phone}
        headers = {'content-type': 'application/json'}
        r=requests.post(url, data=json.dumps(data), headers=headers)
        data = r.json()
        try:
            message = data['Message']
        except:
            session['PhoneNumber']=data['PhoneNumber']
            session['TimeIndex']=data['TimeIndex']
            session['Email']=data['Email']
            session['District']=data['District']
            session['Name']=data['Name']
            session['logged_in'] = True
            return redirect(url_for('dashvolunteer'))
        return render_template("login.html", message=message)
    return render_template("login.html")


@app.route('/admin-login', methods=['GET','POST']) #landing page
def admin_login():
    if request.method =="POST":
        username = request.form['username']
        password = request.form['password']
        url= "https://e7i3xdj8he.execute-api.ap-south-1.amazonaws.com/Dev/admin/login"
        data = {'username':username, 'password': password}
        headers = {'content-type': 'application/json'}
        r=requests.post(url, data=json.dumps(data), headers=headers)
        data = r.json()
        if data['Validation'] == "True":
            # session['PhoneNumber']=data['PhoneNumber']
            # session['TimeIndex']=data['TimeIndex']
            # session['Email']=data['Email']
            # session['District']=data['District']
            # session['Name']=data['Name']
            session['admin_logged_in'] = True
            session['PhoneNumber']='123'
            return redirect(url_for('admin_home'))
        elif data['Validation'] == "False":
            message = "Invalid credentials"
        else:
            message = "Can't connect to server!"

        return render_template("admin-login.html", message=message)
    return render_template("admin-login.html")

@app.route('/verifyrequests', methods=['GET','POST'])
@is_admin_logged_in 
def verifyrequests():
    url ="https://e7i3xdj8he.execute-api.ap-south-1.amazonaws.com/Dev/requests/get-unverified-request"
    headers = {'content-type': 'application/json'}
    r=requests.post(url, headers=headers)
    android = r.json()
    return render_template("verifyrequests.html",android=android)

@app.route('/verifydonors', methods=['GET','POST'])
@is_admin_logged_in 
def verifydonors():
    #data donors
    url ='https://e7i3xdj8he.execute-api.ap-south-1.amazonaws.com/Dev/web/getdonor'
    headers = {'content-type': 'application/json'}
    r=requests.post(url, headers=headers)
    donors = r.json() 
    return render_template("verifydonors.html",donors=donors)

@app.route('/verifyvolunteer', methods=['GET','POST'])
@is_admin_logged_in 
def verifyvolunteer():
    #data vols
    url ='https://e7i3xdj8he.execute-api.ap-south-1.amazonaws.com/Dev/volunteer/get-all'
    headers = {'content-type': 'application/json'}
    r=requests.post(url, headers=headers)
    vols = r.json() 
    print(vols)
    return render_template("verifyvolunteers.html",donors=vols)


@app.route('/admin-dashboard', methods=['GET','POST'])
@is_admin_logged_in 
def admin_dashboard():
    # data requests
    url ="https://e7i3xdj8he.execute-api.ap-south-1.amazonaws.com/Dev/requests/get-unverified-request"
    headers = {'content-type': 'application/json'}
    r=requests.post(url, headers=headers)
    android = r.json()
    
    #data donors
    url ='https://e7i3xdj8he.execute-api.ap-south-1.amazonaws.com/Dev/web/getdonor'
    headers = {'content-type': 'application/json'}
    r=requests.post(url, headers=headers)
    donors = r.json() 
    return render_template("admin-dashboard.html",android=android,donors=donors)


@app.route('/donate', methods=['GET','POST']) #landing page
def donate():
    if request.method =="POST":
        url = 'https://e7i3xdj8he.execute-api.ap-south-1.amazonaws.com/Dev/requests/get-items'
        headers = {'content-type': 'application/json'}
        r=requests.get(url, headers=headers)
        items_from_web = r.json()
        items_from_web = items_from_web['Items']
        name = request.form['name']
        phone = request.form['phone']
        address = request.form['address']
        items_required = {}
        district = request.form['district']
        time1 = time.time()
        time1 = str(time1)
        for each_item in items_from_web:
            try:
                items_required[each_item] = request.form[each_item]
            except:
                print("%s is not added" % each_item)
        if len(items_required.keys()) == 0:
            message = "Items cannot be empty Please select one"
            url = 'https://e7i3xdj8he.execute-api.ap-south-1.amazonaws.com/Dev/requests/get-items'
            headers = {'content-type': 'application/json'}
            r=requests.get(url, headers=headers)
            data = r.json()
            count = len(data['Items'])
            return render_template("donor.html",message = message,data = data,count = count)
        url = 'https://e7i3xdj8he.execute-api.ap-south-1.amazonaws.com/Dev/web/registerdonor'
        data = {'TimeIndex':time1 ,'Name':name,'PhoneNumber':phone,'Items':items_required,'Address':address,'Platform':"Web",'District':district}
        headers = {'content-type': 'application/json'}
        r=requests.post(url, data=json.dumps(data), headers=headers)
        data = r.json()
        print(data)
        message = "Successfully Registered"
        url = 'https://e7i3xdj8he.execute-api.ap-south-1.amazonaws.com/Dev/requests/get-items'
        headers = {'content-type': 'application/json'}
        r=requests.get(url, headers=headers)
        data = r.json()
        count = len(data['Items'])
        return render_template("donor.html",message = message,data = data,count = count)
    url = 'https://e7i3xdj8he.execute-api.ap-south-1.amazonaws.com/Dev/requests/get-items'
    headers = {'content-type': 'application/json'}
    r=requests.get(url, headers=headers)
    data = r.json()
    count = len(data['Items'])
    return render_template("donor.html", data = data,count = count)




@app.route('/requesthelp', methods=['GET','POST']) #landing page
def requesthelp():
    if request.method =="POST":
        url = 'https://e7i3xdj8he.execute-api.ap-south-1.amazonaws.com/Dev/requests/get-items'
        headers = {'content-type': 'application/json'}
        r=requests.get(url, headers=headers)
        items_from_web = r.json()
        items_from_web = items_from_web['Items']
        name = request.form['name']
        phone = request.form['phone']
        address = request.form['address']
        items_required = {}
        district = request.form['district']
        for each_item in items_from_web:
            try:
                items_required[each_item] = request.form[each_item]
            except:
                print("%s is not added" % each_item)
        if len(items_required.keys()) == 0:
            message = "Items cannot be empty Please select one"
            url = 'https://e7i3xdj8he.execute-api.ap-south-1.amazonaws.com/Dev/requests/get-items'
            headers = {'content-type': 'application/json'}
            r=requests.get(url, headers=headers)
            data = r.json()
            count = len(data['Items'])
            return render_template("assistance.html",message = message,data = data,count = count)
        url = 'https://e7i3xdj8he.execute-api.ap-south-1.amazonaws.com/Dev/requests/register-web'
        data = {'Name':name,'PhoneNumber':phone,'Address':address,'Items':items_required,'Platform':"Web",'District':district}
        
        headers = {'content-type': 'application/json'}
        r=requests.post(url, data=json.dumps(data), headers=headers)
        data = r.json()
        
        message = "Successfully Registered"
        url = 'https://e7i3xdj8he.execute-api.ap-south-1.amazonaws.com/Dev/requests/get-items'
        headers = {'content-type': 'application/json'}
        r=requests.get(url, headers=headers)
        data = r.json()
        count = len(data['Items'])
        return render_template("assistance.html",message = message,data = data,count = count)
    url = 'https://e7i3xdj8he.execute-api.ap-south-1.amazonaws.com/Dev/requests/get-items'
    headers = {'content-type': 'application/json'}
    r=requests.get(url, headers=headers)
    data = r.json()
    count = len(data['Items'])
    return render_template("assistance.html", data = data,count = count)



@app.route('/dashboardvolunteer', methods=['GET','POST'])
@is_logged_in
def dashvolunteer():
    # data from web
    url ="https://e7i3xdj8he.execute-api.ap-south-1.amazonaws.com/Dev/requests/get-unverified-request"
    headers = {'content-type': 'application/json'}
    r=requests.post(url, headers=headers)
    android = r.json()
    #data from app
#     url ="https://e7i3xdj8he.execute-api.ap-south-1.amazonaws.com/Dev/android/getall"
#     headers = {'content-type': 'application/json'}
#     r=requests.post(url, headers=headers)
#     android = r.json()
    #data donors android
#     url ='https://e7i3xdj8he.execute-api.ap-south-1.amazonaws.com/Dev/android/getdonor'
#     headers = {'content-type': 'application/json'}
#     r=requests.post(url, headers=headers)
#     donors = r.json()
    
    #data donors web
    url ='https://e7i3xdj8he.execute-api.ap-south-1.amazonaws.com/Dev/web/getdonor'
    headers = {'content-type': 'application/json'}
    r=requests.post(url, headers=headers)
    donors = r.json() 
    return render_template("dashvolunteer.html",android=android,donors=donors)

@app.route('/logout')
def logout():
	session.clear()								#Session is destroyed
	return redirect(url_for('home'))


@app.route('/dashboard', methods=['GET','POST']) 
def dash():

    # Getting all verified and closed requests
    url ="https://e7i3xdj8he.execute-api.ap-south-1.amazonaws.com/Dev/web/getrequest"
    headers = {'content-type': 'application/json'}
    r=requests.post(url, headers=headers)
    data = r.json()
    print(data)

    return render_template("active_req.html",data=data)

@app.route('/donationdashboard', methods=['GET','POST']) 
def donation_dashboard():

    # Getting all verified donors
    url ="https://e7i3xdj8he.execute-api.ap-south-1.amazonaws.com/Dev/android/getdonor"
    headers = {'content-type': 'application/json'}
    r=requests.post(url, headers=headers)
    donors = r.json()
    print(donors)

    return render_template("active_donations.html",donors=donors)

@app.context_processor
def date_processor():
    def change_epoch(epoch):
        ts = float(epoch)
       
        return datetime.fromtimestamp(ts).strftime('%d/%m %I:%M %p')
    return dict(change_epoch=change_epoch)


@app.route('/disclaimer')
def disclaimer():
    return render_template("disclaimer.html")

@app.route('/test')
def test():
    return render_template("test.html")

@app.route('/registerVolunteer', methods=['GET','POST']) #landing page
def volunteer():
    if request.method =="POST":
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        district = request.form['district']
        url = 'https://e7i3xdj8he.execute-api.ap-south-1.amazonaws.com/Dev/volunteer/register'
        data = {'Name':name,'Email':email,'PhoneNumber':phone,'District':district}
        headers = {'content-type': 'application/json'}
        r=requests.post(url, data=json.dumps(data), headers=headers)
        data = r.json()
        if data['Message'] == 'Invalid credentials':
            message = "Invalid Credentials" 
            return render_template("registervolunteer.html",message = message)   
        message = "Successfully Registered"
        return render_template("registervolunteer.html",message = message)
    return render_template("registervolunteer.html")


if __name__=='__main__':
    app.secret_key='secret123'
    app.run(threaded=True,host="0.0.0.0",port=80)
