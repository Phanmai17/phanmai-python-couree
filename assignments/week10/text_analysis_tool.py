#รับค่า password จากผู้ใช้
 
#password นั้นเเข็งเเรงหรือไม่
 
#passwordนั้นเเข็งเเรง ถ้าประกอบไปด้วยตัวเลข ตัวอักษร เเละ @ 1ตัว ยาวมากกว่า8ตัว
#ตัวอย่างหน้าจอ
#please input your passworrd:Boonchoo
#your password is not strong!
#please input your password:Boonchoo@123
#your password is strong!
def check_password():
    password = input("please input your password:")
 
    count_digit = 0
    count_alpha = 0
    count_at = 0
 
    for ch in password:
        if ch.isdigit():
            count_digit += 1
        if ch.isalpha():
            count_alpha += 1
        if ch == '@':
            count_at += 1
 
    if count_digit > 0 and count_alpha > 0 and count_at == 1 and len(password) > 8:
        print("your password is strong!")
    else:
        print("your password is not strong!")
 
check_password()