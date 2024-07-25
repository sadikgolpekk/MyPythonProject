#define led 3  // LED'in pin numarasını tanımlar

void setup() {
  pinMode(led, OUTPUT);  // LED pini çıkış moduna ayarlanır
  Serial.begin(9600);    // Seri iletişim başlatılır (opsiyonel, seri monitör için)
}

void loop() {
  int isik = analogRead(A0);  // A0 pininden analog değeri okur (LDR'den gelen ışık seviyesi)
  Serial.println(isik);       // Okunan ışık seviyesini seri monitöre yazdırır
  delay(50);                  // 50 milisaniye bekler

  if (isik > 470) {
    digitalWrite(led, LOW);   // Eğer ışık seviyesi 470'ten büyükse LED'i kapat
  }

  if (isik < 470) {
    digitalWrite(led, HIGH);  // Eğer ışık seviyesi 470'den küçükse LED'i yak
  }
}

