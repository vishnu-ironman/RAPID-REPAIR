import cv2 as p


import mysql.connector
import random
def intro():
        img=p.imread("LOGO.png")
        res_img=p.resize(img,(1920,1080))
        p.putText(res_img,"PRESS ANY KEY TO START THE ENGINE :))))",(300,1000),p.FONT_HERSHEY_COMPLEX+p.FONT_ITALIC,2,(0,0,0),2,p.LINE_AA)
        p.imshow("IMAGE WINDOW",res_img)

        p.waitKey(0)
        p.destroyAllWindows()
        p.imwrite('res_img.png',res_img)


def main():
        # Database Connection
        db = mysql.connector.connect(host="localhost",    user="root", password="Vishnu@12345",   database="mechanic_service",auth_plugin='mysql_native_password')
        cursor = db.cursor()

        def register_user():
            name = input("Enter your name: ")
            password = input("Create a password: ")
            try:
                cursor.execute("INSERT INTO users (name, password) VALUES (%s, %s)", (name, password))
                db.commit()
                print("Account created successfully!\n")
            except:
                print("User already exists. Try logging in.\n")

        def login_user():
            name = input("Enter your name: ")
            password = input("Enter your password: ")
            cursor.execute("SELECT * FROM users WHERE name=%s AND password=%s", (name, password))
            user = cursor.fetchone()
            if user:
                print("Login successful!\n")
                return True
            else:
                print("Invalid credentials!\n")
                

        def get_service(issue):
            cursor.execute("SELECT name, location FROM service_centers WHERE issue_type=%s", (issue,))
            centers = cursor.fetchall()
            if centers:
                center = random.choice(centers)
                print(f"✅ Assigned Service Center: {center[0]} ({center[1]})\n")
            else:
                print("❌ No service center available for this issue.\n")

        # Main Program
        print("=== Welcome to Web Mechanic Service ===")
        choice = input("Do you have an account? (yes/no): ").lower()

        if choice == "no":
            register_user()
            login_user()
            

        elif choice == "yes":
            if not login_user():
                
                login_user()
                
                

        # After login
        issue = input("Enter your vehicle issue (Engine/Tyres/Battery/Brakes): ")
        get_service(issue)

        db.close()

intro()
main()
