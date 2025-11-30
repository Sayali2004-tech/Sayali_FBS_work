import random
correct_userid = "admin"
correct_password = "12345"
userid = input("Enter User ID: ")
password = input("Enter Password: ")
if userid == correct_userid and password == correct_password:
    captcha = random.randint(1000, 9999)
    print("Captcha:", captcha)
    user_captcha = int(input("Enter the captcha shown above: "))
    if user_captcha == captcha:
        print("Login Successful!")
    else:
        print("Captcha verification failed. Login Denied.")
else:
    print("Invalid User ID or Password.")