# Python ile Görüntü İşleme Staj Projesi
Öncelikle bu pandemi döneminde uzaktan staj çalışması boyunca bana yardımcı olan danışmanım Öğr. Gör. Dr. Alper VAHAPLAR’a teşekkür ederim.

## Görüntü İşleme
Görüntü işleme, bir görüntüyü sayısal hale dönüştürdükten sonra elde edilen verilere matematiksel işlemler ve farklı yöntemler uygulanarak çeşitli çıkarımlar oluşturma ya da yeni görüntüler üretme tekniğidir. Görüntü işleme tekniği, görüntünün netliğini artırma, ışık değerlerini değiştirme ve görüntü üzerinde bulunan herhangi bir nesnenin tanımlanabilmesi gibi birçok amaçla kullanılmaktadır. Görüntü işleme uygulamaları son yıllarda ciddi bir artış göstermiştir. Özellikle araç içi otomasyon sistemlerinden, robot uygulamalarında, askeri uygulamalardan tarım uygulamalarına kadar birçok alanda yaygın olarak kullanılmaktadır. (SAMTAŞ & GÜLESİN, 2011)

### Görüntü İşleme Kütüphaneleri
Python programlama dilinde görüntü işlemede genellikle Numpy, OpenCV, Matplotlib, Pillow, Scipy, Scikit-Image kütüphaneleri kullanılmaktadır.

## Uygulama
Raporda Bölüm Üç Olan	Uygulama kısmında şu konular yer almaktadır:
- Küçültme-Piksel Değiştirme Metodu	14
- Küçültme-İnterpolasyon Metodu	15
- Büyültme-Piksel Değiştirme Metodu	16
- Büyültme-Piksel İnterpolasyonu Metodu	17

## SONUÇ
Python programla dili ile “Görüntü İşleme” projesi kapsamında, Numpy, OpenCV, Matplotlib, Pillow kütüphaneleri kullanılmıştır. OpenCV kütüphanesi yardımıyla Python üzerinde üçgen ve daire gibi geometrik şekiller for döngüsü yardımıyla çizilmiştir. Bu çizilen şekiller üzerinde grayscale dönüşüm yapılarak edge detection uygulanmıştır. Ayrıca elektronik bir ortamda çizilen renkli bir görüntü, dijital olarak Python üzerinde okutulmuştur. Bu okutulan görüntü Kırmızı, Yeşil ve Mavi (RGB) renklerinden oluştuğu için çift katlı array veri yapısında saklanmıştır. Bu görüntü üzerinde Numpy kütüphanesi yardımıyla küçültme ve büyültme yöntemlerini uygulamak için çarpma, toplama gibi matris işlemleri yapılmıştır. 

Piksel interpolasyonu ile küçültme yönteminde Numpy kütüphanesinde yer alan np.mean() fonksiyonu ile orijinal görüntüdeki piksel değerlerinin RGB renk ortalamaları alınmıştır. Bu alınan ortalama değerler yeni görüntüye atanmıştır. Piksel interpolasyonu ile büyültme yönteminde ise orijinal görüntüdeki pikseller yeni görüntüye aktarılmış, yatay ve dikey olarak bu piksellerin arasındaki boş piksellere uzaklıklarına göre bilineer interpolasyon uygulanarak atama işlemi yapılmış ve ardından bu piksellerin arasında kalan boş pikseller de yeni piksellerin bilineer interpolasyonu ile atanmıştır. Bu sayede tek boyut üzerinde çalışan bilineer interpolasyonu iki kez uygulanarak iki boyutlu olan görüntülerdeki uygulaması sağlanmıştır.

Python üzerinde OpenCV gibi kütüphaneler kullanarak görüntü işleme kapsamında anlık kamera görüntüleri üzerindeki canlı ve cansız nesnelerin tespiti, bu nesnelerin davranışları veya durumları tespit edilebilir. Amazon firmasının bazı satış mağazalarında çalışan olmadan sadece görüntü işleme yardımı ile gelen müşterilerin aldıkları ürünleri tespit edilmektedir. Ziraat alanında bitki üzerinde hastalık olup olmadığı olan hastalığın ne olduğunun tespitinde de yine görüntü işleme kullanılmaktadır. Bu gibi projeler detaylandırılabilir ve üzerinde çalışılabilir.
