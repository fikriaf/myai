import pyaudio
import wave
import audioop
import speech_recognition as sr
import threading
import time
import signal
import sys

# Variabel global untuk mengontrol rekaman
recording = True

# Fungsi untuk merekam audio dan deteksi suara
def record_audio():
    while recording:
        print("[Mulai berbicara...]")
        p = pyaudio.PyAudio()
        sample_format = pyaudio.paInt16
        channels = 1
        sample_rate = 44100
        chunk = 1024
        record_seconds = 5
        output_filename = "audio.wav"
        stream = p.open(format=sample_format,
                        channels=channels,
                        rate=sample_rate,
                        frames_per_buffer=chunk,
                        input=True)

        frames = []
        while recording:
            data = stream.read(chunk)
            frames.append(data)
            rms = audioop.rms(data, 2)
            if rms > 1500:
                print("Deteksi suara...")
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

        try:
            recognizer = sr.Recognizer()
            with sr.AudioFile(output_filename) as source:
                audio = recognizer.record(source)
                text = recognizer.recognize_google(audio, language="id-ID")
                print("Hasil pengenalan suara: " + text)
        except sr.UnknownValueError:
            print("Tidak dapat mengenali teks")
        except sr.RequestError as e:
            print("Error pada request Google Speech Recognition: {0}".format(e))
        except Exception as e:
            print("Terjadi kesalahan: {0}".format(e))

# Fungsi untuk menghentikan rekaman
def stop_recording(signal, frame):
    global recording
    recording = False

def main():
    global recording
    recording = True

    # Mengatur sinyal SIGINT (Ctrl+C) untuk menghentikan rekaman secara paksa
    signal.signal(signal.SIGINT, stop_recording)

    # Mulai thread untuk merekam audio
    audio_thread = threading.Thread(target=record_audio)
    audio_thread.start()
    while recording:
        print("ini utama")
        time.sleep(3)
    # Setelah beberapa saat atau tugas selesai, hentikan rekaman
    stop_recording(None, None)  # Menghentikan rekaman secara manual
    audio_thread.join()  # Tunggu hingga thread rekaman selesai

if __name__ == "__main__":
    main()

