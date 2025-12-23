import cv2 as p
import csv
import mysql.connector
import random
import time
import os
import pygetwindow as gw


img=p.imread("IMAGES/LOGO.png")
res_img=p.resize(img,(1620,880))
p.putText(res_img,"PRESS ANY KEY TO START THE ENGINE :))))",(100,800),p.FONT_HERSHEY_COMPLEX+p.FONT_ITALIC,2,(0,0,0),2,p.LINE_AA)
p.imshow("IMAGE WINDOW",res_img)
 
p.waitKey(0)
p.destroyAllWindows()
p.imwrite('IMAGES/res_img.png',res_img)



db = mysql.connector.connect(host="localhost",    user="root", password="Vishnu@12345",   database="mechanic_service",auth_plugin='mysql_native_password')
cursor = db.cursor()
def star():
         for i in range(165):
                        print("*",end="")
         print()
        

def screenshift():
        for i in range (65):
                time.sleep(0.09)
                print(" ")

def register_user():
            screenshift()
            x="SIGN UP".center(200,"*")
            for i in x:
                    print(i,end="")
                    time.sleep(0.002)
            print()
            print()
            a="Enter Your name".center(200)
            name = input(a)
            time.sleep(2)
            b="Create a password:".center(200)
            print()
            star()
            password = input(b)
            try:
                cursor.execute("INSERT INTO users (name, password) VALUES (%s, %s)", (name, password))
                db.commit()
                A="Account created successfully!\n".center(200)
                for i in A:
                        print(i,end="")
                        time.sleep(0.002)
                print()
                star()
            except:
                U="User already exists. Try logging in.\n"
                for i in U:
                        print(i,end="")
                        time.sleep(0.002)
                star()
                print()
                
def billing(issue,total):
    star()
    for i in ("Processing").center(200):
            print(i,end="")
            time.sleep(0.03)
    print()
    time.sleep(2)
    for i in ("Calculating Bill Report").center(200):
            print(i,end="")
            time.sleep(0.03)
    print()
    time.sleep(2)
    star()
    for i in ("Report Ready").center(200):
            print(i,end="")
            time.sleep(0.03)
    print()
    time.sleep(1)
    n="press 1 to download your report ".center(200)
    a=input(n).strip()
    
    if a =="1":
            
            b="bill report for"+ " "+ name+".csv"
            g=open("file counter.txt","a+")
            g.write("*")
            g.write("/n")
            a=g.readlines()
            f=open(b,"a+")
            ven=csv.writer(f)
            ven.writerow("                                                                                   RAPID REPAIR")
            nor=("invoice no - ",len(a)+1)
            ven.writerow(nor)
            pia=("sno","problem","quantity","cost","total")
            ven.writerow(pia)
            e=["Engine bearing failure","Blown head gasket","Blocked engine radiators","Malfunctioning oxygen sensor","Aged spark plugs"]
            bat=["Corrosion","Swollen battery","Deep cycling","Dead battery","Short circuit from separator failure","Charging system problems"]
            brak=["Charging system problems","ABS problems","Grinding brakes","Seized caliper","Break wire"]
            tyre=["Puncture","Under inflation","Sidewall damage","Cracking and bulging","Tread wear"]
            i=issue.lower()
            if i == "engine":
                    x=random.randint(1,3)
                    v=[]
                    c=0
                    for i in range(x) :
                            ind=total/x
                            n=random.randint(1,3)
                            
                            for j in e :
                                    if j not in v:
                                            v+=[j]
                                            h=len(v)
                                            er=(x,v[h-1],n , ind/n,ind)
                                            ven.writerow(er)
                                            
                                            c+=1
                                    else:
                                            continue
                            if c== x :
                                     break
                           
                    ver=("total cost = ",total)
                    ven.writerow(ver)
            if i=="tires":
                   x=random.randint(1,5)
                   v=[]
                   c=0
                   for i in range(x) :
                            ind=total/x
                            n=random.randint(1,3)
                            
                            for j in tyres :
                                    if j not in v:
                                            v+=[j]
                                            h=len(v)
                                            er=(x,v[h-1],n , ind/n,ind)
                                            ven.writerow(er)
                                            
                                            c+=1
                                    else:
                                            continue
                            if c== x :
                                     break
                   ver=("total cost = ",total)
                   ven.writerow(ver)
            if i=="battery":
                            x=random.randint(1,5)
                            v=[]
                            c=0
                            for i in range(x) :        
                                    ind=total/x
                                    n=random.randint(1,3)
                                    
                                    for j in brat :
                                            if j not in v:
                                                    v+=[j]
                                                    h=len(v)
                                                    er=(x,v[h-1],n , ind/n,ind)
                                                    ven.writerow(er)
                                                    
                                                    c+=1
                                            else:
                                                    continue
                                    if c== x :
                                           break
                            ver=("total cost = ",total)
                            ven.writerow(ver)

            if i=="brakes":
                            x=random.randint(1,5)
                            v=[]
                            c=0
                            for i in range(x) :
                              ind=total/x
                              n=random.randint(1,3)
                            
                              for j in tyres :
                                    if j not in v:
                                            v+=[j]
                                            h=len(v)
                                            er=(x,v[h-1],n , ind/n,ind)
                                            ven.writerow(er)
                                            
                                            c+=1
                                    else:
                                            continue
                                    if c== x :
                                              break
                            ver=("total cost = ",total)
                            ven.writerow(ver)


def eta(issue,cen):
        
        screenshift()
        for i in ("SEARCHING FOR MECHANIC").center(200,"-"):
            print(i,end="")
            time.sleep(0.03)
        time.sleep(2)
        print()
        star()
        print()
        for i in ("MECHANIC FOUND").center(200):
            print(i,end="")
            time.sleep(0.03)
        time.sleep(2)
        f=open("mechanics.txt","r")
        m=f.readline()
        a=m.split(",")
        img=p.imread("IMAGES/mech.jpg")
        res_img=p.resize(img,(1720,980))
        p.putText(res_img,"------Mechanic Details -----",(100,100),p.FONT_HERSHEY_COMPLEX+p.FONT_ITALIC,2,(244, 234,255),2,p.LINE_AA)
        namer="Mechanic Name             "+random.choice(a)
        p.putText(res_img,namer,(100,300),p.FONT_HERSHEY_COMPLEX+p.FONT_ITALIC,2,(244, 234,255),2,p.LINE_AA)
        pricer="Company name               "+str(cen)
        p.putText(res_img,pricer,(100,500),p.FONT_HERSHEY_COMPLEX+p.FONT_ITALIC,2,(244, 234,255),2,p.LINE_AA)
        issuer="Phone no                     "+str(random.randint(9047562456,9923565786))
        p.putText(res_img,issuer,(100,700),p.FONT_HERSHEY_COMPLEX+p.FONT_ITALIC,2,(244, 234,255),2,p.LINE_AA)
        p.putText(res_img,"----PRESS ANY KEY TO PROCEED  -----",(100,900),p.FONT_HERSHEY_COMPLEX+p.FONT_ITALIC,2,(244, 234,255 ),2,p.LINE_AA)
        p.imshow("IMAGE WINDOW",res_img)

        p.waitKey(0)
        p.destroyAllWindows()
        p.imwrite('IMAGES/resss.jpg',res_img)
        

        maps=["IMAGES/map1.jpeg","IMAGES/map2.jpeg","IMAGES/map3.jpeg","IMAGES/map4.jpeg"]
        img=p.imread(random.choice(maps))
        res_img=p.resize(img,(1620,880))
        eter="estimated time of arrival  "+str(random.randint(15,30))+"min"
        p.putText(res_img,eter,(100,800),p.FONT_HERSHEY_COMPLEX+p.FONT_ITALIC,2,(0,0,0),2,p.LINE_AA)
        p.imshow("IMAGE WINDOW",res_img)
 
        p.waitKey(0)
        p.destroyAllWindows()
        p.imwrite('IMAGES/resss_img.jpeg',res_img)
        payment(issue)
        
def payment(issue):
        screenshift()
        for i in ("PROCEEDING TO PAYMENT").center(200):
            print(i,end="")
            time.sleep(0.03)
        print()
        time.sleep(2)
        star()
        for i in ("WELCOME TO PAYEMENT PAGE").center(200):
            print(i,end="")
            time.sleep(0.03)
        print()
        print()
        star()
        time.sleep(2)
        for i in ("Calculating your total").center(200):
            print(i,end="")
            time.sleep(0.03)
        print()
        time.sleep(2)
        a=len(issue)*100+random.randint(200,300)
        star()
        q="YOUR TOTAL IS "+str(a)
        for i in (q).center(200):
            print(i,end="")
            time.sleep(0.03)
        print()
        namer="NAME                      "+name
        issuer="ISSUE                    "+issue
        pricer="PRICE                   "+str(a)
        
        img=p.imread("IMAGES/bill.jpeg")
        res_img=p.resize(img,(1620,880))
        p.putText(res_img,"------YOUR BILL REPORT -----",(300,100),p.FONT_HERSHEY_COMPLEX+p.FONT_ITALIC,2,(244, 234,255),2,p.LINE_AA)
        p.putText(res_img,namer,(100,300),p.FONT_HERSHEY_COMPLEX+p.FONT_ITALIC,2,(244, 234,255),2,p.LINE_AA)
        p.putText(res_img,pricer,(100,500),p.FONT_HERSHEY_COMPLEX+p.FONT_ITALIC,2,(244, 234,255),2,p.LINE_AA)
        p.putText(res_img,issuer,(100,700),p.FONT_HERSHEY_COMPLEX+p.FONT_ITALIC,2,(244, 234,255),2,p.LINE_AA)
        p.putText(res_img,"----PRESS ANY KEY TO PROCEED  -----",(100,800),p.FONT_HERSHEY_COMPLEX+p.FONT_ITALIC,2,(244, 234,255),2,p.LINE_AA)
        p.imshow("IMAGE WINDOW",res_img)

        p.waitKey(0)
        p.destroyAllWindows()
        p.imwrite('IMAGES/res.jpeg',res_img)
        billing(issue,a)

def login_user():
                a=0
                while a==0:
                    l="Login".center(200)
                    for i in l:
                            print(i,end="")
                    print()
                    time.sleep(2)
                    b="Enter Name".center(100)
                    name = input(b)
                    print("..............".center(200))
                    time.sleep(2)
                    print()
                    c="Enter Your Password".center(100)
                    password = input(c)
                    print()
                    star()
                    print()
                    cursor.execute("SELECT * FROM users WHERE name=%s AND password=%s", (name, password))
                    user = cursor.fetchone()
                    print()
                    star()
                    if user:
                        print("\n"*3)
                        p=" Login successful!\n".center(200)
                        for i in p:
                                print(i,end="")
                                time.sleep(0.05)
                        z='''Enter your vehicle issue
                                            Engine
                                            Tyres
                                            Battery
                                            Brakes
                                                                             '''.center(200)
                        issue = input(z)
                        get_service(issue)
                        a=1
                        break
                        db.close()

                    else:
                        print("Invalid credentials!\n")
                        continue
                        
def get_service(issue):
            cursor.execute("SELECT name, location FROM service_centers WHERE issue_type=%s", (issue,))
            centers = cursor.fetchall()
            if centers:
                center = random.choice(centers)
                
                s="SEARCHING.....".center(200)
                for i in s :
                        print(i,end="")
                        
                        time.sleep(0.05)
                print("\n")
                star()
                        
                print("\n")
                print((f"✅ Assigned Service Center: {center[0]} ({center[1]})\n").center(100,"*"))
                cen=center[0]
                eta(issue,cen)
                return
                
            else:
                print("❌ No service center available for this issue.\n".center(100,"*"))

        # Main Program

star()
a="******Welcome To Rapid Repair******".center(200)
for i in a :
        print(i,end="")
        time.sleep(0.05)
print("\n"*5)
c="Enter Your Name ".center(100)
name=input(c).upper()
print("\n"*2)
x=("Welcome "+name).center(200)
for i in x:
        print(i,end="")
        time.sleep(0.025)
print("\n"*2)
b="Do you have an account? (yes/no): ".center(100)
choice = input(b).lower()

if choice == "no":
            register_user()
            login_user()
            

elif choice == "yes":
           
                
            login_user()


#end screen
screenshift()
for i in ("WE HOPE YOUR PROBLEM HAS BEEN RECTIFIED").center(200):
            print(i)
            
            time.sleep(0.03)
print()
star()
for i in ("RAPID REPAIR").center(200):
            print(i,end="")
            time.sleep(0.03)
            
print()
star()




        
    

                    
            


                

 

