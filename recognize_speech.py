# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 17:54:06 2023

@author: Mahendran
"""
from pydub import AudioSegment
#from pydub.silence import split_on_silence
import speech_recognition as sr
import os
from datetime import datetime as dt
from TAAD import get_prediction
from audio_split import split_audio
def get_speech(app_path):
    src=os.path.join(app_path,"audio.wav")
    afile=AudioSegment.from_file(src)
    length=len(afile)
    wcounts_emn={}
    pred_emn={}
    #predt=[]
    ptime_emn={}
    convert=dt.now()-dt.now()
    if length<60000:
        start_time=dt.now()
        recognizer=sr.Recognizer()
        audiofile= sr.AudioFile(src)
        with audiofile as source:
            #recognizer.adjust_for_ambient_noise(source,duration=5)
            data=recognizer.record(source)
        whatspoke = recognizer.recognize_google (data, language="ta-IN",show_all=True)
        if len(whatspoke['alternative'])>1:
            whatspoke=whatspoke['alternative'][1]['transcript']
        else:
            whatspoke=whatspoke['alternative'][0]['transcript']
        convert=str(dt.now()-start_time).split(".")[0]
        pred_emn[1],wcounts_emn[1]=get_prediction(whatspoke)
        ptime_emn[1]=str(dt.now()-start_time)#.split(".")[0]
        return whatspoke,pred_emn,wcounts_emn,ptime_emn,convert,length
    else:
        return split_audio(afile,length,app_path)