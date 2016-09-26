# BroIDS Kurulum ve Kullanım Klavuzu
![BroIDS Logo](https://pbs.twimg.com/profile_images/464030354991357952/7-h9JZh4_400x400.png)
### 1) BroIDS Nedir?
**BroIDS** ilk başlarda **Vern Paxson** tarafından C++ dilinde geliştirilmeye başlanan, daha sonra açık kaynak hale gelerek herkesin katkıda bulunduğu Linux tabanlı bir **ağ trafiği analiz ve müdahale** yazılımıdır. **Bro**'nun adı, "Big Brother" yani "Büyük Kardeş"ten (Big Brother, siber güvenlik dünyasında genel olarak NSA'in lakabıdır) gelmektedir. "Büyük Kardeş"in bizi hep izlediği varsayımından esinlenilerek bu isim verilmiştir. BroIDS'in piyasada benzer işlevlere sahip diğer yazılımlardan ayırt edici özelliği, yüksek "throughput" seviyelerinde (Gigabitler) çalışabilmesidir.

Bro yazılımı :
* Saldırı Tespit Sistemi
* Saldırı Engelleme Sistemi
* Ağ trafiği izleme

amaçları doğrultusunda kullanılabilmektedir.

Fakat biz bu yazıda **Saldırı Tespit Sistemini** inceleyeceğiz.
***
### 2) Kurulum

BroIDS kurmak için öncelikle bir Linux sisteminde olmalısınız. 

Kuruluma başlamadan önce sisteminizin **güncel** olması gerekir. Dolayısıyla, komut satırınıza : 

> sudo apt-get update && apt-get upgrade

yazarsanız sisteminiz güncellenir. Daha sonra, Bro'nun bilgisayarınızda çalışabilmesi için önceden yüklü olması gereken paketleri yüklemelisiniz. Bunun için :

> sudo apt-get install cmake make gcc g++ flex bison libpcap-dev libssl-dev python-dev swig zlib1g-dev

yazarsanız bütün gerekli paketler indirilecektir. Artık Bro'yu indirmek için sistemimiz hazır.

Şimdi, Bro'yu indirmek istediğiniz dizine gidin. Örneğin, 

> cd ~/ids/

Bro yazılımı açık kaynaklı olduğundan açık kaynak yazılımların bulunduğu Git sitesinde de bir deposu (repository) bulunmaktadır. Dolayısıyla yazılımı indirmek için sadece o depodaki dosyaları bilgisayarımıza indirmemiz yeterlidir. Bunun için komut satırınıza :

> git clone --recursive git://git.bro.org/bro

yazın. Bro, otomatik olarak bulunduğunuz dizine indirlecektir. Dosyalar elimizde olduğuna göre şimdi kuruluma geçebiliriz. Öncelikle indirdiğimiz Bro klasörüne gitmemiz gerekiyor. Eğer hala aynı dizinde iseniz komut satırına :

> cd bro

girin. Doğru klasörde olup olmadığınızı anlamak için "_ls_" komutu girin. Aşağıdakine benzer bir çıktı almanız gerekir : 

```sh
root@kali:~/bro# ls
aux              build    CMakeLists.txt  doc       man   README      src
bro-config.h.in  CHANGES  configure       INSTALL   NEWS  README.rst  testing
bro-path-dev.in  cmake    COPYING         Makefile  pkg   scripts     VERSION
```

Daha sonra kuruluma başlamak için :

> ./configure && make && make install

yazın. Sonra kurulumunuz başlar. Tercihen, Bro'yu kuracağınız dizini belirlemek istiyorsanız "- -prefix" parametresi eklemeniz gerekir. Örnek : 

> ./configure --prefix=/etc/bro && make && make install

Eklemezseniz otomatik olarak "/usr/local/bro" klasörüne kurar.

Kurulumunuz bitince Bro kullanıma hazırdır.

Son olarak Bro'yu her dizinden komut satırından çalıştırabilmek için "PATH"e ekleriz (eğer - -prefix parametresini eklemediyseniz) :

> export PATH=/usr/local/bro/bin:$PATH

### 3) Kullanım
***
##### a) broctl

Bro, yazılımı kontrol etmek için bir kontrol betiğine (script) sahiptir ; **broctl**

Komut satırına :

> broctl

girin ve Bro arayüzüyle karşılaşacaksınız. Burada :

> help

komutu girerseniz size yardımcı olacak, hangi komutları girebileceğinizi yazan ekran gelir. Komut satırına :

> start 

girin. Bro bu komut sonrasında çalışır duruma geçer. Emin olmak için : 

> status

komutunu girin. Bro'nun prosesi (process) hakkında bilgi alacaksınız.

Bro şu anda paketleri yakalayıp içerisinde zaten bulunmakta olan imzalara yönelik alarmlar üretmekte.

Birkaç komut örneği :

```sh
stop        # Bro'yu durdurur
update      # Konfigürasyon dosyalarını günceller
restart     # Bro'yu yeniden başlatır
exit        # broctl'den çıkar
diag        # Herhangi bir sorun çıkınca logları bu komutla görebilirsiniz
```
##### b) Loglar

Bro'nun ürettiği logları görebilmek için önce **broctl**'den çıkın :

> exit

Şimdi, Bro'nun ürettiği loglara gözatmak için aşağıdaki komut ile internetten bir dosya indirin : 

> wget www.testmyids.com

Sonra Bro'yu kurduğunuz dizindeki "logs" klasörüne gidin :

> cd /usr/local/bro/logs/

Burada :

> ls

komutunu çalıştırın. Çıktı olarak şu ana kadar üretilen logların tarih olarak ayırt edilmiş olacağını ve kaydetmekte olduğunuz trafik loglarını "current" klasörü içinde göreceksiniz :

> cd current

Sonra :

> ls

Burada kategorilere ayrılmış log dosyalarını göreceksiniz (http.log, dns.log, weird.log, conn.log... vb.). Herhangi birini incelemek için, örneğin :

> less http.log

komutunu girin. Burada Bro'nun ürettiği http loglarını görmektesiniz. Bro herhangi bir zararlı veya dikkate değer paket yakalarsa bunu notice.log içerisine kaydeder.

##### c) İmzalar

Bro, imzaları için kendine özgü bir dile sahiptir. Örnek bir imza dosyasının içeriğine bakmak istiyorsanız aşağıdaki komutu girin :

> less /usr/local/bro/share/bro/base/protocols/dhcp/dpd.sig

Karşınıza buna benzer bir ekran gelir :

```
signature dhcp_cookie {
  ip-proto == udp
  payload /^.*\x63\x82\x53\x63/
  enable "dhcp"
}
```

Bu imza dhcp paketleri için yazılmıştır. İmzanın anlamı :
* Protokolü UDP olan
* paketin içerik (payload) kısmında "/^.*\x63\x82\x53\x63/" yani "cSc" gibi bir şey varsa
* Bro'nun içinde var olan dhcp protokol analizcisini etkinleştir

İmzaların payload kısmı, iki tane "/" karakteri arasındaki "regular expression"ları algılar.

Kendi imzamızı yazmayı öğrenmek istiyorsak Bro'nun https://www.bro.org/sphinx/frameworks/signatures.html sitesini ziyaret edebiliriz.

Bro, imzalarını /usr/local/bro/share/bro/base/protocols/ dizininin alt klasörlerinde tutuyor. Bu klasöre gidersek :

> cd /usr/local/bro/share/bro/base/protocols/

ve 

> ls

çalıştırırsak, bazı protokolleri görürüz (http, ftp, dchp vb.) bunlardan herhangi birine girince :

> cd http

ve

> ls

burada http protokolünü analiz etmek için kullanılan dosyalar var. Bunlardan "sig" uzantılı dosya imzaların (signature) olduğu dosyadır. Basit bir imza yazacak olursak :

> nano dpd.sig

dosyada görebileceğiniz gibi önceden yazılmış imzalar var. Bir tane basit bir imza ekleyecek olursak :

```
signature imza {

  ip-proto == tcp
  dst-port == 80
  event "basarili"

}
```

Bu imza :
* Protokol TCP ise
* Hedef portu 80 ise
* Alarm üretir ve mesajını "basarili" olarak belirler

Şimdi imzamızı görmesi için Bro'yu baştan başlatmamız gerekli : 

> broctl restart

Eğer Bro başlarken hata oluşursa yazım hatalarını kontrol edin.

Daha sonra alarm üretebilecek bir paket alış-verişinde bulunalım :

> wget www.google.com

İmzamızın çalışıp çalışmadığını görebilmek için notice.log dosyasına bakalım : 

> cat /usr/local/bro/logs/current/notice.log && grep -i --color basarili

Bu komutu giridiğinizde karşınıza üretilen alarm ve detayları çıkmalıdır.

Bu arada dikkat ettiyseniz "notice.log" dosyası oluşmuş. Öncesinde log dosyalarına baktığımızda yoktu. Bunun nedeni Bro'nun bir imzaya uyan paket görüp tehdit olarak "notice.log"a eklemesidir.

Başka bir imza yazacak olursak :

```
signature karaliste {

  ip-proto == tcp
  dst-ip == 104.154.89.105
  event "saldiri"

}
```

Bu imzada :
* Protokol TCP ise
* Hedef IP karalisteye (blacklisting) aldığımız IP'lerden biriyse
* Alarm üretir ve mesajını "saldiri" olarak tanımlar

Bu imzayı aşağıdaki komutla yakalabiliriz :

> wget www.badssl.com

Başka bir imza örneği :

```
signature LAND-sig {

  same-ip
  event "LAND saldirisi!"

}
```

Bu imzada ise sistem, LAND saldırısını yakalıyor. Hedef ve kaynak IP adresi eşit ise "LAND saldirisi!" mesajlı bir alarm üretir.

Son bir imza örneği ise :

```
signature attack-sig {
    ip-proto == tcp
    dst-port == 80
    payload /.*root/
    event "root"
}
```

Bu imza :
* TCP kullanıyorsa
* Hedef port 80 ise
* İçeriğinde ".*root" olan
* Paket gördüğünde mesajı "root" olan bir alarm üretir.


