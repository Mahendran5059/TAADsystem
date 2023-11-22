import numpy as np
import joblib
from datetime import datetime as dt
from tamilstemmer import TamilStemmer
import matplotlib.pyplot as plt
import seaborn as sns

def load_lexicon(file):
    abw=open("./corpus/"+file,'r',encoding='utf-8')
    absn=[]
    for i in abw.readlines():
        absn.append(i.strip(" ,.\n"))
    abw.close()
    return absn
abd=load_lexicon("ausive_words.txt")
hrsd=load_lexicon("harsh.txt")
hrsd1=load_lexicon("harsh1.txt")
hrsd2=load_lexicon("harsh2.txt")
labd1=load_lexicon("less_abusive 1.txt")
labd2=load_lexicon("lessausive2.txt")
drd=load_lexicon("disrespect.txt")
counts=np.zeros(11)
speech_len=0
def extract_features(sn):
    record=np.zeros((10))
    k=0
    for j in sn.strip(" ").split(" "):
        if j in abd:
            record[0]=1
            k=k+1
            print(j)
            #break
    print(k)
    counts[0]=k
    k=0
    for j in sn.strip(" ").split(" "):
        for l in abd:
            if j==l:
                record[0]=1
                k=k+1
                print(j)
                #break
    print(k)
    counts[1]=k
    tam=TamilStemmer()
    k=0
    for j in tam.stemWords(sn.strip(" ").split(" ")):
        if j in abd:
            record[1]=1
            k=k+1
            print(j)
            #break
    print(k)
    counts[2]=k
    k=0
    for j in sn.strip(" ").split(" "):
        if j in labd1:
            record[2]=1
            k=k+1
            print(j)
            #break
        
    print(k)
    counts[3]=k
    k=0
    for j in sn.strip(" ").split(" "):
        if j in labd2:
            record[3]=1
            k=k+1
            print(j)
            #break
    counts[4]=k
    print(k)
    k=0
    for j in sn.strip(" ").split(" "):
        if j in hrsd:
            record[4]=1
            k=k+1
            print(j)
            #break
    counts[5]=k
    print(k)
    k=0
    for j in sn.strip(" ").split(" "):
        if j in hrsd1:
            record[5]=1
            k=k+1
            print(j)
            #break
    counts[6]=k   
    print(k)
    k=0
    for j in sn.strip(" ").split(" "):
        if j in hrsd2:
            record[6]=1
            k=k+1
            print(j)
            #break
    counts[7]=k    
    print(k)
    k=0
    for j in sn.strip(" ").split(" "):
        if j in drd:
            record[7]=1
            k=k+1
            print(j)
            #break
    counts[8]=k    
    print(k)
    k=0
    for j in tam.stemWords(sn.strip(" ").split(" ")):
        if j in hrsd:
            record[8]=1
            k=k+1
            print(j)
            #break
    counts[9]=k   
    print(k)
    k=0
    for j in tam.stemWords(sn.strip(" ").split(" ")):
        if j in drd:
            record[9]=1
            k=k+1
            print(j)
            #break
    counts[10]=k    
    print(k)
    return record

def get_prediction(speech,apath=None):
    global speech_len
    ptime=dt.now()
    if apath==None:
        speech_len=len(speech.split(" "))
        featured=extract_features(speech)
        model=joblib.load(open("nb.pkl",'rb'))
        pred=model.predict([featured])
        print("carray",counts)
        return pred,speech_len
    else:
        speech_len=len(speech.split(" "))
        featured=extract_features(speech)
        model=joblib.load(open("nb.pkl",'rb'))
        pred=model.predict([featured])
        ptime=dt.now()-ptime
        print("carray",counts)
        graph(apath)
        return pred,speech_len,ptime


def get_wcounts():
    wcounts=np.zeros(5)
    wcounts[0]=counts[0]
    wcounts[1]=counts[3]+counts[4]
    wcounts[2]=counts[5]+counts[6]+counts[7]
    wcounts[3]=counts[8]
    wcounts[4]=speech_len-(wcounts[0]+wcounts[1]+wcounts[2]+wcounts[3])
    if(counts[1]-counts[0])>0:
        wcounts[0]=counts[0]+(counts[1]-counts[0])
    if (counts[0]==0) and (counts[1]==0):
        wcounts[0]=wcounts[0]+counts[2]
    if wcounts[2]==0:
        wcounts[2]=counts[9]
    if wcounts[3]==0:
        wcounts[3]=counts[10]
    return wcounts

def graph(apath):
    y=get_wcounts()
    x=["abusive","less abusive","harsh","disrespect","normal"]
    fig, ax = plt.subplots(figsize=(9, 6))
    plt.xlabel("Categories",fontsize=17)
    plt.ylabel("No fo Words",fontsize=17)
    plt.title("WORDS COUNT",fontsize=17,color="brown")
    sns.barplot(x=x,y=y,ax=ax)
    ax.bar_label(ax.containers[0], label_type='edge')
    ax.margins(y=0.1)
    print(apath+"/static/plots/count_words.png")
    plt.savefig(apath+"/static/plots/count_words.png")
