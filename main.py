'''
Created on Mar 2, 2017

@author: Krystal
'''
#from __init__ import *

from tkinter import *
from main import *

import os, glob
import datetime


alphabet = "abcdefghijklmnopqrstuvwxyz"
numberS = ["1","2","3","4","5","6","7","8","9","0"]
shift = 1


list1=list("abcdefghijklmnopqrstuvwxyz")  
num=1 
list2 = []








PasswordLibrary = []

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
myfile_path = os.path.join(ROOT_PATH)

RecentActivity = open("RecentActivity.txt", "a")
PasswordLog = open("PasswordLog.txt", "a")


def main_Runner():
    RecentActivity.write("\n\n\nNew Session Started! - " + str(datetime.datetime.now()) +"- Word Cryption --MagixCaseCode#" + str(shift * 26 - 23) + "\n")
    global phraseStr
    global Encode
    global Decode
    global newPhrase
    global shiftEntry
    global UnNumber
    phrase = ""
    purpose = "encrypt"
    newPhraseu = "_"
    
    with open('PasswordLog.txt', 'r+') as myfile:
        data=myfile.readlines()
    counter1 = 0
    for item in data:
        if "\n" in item:
            item = item[16:-3]
        elif "\n" not in item:
            item = item[16:-2]
        PasswordLibrary.append(item) 
        counter1 += 1
    
    counter = 0
    if "Un" not in data:
        UnNumber = int("000000")
        
        
    elif "Un" in data:
        counter8 = -1
        UnNumber = data[counter8][3:11]
        
    def GUI_Setup():
        global root
        global newPhrase
        global WhiteSpace
        global sendLabel
        global phraseField
        global returnLabel
        global resultLabel
        global EncodeButton
        global DecodeButton
        global PasswordAttempt
        
        root = Tk()
        root.title("Crypter")
        root.geometry("250x150")
        
        global phraseStr
        global shiftEntry
        global shiftLabel
        phraseStr = StringVar()
        
        phraseField = Entry(root, textvariable = phraseStr)
        WhiteSpace = Label(root, text = "                    ")
        WhiteSpace2 = Label(root, text = "                    ")
        resultLabel = Label(root, text = newPhraseu)
        returnLabel = Label(root, text = "Here is your \nreturned message:")
        sendLabel = Label(root, text = "Please text your \nmessage below.")
        EncodeButton = Button(root, text = "Encrypt", command=EncodePassThrough)
        DecodeButton = Button(root, text = "Decrypt", command=DecodePassThrough)
        shiftDONOTUSEStr = StringVar()
        shiftEntry = Entry(root, textvariable = shiftDONOTUSEStr, width = 10)
        shiftLabel = Label(root, text = "Password:")
        
        WhiteSpace.grid(row=0, column=0, rowspan=4) 
        sendLabel.grid(row=0, column=1, columnspan = 2)
        phraseField.grid(row=1, column=1, columnspan = 2)
        phraseField.focus_force()
        shiftEntry.grid(row=5, column = 2)
        shiftLabel.grid(row=5, column = 1)
        returnLabel.grid(row=2, column=1, columnspan = 2)
        resultLabel.grid(row=4, column=1, columnspan = 2)
        EncodeButton.grid(row=5, column=0)
        DecodeButton.grid(row=5, column=3)
        
        def center(toplevel):
            toplevel.update_idletasks()
            w = toplevel.winfo_screenwidth()
            h = toplevel.winfo_screenheight()
            size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
            x = w/2 - size[0]/2
            y = h/2 - size[1]/2
            toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))
        PasswordAttempt = shiftEntry.get()
        win = root
        center(win)
        #root.resizable(0, 0)
        root.mainloop()
        
        sys.exit(0)
        
        
    def passwordENDE():
        global shift
        global UnNumber
        global PasswordAttempt
        counter7 = -1
        if len(shiftEntry.get()) == 0:
            counter7 = 0
        for x in range(0,len(shiftEntry.get())):
            if shiftEntry.get()[x] in numberS:
                counter7 += 1
            elif shiftEntry.get()[x] not in numberS:
                counter7 += 0
            else:
                print("ERROR 1003")
        if counter7+1 == len(shiftEntry.get()):
            PasswordAttempt = shiftEntry.get()
        elif counter7+1 != len(shiftEntry.get()):
            PasswordAttempt = int("10000001")
        else:
            print("ERROR 1004")
            
        with open('PasswordLog.txt', 'r+') as myfile:
            data=myfile.read()
        
        counter2 = 0
            
        for x in str(PasswordAttempt):
            if x not in alphabet:
                counter2 += 1
            elif x in alphabet:
                counter2 += 0
            else:
                print("ERROR 1002")
                
        if len(str(PasswordAttempt)) > 8 and counter2 == 8:
            PasswordAttempt = PasswordAttempt[:9]
            
        if counter2 == 8:
            PasswordAttempt = int(PasswordAttempt)
            shift = int(PasswordAttempt%26)
            if shift == 0 or shift == 26:
                shift += 8

        
    
        if str(PasswordAttempt) not in PasswordLibrary:
            PasswordLibrary.append(PasswordAttempt)
            UnNumber = int(UnNumber)
            UnNumber += 1
            PasswordLog.write("\nUN#" + str(UnNumber) + " -> |#" + str(PasswordAttempt) + "#|\n")
            
    def EncodePassThrough(*args):
        global phraseStr
        passwordENDE()
        phrasey = str(phraseField.get())
        Encode(phrasey.lower(), shift)
        
    def DecodePassThrough(*args):
        global phraseStr
        passwordENDE()
        phrasey = str(phraseField.get())
        Decode(phrasey.lower(), -shift)
        
    def ReFRESH(newPhrasey):
        global phraseStr
        root.update()
        global WhiteSpace
        global sendLabel
        global phraseField
        global returnLabel
        global resultLabel
        global EncodeButton
        global DecodeButton
        global shiftEntry
        global shiftLabel
        
        shiftDONOTUSEStr = StringVar()
        
        shiftEntry.destroy()
        shiftLabel.destroy()
        WhiteSpace.destroy()
        sendLabel.destroy()
        phraseField.destroy()
        returnLabel.destroy()
        resultLabel.destroy()
        EncodeButton.destroy()
        DecodeButton.destroy()
        
        WhiteSpace = Label(root, text = "                    ")
        WhiteSpace2 = Label(root, text = "                    ")
        resultLabel = Label(root, text = newPhrasey)
        returnLabel = Label(root, text = "Here is your \nreturned message:")
        sendLabel = Label(root, text = "Please text your \nmessage below.")
        phraseField = Entry(root, textvariable = str(phraseStr))
        EncodeButton = Button(root, text = "Encrypt", command=EncodePassThrough)
        DecodeButton = Button(root, text = "Decrypt", command=DecodePassThrough)
        shiftEntry = Entry(root, textvariable = shiftDONOTUSEStr, width = 10)
        shiftLabel = Label(root, text = "Password:")
        
        WhiteSpace.grid(row=0, column=0, rowspan=4) 
        sendLabel.grid(row=0, column=1, columnspan = 2)
        phraseField.grid(row=1, column=0, columnspan = 4)
        phraseField.focus_force()
        shiftEntry.grid(row=5, column = 2)
        shiftLabel.grid(row=5, column = 1)
        returnLabel.grid(row=2, column=1, columnspan = 2)
        resultLabel.grid(row=4, column=1, columnspan = 2)
        EncodeButton.grid(row=5, column=0)
        DecodeButton.grid(row=5, column=3)
        
        phraseField.focus_force()
        root.update()
             
    
    def Encode(phrase, shift):
        global PasswordAttempt
        global alphabet
        global phraseStr
        alphabet = ""
        list1=list("abcdefghijklmnopqrstuvwxyz")  
        num=1 
        list2 = []
        PasswordAttempt = str(PasswordAttempt)
        reOrder = str(PasswordAttempt[-1])
        reOrder = int(reOrder)
        newPhrase = ""
        lengthOfPhrase = len(phrase)
        counterLength = lengthOfPhrase
        jumper = 0
        
        for i in range(0,13): 
            if num > 26:
                num -= 26
            variable1=list1.pop(num)
            list2.append(variable1)
            num=num+1
        for x in range(0,len(list2)):
            if jumper >= (len(list2)-1):
                jumper -= int(len(list2))
            list1.append(list2[jumper])
            jumper += reOrder
        for x in range(0,26):
            alphabet += list1[x]
        
        for i in phrase:
            if i in alphabet:
                x = alphabet.index(i)
                if x < 26-shift:
                    newPhrase += alphabet[x+shift]
                elif x >= 26-shift:
                    newPhrase += alphabet[(x+shift)-26]
            elif i not in alphabet:
                newPhrase += i
            else:
                print("ERROR 1001") 
        
        RecentActivity.write("\nNew Log! -" + str(datetime.date.today()) + "- Word Encryption --MagixCaseCode#" + str(UnNumber) + " -- " + phrase + " -> " + newPhrase + "\n")
        root.geometry("250x150")
        counter6 = 0
        for x in range(0,(int(len(newPhrase)/10))):
            newPhrase = newPhrase[0:x*10] + "\n" + newPhrase[x*10:]
            counter6 = x
        root.geometry("250x" + str(165+((counter6*15))))
        root.update_idletasks()     
        ReFRESH(newPhrase)
        
    def Decode(phrase, shift):
        global PasswordAttempt
        global alphabet
        global phraseStr
        alphabet = ""
        list1=list("abcdefghijklmnopqrstuvwxyz")  
        num=1 
        list2 = []
        PasswordAttempt = str(PasswordAttempt)
        reOrder = str(PasswordAttempt[-1])
        reOrder = int(reOrder)
        newPhrase = ""
        lengthOfPhrase = len(phrase)
        counterLength = lengthOfPhrase
        jumper = 0
        
        for i in range(0,13): 
            if num > 26:
                num -= 26
            variable1=list1.pop(num)
            list2.append(variable1)
            num=num+1
        for x in range(0,len(list2)):
            if jumper >= (len(list2)-1):
                jumper -= int(len(list2))
            list1.append(list2[jumper])
            jumper += reOrder
        for x in range(0,26):
            alphabet += list1[x]
        
        for i in phrase:
            if i == " ":
                newPhrase += " "
            if i in alphabet:
                x = alphabet.index(i)
                if x < 26-shift:
                    newPhrase += alphabet[x+shift]
                elif x >= 26-shift:
                    newPhrase += alphabet[(x+shift)+26]
            if i in numberS:
                newPhrase += i
            if i == "." or i == "," or i == "!":
                newPhrase += i
             
        RecentActivity.write("\nNew Log! -" + str(datetime.date.today()) + "- Word Encryption --MagixCaseCode#" + str(UnNumber) + " -- " + phrase + " -> " + newPhrase + "\n")
        root.geometry("250x150")
        counter6 = 0
        for x in range(0,(int(len(newPhrase)/10))):
            newPhrase = newPhrase[0:x*10] + "\n" + newPhrase[x*10:]
            counter6 = x
        root.geometry("250x" + str(165+((counter6*15))))
        root.update_idletasks()     
        ReFRESH(newPhrase)
        
    GUI_Setup()
    
if __name__ == '__main__':
    main_Runner()
    quit()    