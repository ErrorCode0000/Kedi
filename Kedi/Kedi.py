import tkinter as tk
from PIL import Image, ImageTk
import random
import pygame
import time

class SonsuzKediSevgisi:
    def __init__(self, master):
        self.master = master
        master.title("Sonsuz Kedi Sevgisi")
        master.protocol("WM_DELETE_WINDOW", self.on_closing)  # Pencere kapatma butonunu engelle

        self.kedi_resimleri = [
            "kedi1.jpg",  # Bu dosya yollarını kendi kedi resimlerinizle değiştirin
            "kedi2.jpg",
            "kedi3.jpg"
        ]
        self.miyav_sesleri = [
            "kedi1.wav",  # Bu dosya yollarını kendi miyav seslerinizle değiştirin
            "kedi2.wav"
            # Daha fazla miyav sesi ekleyebilirsiniz
        ]

        pygame.mixer.init()

        self.kedi_etiketi = tk.Label(master)
        self.kedi_etiketi.pack()

        self.kapatma_sayaci = 0
        self.gizli_kapatma_sirasi = [0, 1, 0] # Örnek gizli tıklama sırası
        self.tiklama_sirasi = []

        self.kapat_butonu = tk.Button(master, text="Tamam, Yeterince Kedi Gördüm (Belki)", command=self.kapatma_denemesi)
        self.kapat_butonu.pack(pady=10)

        self.goster_rastgele_kedi()
        self.baslangic_miyav_cal()

    def goster_rastgele_kedi(self):
        try:
            rastgele_resim = random.choice(self.kedi_resimleri)
            kedi_img = Image.open(rastgele_resim)
            kedi_img = kedi_img.resize((300, 300), Image.Resampling.LANCZOS) # Boyutu ayarlayabilirsiniz
            self.kedi_photo = ImageTk.PhotoImage(kedi_img)
            self.kedi_etiketi.config(image=self.kedi_photo)
            self.kedi_etiketi.image = self.kedi_photo
            self.master.after(2000, self.goster_rastgele_kedi) # Her 2 saniyede bir yeni kedi
        except FileNotFoundError:
            self.kedi_etiketi.config(text="Kedi resimleri bulunamadı!")

    def baslangic_miyav_cal(self):
        try:
            rastgele_ses = random.choice(self.miyav_sesleri)
            pygame.mixer.music.load(rastgele_ses)
            pygame.mixer.music.play(-1) # Sonsuz döngüde çal
        except pygame.error:
            print("Ses dosyaları yüklenirken bir hata oluştu.")

    def kapatma_denemesi(self):
        self.kapatma_sayaci += 1
        print(f"Kapatma denemesi: {self.kapatma_sayaci}")
        self.ekran_kaosu()

    def ekran_kaosu(self):
        for _ in range(10): # Birkaç tane rastgele kedi resmi daha aç
            rastgele_resim = random.choice(self.kedi_resimleri)
            try:
                kedi_img = Image.open(rastgele_resim)
                boyut = random.randint(50, 200)
                kedi_img = kedi_img.resize((boyut, boyut), Image.Resampling.LANCZOS)
                kedi_photo = ImageTk.PhotoImage(kedi_img)
                rastgele_etiket = tk.Label(self.master, image=kedi_photo)
                rastgele_etiket.image = kedi_photo
                x = random.randint(0, self.master.winfo_width() - boyut)
                y = random.randint(0, self.master.winfo_height() - boyut)
                rastgele_etiket.place(x=x, y=y)
            except FileNotFoundError:
                pass

        for _ in range(3): # Birkaç tane miyav sesi daha çal
            try:
                rastgele_ses = random.choice(self.miyav_sesleri)
                pygame.mixer.Sound(rastgele_ses).play()
            except pygame.error:
                pass

        # Sahte bir "kapanıyor" mesajı (aslında kapanmıyor)
        sahte_kapanma_etiketi = tk.Label(self.master, text="Kapanıyor...", font=("Arial", 16))
        sahte_kapanma_etiketi.pack(pady=10)
        self.master.after(2000, sahte_kapanma_etiketi.destroy) # 2 saniye sonra kaldır

    def on_closing(self):
        # Pencere kapatma butonuna basıldığında yapılacaklar (hiçbir şey yapma)
        tk.messagebox.showinfo("Hayır!", "Bu kedilerden kaçamazsın! (Şimdilik)")

if __name__ == "__main__":
    root = tk.Tk()
    app = SonsuzKediSevgisi(root)
    root.mainloop()