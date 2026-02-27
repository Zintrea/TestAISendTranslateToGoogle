import openai
from deep_translator import GoogleTranslator

# ตั้งค่า Client สำหรับเชื่อมต่อกับ LM Studio
client = openai.OpenAI(base_url="http://172.16.0.2:1234/v1", api_key="lm-studio")

def chat_with_ai():
    print("AI Bridge พร้อมใช้งานแล้ว (พิมพ์ 'exit' เพื่อเลิก)")
    
    while True:
        user_input = input("คุณ: ")
        if user_input.lower() == 'exit':
            break

        # 1. แปล ไทย -> อังกฤษ ด้วย deep-translator
        translated_input = GoogleTranslator(source='th', target='en').translate(user_input)
        
        # 2. ส่งคำถามภาษาอังกฤษให้ LM Studio
        try:
            response = client.chat.completions.create(
                model="local-model", # หรือใส่ชื่อ model ที่โหลดใน LM Studio
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": translated_input}
                ],
                temperature=0.7,
            )
            english_reply = response.choices[0].message.content
        except Exception as e:
            print(f"เกิดข้อผิดพลาดในการเชื่อมต่อ LM Studio: {e}")
            continue

        # 3. แปล อังกฤษ -> ไทย ด้วย deep-translator
        final_reply = GoogleTranslator(source='en', target='th').translate(english_reply)
        
        # print(f"\nAI (English): {english_reply}")
        print(f"AI : {final_reply}\n")

if __name__ == "__main__":
    chat_with_ai()