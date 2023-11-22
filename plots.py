# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 22:10:01 2023

@author: Mahendran
"""

import matplotlib.pyplot as plt
import seaborn as sns


def plot_laudio(pred_emn,ptime_emn,wcounts_emn,root_path):
    x=list(wcounts_emn.keys())
    y=list(wcounts_emn.values())
    fig, ax = plt.subplots(figsize=(14, 8))
    sns.barplot(x=x,y=y,ax=ax,color="blue",saturation=0.3)
    plt.title("NO OF WORDS SPOKE ON EACH MINUTES",fontsize=17,color="brown")
    plt.xlabel("Minutes",fontsize=17)
    plt.ylabel("No fo Words",fontsize=17)
    ax.bar_label(ax.containers[0],label_type='edge')
    ax.margins(y=0.1)
    plt.savefig(root_path+"/static/plots/no_of_words.png")
    
    plt.figure(figsize=(16,8))
    plt.title("PROCESSING TIME FOR EACH MINUTE",fontsize=17,color="brown")
    x=list(ptime_emn.keys())
    y=list(ptime_emn.values())
    plt.plot(x,y)
    plt.scatter(x,y,color='g')
    plt.xlim(0,max(x)+1)
    plt.ylim(0,2.5)
    plt.xticks(range(0,max(x)+1))
    plt.xlabel("Minutes",fontsize=15)
    plt.ylabel("Processing Time(in mins)",fontsize=15)
    plt.savefig(root_path+"/static/plots/processing.png")
    
    plt.figure(figsize=(16,8))
    plt.title("UNDISSERVED SPEECH ON WHICH MINUTES",fontsize=15,color="brown")
    x=list(pred_emn.keys())
    y=list(pred_emn.values())
    plt.plot(x,y)
    plt.scatter(x,y,color='r')
    plt.xlim(0,max(x)+1)
    plt.yticks([-1,0,1,2,3,4],[' ',"Normal","Disrespect","Less Abusive","Abusive"," "])
    plt.xlabel("Minutes",fontsize=15)
    plt.ylabel("Speech Category",fontsize=15)
    plt.xticks(range(0,max(x)+1))
    plt.savefig(root_path+"/static/plots/undisserved.png")
    return 0


def plot_saudio(pred,ptime,wcounts,root_path):
    plt.figure(figsize=(16,8))
    plt.title("UNDISSERVED SPEECH ON WHICH MINUTES",fontsize=15,color="brown")
    p=pred[1]
    n=[str(x) for x in range(0,2,1)]
    y=[p for x in range(0,2,1)]
    plt.plot(n,y)
    plt.xlim(0,1)
    plt.yticks([-1,0,1,2,3,4],[' ',"Normal","Disrespect","Less Abusive","Abusive"," "])
    plt.xlabel("Minutes",fontsize=15)
    plt.ylabel("Speech Category",fontsize=15)
    plt.savefig(root_path+"/static/plots/undisserved.png")
    
    plt.figure(figsize=(16,8))
    plt.title("PROCESSING TIME FOR EACH MINUTE",fontsize=17,color="brown")
    l=2
    p=ptime[1]
    n=[str(x) for x in range(0,l,1)]
    y=[p for x in range(0,l,1)]
    plt.plot(n,y)
    plt.xlim(0,1)
    plt.xlabel("Minutes",fontsize=15)
    plt.ylabel("Processing Time",fontsize=15)
    plt.savefig(root_path+"/static/plots/processing.png")
    
    fig, ax = plt.subplots(figsize=(14, 8))
    sns.barplot(x=['1','2'],y=[wcounts[1],0],ax=ax)
    plt.title("NO OF WORDS SPOKE ON EACH MINUTES",fontsize=17,color="brown")
    plt.xlabel("Minutes",fontsize=17)
    plt.ylabel("No fo Words",fontsize=17)
    ax.bar_label(ax.containers[0], label_type='edge')
    ax.margins(y=0.1)
    plt.savefig(root_path+"/static/plots/no_of_words.png")