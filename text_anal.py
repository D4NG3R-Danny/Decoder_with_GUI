#Author:D4NG3R-D4NNY
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

def count_plot(data: dict):
    
    values_data = []
    keys_data   = []
    for keys, values in data.items():
        values_data.append(values)
        keys_data.append(keys)

    fig = plt.figure(figsize=(10,30))
    p1 = plt.bar(keys_data,values_data, width=1,edgecolor="white")
    
    #Watermark by D4NG3R-D4NNY
    #plt.text(0,0,"GITHUB:D4NGER-D4NNY")
    plt.legend(["D4NG3R-D4NNY"])

    #Labeling
    plt.xlabel("Letters")
    plt.ylabel("Frequency")
    plt.title("Distr. of letters in a text")

    #Create the plot in a window
    return fig

#return a dict of amount of each letter {a:0,b:13,c: ...}
def letter_count(text: str)-> dict:
    counter = {}
    for letters in text:
        counter.setdefault(letters,0)
        counter[letters] += 1
    
    return counter

if __name__ == "__main__":
    a = letter_count(" i am an utter idiot like a fox with wings of xylophon")
    count_plot(a)
