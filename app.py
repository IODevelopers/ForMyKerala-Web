import os
import sys
import json
from datetime import datetime
import time
import requests
from flask import Flask ,render_template, redirect, url_for, session, request, logging

app = Flask(__name__)
@app.route('/', methods=['GET','POST']) #landing page
def home():
    return render_template("index.html")

@app.route('/donate', methods=['GET','POST']) #landing page
def donate():
    if request.method =="POST":
        name = request.form['name']
        phone = request.form['phone']
        address = request.form['address']
        count = request.form['no']
        item = request.form['item']
        district = request.form['district']
        print(name,phone,address,count,item)
        time1 = time.time()
        time1 = str(time1)
        url = 'https://e7i3xdj8he.execute-api.ap-south-1.amazonaws.com/Dev/web/registerdonor'
        data = {'TimeIndex':time1 ,'Name':name,'PhoneNumber':phone,'Address':address,'Count':count,'Item':item,'Platform':"Web",'District':district}
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
        name = request.form['name']
        phone = request.form['phone']
        address = request.form['address']
        count = request.form['no']
        item = request.form['item']
        district = request.form['district']
        print(name,phone,address,count,item)
        url = 'https://e7i3xdj8he.execute-api.ap-south-1.amazonaws.com/Dev/requests/register-web'
        data = {'Name':name,'PhoneNumber':phone,'Address':address,'Count':count,'Item':item,'Platform':"Web",'District':district}
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

@app.route('/dashboard', methods=['GET','POST']) 
def dash():

    # data from web
    url ="https://e7i3xdj8he.execute-api.ap-south-1.amazonaws.com/Dev/web/getrequest"
    headers = {'content-type': 'application/json'}
    r=requests.post(url, headers=headers)
    data = r.json()
    
    #data from app
    url ="https://e7i3xdj8he.execute-api.ap-south-1.amazonaws.com/Dev/android/getall"
    headers = {'content-type': 'application/json'}
    r=requests.post(url, headers=headers)
    android = r.json()
    
    

    #data donors android
    url ='https://e7i3xdj8he.execute-api.ap-south-1.amazonaws.com/Dev/android/getdonor'
    headers = {'content-type': 'application/json'}
    r=requests.post(url, headers=headers)
    donors = r.json()
    
    

    #data donors web
    url ='https://e7i3xdj8he.execute-api.ap-south-1.amazonaws.com/Dev/web/getdonor'
    headers = {'content-type': 'application/json'}
    r=requests.post(url, headers=headers)
    donorweb = r.json()
    


    return render_template("active_req.html",data=data,donorweb=donorweb,android=android,donors=donors)

@app.context_processor
def date_processor():
    def change_epoch(epoch):
        ts = float(epoch)
       
        return datetime.fromtimestamp(ts).strftime('%d/%m %I:%M %p')
    return dict(change_epoch=change_epoch)



@app.route('/registerVolunteer', methods=['GET','POST']) #landing page
def volunteer():
    if request.method =="POST":
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        district = request.form['district']
        url = 'https://e7i3xdj8he.execute-api.ap-south-1.amazonaws.com/Dev/volunteer/register'
        data = {'Name':name,'Email':email,'Phone':phone,'District':district}
        headers = {'content-type': 'application/json'}
        r=requests.post(url, data=json.dumps(data), headers=headers)
        data = r.json()
        print(data)
        message = "Successfully Registered"
        return render_template("registervolunteer.html",message = message)
    return render_template("registervolunteer.html")


if __name__=='__main__':

	app.run(threaded=True,host="0.0.0.0",port=80)