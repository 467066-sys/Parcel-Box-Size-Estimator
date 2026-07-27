print("📦==========================================📦")
print("        🎉 Parcel Box Size Estimator 🎉")
print("         โปรแกรมคำนวณขนาดกล่องพัสดุ")
print("📦==========================================📦")

while True:
    print("\nกรุณากรอกขนาดของสินค้า")

    width = float(input("📏 ความกว้าง (ซม.) : "))
    length = float(input("📐 ความยาว (ซม.) : "))
    height = float(input("📦 ความสูง (ซม.) : "))

    # เผื่อพื้นที่กันกระแทก 2 ซม. รอบด้าน
    padding = 2
    box_width = width + (padding * 2)
    box_length = length + (padding * 2)
    box_height = height + (padding * 2)

    # คำนวณปริมาตร
    product_volume = width * length * height
    box_volume = box_width * box_length * box_height

    # จัดประเภทกล่อง
    largest_side = max(box_width, box_length, box_height)

    if largest_side <= 20:
        box_type = "🟢 S"
        shipping = 35
    elif largest_side <= 40:
        box_type = "🔵 M"
        shipping = 50
    elif largest_side <= 60:
        box_type = "🟠 L"
        shipping = 70
    else:
        box_type = "🔴 XL"
        shipping = 100

    # แนะนำวัสดุกันกระแทก
    if product_volume < 3000:
        packing = "📄 กระดาษกันกระแทก"
    elif product_volume < 10000:
        packing = "🫧 บับเบิลกันกระแทก"
    else:
        packing = "🧽 โฟม + บับเบิลกันกระแทก"

    # แสดงผล
    print("\n🎊========== ผลการคำนวณ ==========")
    print(f"📦 ขนาดสินค้า : {width:.1f} x {length:.1f} x {height:.1f} ซม.")
    print(f"📦 ขนาดกล่องที่แนะนำ : {box_width:.1f} x {box_length:.1f} x {box_height:.1f} ซม.")
    print(f"📊 ปริมาตรสินค้า : {product_volume:.2f} ลูกบาศก์เซนติเมตร")
    print(f"📦 ปริมาตรกล่อง : {box_volume:.2f} ลูกบาศก์เซนติเมตร")
    print(f"📮 ประเภทกล่อง : {box_type}")
    print(f"🎁 วัสดุกันกระแทก : {packing}")
    print(f"💰 ค่าจัดส่งโดยประมาณ : {shipping} บาท")
    print("======================================")

    again = input("\n🔄 ต้องการคำนวณอีกครั้งหรือไม่? (Y/N): ").strip().upper()

    if again != "Y":
        print("\n🙏 ขอบคุณที่ใช้โปรแกรม Parcel Box Size Estimator")
        print("👋 แล้วพบกันใหม่")
        break
