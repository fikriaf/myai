print("Loading data...", end="\r")
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 140)
engine.say("Analyzing Databases")
engine.runAndWait()

import threading
import signal
import cv2
import math
import time, os, random, re, sys
import datetime
import pyaudio
import wave
import audioop
from pyAudioAnalysis import audioBasicIO
from pyAudioAnalysis import audioSegmentation
import speech_recognition as sr
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
from playsound import playsound
from deepface import DeepFace
import shutil
import webbrowser
import pyautogui
import clipboard, keyboard
from pytube import YouTube
from googletrans import Translator
from Plagiarisme import CekPlag
import subprocess
import pyperclip

username_collabor = ""
pass_collabor = ""

def klik(x, y):
    pyautogui.click(x, y)
def scroll(ab):
    pyautogui.moveTo(650, 400)
    time.sleep(1)
    if "atas" in ab:
        pyautogui.scroll(600)
    if "bawah" in ab:
        pyautogui.scroll(-600)

def keluar_app():
    klik(1340, 20)

def minimize_app():
    klik(1250, 10)

def open(path):
    subprocess.Popen(path, shell=True)

def sound(path2sound):
    #play(AudioSegment.from_file(path2sound, format="mp3"))
    playsound(path2sound)

def efek(x):
    if x == "search":
        sound(r"C:\Users\User\Documents\script\PYTHON\myai\effect\search.mp3")

def copy(x, y):
    source_file = rf"C:\Users\User\Documents\script\PYTHON\myai\source\{y}"
    destination_folder = r"C:\Users\User\Documents\script\PYTHON\myai\source\saved"
    shutil.copy2(source_file, os.path.join(destination_folder, f"{x}.jpg"))

def find_max():
    file_names = os.listdir(r"C:\Users\User\Documents\script\PYTHON\myai\source")
    try:
        if file_names:
            file_names_with_number = [name for name in file_names if name.startswith("foto") and name.endswith(".jpg")]
            file_names_with_number.sort(key=lambda x: int(''.join(filter(str.isdigit, x))), reverse=True)
            max_number = ''.join(filter(str.isdigit, file_names_with_number[0]))
            return max_number
        else:
            return False
    except Exception as e:
        return False

def find_terdekat(target, file_names):
    terdekat = min(file_names, key=lambda x: abs(int(x.strip("foto").strip(".jpg")) - target))
    return terdekat

def suara(x):
    tts = gTTS(x, lang='id', slow=False)
    tts.save('output.mp3')
    print(f"[{tgltime('waktu')}] Respon : {x}")
    sound(r"C:\Users\User\Documents\script\PYTHON\myai\output.mp3")

def web(link, q=None):
    if q is not None:
        webbrowser.open_new_tab(link)
        time.sleep(9)
        pyautogui.typewrite("'")
        pyautogui.typewrite(q)
        time.sleep(3)
        pyautogui.press("enter")
    else:
        webbrowser.open_new_tab(link)
        
def read_this():
    keyboard.press_and_release('ctrl+c')
    time.sleep(0.1)
    clipboard_history = clipboard.paste()
    return clipboard_history

def musik():
    folder = r"C:\Users\User\Music\all"
    files = os.listdir(folder)
    mp3_files = [file for file in files if re.search(r"\.mp3$", file)]
    
    if mp3_files:
        random_music = random.choice(mp3_files)
        music_path = os.path.join(folder, random_music)
        os.startfile(music_path)
    else:
        print("Tidak ada file musik dalam direktori.")

def respon(x):
    now = datetime.datetime.now()
    if now.hour > 0 and now.hour < 11:
        waktu = "selamat pagi"
        waktu_en = "morning"
    elif now.hour >= 11 and now.hour < 14:
        waktu = "selamat siang"
        waktu_en = "afternoon"
    elif now.hour >= 14 and now.hour < 18:
        waktu = "selamat sore"
        waktu_en = "evening"
    elif now.hour >= 18 and now.hour < 24:
        waktu = "selamat malam"
        waktu_en = "night"

    rand_resp = random.choice(["Ada yang bisa saya bantu?", "apa yang mau dibantu?", "Ada perlu apakah?", "apa yang bisa dibantu",
    "saya, elektra,  ada yang bisa saya bantu?", "saya eletra, Ada yang bisa saya bantu?", "saya elektra, apa yang mau dibantu?",
    "saya elektra, Ada perlu apakah?", "saya elektra, apa yang bisa dibantu", "Saya ada di sini untuk membantu", "Saya elektra, ada di sini untuk membantu"])
    if x == "sapa":
        rand=random.randint(1,2)
        if rand == 1:
            return random.choice([f"Hi, {waktu} {rand_resp}", f"Halo, {waktu} {rand_resp}"])
        elif rand == 2:
            return random.choice([f"Hi, {rand_resp}", f"Halo, {rand_resp}"])
    elif x == "waktu_en":
        return waktu_en
    elif x == "detek":
        return random.choice(["halo yang disana, siapa namamu?", "saya melihat seseorang disana", "saya elektra, siapa disana?", "Halo, elektra di sini, Ada yang perlu saya bantu?", "Halo, elektra di sini, siapa disana?", "Hi, kamu, Ada yang perlu saya bantu?"])
    elif x == "kabar":
        return random.choice(["bagaimana kabarmu", "apakah sehat?", "bagaimana kabarmu? apakah sehat"])
    elif x == "tanya":
        return random.choice(["siapa namamu?", "siapa nama kamu", "nama kamu siapa?", "Hi, siapa namamu?", "halo, nama kamu siapa?", "Hi, siapa nama kamu?"])
    elif x == "awal":
        return random.choice([f"halo, {waktu} saya elektra,", f"Hi, {waktu},", f"halo, {waktu},", f"Hi, {waktu}, namaku elektra,", f"Hi, {waktu}, saya elektra,"])
    elif x == "selesai":
        return random.choice(["ini dia", "berikut perintah anda", "selesai", "ini, semoga sesuai"])
    elif x == "introduce":
        return random.choice(["saya elektra", "nama saya elektra", "saya elektra, salam kenal", "namaku elektra", "namaku elektra, salam kenal"])
    elif x == "jawab":
        return random.choice(["hola", "disini", "ok", "ya", "yo"])
    elif x == "gagal":
        return random.choice(["maaf, tampaknya ada sedikit gangguan", "gagal memproses, silakan coba lagi", "maaf gagal, silakan cek koneksi internet atau cek perintah anda", "ada yang salah, silakan cek kembali", "tampaknya ada sedikit masalah"])
    elif x == "ulang":
        return random.choice(["bisa ulangi perintah itu?", "maaf, bisa diulang?", "maaf, ulang perintah anda", "maaf, perintah anda kurang jelas, bisa diulang?", "maaf, perintah anda kurang jelas", "tolong diulang perintahnya"])
    elif x == "thanks":
        return random.choice(["thanks", "trima kasih", "makasih", "terima kasih"])
    elif x == "setuju":
        return random.choice(["OK", "baik, silakan ditunggu!", "permintaan diterima, silakan tunggu", "sedang memproses", "baiklah", "oke, tunggu sebentar"])

def tgltime(x):
    now = datetime.datetime.now()
    if x == "lengkap":
        return now.strftime("%d-%m-%y %H:%M:%S")
    elif x == "tanggal":
        return now.date()
    elif x == "waktu":
        return now.strftime("%H:%M:%S")
    elif x == "jam":
        return now.hour
    elif x == "menit":
        return now.minute
    elif "id":
        return now.strftime("%M%S")


def compare_wajah(dalam=None, luar=None):
    try:
        image1 = fr"C:\Users\User\Documents\script\PYTHON\myai\source\saved\{dalam}"
        image2 = fr"C:\Users\User\Documents\script\PYTHON\myai\source\{luar}"
        result = DeepFace.verify(img1_path = image1, img2_path = image2)
        if result["distance"] < 0.31:
            return True
        else:
            return False
    except:
        return False
def save_identitas():
    suara("data wajah kamu belum tersimpan. apakah ingin menyimpan?")
    while True:
        confirm = mikrofon()
        if confirm:
            print(f"Anda : {confirm}")
            if "ya" in confirm or "yes" in confirm or "iya" in confirm or "iyo" in confirm or "yo" in confirm:
                suara("tolong ketik namamu")
                cek_kondisi = True
                while cek_kondisi:
                    confirm_name = input("Nama : ")
                    if confirm_name:
                        suara(f"sedang memproses, silakan ditunggu ya {confirm_name}")
                        while True:
                            find_jpg_luar = f"foto{find_max()}.jpg"
                            copy(confirm_name, find_jpg_luar)
                            suara("data identitas telah berhasil ditambahkan")
                            namanya = confirm_name
                            suara(f"{respon('sapa')} {confirm_name}")
                            break
                        cek_kondisi = False
                    else:
                        suara("gak punya nama kah?")
                if cek_kondisi == False:
                    break
def identitas():
    while True:
        foto_files = os.listdir(r"C:\Users\User\Documents\script\PYTHON\myai\source\saved")
        if foto_files is None:
            save_identitas()
        cocok = f"foto{find_max()}.jpg"
        print(f"File terbaru adalah {cocok}")
        for foto in foto_files:
            hasil = compare_wajah(dalam=foto, luar=cocok)
            if hasil == True:
                kondisi = foto.replace(".jpg", "")
                print("[Compare face is True]")
                
            else:
                print("[Compare face is False]")
                kondisi = False

        return kondisi
        break

def detect(not_save=None, sebut_nama=None):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    video_capture = cv2.VideoCapture(0)
    cv2.setUseOptimized(True)
    cv2.setNumThreads(0)
    video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    jarak_max = 200
    while True:
        ret, frame = video_capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(100, 100))
        if len(faces) > 0:
            x, y, w, h = faces[0]
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            
            frame_center_x = frame.shape[1] // 2
            frame_center_y = frame.shape[0] // 2
            face_center_x = x + (w // 2)
            face_center_y = y + (h // 2)
            jarak = math.sqrt((frame_center_x - face_center_x)**2 + (frame_center_y - face_center_y)**2)
            print(jarak)
            if jarak <= jarak_max:
                if not_save is None:
                    get_max = find_max()
                    if get_max:
                        id_foto = int(get_max) + 1
                        file_foto = os.path.join(r"C:\Users\User\Documents\script\PYTHON\myai\source", f"foto{str(id_foto)}.jpg")
                        cv2.imwrite(file_foto, frame)
                        suara("Berhasil terdeteksi")
                        print(f"[Success taking a foto < foto{str(id_foto)}.jpg >]")
                        if sebut_nama is not None:
                            get_nama_cuy = identitas()
                            if get_nama_cuy:
                                suara(f"{respon('awal')} {get_nama_cuy}")
                                break
                            else:
                                suara(f"{respon('awal')}")
                                break
                        break
                    else:
                        file_foto = os.path.join(r"C:\Users\User\Documents\script\PYTHON\myai\source", "foto1.jpg")
                        cv2.imwrite(file_foto, frame)
                        print("[Success taking a foto < foto1.jpg >]")
                        break
                elif not_save == True:
                    get_max = find_max()
                    if get_max:
                        id_foto = int(get_max) + 1
                        file_foto = os.path.join(r"C:\Users\User\Documents\script\PYTHON\myai\source", f"foto{str(id_foto)}.jpg")
                        cv2.imwrite(file_foto, frame)
                        get_nama_cuy = identitas()
                        if get_nama_cuy:
                            os.remove(file_foto)
                            print("[Mengenali]")
                            break
                        else:
                            print(f"[Success taking a foto < foto{str(id_foto)}.jpg >]")
                            suara(respon("detek"))
                            break
                        
                    else:
                        file_foto = os.path.join(r"C:\Users\User\Documents\script\PYTHON\myai\source", "foto1.jpg")
                        cv2.imwrite(file_foto, frame)
                        print("[Success taking a foto < foto1.jpg >]")
                        break
                    break

    video_capture.release()
    cv2.destroyAllWindows()

def mikrofon():
    print("[Mulai berbicara...]")
    p = pyaudio.PyAudio()
    sample_format = pyaudio.paInt16
    channels = 1
    sample_rate = 44100
    chunk = 1024  #
    record_seconds = 5
    output_filename = "audio.wav"
    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=sample_rate,
                    frames_per_buffer=chunk,
                    input=True)

    frames = []
    while True:
        data = stream.read(chunk)
        frames.append(data)
        rms = audioop.rms(data, 2)
        if rms > 1700:
            efek("search")
            break
        if len(frames) >= int(sample_rate / chunk * record_seconds):
            break
    stream.stop_stream()
    stream.close()
    p.terminate()
    with wave.open(output_filename, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(p.get_sample_size(sample_format))
        wf.setframerate(sample_rate)
        wf.writeframes(b''.join(frames))
        
    recognizer = sr.Recognizer()
    with sr.AudioFile("audio.wav") as source:
        audio = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio, language="id-ID")
        #speech=sr.Recognizer()
        #with sr.Microphone() as source:
        #    print("[Mulai berbicara...]")
        #    audio = speech.listen(source, timeout=50)
        #text = speech.recognize_google(audio, language="id-ID")
        return text

    except Exception:
        return None
    except KeyboardInterrupt:
        exit("[Program Exit]")

def ketik():
    efek("search")
    while True:
        get_mic_ketik = mikrofon()
        if get_mic_ketik is not None:
            char_mic = get_mic_ketik.lower()
            pyautogui.typewrite(char_mic)
            print(f"[Typing '{char_mic}']")
            break

def colabor():
    open(r'"C:\Program Files\Google\Chrome\Application\chrome.exe" --profile-directory="default"')
    time.sleep(2)
    pyautogui.hotkey('alt', 'space')
    time.sleep(0.5)
    pyautogui.press('x')
    pyautogui.hotkey('ctrl', 't')
    klik(300, 50)
    pyperclip.copy("https://collabor.upj.ac.id/login/index.php")
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press('enter')
    time.sleep(3)
    klik(300, 390)
    pyautogui.typewrite(username_collabor)
    time.sleep(1)
    klik(300, 450)
    pyperclip.copy(pass_collabor)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(3)
    pyautogui.press('enter')

def myupj():
    open(r'"C:\Program Files\Google\Chrome\Application\chrome.exe" --profile-directory="Profile 7"')
    time.sleep(2)
    pyautogui.hotkey('alt', 'space')
    time.sleep(0.5)
    pyautogui.press('x')
    pyautogui.hotkey('ctrl', 't')
    klik(300, 50)
    pyperclip.copy("https://my.upj.ac.id/gate/login")
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press('enter')
    time.sleep(3)
    klik(1000, 370)
    time.sleep(2)
    klik(370, 460)
    klik(1000, 450)

def spotify():
    os.system(r"start C:\Users\User\AppData\Roaming\Spotify\Spotify.exe")
    while True:
        perintah = mikrofon()
        if perintah is not None:
            char_mic = perintah.lower()
            if "keluar" in char_mic:
                keluar_app()
            elif "minimize" in char_mic:
                minimize_app()
            elif "ulang" in char_mic :
                klik(820, 670)
            elif "stop" in char_mic:
                pyautogui.press("space")
            elif "lirik" in char_mic:
                klik(1140, 680)
            elif "cari lagu" in char_mic or "lagu" in char_mic:
                efek("search")
                queries = ["cari lagu", "lagu"]
                result = None
                for query in queries:
                    if query in char_mic:
                        split_text = char_mic.split(query)
                        if len(split_text) > 1:
                            result = split_text[1]
                            break
                if result is not None and len(result) > 0:
                    print(result)
                    klik(40, 120)
                    time.sleep(1)
                    klik(530, 70)
                    pyautogui.typewrite(result)
                    time.sleep(4)
                    klik(450, 390)
                    klik(450, 390)
                else:
                    print(result)
                    klik(40, 120)
                    time.sleep(1)
                    klik(530, 70)
                    ketik()
                    time.sleep(4)
                    klik(450, 390)
                    klik(450, 390)

def plagiarisme():
    suara("memulai scanning teks")
    x = read_this()
    cekplag = CekPlag(x)
    suara(f"Keunikan {float(cekplag['percent']):.0f} persen, plagiarisme {100 - float(cekplag['percent']):.0f} persen")

def dlyt():
    suara("Ok, memulai download")
    x = read_this()
    yt = YouTube(x)
    video_stream = yt.streams.filter(res="360p").first()
    download_path = r"C:\Users\User\Downloads"
    video_stream.download(output_path=download_path)
    suara("Download selesai")

def yt(x):
    queries = ["buka youtube", "open youtube", "cari di youtube", "cari diyoutube"]
    result = None
    for query in queries:
        if query in x:
            split_text = x.split(query)
            if len(split_text) > 1:
                result = split_text[1]
                break

    if result is not None and len(result) > 0:
        print(result)
        efek("search")
        webbrowser.open_new_tab(f"https://www.youtube.com/results?search_query={result.replace(' ', '+')}")
        suara(respon("selesai"))
        
    else:
        suara("Ingin mencari apa?")
        efek("search")
        while True:
            search = mikrofon()
            if search:
                print(f"Query : {search}")
                webbrowser.open_new_tab(f"https://www.youtube.com/results?search_query={search.replace(' ', '+')}")
                suara(respon("selesai"))
                break

def translate():
    x = read_this()
    translator = Translator()
    bahasa_asal = translator.detect(x).lang
    terjemahan = translator.translate(x, src=bahasa_asal, dest="id").text
    suara(terjemahan)

def google(x):
    queries = ["buka google", "open google", "cari di google", "cari digoogle"]
    result = None
    for query in queries:
        if query in x:
            split_text = x.split(query)
            if len(split_text) > 1:
                result = split_text[1]
                break

    if result is not None and len(result) > 0:
        print(result)
        efek("search")
        web("google.com", result)
        suara(respon("selesai"))
        
    else:
        suara("Ingin mencari apa?")
        efek("search")
        while True:
            search = mikrofon()
            if search:
                print(f"Query : {search}")
                web("google.com", search)
                suara(respon("selesai"))
                break

def tanya_nama():
    intro = respon("introduce")
    if random.randint(1,2) == 2:
        try:
            suara(f"{intro}")
            get_nama = identitas()
            suara(f"{respon('kabar')} {get_nama}")
        except Exception as e:
            print(e)
            suara(intro)
    else:
        suara(intro)

def kenal_saya():
    ulang = False
    while True:
        #-----------------------------------------------------------------#
        cek_save = os.listdir(r"C:\Users\User\Documents\script\PYTHON\myai\source\saved")
        if cek_save:
            print("[ada data di directory saved]")
        else:
            save_identitas()
            break
        #-----------------------------------------------------------------#
        suara("Analisis data wajah")
        get_nama = identitas()
        if get_nama:
            suara(f"analisis selesai. {respon('awal')} {get_nama}")
            break
        #-----------------------------------------------------------------#
        while True:
            suara("posisikan wajah didepan kamera dan dengan pencahayaan yang terang")
            detect()
            get_nama_ulang = identitas()
            if get_nama_ulang:
                suara(f"analisis selesai. {respon('awal')} {get_nama_ulang}")
                break
            elif get_nama_ulang == False:
                save_identitas()
                continue
            else:
                print("[IndexError: tidak ada yang cocok]")
            break
        #-----------------------------------------------------------------#
        break


def main():
    loop = 0
    while True:
        try:
            micnotlower = mikrofon()
            if loop > 100:
                detect(not_save=True)
                max_id = find_max()
                #os.system(rf"start C:\Users\User\Documents\script\PYTHON\myai\source\foto{max_id}.jpg")            
                loop = 0

            if micnotlower is not None:
                loop = 0
                mic = micnotlower.lower()
                print(f"Anda : {mic}")

                if mic == "elektra" or mic == "electron" or mic == "elektro" or mic == "electra" or mic == "elektron":
                    suara(respon("jawab"))    
                elif "siapa nama saya" in mic or "siapa namaku" in mic or "kamu tahu namaku" in mic or "kamu kenal saya" in mic or "kamu mengenal saya" in mic or "kamu tahu nama saya" in mic or "siapa saya" in mic:
                    kenal_saya()
                elif "scroll ke atas" in mic or "scroll atas" in mic or "ke atas lagi" in mic or "atas lagi" in mic:
                    scroll("atas")
                    time.sleep(1)
                elif "scroll ke bawah" in mic or "scroll bawah" in mic or "ke bawah lagi" in mic or "bawah lagi" in mic:
                    scroll("bawah")
                    time.sleep(1)
                elif "klik" in mic or "pilih" in mic:
                    if "video" in mic:
                        if "1" in mic:
                            klik(450, 340)
                            time.sleep(1)
                        elif "2" in mic:
                            klik(450, 550)
                            time.sleep(1)
                        elif "3" in mic:
                            klik(450, 710)
                            time.sleep(1)
                        else:
                            pass
                    else:
                        if "1" in mic:
                            klik(300, 200)
                            time.sleep(1)
                        elif "2" in mic:
                            klik(300, 400)
                            time.sleep(1)
                        elif "3" in mic:
                            klik(300, 650)
                            time.sleep(1)
                        else:
                            pass
                elif "siapa nama kamu" in mic or "siapa namamu" in mic or "kamu siapa" in mic or "namamu siapa" in mic or "siapa kamu" in mic:
                    tanya_nama()
                elif "jam berapa" in mic or "sekarang jam" in mic:
                    suara(f"Jam {tgltime('jam')} lebih {tgltime('menit')} menit")
                elif "simpan saya" in mic or "save saya" in mic or "simpan nama saya" in mic or "save nama saya" in mic or "simpan identitas saya" in mic or "save identitas" in mic:
                    save_identitas()
                elif "keluar" in mic or "tutup" in mic:
                    keluar_app()
                elif "exit" in mic:
                    exit()
                elif "buka youtube" in mic or "open youtube" in mic or "cari di youtube" in mic or "cari diyoutube" in mic:
                    yt(mic)
                elif "buka google" in mic or "cari digoogle" in mic or "cari di google" in mic or "cari digoogle" in mic:
                    google(mic)
                elif "music" in mic or "musik" in mic:
                    musik()
                elif "baca ini" in mic or "baca" in mic:
                    suara(read_this())
                elif "download ini" in mic or "download video ini" in mic or "download link ini" in mic:
                    dlyt()
                elif "ini artinya apa" in mic or "artinya apa" in mic or "translate ini" in mic or "translatekan ini" in mic or "artikan" in mic or "terjemahkan ini" in mic:
                    translate()
                elif "cek plagiarisme" in mic or "cek plagiat" in mic or "cek plagiarisme teks ini" in mic or "cek plagiat teks ini" in mic:
                    plagiarisme()
                elif "ketik" in mic:
                    ketik()
                elif "spotify" in mic:
                    spotify()
                elif "upj" in mic or "ufc" in mic or "pubg" in mic:
                    myupj()
                elif "colabor" in mic or "collabor" in mic  or "kolabor" in mic or "kollabor" in mic or "kolabo" in mic:
                    colabor()
            else:
                loop+=1
        except Exception as e:
            loop += 1
            print("error di main")
            print(e)

recording = True

def stop_recording(signal, frame):
    global recording
    recording = False

def thread():
    global recording
    recording = True
    signal.signal(signal.SIGINT, stop_recording)
    audio_thread = threading.Thread(target=main)
    audio_thread.start()
    stop_recording(None, None)
    audio_thread.join()

def banner():
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    BG_BLACK = "\033[40m"
    BG_RED = "\033[41m"
    BG_GREEN = "\033[42m"
    BG_YELLOW = "\033[43m"
    BG_BLUE = "\033[44m"
    BG_MAGENTA = "\033[45m"
    BG_CYAN = "\033[46m"
    BG_WHITE = "\033[47m"

    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    RESET = "\033[0m"
    print(r"""
────────────────────────────────────────────────────────────────────────────────────────────────────────────────
─██████████████─██████─────────██████████████─██████──████████─██████████████─████████████████───██████████████─
─██░░░░░░░░░░██─██░░██─────────██░░░░░░░░░░██─██░░██──██░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░░░██───██░░░░░░░░░░██─
─██░░██████████─██░░██─────────██░░██████████─██░░██──██░░████─██████░░██████─██░░████████░░██───██░░██████░░██─
─██░░██─────────██░░██─────────██░░██─────────██░░██──░░████───────██░░██─────██░░██────██░░██───██░░██──██░░██─
─██░░██████████─██░░██─────────██░░██████████─██░░██░░██████───────██░░██─────██░░████████░░██───██░░██████░░██─
─██░░░░░░░░░░██─██░░██─────────██░░░░░░░░░░██─██░░░░░░░░░░██───────██░░██─────██░░░░░░░░░░░░██───██░░░░░░░░░░██─
─██░░██████████─██░░██─────────██░░██████████─██░░██████░░██───────██░░██─────██░░██████░░████───██░░██████░░██─
─██░░██─────────██░░██─────────██░░██─────────██░░██──██░░██───────██░░██─────██░░██──██░░██─────██░░██──██░░██─
─██░░██████████─██░░██████████─██░░██████████─██░░██──██░░████─────██░░██─────██░░██──██░░██████─██░░██──██░░██─
─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░██──██░░░░██─────██░░██─────██░░██──██░░░░░░██─██░░██──██░░██─
─██████████████─██████████████─██████████████─██████──████████─────██████─────██████──██████████─██████──██████─
────────────────────────────────────────────────────────────────────────────────────────────────────────────────""")
    print(r"""__________________        _____      _____           ______  
___  __/__(_)__  /___________(_)     __  /______________  /_ 
__  /_ __  /__  //_/_  ___/_  /_______  __/  _ \  ___/_  __ \
_  __/ _  / _  ,<  _  /   _  /_/_____/ /_ /  __/ /__ _  / / /
/_/    /_/  /_/|_| /_/    /_/        \__/ \___/\___/ /_/ /_/ 
                                                             
{RESET}""")

if __name__=="__main__":
    try:
        print("[MEMPERSIAPKAN KAMERA]")
        banner()
        detect(sebut_nama=True)
        engine.say("Loading Completed")
        engine.say(f"Im Electra, {respon('waktu_en')} sir")
        engine.runAndWait()
        thread()
    except KeyboardInterrupt:
        exit("[Program Exit]")
