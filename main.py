from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QTextEdit

def addnum(num):
    global num1
    global num2
    global displaytext
    try:
        if other == None or (other == '' and num2 == ''):
            num1 += num
        else:
            num2 += num
        displaytext += num
        refresh()
    except:
        reset()

def addsymbol(symbol):
    global other
    global displaytext
    try:
        other = symbol
        displaytext += symbol
        refresh()
    except:
        reset()

def add1():
    addnum('1')
    
def add2():
    addnum('2')

def add3():
    addnum('3')

def add4():
    addnum('4')

def add5():
    addnum('5')

def add6():
    addnum('6')

def add7():
    addnum('7')

def add8():
    addnum('8')

def add9():
    addnum('9')
    
def add0():
    addnum('0')
    
def dot():
    addnum('.')

def add():
    global other
    if other == '' or other == None:
        addsymbol('+')

def remove():
    global other
    if other == '' or other == None:
        addsymbol('-')

def multiply():
    global other
    if other == '' or other == None:
        addsymbol('*')

def divide():
    global other
    if other == '' or other == None:
        addsymbol('/')

def equals():
    global other
    global result
    global displaytext
    global num1
    global num2
    global total
    try:
        if other == '+':
            result = float(num1) + float(num2)
        elif other == '-':
            result = float(num1) - float(num2)
        elif other == '*':
            result = float(num1) * float(num2)
        elif other == '/':
            result = float(num1) / float(num2)
        if not (other == '' or other == None):  
            num1 = str(result)
            num2 = ''
            other = ''
            displaytext += '\n' + str(result)
            result = None
            refresh()
    except:
        reset()

def refresh():
    global total
    if other == '' and num2 == '':
        if num1 != '':
            total = num1
    elif other == None:
        if num1 == '':
            total = ''
        else:
            total = num1
    else:
        total = num1 + other + num2
    display.setText(displaytext)

def reset():
    global other
    global result
    global displaytext
    global num1
    global num2
    global total
    total = None
    num1 = ''
    num2 = ''
    other = None
    result = None
    displaytext = ''
    refresh()

def erase():
    global total
    global displaytext
    global num1
    global num2
    global other
    global result
    try:
        if displaytext[len(displaytext) - 1] != '\n' and len(displaytext) != 0:
            symbols = ['/', '*', '+', '-']
            counter = 0
            IsAtTheEnd = False 
            for i in symbols:
                if total.find(i) >= 0:
                    counter += 1
                    if total.find(i) == (len(total) - 1):
                        IsAtTheEnd = True
            if counter != 0:
                if IsAtTheEnd:
                    fvar = other
                    other = erasef(fvar)
                else:
                    fvar = num2
                    num2 = erasef(fvar)
            else:
                fvar = num1
                num1 = erasef(fvar)
            fvar = total
            total = erasef(fvar)
            fvar = displaytext
            displaytext = erasef(fvar)
        refresh()
    except:
        reset()

def power(var):
    global result
    global num1
    global num2
    global other
    global total
    global displaytext
    try:
        result = pow(float(num1), var)
        num1 = str(result)
        displaytext += '\n' + str(result)
        result = None
        refresh()
    except:
        reset()

def erasef(x):
    localvar = ''
    for i in range(len(x) - 1):
        localvar += x[i]
    x = ''
    for i in localvar:
        x += i
    return x

def square():
    power(2)

def squareroot():
    power(1/2)

def neg():
    try:
        global num1
        global num2
        global displaytext
        if num2 == '':
            times = len(num1)
            num1 = float(num1)
            num1 *= -1
            num1 = str(num1)
            numlocal = num1
        else:
            times = len(num2)
            num2 = float(num2)
            num2 *= -1
            num2 = str(num2)
            numlocal = num2
        displaytextlocal = []
        counter = times
        for i in range(times):
            displaytextlocal.append(displaytext[len(displaytext)-(counter+1)])
            counter -= 1
        displaytextlocal2 = []
        for i in range(len(displaytext)-times):
            displaytextlocal2.append(displaytext[i])
        displaytext = ''
        for i in displaytextlocal2:
            displaytext += i
        for i in range(times):
            displaytextlocal.remove(displaytextlocal[len(displaytextlocal)-1])
        displaytextlocal.append('(')
        for i in numlocal:
            displaytextlocal.append(str(i))
        displaytextlocal.append(')')
        for i in displaytextlocal:
            displaytext += i
        refresh()
    except:
        reset()

app = QApplication([])
w = QWidget()
num1 = ''
num2 = ''
other = None
result = None
total = None
displaytext = ''
w.setWindowTitle('Calculator')
w.resize(300, 500)
pb1 = QPushButton('1')
pb2 = QPushButton('2')
pb3 = QPushButton('3')
pb4 = QPushButton('4')
pb5 = QPushButton('5')
pb6 = QPushButton('6')
pb7 = QPushButton('7')
pb8 = QPushButton('8')
pb9 = QPushButton('9')
pb10 = QPushButton('0')
pb11 = QPushButton('+')
pb12 = QPushButton('-')
pb13 = QPushButton('X')
pb14 = QPushButton('/')
pb15 = QPushButton('=')
pb16 = QPushButton('.')
pb17 = QPushButton('Reset')
pb18 = QPushButton('Erase')
pb19 = QPushButton('x*x')
pb20 = QPushButton('squareroot')
pb21 = QPushButton('+ -> -')
display = QTextEdit()
display.setReadOnly(True)
lh1 = QHBoxLayout()
lh2 = QHBoxLayout()
lh3 = QHBoxLayout()
lh4 = QHBoxLayout()
lh5 = QHBoxLayout()
lv1 = QVBoxLayout()
lh1.addWidget(pb1)
lh1.addWidget(pb2)
lh1.addWidget(pb3)
lh1.addWidget(pb11)
lh2.addWidget(pb4)
lh2.addWidget(pb5)
lh2.addWidget(pb6)
lh2.addWidget(pb12)
lh3.addWidget(pb7)
lh3.addWidget(pb8)
lh3.addWidget(pb9)
lh3.addWidget(pb13)
lh4.addWidget(pb16)
lh4.addWidget(pb10)
lh4.addWidget(pb15)
lh4.addWidget(pb14)
lh5.addWidget(pb17)
lh5.addWidget(pb21)
lh5.addWidget(pb18)
lh5.addWidget(pb19)
lh5.addWidget(pb20)
lv1.addWidget(display)
lv1.addLayout(lh1)
lv1.addLayout(lh2)
lv1.addLayout(lh3)
lv1.addLayout(lh4)
lv1.addLayout(lh5)
w.setLayout(lv1)
w.show()
pb1.clicked.connect(add1)
pb2.clicked.connect(add2)
pb3.clicked.connect(add3)
pb4.clicked.connect(add4)
pb5.clicked.connect(add5)
pb6.clicked.connect(add6)
pb7.clicked.connect(add7)
pb8.clicked.connect(add8)
pb9.clicked.connect(add9)
pb10.clicked.connect(add0)
pb11.clicked.connect(add)
pb12.clicked.connect(remove)
pb13.clicked.connect(multiply)
pb14.clicked.connect(divide)
pb15.clicked.connect(equals)
pb16.clicked.connect(dot)
pb17.clicked.connect(reset)
pb18.clicked.connect(erase)
pb19.clicked.connect(square)
pb20.clicked.connect(squareroot)
pb21.clicked.connect(neg)
app.exec()