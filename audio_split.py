# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 11:36:15 2023

@author: Mahendran
"""
from pydub import AudioSegment
import speech_recognition as sr
from TAAD import get_prediction
from datetime import datetime as dt
from numpy import sum 
import os
def split_audio(file,length,root_path):
    counter=1
    interval=59*1000
    overlap=1.5*1000
    start=0
    end=0
    r=sr.Recognizer()
    text=""
    wcounts_emn={}
    pred_emn={}
    #predt=[]
    ptime_emn={}
    #start_time=dt.now()
    convert=dt.now()-dt.now()
    for i in range(0,length,interval):
        start_time=dt.now()
        if i==0:
            start=0
            end=interval
        else:
            start=end-overlap
            end=interval+start
        if end>=length:
            end=length
        chunk=file[start:end]
        filename=root_path+"/chunks/"+str(counter)+".wav"
        chunk.export(filename,format="wav")
        with sr.AudioFile(filename) as source:
            data=r.record(source)
        spoke = r.recognize_google (data, language="ta-IN",show_all=True)
        if len(spoke['alternative'])>1:
            spoke=spoke['alternative'][1]['transcript']
        else:
            spoke=spoke['alternative'][0]['transcript']
        
        convert=convert+(dt.now()-start_time)
        pred_emn[counter],wcounts_emn[counter]=get_prediction(spoke)
        ptime_emn[counter]=(dt.now()-start_time).total_seconds()/60
        counter=counter+1
        text=text+spoke

        if os.path.exists(filename):
            os.remove(filename)
            print("file deleted ")
    return text,pred_emn,wcounts_emn,ptime_emn,convert,length
