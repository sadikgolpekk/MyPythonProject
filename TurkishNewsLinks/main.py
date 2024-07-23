import feedparser ## feedparser modülünü projeye dahil eder, bu modül RSS feed'lerini işlemek için kullanılır.

url="https://www.ntv.com.tr/gundem.rss" ## Haberleri almak istediğiniz RSS feed'in URL'sini tanımlar.Ayrıca diğerleri için https://gist.github.com/e-budur/983d969c0f6cf756bbbb60a2892aa964
news=feedparser.parse(url) ## Belirtilen URL üzerinden RSS feed'i parse eder.

i=0

for information in news.entries: ## RSS feed'deki her bir haber öğesi için döngü başlatır.
    i+=1
    print(i)
    print(information.title) ## Başlık
    print(information.link) ## Link
    print(information.summary) ## Özet
    print("\n")
