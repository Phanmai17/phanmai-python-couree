"""
Assignment 2.2: โปรแกรมช่วยตัดสินใจเลือกซื้อสินค้าภายใต้งบประมาณรวม (buy-notbuy.py)

ให้รับราคาสินค้าจำนวน 6 รายการเก็บไว้ในตัวแปรชนิด list และรับงบประมาณ "รวม" จากผู้ใช้ 1 ค่า จากนั้นให้พิจารณาสินค้าตามลำดับใน list ว่าสามารถซื้อได้หรือไม่ โดยถ้าการซื้อสินค้าชิ้นนั้นแล้วทำให้ยอดใช้จ่ายรวมไม่เกินงบประมาณ ให้ถือว่า “buy” และนำราคาสินค้านั้นไปรวมกับยอดใช้จ่าย แต่ถ้าทำให้ยอดรวมเกินงบประมาณ ให้ถือว่า “cannot buy”

ทั้งนี้ให้โปรแกรมขอให้ “พิจารณาตามลำดับใน list” และ “ใช้ยอดสะสมรวมในการตัดสิน” ไม่ใช่ "งบต่อชิ้น" แต่เป็นงบทั้งก้อนที่ลดลงเรื่อย ๆ ตามรายการที่ซื้อ

กระบวนการทำงาน 
รับราคาสินค้า 6 ค่าและเก็บใน list
รับงบประมาณรวม 1 ค่า
ใช้ loop และ if-else ตรวจสอบราคาสินค้าทีละรายการตามลำดับ
ใช้ตัวแปรสำหรับเก็บยอดใช้จ่ายสะสม
ถ้ายอดใช้จ่ายสะสมบวกกับราคาสินค้าชิ้นปัจจุบันแล้วไม่เกินงบประมาณ ให้แสดงข้อความว่า “buy”
ถ้าเกินงบประมาณ ให้แสดงว่า “cannot buy”
เก็บรายการสินค้าที่ซื้อได้ไว้ใน list ใหม่
แสดงรายการสินค้าที่ซื้อได้ ยอดใช้จ่ายรวม และงบประมาณคงเหลือ
"""
prices = []

# Input prices of 6 items
print("Enter prices of 6 items:")

for i in range(6):
    price = int(input(f"Item {i + 1}: "))
    prices.append(price)

# Input total budget
budget = int(input("\nEnter total budget: "))

# Initialize variables
total = 0
bought_items = []

print()

# Check each item in order
for i in range(6):
    price = prices[i]

    if total + price <= budget:
        print(f"Item {i + 1} = {price} -> buy")

        total += price
        bought_items.append(price)
    else:
        print(f"Item {i + 1} = {price} -> cannot buy")

    print(f"Current total = {total}\n")

# Display summary
print(f"Bought items: {bought_items}")
print(f"Total spent: {total}")
print(f"Remaining budget: {budget - total}")