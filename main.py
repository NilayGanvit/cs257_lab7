from flask import Flask, render_template,request,url_for,redirect
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
import joblib


import  re


app = Flask(__name__)


model = joblib.load('Email_Class')







@app.route('/',methods=['GET','POST'])
def login():
    msg = ''
    var3="Enter Your Message Below!!!"
    var2 = 'intro3'

    if request.method=='POST':

        s=request.form.get('paragraph')
        if(s==""):
            var3="Please fill the box."
            return render_template('Home.html', msg=var3, msg2=var2)

        op = model.predict([s])
        var4=op[0]


        if(var4=="spam"):
            var4="SPAM!!!"
            var2 = 'intro2'
            return render_template('Home.html',msg=var4,msg2=var2)
        else:
            var4="NOT SPAM!!!"
            var2 = 'intro1'
            return render_template('Home.html', msg=var4, msg2=var2)


    return render_template('Home.html',msg=var3,msg2=var2)






if   __name__ == "__main__":
    app.run(debug=True)



