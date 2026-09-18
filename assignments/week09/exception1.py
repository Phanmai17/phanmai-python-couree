"""
โจทย์ 1: เครื่องคำนวณอย่างปลอดภัย

เขียนโปรแกรมเครื่องคำนวณอย่างปลอดภัย โดยรับ ตัวเลข 2 จำนวน และ ตัวดำเนินการ 1 ตัว ได้แก่ + - * / แล้วแสดงผลลัพธ์

โปรแกรมต้องจัดการกรณีต่อไปนี้

ผู้ใช้กรอกข้อมูลที่ไม่ใช่ตัวเลข → ValueError

ผู้ใช้เลือกตัวดำเนินการอื่นนอกเหนือจาก + - * / → ใช้ raise ValueError

ผู้ใช้พยายามหารด้วยศูนย์ → ZeroDivisionError

โปรแกรมต้องแสดง จบการทำงานเสมอด้วย finally

ตัวอย่างผลลัพธ์ที่คาดหวัง

ตัวเลขที่ 1: 10

ตัวเลขที่ 2: 0

เครื่องหมาย (+, -, *, /): /

ไม่สามารถหารด้วยศูนย์ได้

จบการทำงาน
"""
 
try:
    num1= float(input("ตัวเลขที่ 1:"))
    num2= float(input("ตัวเลขที่ 2:"))

    operator = input("เครื่องหมาย (+,-,*,/):")

    if operator =="+":
        result = num1+num2
    elif operator=="-":
         result = num1-num2
    elif operator=="*":
        result = num1*num2
    elif operator=="/":
        if num2==0:
            raise ZeroDivisionError

         result = num1/num2
           else:

            raise ValueError("เครื่องหมายไม่ถูกต้อง")

        print("ผลลัพธ์:", result)

    except ValueError:

        print("กรุณากรอกข้อมูลให้ถูกต้อง")

    except ZeroDivisionError:

        print("ไม่สามารถหารด้วยศูนย์ได้")

    finally:

        print("จบการทำงาน")
    calculator()