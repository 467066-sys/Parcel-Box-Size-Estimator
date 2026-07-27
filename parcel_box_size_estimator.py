print("======================================")
print(" Parcel Box Size Estimator")
print(" โปรแกรมคำนวณขนาดกล่องพัสดุ")
print("======================================")

# รับค่าจากผู้ใช้
width = float(input("กรอกความกว้างของสินค้า (ซม.): "))
length = float(input("กรอกความยาวของสินค้า (ซม.): "))
height = float(input("กรอกความสูงของสินค้า (ซม.): "))

# เผื่อกันกระแทก 2 ซม. รอบด้าน
box_width = width + 4
box_length = length + 4
box_height = height + 4

# คำนวณปริมาตร
product_volume = width * length * height
box_volume = box_width * box_length * box_height

# จัดประเภทกล่อง
largest_side = max(box_width, box_length, box_height)

if largest_side <= 20:
    box_type = "S"
elif largest_side <= 40:
    box_type = "M"
elif largest_side <= 60:
    box_type = "L"
else:
    box_type = "XL"

# แสดงผล
print("\n========== ผลการคำนวณ ==========")
print(f"ขนาดสินค้า : {width} x {length} x {height} ซม.")
print(f"ขนาดกล่องที่แนะนำ : {box_width} x {box_length} x {box_height} ซม.")
print(f"ปริมาตรสินค้า : {product_volume:.2f} ลูกบาศก์เซนติเมตร")
print(f"ปริมาตรกล่อง : {box_volume:.2f} ลูกบาศก์เซนติเมตร")
print(f"ประเภทกล่อง : {box_type}")

print("\nขอบคุณที่ใช้โปรแกรม Parcel Box Size Estimator")
