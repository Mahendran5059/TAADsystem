# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 00:44:57 2023

@author: Mahendran
"""
from flask import Flask,request,render_template#,redirect,flash,jsonify
import speech_recognition as sr
from recognize_speech import get_speech
from TAAD import get_prediction
import subprocess
import os
import sys
import traceback
from datetime import datetime as dt
from plots import plot_saudio,plot_laudio
#import send_somewhere

app=Flask(__name__)
app.config['MAX_CONTENT_LENGTH']=20*1000*1000
app.secret_key="21433253"
@app.route('/')
def home():
    return render_template('index1.html')

def process():
    global v
    v=0


@app.route('/predict', methods=['GET','POST'])
#print("predict")
def predict():
    global wcounts_emn,pred_emn,ptime_emn,convert,sp_len,ptime,up_fsize,wav_fsize,tlength,ftime,up_format
    print('in pred part')
    try:
        if request.method=='POST':
            print('in post')
            #file=request.files['file']
            print('in post')
            print(request.files)
            if 'file' not in request.files:
                print('no file part')
                return render_template('index1.html',warning="file not received, upload again, check internet connection")
            print(request.files)
            file=request.files['file']
            if file.filename =='':
                return render_template('index1.html',warning="file not received or selected")
            if file:
                print("speech")
                fpath=os.path.join(app.root_path,file.filename)
                up_format=str(file.filename).split(".")[1]
                file.save(fpath)
                file.close()
                up_fsize=os.path.getsize(fpath)
                print("instance"+str(app.instance_path))
                print("instance"+str(app.root_path))
                apath=os.path.join(app.root_path,"audio.wav")
                if os.path.exists(apath):
                    os.remove(apath)
                    print("file deleted1 ")
                ftime=dt.now()
                subprocess.call(['ffmpeg', '-i',fpath,apath])
                ftime=dt.now()-ftime
                print("saved")
                wav_fsize=os.path.getsize(apath)
                rspeech,pred_emn,wcounts_emn,ptime_emn,convert,tlength=get_speech(app.root_path)
                print(rspeech)
                print("speech1")
                bef=dt.now()
                print(bef)
                result,sp_len,ptime=get_prediction(rspeech,app.root_path)
                now=dt.now()
                if tlength>60000:
                    plot_laudio(pred_emn, ptime_emn, wcounts_emn, app.root_path)
                else:
                    plot_saudio(pred_emn, ptime_emn, wcounts_emn, app.root_path)
                print(now)
                print("diff = "+str(now-bef))
                print("pred")
                print(result)
                if os.path.exists(fpath):
                    os.remove(fpath)
                    print("file deleted2 ")
                path=os.path.join(app.root_path,"audio_op")

    except Exception as e:
        print(traceback.format_exception(*sys.exc_info()))
        print(e)
    print(path)
    if result==3:
        text="இவர் ஆபாசமாக பேசியுள்ளார்"
        os.system(path+"/t1.mp3")
        
    if result==2:
        text="இவர் தவறான சொற்களை பயன்படித்தியுள்ளார்"
        os.system(path+"/t2.mp3")
        
    if result==1:
        text="இவர் மரியாதை குறைவாக பேசியுள்ளார்"
        os.system(path+"/t3.mp3")
       
    if result==0:
        text="இவர் நல்ல முறையில் பேசியுள்ளார்"
        os.system(path+"/t4.mp3")
        
    return render_template('index.html',results=text)

def process1():
    return render_template("index1.html",msg="Got it: Audio under processing....please wait")



@app.route('/record', methods=["GET","POST"])
def record():
    try:
        result=4
        print("before if")
        if request.method=="POST":
            print("process")
            #redirect(process())
            r = sr.Recognizer()
            print("source")
            with sr.Microphone() as source:
                audio = r.listen (source,timeout=5,phrase_time_limit=7)
            print("process1")
            #redirect(process1())
            whatspoke = r.recognize_google(audio, language="ta-IN",show_all=True)
            print("recognize")
            if len(whatspoke['alternative'])>1:
                whatspoke=whatspoke['alternative'][1]['transcript']
            else:
                whatspoke=whatspoke['alternative'][0]['transcript']
            result,spl,prtime=get_prediction(whatspoke,app.root_path)
    except Exception as e:
        print(traceback.format_exception(*sys.exc_info()))
        print(e)
    path=os.path.join(app.root_path,"audio_op")
    if result==3:
        text="இவர் ஆபாசமாக பேசியுள்ளார்"
        os.system(path+"/t1.mp3")
        
    elif result==2:
        text="இவர் தவறான சொற்களை பயன்படித்தியுள்ளார்"
        os.system(path+"/t2.mp3")
        
    elif result==1:
        text="இவர் மரியாதை குறைவாக பேசியுள்ளார்"
        os.system(path+"/t3.mp3")
       
    elif result==0:
        text="இவர் நல்ல முறையில் பேசியுள்ளார்"
        os.system(path+"/t4.mp3")
    else:
        text="not recognized"
    return render_template('index1.html',results=text)  


@app.route('/details', methods=["GET","POST"])
def details():
    if request.method =="POST":
        sec=tlength/1000
        l=str(int(sec/3600))+":"+str(int((sec%3600)/60))+":"+str(sec%60)
        return render_template("details.html",upsize=up_fsize,upformat=up_format,wsize=wav_fsize,ftime=ftime,ctime=convert,tptime=ptime,alength=l,twords=sp_len)

     
if __name__ == "__main__":
    os.environ.setdefault('FLASK_DEBUG', 'development')
    app.run(debug=False)