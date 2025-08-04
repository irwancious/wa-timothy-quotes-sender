import os
import pywhatkit
from datetime import datetime, timedelta
from dotenv import load_dotenv
from google import genai

# config
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY tidak ditemukan di file .env")

# Konfigurasi Gemini API
client = genai.Client(api_key=GEMINI_API_KEY)

NOMOR_TUJUAN = "+6285755196900"

def getQuote():
    try:  
        prompt = (
            "Buatkan satu quote kritik pedas dan kasar dengan gaya bahasa Timothy Ronald. "
            "Fokus pada mentalitas, kerja keras, dan kritik terhadap orang yang malas atau banyak mengeluh. "
            "Jangan berikan salam pembuka atau penutup, langsung saja quotenya."
        )
        
        response = client.models.generate_content(
            model="gemini-2.5-flash", contents=prompt
            )
        return response.text
    
    except Exception as e:
        print(f"Gagal mengambil quote dari Gemini API: {e}")
        return "Gagal mendapatkan quote. Coba lagi nanti!"
    
def sendWa(nomor, pesan):
    try:
        sekarang = datetime.now() + timedelta(minutes=2)
        jam = sekarang.hour
        menit = sekarang.minute
        
        pywhatkit.sendwhatmsg(nomor, pesan, jam, menit, wait_time=20, tab_close=True, close_time=25)
        print(f"Pesan telah dikirim ke {nomor} pada pukul {jam}:{menit}")
    except Exception as e:
        print(f"Gagal mengirim pesan: {e}")

print(">>>>> Program Send Quotes Timothy Ronald by @irwancodes <<<<<")
quote_to_send = getQuote()
print(f"Quote yang akan dikirim: '{quote_to_send}'")

if "Gagal" not in quote_to_send:
    sendWa(NOMOR_TUJUAN, quote_to_send)
else:
    print("Pengiriman pesan dibatalkan karena gagal mengambil quotes.")