""" Kullanıcıdan isim ve yaş bilgisi alır, 
ardından 1 ile 100 arasında rastgele bir sayı seçer. 
Kullanıcının 5 tahmin hakkı vardır ve her tahminde kullanıcının
girdiği sayıya göre ipuçları verir. Kullanıcı doğru sayıyı 
tahmin ederse tebrik eder,
tahmin hakkı biterse oyun sona erer. """
import random
isim=str(input("İsminizi giriniz"))
yas=int(input("Yaşınızı giriniz"))
hedef_sayi=random.randint(1,100)

print(f"\nMerhaba {isim}! {yas} yaşındasın ve bir tahmin oynununa hoşgeldin")
print("1-100 arası bir sayı tahmin etmeye çalış")

counter=5
while(counter>0):
    tahmin=int(input("Tahmininiz: "))
    if(tahmin==hedef_sayi):
        print("Sayıyı doğru tahmin ettiniz,tebrikler")
        break
        
    elif(tahmin<hedef_sayi):
        print("Daha büyük bir sayı söyleyiniz")
        
    elif(tahmin>hedef_sayi):
        print("Daha küçük bir sayı söyleyiniz")
        
    counter-=1
    
    
    if(counter==0):
        
        print("Maalsef hakkınız bitti doğru cevap",hedef_sayi)
    
    
print("Oyun sona erdi...")
