คำสั่ง activate venv
-- venv\Scripts\activate --

สำหรับติดตั้ง
# สร้าง venv และ activate
python -m venv venv
source venv/bin/activate  # สำหรับ Mac/Linux
# หรือ venv\Scripts\activate สำหรับ Windows

# ติดตั้ง Library ที่จำเป็น
pip install openai googletrans==4.0.0-rc1

แต่ๆๆ ใช้อันนี้ด้วย เพราะครั้งแรกรันแล้วพัง
pip install --upgrade openai
ใช้ด้านบนเพราะตอนแรกเก่าเกินไป

ด้านล่างคือ เวอร์ไม่ตรงติดตั้งไปเลย ทีละคำสั่ง
pip uninstall googletrans -y
pip install deep-translator