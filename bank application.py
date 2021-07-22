
import sys,os,csv
from datetime import *
b = 0
fname = 'newfile.txt'
def log_screen():

    print('1:create accont')
    print('2:login')
    print('3:exit')

    ch = int(input('enter choice:'))
    return ch

def write_data(x):
    f = open(fname,'a')
    obj = csv.writer(f)
    obj.writerow(x)
    f.close()

def create_ac():
    while True:
        u = input('enter username:')
        if os.path.exists(fname):
            info = read_data()
        else:
            info = {}
        if u not in info:
            break
        print('username already exits')

    while True:
        p = input('enter password:')
        if len(p)==4:
            break
        print('length must be 4')
    final = [u,p]
    write_data(final)

def read_data():
    #result = {}
    f1 = open(fname,'r')
    obj = csv.reader(f1)
    d = list(obj)
    f1.close()
    result = dict(d)
    print(result)
    return result   
def login():
    u = input('enter username:')
    p = input('enter password:')
    
    if os.path.exSits(fname):
        info = read_data()
    else:
         info = {}
    if u in info:
        if p==info[u]:
            return True
        else:
            print('pwd not match')
    else:
        print('username not found')




def main_screen():
    print('1:deposit')
    print('2:withdrwa')
    print('3:balance')
    print('4:logout')

    ch = int(input('enter choice:'))
    return ch
def deposit():
    global b
    amt = int(input('enter amount'))
    b = b+amt

def withdrwa():
    global b
    amt = int(input('enter amount:'))
    b = b-amt

def balance():
    print('bal is {}'.format(b))

while True:  
    k = log_screen()
    if k==1:
        create_ac()
    elif k==2:
        d = login()
        if d==True:
            while True:
                m = main_screen()
                if m==1:
                    deposit()
                elif m==2:
                    withdrwa()
                elif m==3:
                    balance()
                elif m==4:
                    break
                else:
                    print('plz enter a valid input')
        elif k==3:
            
            sys.exit()
        else:
            print('plz enter a valid input')


                

             
        
