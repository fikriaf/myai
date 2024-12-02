import pyautogui
import time
import threading
import speech_recognition as sr

scrolling = True  # Variabel untuk mengontrol scroll

def klik(x, y):
    pyautogui.click(x, y)

def scroll(ab):
    global scrolling
    pyautogui.moveTo(650, 400)
    time.sleep(1)
    if "atas" in ab:
        while scrolling:
            pyautogui.scroll(600)
            time.sleep(1)
    elif "bawah" in ab:
        while scrolling:
            pyautogui.scroll(-600)
            time.sleep(1)

# Fungsi untuk menghentikan scroll
def hentikan_scroll():
    global scrolling
    scrolling = False

# Fungsi untuk mengenali perintah suara
def recognition_thread():
    r = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            print("Katakan sesuatu...")
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio, language="id-ID")
                print("Anda mengatakan:", text)
                if "berhenti" in text:  # Jika ditemukan perintah "berhenti", hentikan scroll
                    hentikan_scroll()
            except sr.UnknownValueError:
                print("Tidak dapat mengenali suara")
            except sr.RequestError as e:
                print("Error saat menghubungi layanan pengenalan suara:", str(e))

if __name__ == "__main__":
    scroll_thread = threading.Thread(target=scroll, args=("atas",))
    recognition_thread = threading.Thread(target=recognition_thread)

    scroll_thread.start()
    recognition_thread.start()

    scroll_thread.join() 
    recognition_thread.join() 