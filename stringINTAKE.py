#Author:D4NG3R-Danny
#A python script to process a file or text-string into list
from pathlib import Path

def processSTR(txt: str = '',skip:list = []):
    '''
    processSTR takes in a string to turn it into a list with words in it and without comma,full-stop,etc..

    Attributes:
        txt: a string (Can also be a txt file with a txt in it)
        skip: a list full of words which will be skipped
    
    Additional:
        the input str and list[str] can be uppercase or lowercase, because it will be all turned lowercase
    '''
    #Catch if its a file and not a text inside a string
    if type(txt) != str:
        try:
            txt = processTXT()
        except TypeError:
            raise TypeError("Invalid Input: Needed string or file.txt",)
        except:
            raise Exception("Something realy wrong")
    
    end = ['.',' ',',',':',';',"!"]
    output = []
    txt = txt.lower()
    word = ''
    for letters in txt:
        if not(letters.isalpha()) or letters in end :
            if word == '':
                continue
            output.append(word)
            word = ''
            continue
        else:
            word += letters
            continue

    #Removes words from the output which are specified in the second parameter
    if skip != []:
        for words in output:
            if words in skip:
                output.remove(words)
            else:
                continue
    return output

def processTXT():
    '''
    processTXT takes a txt file and reads it and turns it into a string 
               which can be processed by processSTR()
    '''
    current = str(Path.cwd())
    while True:
        print("You are in the current directory:",current)
        print("Change the directory with filename.")
        file = input("Write complete filename (with .txt extension at the end from)")
        answer = input(file+"is this correct [y]/[n]")
        if answer == 'y':
            source = str(Path.cwd()) + file 
            break
    with open(source,'r',encoding='utf8') as new:
        txt = new.read()
    #alternative
    #txt = str(Path(source).read_text())
    return txt
