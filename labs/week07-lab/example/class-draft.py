"""
การเขียนโปรแกรมมี 2 รูปแบบ

1) Structured Program
   ==> การเขียนโปรแกรมแบบมีโครงสร้าง เช่น C, Python

2) Object-Oriented Program (OOP)
   ==> การเขียนโปรแกรมเชิงวัตถุ เช่น Java, C#, Python
"""


"""
แนวคิดของ OOP

เราออกแบบโปรแกรมของเราใน Class

การเขียนโปรแกรมเพื่อแก้ปัญหา
ต้องมี
- ข้อมูล (Data) ==> Attribute
- การกระทำ (Action) ==> Method
"""


class ClassName:
    # Constructor method
    # กำหนดข้อมูลที่จำเป็นต้องใช้ในการแก้ปัญหา

    def __init__(self, parameters):
        self.attribute = parameters

    # Method
    # การกระทำหรือวิธีการในการแก้ปัญหา

    def method_name1(self):
        # คืนค่าข้อมูลของวัตถุ
        return self.attribute

    def method_name2(self):
        # แสดงข้อความ
        print("นี่คือการทำงานของ Method ที่ 2")


# การสร้างวัตถุจาก Class
# เปรียบเสมือนการปั๊มภาพจากแม่แบบ

myObj = ClassName(10)


# การแสดงข้อมูลของวัตถุ
print(myObj.attribute)


# การเรียกใช้งาน Method ที่ 1
resultFromMethod = myObj.method_name1()

print(resultFromMethod)


# การเรียกใช้งาน Method ที่ 2
myObj.method_name2()


# สร้างวัตถุตัวที่ 2 จาก Class เดิม
myObj2 = ClassName(20)


# แสดงข้อมูลของวัตถุตัวที่ 2
print(myObj2.attribute)


# เรียกใช้งาน Method ของวัตถุตัวที่ 2
print(myObj2.method_name1())

myObj2.method_name2()