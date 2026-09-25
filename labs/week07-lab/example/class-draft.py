"""

programming

2 types

1) structured program ==> c, python
2) object-oriented program (OOP การเขียนโปรแกรมเชิงวัตถุ) ==>java,c#,python

"""

"""
เราออกแบบโปรแกรมของเราใน class
เขียนโปรแกรมเพื่อแก้ปัญหา ต้องมีข้อมูล(data),การกระทำ(method)
"""
class ClassName: #แนวทางการแก้ปัญหาหนึ่งเรื่อง/ตรายาง/template/แม่พิมพ์

       # Constructor method
       #การกำหนดข้อมูลที่จำเป็นต้องใช้ในการแก้ปัญหานั้นๆ
    
    def __init__(self, parameters):
        self.attribute = parameters
    
    # method การกระทำ วิธีการในการแก้ปัญหา
    def method_name1(self):
        # Instance method
        return something

    def method_name2(self):
        # statement ของการการทำ

#การสร้างวัตถุจาก class ==> การนำแนวทางในการแก้ปัญหาที่ออกแบบไว้มาใช้
การปั้มภาพจากแม่แบบหรือจากตรายาง
myObj = ClassName(parameters)

#การ print ข้อมูลที่ใช้ของวัตถุจาก class
print(myObj.attribute)

#การใช้งาน method ในวัตถุของคลาส
resultFromMethod = myObj.method_name()
myObj.method_name2()

myObj.method_name(1)
print(myObj2.attribute)

print(myObj2.method_name1())
myObj2.method_name2()