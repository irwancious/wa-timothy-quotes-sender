import pywhatkit

def sendWa(nomerhp, text, jam, menit, wait_time, tab_close, close_time):
    pywhatkit.sendwhatmsg(nomerhp, text, jam, menit, wait_time, tab_close, close_time)
    print("Mengirim pesan...")

sendWa("+6285755196900", "Halo testing", 22, 7, 15, True, 5)