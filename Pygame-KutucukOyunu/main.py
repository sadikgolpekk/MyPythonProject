import pygame
import sys
import random

 ## @author Sadık GÖLPEK
# Pygame başlatma
pygame.init()

# Oyun penceresi boyutları
ekran_genislik = 800 
ekran_yukseklik = 600
ekran =pygame.display.set_mode((ekran_genislik, ekran_yukseklik)) #boyut
pygame.display.set_caption("Kutucuk Oyunu")

# Kutucuğun başlangıç pozisyonu ve boyutu

kutucuk_genislik=50
kutucuk_yukseklik=50
kutucuk_renk=(0,0,255) # Mavi renk
kutucuk=pygame.Rect(ekran_genislik //2 - kutucuk_genislik //2,500,kutucuk_genislik,kutucuk_yukseklik)


# Yiyecek nesnesinin başlangıç pozisyonu ve boyutu
yiyecek_genislik=20
yiyecek_yukseklik=20
yiyecek_renk=(255,0,0) # kırmızı renk
yiyecek=pygame.Rect(random.randint(0,ekran_genislik-yiyecek_genislik),0,yiyecek_genislik,yiyecek_yukseklik)
yiyecek_hiz=3

# Puanlama ve can hakkı sistemi
puan=0 # başlangıç puanı 0
can=3 # başlangıç canı 3
font=pygame.font.Font(None,36) # Yazı fontu

# Ana oyun döngüsü
flag = True
süre=pygame.time.Clock()

while flag and can>0:
    # Olayları işleme
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False
            
    # Klavye kontrolleri(kutucuk hareketi)        
    
    tuşlar=pygame.key.get_pressed()
    if tuşlar[pygame.K_LEFT]:
        kutucuk.x-=5
    if tuşlar[pygame.K_RIGHT]:
        kutucuk.x+=5                 
             
            
    # Ekran sınırıları kontrolü
    
    if kutucuk.left < 0:
        kutucuk.left = 0
    elif kutucuk.right > ekran_genislik:
        kutucuk.right = ekran_genislik
            
    # Yiyecek düşürme ve kontrol
    yiyecek.y+=yiyecek_hiz
    
    if yiyecek.y>ekran_yukseklik:
        yiyecek.y=0
        yiyecek.x=random.randint(0,ekran_genislik-yiyecek_genislik)
        can-=1 # yiyeceği kaçırdığında can hakkı düşer
    
    # Çarpışma kontrolü
    if kutucuk.colliderect(yiyecek):
        yiyecek.y=0
        yiyecek.x = random.randint(0, ekran_genislik - yiyecek_genislik)
        puan += 10

    # Ekranı temizleme
    ekran.fill((255, 255, 255))  # Beyaz arka plan
    
    # Kutucuğu çizme
    pygame.draw.rect(ekran,kutucuk_renk,kutucuk)
    # Yiyeceği çizme
    pygame.draw.rect(ekran, yiyecek_renk, yiyecek)
    
    # Puanı ve can hakkını ekrana yazdırma
    yaz_puan = font.render("Puan: " + str(puan), True, (0, 0, 0))
    yaz_can = font.render("Can: " + str(can), True, (0, 0, 0))
    ekran.blit(yaz_puan, (10, 10))
    ekran.blit(yaz_can, (10, 50))
    
    # Ekranı güncelleme
    pygame.display.flip()
    
    # Oyun hızını ayarlama
    süre.tick(60)  # Oyun hızı 60 FPS olarak ayarlandı
    
# Oyun bittiğinde sonucu gösterme
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    ekran.fill((255, 255, 255))  # Beyaz arka plan
    sonuc = font.render("Oyun Bitti! Toplam Puan: " + str(puan), True, (0, 0, 0))
    ekran.blit(sonuc, (ekran_genislik // 2 - 200, ekran_yukseklik // 2 - 50))
    pygame.display.flip()    
