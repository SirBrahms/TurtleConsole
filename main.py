from gpanel import *
from gturtle import *
import os
import thread
makeTurtle()
hideTurtle()

############################################
#setup
############################################
Ypos = 230 #varible zur aufbewahrung des zurzeitlichen Y-Positionswert
setPos(-350, Ypos) #setzung der Turtleposition (Cursor)
setPenColor("green") #einstellung der default-Backgroundcolor
clear("black") #initialisierung des Hintergrundes
ctrlList = [] #Liste zur implementierung von programmen u/o logik
setFillColor("green") #setzung der standard Füllfarbe
flag = "" #flag-variable für codeimplementierung
saveVar = "C:\\Drawings\\" #standardpfad zur speicherung von "Zeichnungen"
try:
    os.mkdir("C:\\Drawings") #versuch ein ordner für die Zeichnungen zu erstellen
except OSError as error: 
    print(error)
col = 1 #variable zur navigation des "coldict" dictionarys
coldict = {
    "1" : [],
    "2" : [],
    "3" : [],
    "4" : [],
    "5" : [],
    "6" : [],
    "7" : [],
    "8" : [],
    "9" : [],
    "10" : [],
    "11" : [],
    "12" : [],
    "13" : [],
    "14" : [],
    "15" : [],
    "16" : [],
    "17" : [],
    "18" : []
}


############################################
#Definition der ASCII Nummern für Buchstaben
############################################
KEY_Q = 81
KEY_W = 87
KEY_E = 69
KEY_R = 82
KEY_T = 84
KEY_Z = 90
KEY_U = 85
KEY_I = 73
KEY_O = 79
KEY_P = 80
KEY_A = 65
KEY_S = 83
KEY_D = 68
KEY_F = 70
KEY_G = 71
KEY_H = 72
KEY_J = 74
KEY_K = 75
KEY_L = 76
KEY_Y = 89
KEY_X = 88
KEY_C = 67
KEY_V = 86
KEY_B = 66
KEY_N = 78
KEY_M = 77
KEY_EMPTY = 32
KEY_RETURN = 10
KEY_DOT = 46
KEY_COMMA = 44
KEY_DEL = 8

############################################
#Funktionen zum Zeichnen einzelner Buchstaben
############################################
def A():
    right(30)
    forward(20)
    right(130)
    forward(20)
    right(180)
    forward(10)
    left(70)
    forward(10)

def B():
    I()
    fd(4)
    left(180)
    repeat(45):
        fd(0.35)
        right(4)
    left(180)
    repeat(45):
        fd(0.35)
        right(4)

def C():
    pu()
    fd(10)
    setH(90)
    fd(10)
    setH(360)
    pd()
    right(90)
    dot(20)
    forward(2)
    setPenColor("black")
    dot(18)
    setPenColor("green")

def D():
    I()
    fd(4)
    left(180)
    repeat(45):
        fd(0.7)
        right(4)

def E(): 
    right(90)
    forward(15)
    back(15)
    left(90)
    forward(10)
    right(90)
    forward(10)
    back(10)
    left(90)
    forward(10)
    right(90)
    forward(15)

def F(): 
    forward(20)
    right(90)
    forward(15)
    back(15)
    right(90)
    forward(10)
    left(90)
    forward(5)

def G(): 
    C()
    setPenColor("green")
    pu()
    right(90)
    forward(3)
    pd()
    right(270)
    forward(3)
    right(90)
    forward(5)

def H():
    I()
    fd(4)
    left(90)
    fd(10)
    left(90)
    fd(12)
    right(90)
    fd(10)
    left(180)
    I()

def I():
    left(90)
    fd(4)
    back(8)
    fd(4)
    right(90)
    forward(20)
    left(90)
    fd(4)
    back(8)

def J():
    pu()
    setH(180)
    fd(5)
    setH(360)
    pd()
    pu()
    right(90)
    fd(10)
    left(90)
    fd(10)
    pd()
    fd(10)
    left(90)
    fd(4)
    bk(8)
    fd(4)
    left(90)
    fd(10)
    repeat(45):
        fd(0.25)
        right(4)

def K():
    I()
    pu()
    fd(4)
    left(90)
    fd(10)
    pd()
    right(50)
    bk(15)
    fd(15)
    right(75)
    bk(15)

def L():
    forward(20)
    left(90)
    forward(6)
    back(14)
    forward(6)
    left(90)
    forward(20)
    right(90)
    forward(4)
    back(15)
    right(90)
    forward(4)

def M():
    I()
    fd(4)
    left(135)
    fd(12)
    left(90)
    fd(12)
    right(135)
    pu()
    forward(20)
    left(180)
    pd()
    I()

def N():
    I()
    fd(4)
    left(90)
    left(30)
    fd(23)
    left(150)
    I()

def O():
    pu()
    fd(10)
    pd()
    dot(20)
    setPenColor("black")
    dot(18)
    setPenColor("green")

def P():
    rt(180)
    pu()
    back(20)
    pd()
    I()
    fd(4)
    left(180)
    left(90)
    pu()
    back(16)
    left(90)
    forward(5)
    dot(11)
    setPenColor("black")
    dot(9)
    pd()
    setPenColor("green")

def Q():
    O()
    setPenColor("green")
    right(130)
    pu()
    forward(6)
    pd()
    forward(8)

def R():
    P()
    right(150)
    pu()
    forward(5)
    pd()
    left(100)
    forward(18)

def S():
    right(90)
    fd(9)
    left(90)
    fd(10)
    left(90)
    fd(9)
    right(90)
    fd(10)
    right(90)
    fd(9)

def T():
    forward(20)
    left(90)
    forward(10)
    bk(20)

def U():
    J()
    forward(10)
    left(90)
    forward(2.5)
    bk(5)

def V():
    pu()
    right(90)
    fd(5)
    left(90)
    pd()
    left(30)
    fd(22)
    left(60)
    fd(4)
    back(8)
    fd(4)
    left(120)
    fd(22)
    left(120)
    fd(22)
    left(120)
    fd(4)
    back(8)

def W():
    pu()
    forward(20)
    pu()
    setH(90)
    forward(20)
    setH(360)
    pd()
    right(180)
    M()

def X():
    left(90)
    fd(4)
    back(8)
    fd(4)
    right(130)
    fd(24)
    left(130)
    fd(4)
    bk(8)
    fd(4)
    left(50)
    fd(12)
    right(100)
    fd(12)
    left(45)
    fd(4)
    bk(8)
    fd(4)
    left(135)
    fd(24)
    left(45)
    fd(4)
    bk(8)

def Y():
    left(90)
    fd(4)
    bk(8)
    fd(4)
    right(90)
    fd(10)
    left(40)
    fd(12)
    left(50)
    fd(4)
    bk(8)
    fd(4)
    left(130)
    fd(12)
    left(100)
    fd(12)
    left(130)
    fd(4)
    bk(8)
    fd(4)

def Z():
    right(90)
    forward(20)
    left(90)
    forward(5)
    pu()
    bk(5)
    left(90)
    fd(20)
    right(130)
    pd()
    fd(31)
    left(130)
    fd(20)
    left(90)
    fd(5)

def E(): 
    right(90)
    forward(15)
    back(15)
    left(90)
    forward(10)
    right(90)
    forward(10)
    back(10)
    left(90)
    forward(10)
    right(90)
    forward(15)

def N():
    I()
    fd(4)
    left(90)
    left(30)
    fd(23)
    left(150)
    I()
    
def I():
    left(90)
    fd(4)
    back(8)
    fd(4)
    right(90)
    forward(20)
    left(90)
    fd(4)
    back(8)

def blob():
    startPath()
    repeat(2):
        forward(10)
        right(90)
        forward(20)
        right(90)
    fillPath()
    pu()
    setH(90)
    fd(30)
    setH(360)
    pd()

def leer():
    pu()
    right(90)
    fd(25)
    setH(360)
    pd()

def punkt():
    dot(6)
    pu()
    setH(90)
    fd(6)
    setH(360)
    pd()

def komma():
    dot(6)
    setH(180)
    fd(5)
    bk(5)
    pu()
    setH(90)
    fd(6)
    setH(360)
    pd()
    
def enter():
    global Ypos #initialisierung der Y-Position (r/w zugriff)
    global ctrlList #initialisierung der Command-Liste (r/w zugriff)
    
    Ypos -= 30
    setPos(-350, Ypos)
    interpret(ctrlList)
    ctrlList = []
    
#funktion zur überprüfung der Position
def posJmp():
    global Ypos, col #initialisierung der Y-Positionsvariable (r/w zugriff)
    pos = getX() #die X-Koordinate wird in der Variable "pos" gespeichert
    #Umbruch Seitlich
    if(pos >= 350):
        Ypos -= 30
        setPos(-350, Ypos)
        col += 1
    #Wechsel der Seite
    if(Ypos == -280):
        clear("black")
        Ypos = 230
        setPos(-350, Ypos)
        col = 1

def interpret(ctrlList):
    global flag #initialisierung der "flag"-variable (r/w zugriff)
    global Ypos #initialisierung der Y-Positionsvariable (r/w zugriff)
    global saveVar #initialisierung des Default-Pfads für Zeichnungen (r/w zugriff)
    
    #flag-überprüfende-instanz (FÜI)
    #sie erlaubt es, eingaben "nachzuliefern"
    if(flag == "SC"):
        saveVar += StringList(ctrlList)
        savePlayground(saveVar, "png") #speichern des playgrounds
        if((savePlayground(saveVar + ".png", "png") == True)): #überprüft, ob die datei erfolgreich gespeichert werden konnte
            msgDlg("Datei erfolgreich Gespeichert!\nSpeicherort: C:\\Drawings", title = "Erfolg")
            flag = ""
            os.remove(saveVar) #entfernung der endungslosen datei, die dazugeneriert wird
            saveVar = "C:\\Drawings\\"
            return
        else:
            flag = ""
            msgDlg("Fehler während dem Erstellen der Datei:\nEine mögliche Lösung wäre es, die Konsole neuzustarten", title = "Fehler")
    
    #funktionen für befehle nach folgendem Schema hier:
    if(ctrlList == ['E', 'C', 'H', 'O']): #überprüfung der Liste zur interpretation
        test = inputString("Test")
        testsplit = split(test)
        for e in testsplit:
            key = ord(e.upper())
            draw_letter(key)
        draw_letter(KEY_RETURN)
    elif(ctrlList == ['S', 'C']): #command zur speicherung der "Zeichnung" (SC = SaveConsole oder SignCanvas)
         draw_letter("blob")
         flag = "SC"
    elif(ctrlList == ['C', 'L', 'S']): #command zur leerung des Bildschirmes
        clear("black")
        Ypos = 230
        setPos(-350, Ypos)
        
    #elif(...):

def deleteChar():
    global ctrlList, Ypos, coldict, KEY_RETURN, col
    if(ctrlList != []):   
        ctrlList.pop()
        clear("black")
        setPos(-350, Ypos)
        for e in coldict:
            if(coldict[e] != []):
                for letter in coldict[e]:
                    draw_letter(ord(letter), False)
                if(int(e) != col):
                    draw_letter(KEY_RETURN, False)

def editCtrlList(letter):
    global col, ctrlList, coldict
    ctrlList.append(letter)
    coldict[str(col)] = ctrlList
    print(coldict)

def StringList(List):
    #funktion um Array in Strings umzuwandeln
    string_catcher = "" #späterer Rückgabewert
    for e in List:
        string_catcher += e
    return string_catcher  

def draw_letter(key, add = True):
    global ctrlList, col #initialisierung der Command-Liste (r/w zugriff)
    """
    Aufbau eines Schriftabgleiches:
    
    1. Eigentiche Funktion wird aufgerufen (z.B: Q() oder W())
    2. Positionierung der Turtle, so dass der nächste buchstabe korrekt positioniert ist
    *Bei punkt, enter, komma, blob sind diese Abgleich nicht vonnöten, da die Funktion selbst sie bereits übernimmt
    """
    #abgleichung der Variable "key" mit den Vorher definierten ASCII variablen
    
    if key == KEY_Q:
        Q()
        setH(90)
        pu()
        fd(10)
        setH(180)
        fd(1)
        pd()
        setH(360)
        if(add):
            editCtrlList("Q")
    elif key == KEY_W:
        W()
        pu()
        fd(30)
        setH(360)
        pd()
        if(add):
            editCtrlList("W")
    elif key == KEY_E:
        E()
        pu()
        right(90)
        fd(20)
        left(90)
        fd(5)
        setH(360)
        pd()
        if(add):
            editCtrlList("E")
    elif key == KEY_R:
        R()
        pu()
        left(45)
        fd(5)
        setH(360)
        fd(0.75)
        pd()
        if(add):
            editCtrlList("R")
    elif key == KEY_T:
        T()
        pu()
        setH(180)
        fd(20)
        setH(90)
        fd(5)
        setH(360)
        pd()
        if(add):
            editCtrlList("T")
    elif key == KEY_Z:
        Z()
        pu()
        setH(90)
        forward(25)
        setH(180)
        forward(18.75)
        setH(360)
        pd()
        if(add):
            editCtrlList("Z")     
    elif key == KEY_U:      
        U()
        pu()
        setH(90)
        fd(15)
        setH(180)
        fd(15)
        setH(360)
        pd()
        if(add):
            editCtrlList("U")
    elif key == KEY_I:
        I()
        pu()
        setH(180)
        fd(20)
        setH(90)
        fd(5)
        setH(360)
        pd()
        if(add):
            editCtrlList("I")
    elif key == KEY_O:
        O()
        pu()
        setH(90)
        fd(22)
        setH(180)
        fd(10)
        setH(360)
        pd()
        if(add):
            editCtrlList("O")
    elif key == KEY_P:
        P()
        pu()
        fd(10)
        setH(180)
        fd(16)
        setH(360)
        pd()
        if(add):
            editCtrlList("P")
    elif key == KEY_A:
        A()
        pu()
        setH(90)
        fd(15)
        setH(180)
        fd(7.9)
        setH(360)
        pd()
        if(add):
            editCtrlList("A")
    elif key == KEY_S:
        S()
        pu()
        fd(5)
        setH(180)
        fd(20)
        setH(360)
        pd()
        if(add):
            editCtrlList("S")
    elif key == KEY_D:
        D()
        pu()
        setH(90)
        forward(15)
        setH(360)
        pd()
        if(add):
            editCtrlList("D")
    elif key == KEY_F:
        F()
        pu()
        fd(15)
        setH(180)
        fd(10)
        setH(360)
        pd()
        if(add):
            editCtrlList("F")
    elif key == KEY_G:
        G()
        pu()
        setH(90)
        fd(10)
        setH(180)
        fd(2)
        setH(360)
        pd()
        if(add):
            editCtrlList("G")
    elif key == KEY_H:
        H()
        pu()
        setH(90)
        fd(10)
        setH(180)
        fd(20)
        setH(360)
        pd()
        if(add):
            editCtrlList("H")
    elif key == KEY_J:
        J()
        pu()
        setH(90)
        fd(15)
        setH(180)
        fd(4.75)
        setH(360)
        pd()
        if(add):
            editCtrlList("J")
    elif key == KEY_K:
        K()
        pu()
        setH(90)
        fd(5)
        setH(180)
        fd(1.4)
        setH(360)
        pd()
        if(add):
            editCtrlList("K")
    elif key == KEY_L:
        L()
        pu()
        setH(180)
        fd(4)
        setH(90)
        fd(5)
        setH(360)
        pd()
        if(add):
            editCtrlList("L")
    elif key == KEY_Y:
        Y()
        pu()
        setH(90)
        fd(5)
        setH(180)
        fd(19.2)
        setH(360)
        pd()
        if(add):
            editCtrlList("Y")
    elif key == KEY_X:
        X()
        pu()
        fd(10)
        setH(0)
        fd(0.52)
        setH(360)
        pd()
        if(add):
            editCtrlList("X")
    elif key == KEY_C:
        C()
        pu()
        fd(10)
        setH(180)
        fd(10)
        setH(360)
        pd()
        if(add):
            editCtrlList("C")
    elif key == KEY_V:
        V()
        pu()
        setH(90)
        fd(5)
        setH(180)
        fd(19.05)
        setH(360)
        pd()
        if(add):
            ctrlList.append("V")
    elif key == KEY_B:
        B()
        pu()
        setH(90)
        fd(10)
        setH(360)
        pd()
        if(add):  
            editCtrlList("B")
    elif key == KEY_N:
        N()
        pu()
        setH(90)
        fd(10)
        setH(180)
        fd(20)
        setH(360)
        pd()
        if(add):
            editCtrlList("N")
    elif key == KEY_M:
        M()
        pu()
        setH(90)
        fd(10)
        setH(180)
        fd(20)
        setH(360)
        pd()
        if(add):
            editCtrlList("M")
    elif key == KEY_EMPTY:
        leer()
        if(add):
            editCtrlList(" ")
    elif key == KEY_RETURN:
        enter()
        if(add):
            col += 1
        print(col)
    elif key == KEY_DOT:
        punkt()
        if(add):
            editCtrlList(".")
    elif key == KEY_COMMA:
        komma()
        if(add):
            editCtrlList(",")
    elif key == "blob":
        blob()
    elif key == KEY_DEL:
        deleteChar()

#funktion zur aufteilung eines String in eine Liste
def split(word):
    return list(word)

#Anzeige der Willkommensnachricht
"""
msgListWelcome = ['W', 'I', 'L', 'L', 'K', 'O', 'M', 'M', 'E', 'N']
for letter in msgListWelcome:
    draw_letter(ord(letter))
draw_letter(KEY_RETURN)
"""

#Hauptausführungsloop   
while True:
    key = ""
    key = getKeyCodeWait() #Füllen des Buchstaben-ASCII codes in die Variable "key"  
    draw_letter(key) #übergabe des Key-Wertes an die Zeichnungsfunktion
    posJmp() #überprüfen, ob ein seitenumbruch vonnöten ist
    