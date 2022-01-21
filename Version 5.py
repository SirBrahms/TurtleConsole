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

############################################
#Definition der ASCII Nummern für Buchstaben
############################################
KEY_1 = 49
KEY_2 = 50
KEY_3 = 51
KEY_4 = 52
KEY_5 = 53
KEY_6 = 54
KEY_7 = 55
KEY_8 = 56
KEY_9 = 57
KEY_0 = 48
KEY_Q = 81 
KEY_W = 87
KEY_E = 69
KEY_R = 82
KEY_T = 84
KEY_Z = 90
KEY_U = 85
KEY_I = 73
KEY_O = 79
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

############################################
#Funktionen zum Zeichnen einzelner Buchstaben und Zahlen
############################################
def eins():
    left(90)
    fd(4)
    bk(8)
    fd(4)
    right(90)
    fd(20)
    left(135)
    fd(8)

def zwei():
    right(90)
    fd(10)
    bk(10)
    left(55)
    fd(15)
    repeat(45):
        fd(0.4)
        left(4)

def drei():
    right(90)
    fd(8)
    left(90)
    fd(20)
    left(90)
    fd(8)
    bk(8)
    left(90)
    fd(10)
    right(90)
    fd(5)

def vier():
    left(90)
    fd(4)
    bk(8)
    fd(4)
    right(90)
    fd(20)
    left(135)
    fd(12)
    left(135)
    fd(15)

def fuenf():
    right(90)
    fd(10)
    left(90)
    fd(10)
    left(90)
    fd(10)
    right(90)
    fd(10)
    right(90)
    fd(10)

def sechs():
    right(90)
    repeat(4):
        fd(10)
        left(90)
    left(90)
    fd(20)
    right(90)
    fd(10)

def sieben():
    right(20)
    fd(21)
    left(110)
    fd(10)

def acht():
    fd(20)
    right(90)
    fd(8)
    right(90)
    fd(20)
    bk(10)
    right(90)
    fd(8)
    left(90)
    fd(10)
    left(90)
    fd(8)

def neun():
    right(90)
    fd(10)
    left(90)
    fd(10)
    left(90)
    repeat(4):
        fd(10)
        right(90)

def null():
    right(90)
    fd(10)
    left(90)
    fd(20)
    left(90)
    fd(10)
    left(90)
    fd(20)
    left(90)
def A():
    left(90)
    fd(3)
    bk(6)
    fd(3)
    right(90)
    fd(20)
    right(90)
    fd(10)
    right(90)
    fd(20)
    left(90)
    fd(2)
    bk(4)
    fd(2)
    left(90)
    fd(10)
    left(90)
    fd(10)
    left(180)

def B():
    fd(20)
    left(90)
    fd(2)
    bk(10)
    left(90)
    fd(10)
    right(90)
    fd(8)
    bk(8)
    left(90)
    fd(10)
    right(90)
    fd(10)

def C():
    right(90)
    fd(10)
    bk(10)
    left(90)
    fd(20)
    right(90)
    fd(10)

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
    forward(12)
    back(12)
    right(90)
    forward(10)
    left(90)
    forward(5)

def G():
    C()
    pu()
    bk(10)
    right(90)
    fd(20)
    left(90)
    fd(10)
    pd()
    left(90)
    fd(7)
    left(90)
    fd(7)
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
    forward(20)
    left(90)
    fd(4)
    back(8)
    fd(4)
    left(90)
    fd(20)
    right(90)
    fd(10)
    right(90)
    fd(8)
    left(90)
    fd(3)
    bk(6)
    left(180)


def K():
    I()
    pu()
    fd(4)
    left(90)
    fd(10)
    pd()
    right(45)
    bk(13)
    fd(13)
    right(90)
    bk(13)

def L():
    forward(20)
    left(90)
    forward(6)
    back(12)
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
    right(90)
    fd(15)
    left(90)
    fd(20)
    left(90)
    fd(15)
    left(90)
    fd(20)
    left(90)

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
    fd(15)
    right(50)
    forward(3)
    bk(10)
    fd(7)
    left(50)
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
    fd(20)
    left(90)
    fd(2)
    bk(4)
    fd(2)
    left(90)
    fd(20)
    left(90)
    fd(10)
    left(90)
    fd(20)
    left(90)
    fd(2)
    bk(4)

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
    fd(5)
    back(10)
    fd(5)
    right(130)
    fd(26)
    left(130)
    fd(5)
    bk(10)
    fd(5)
    left(50)
    fd(13)
    right(100)
    fd(13)
    left(45)
    fd(5)
    bk(10)
    fd(5)
    left(135)
    fd(26)
    left(45)
    fd(5)
    bk(10)

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
    forward(12)
    left(90)
    forward(5)
    pu()
    bk(5)
    left(90)
    fd(12)
    right(120)
    pd()
    fd(23)
    left(120)
    fd(12)
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
######################################    
#funktion zur überprüfung der Position
######################################
def posJmp():
    global Ypos #initialisierung der Y-Positionsvariable (r/w zugriff)
    pos = getX() #die X-Koordinate wird in der Variable "pos" gespeichert
    #Umbruch Seitlich
    if(pos >= 350):
        Ypos -= 30
        setPos(-350, Ypos)
    #Wechsel der Seite
    if(Ypos == -280):
        clear("black")
        Ypos = 230
        setPos(-350, Ypos)

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

def StringList(List):
    #funktion um Array in Strings umzuwandeln
    string_catcher = "" #späterer Rückgabewert
    for e in List:
        string_catcher += e
    return string_catcher  

def draw_letter(key):
    global ctrlList #initialisierung der Command-Liste (r/w zugriff)
    """
    Aufbau eines Schriftabgleiches:
    
    1. Eigentiche Funktion wird aufgerufen (z.B: Q() oder W())
    2. Positionierung der Turtle, so dass der nächste buchstabe korrekt positioniert ist
    *Bei punkt, enter, komma, blob sind diese Abgleich nicht vonnöten, da die Funktion selbst sie bereits übernimmt
    """
    #abgleichung der Variable "key" mit den Vorher definierten ASCII variablen
    if key == KEY_1:
        eins()
        pu()
        left(135)
        fd(18)
        right(90)
        fd(14.35)
        left(180)
        pd()
        ctrlList.append("1")
    elif key == KEY_2:
        zwei()
        pu()
        left(125)
        fd(15)
        right(90)
        fd(19.2)
        left(180)
        pd()
        ctrlList.append("2")
    elif key == KEY_3:
        drei()
        pu()
        setH(90)
        fd(20)
        right(90)
        fd(10)
        left(180)
        pd()
        ctrlList.append("3")
    elif key == KEY_4:
        vier()
        pu()
        fd(10)
        right(90)
        fd(11.5)
        left(180)
        pd()
        ctrlList.append("4")
    elif key == KEY_5:
        fuenf()
        pu()
        fd(10)
        right(90)
        fd(20)
        left(180)
        pd()       
        ctrlList.append("5")
    elif key == KEY_6:
        sechs()
        pu()
        fd(10)
        right(90)
        fd(20)
        left(180)
        pd()
        ctrlList.append("6")
    elif key == KEY_7:
        sieben()
        left(180)
        pu()
        fd(20)
        right(90)
        fd(19.83)
        left(180)
        pd()
        ctrlList.append("7")
    elif key == KEY_8:
        acht()
        pu()
        fd(12)
        right(90)
        left(180)
        pd()
        ctrlList.append("8")
    elif key == KEY_9:
        neun()
        pu()
        left(180)
        fd(15)
        right(90)
        fd(10)
        left(180)
        pd()
        ctrlList.append("9")
    elif key == KEY_0:
        null()
        pu()
        fd(20)
        left(90)
        pd()
        ctrlList.append("0")
        
    elif key == KEY_Q:
        Q()
        pu()
        fd(10)
        setH(180)
        pd()
        setH(360)
        ctrlList.append("Q")
    elif key == KEY_W:
        W()
        pu()
        fd(30)
        setH(360)
        pd()
        ctrlList.append("W")
    elif key == KEY_E:
        E()
        pu()
        right(90)
        fd(20)
        left(90)
        fd(9)
        setH(360)
        pd()
        ctrlList.append("E")
    elif key == KEY_R:
        R()
        pu()
        left(45)
        fd(11)
        setH(360)
        fd(1.2)
        pd()
        ctrlList.append("R")
    elif key == KEY_T:
        pu()
        right(90)
        fd(8)
        left(90)
        pd()
        T()
        pu()
        setH(180)
        fd(20)
        setH(90)
        fd(5)
        setH(360)
        pd()
        ctrlList.append("T")
    elif key == KEY_Z:
        Z()
        pu()
        setH(90)
        forward(25)
        setH(180)
        forward(15)
        setH(360)
        pd()
        ctrlList.append("Z")      
    elif key == KEY_U:      
        U()
        pu()
        setH(90)
        fd(11)
        setH(180)
        fd(20)
        setH(360)
        pd()
        ctrlList.append("U")
    elif key == KEY_I:
        I()
        pu()
        setH(180)
        fd(20)
        setH(90)
        fd(8)
        setH(360)
        pd()
        ctrlList.append("I")
    elif key == KEY_O:
        O()
        pu()
        setH(90)
        fd(25)
        setH(180)
        fd(0)
        setH(360)
        pd()
        ctrlList.append("O")
    elif key == KEY_P:
        P()
        pu()
        fd(10)
        setH(180)
        fd(16)
        setH(360)
        pd()
        ctrlList.append("P")
    elif key == KEY_A:
        A()
        pu()
        fd(22)
        right(90)
        fd(10)
        left(180)
        pd()
        ctrlList.append("A")
    elif key == KEY_S:
        S()
        pu()
        fd(10)
        setH(180)
        fd(20)
        setH(360)
        pd()
        ctrlList.append("S")
    elif key == KEY_D:
        D()
        pu()
        setH(90)
        forward(15)
        setH(360)
        pd()
        ctrlList.append("D")
    elif key == KEY_F:
        F()
        pu()
        fd(15)
        setH(180)
        fd(10)
        setH(360)
        pd()
        ctrlList.append("F")
    elif key == KEY_G:
        G()
        pu()
        setH(90)
        fd(16)
        setH(180)
        fd(7)
        setH(360)
        pd()
        ctrlList.append("G")
    elif key == KEY_H:
        H()
        pu()
        setH(90)
        fd(10)
        setH(180)
        fd(20)
        setH(360)
        pd()
        ctrlList.append("H")
    elif key == KEY_J:
        right(90)
        pu()
        fd(15)
        left(90)
        pd()
        J()
        pu()
        fd(20)
        setH(180)
        fd(8)
        left(180)
        pd()
        ctrlList.append("J")
    elif key == KEY_K:
        K()
        pu()
        setH(90)
        fd(10)
        setH(180)
        fd(0.8)
        setH(360)
        pd()
        ctrlList.append("K")
    elif key == KEY_L:
        L()
        pu()
        setH(180)
        fd(4)
        setH(90)
        fd(8)
        setH(360)
        pd()
        ctrlList.append("L")
    elif key == KEY_Y:
        pu()
        right(90)
        fd(10)
        left(90)
        pd()
        Y()
        pu()
        setH(90)
        fd(12)
        setH(180)
        fd(19.2)
        setH(360)
        pd()
        ctrlList.append("Y")
    elif key == KEY_X:
        X()
        pu()
        fd(24)
        setH(0)
        fd(2)
        setH(360)
        pd()
        ctrlList.append("X")
    elif key == KEY_C:
        C()
        pu()
        fd(8)
        setH(180)
        fd(20)
        setH(360)
        pd()
        ctrlList.append("C")
    elif key == KEY_V:
        V()
        pu()
        setH(90)
        fd(5)
        setH(180)
        fd(19.05)
        setH(360)
        pd()
        ctrlList.append("V")
    elif key == KEY_B:
        B()
        pu()
        setH(90)
        fd(20)
        setH(360)
        pd()
        ctrlList.append("B")
    elif key == KEY_N:
        N()
        pu()
        setH(90)
        fd(10)
        setH(180)
        fd(20)
        setH(360)
        pd()
        ctrlList.append("N")
    elif key == KEY_M:
        M()
        pu()
        setH(90)
        fd(10)
        setH(180)
        fd(20)
        setH(360)
        pd()
        ctrlList.append("M")
    elif key == KEY_EMPTY:
        leer()
        ctrlList.append(" ")
    elif key == KEY_RETURN:
        enter()
    elif key == KEY_DOT:
        punkt()
        ctrlList.append(".")
    elif key == KEY_COMMA:
        komma()
        ctrlList.append(",")
    elif key == "blob":
        blob()
    else:
        print "Diese Taste gibt es nicht"

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
