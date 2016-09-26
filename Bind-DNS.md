# Bind-DNS-Sikilastirma-Klavuzu
# GİRİŞ
Alan Adı Hizmetiniz (DNS) sizin İnternetteki sisteminiz için yol götericinizdir. Ağınız ne kadar güçlü ve gevenli olursa olsun, posta ve diğer sunucular, risk altında olan ve yozlaşmış DNS sistemleri müşterilerin ve meşru kullanıcıların size ulaşmasını engelleye bilir.
BIND [1] en sık kullanılan DNS sunucusudur ve ISC tarafından sürdürülmektedir. Bekletici programın da isminin aynı olmasından dolayı "adlandırılan" olarakta bilinmektedir. Bir çok uygulamanın artan kötü niyetli İnternet ortamına maruz kalmasından dolayı, güvenlik zaafiyetleri  BIND tarafından keşfediliyor. Üç ana versiyon bulunmaktadır:
* 1.	v4 1998 yılına kadar bir çok UNIX sistemleri ile birlikte paketlenmiştir. Bir çok satıcılar bundan vazgeçmiştir. OpenBSD ekibi v4 ve sonrasında v9’da bazı düzeltmeler yaptı (v8 ekip tarafından fazla karmaşık olarak değerlendirildi).
* 2.	 v8 hala kullanımda olmasına rağmen eskiyor. Bu versiyonun sağlamlaştırılması bir başka makalede tartışılmıştır [13].
* 3.	 v9 tamamen yeniden yazılmıştır, ücretsiz ve aynı zamanda ticari desteklidir. Birçok yeni özellikleri mevcuttur (kullanışlı fakat güvenliği kuşkulu). v9 2000 yılı ekim ayında üretim status almıştır ve o gün itibarile düzenli olarak geliştiriliyor. 
BIND9’un yaratıcısı Nominum’daki mühendis ekibi DNS topluluğunun uzmanlarıdır. DNS ve DHCP için yazılım, donanım, eğitim,danışmanlık ve aynı zamanda DNS ev sahipliği hizmetlerini www.secondary.com üzerinden temin ediyorlar.
Bu makale  Bind 9. versiyonu güvenli kullanmayı anlatıyor.

# Neden Rahatsız Ediyor? Güvenliksiz Bir BIND Ne Gibi Riskler İçeriyor?

Gerçekten DNS  için endişe duymalı mıyız? Risk altındaki bir DNS sunucusu bazı enteresan riskler içerir:
*  **1) Eğer bölgesel geçitlere izin veriliyorsa saldırgan birçok bilgi elde edebilir:** ev sahibi ve yönlendiricilerin IP addresleri, isimleri ve bazı isim ve lokasyon içerikli yorumların tüm listesi gibi.
*  **2) Hizmet Tekzibi:** Eğer sizin İnternet DNS sunucularınız çökerse,
      * Siteniz artık görünür olamaz (diğer siteler IP adresinizi göremez).
      * E-postalarınız ulaştırılamaz (yakın zamanda bilgi alış-verişinde bulunduğunuz bazı diğer internet siteleri DNS girdilerinizi saklı tutmuş olabilir, ama bunlar da birkaç günden fazla dayanmaz).
      * Saldırgan sizin sunucunuz gibi görünen ve alanınız ile ilgili internete yanlış DNS  bilgisi yayan sahte bir DNS sunucusu yaratabilir. Bu bütünlük kaybı demektir, sonraki kesite bakınız.
      
*  **3)Bütünlük kaybı:** Eğer saldırgan DNS verilerini değişir ve ya yanlış bilgiye inanacak başka siteleri kandırırsa (bu DNS zehirlenmesi olarak bilinir), bu çok tehlikelidir:
      
      * Sahte siteler sizinmiş gibi görünür ve siteniz tarafından yönetilen kullanıcı girdilerini ele geçirebilir, bu girdiler kullanıcı PIN ve şifreleri de dahil birçok hesap bilgisi olabilir.
      * Bütün e-postalar onları sizin sitenize ulaşmadan önce değişen, kopyalayan ve silen bir röleye yönlendirilebilir.
      * Eğer güvenlik duvarınız veya herhangi bir internet ulaşımı mevcut ev sahibi kimlik doğrulamak için DNS ismini kullanıyor ya da partnerliğinize güveniyorsa, bunlar kesinlikle kötüye kullanılabilir, özellikle İnternet sunucuları ve İntranet zayıf bir filtre paketi ile korunuyorsa. Sadece *.mydomain.com’dan gelen vekil taleplerine izin vermek için ayarlanmış bir Ağ vekili hayal edin. Saldırgan kendi ev sahibini alana ekliyor ve bu zaman Ağ vekili saldırgan HTTP’ye  ondan gelen taleplere izin vererek internet ulaşımı sağlıyor. 
     SSH kullanan bir internet yöneticisi hayal edin, fakat güvenlik duvarı ev sahiplerinin "admin.mydomain.com"a inanan bir ".shosts"u var ve burada "admin" yöneticinin iş istasyonu demek. Eğer saldırgan DNS girdisini "admin.mydomain.com" ile değişebilirse bu onun güvenlik duvarı ev sahibine şifresiz ulaşımı olduğu demektir.
2001 kışı ve 2008 yazında ortaya çıkan DNS zaaflarını kullanan otomatik saldırı araçları ve solucanlarından yola çıkarak DNS’in internet hacker’larının favori hedefi olduğu kanaatine gelinmektedir.

# Peki Yapılması Gerekenler Neler?
BIND riskleri bazı koruma önlemleri ile azaltılabilir:
*  **1)İzolasyon Kaynakları:** İnternet DNS’i için adanmış, sağlamlaştırılmış sunucular kullanın ve diğer servisler ile paylaşmayın ve özellikle kullanıcı girişlerine izin vermeyin. Minimal sayıdaki kullanıcı çalışan programların ve akabinde internet saldırılarının azalması anlamına gelir. Ayrılma yerel zaafiyetleri kullanan diğer servislerin ve kullanıcıların BIND’e saldırmalarını önler.
*  **2)Fazlalık:** Başka bir internet bağlantısına ikincil bir yükleme yapın (şirketinizin yabancı bir şubesi, başka bir ISP v.b.). Eğer siteniz ölürse, en azından diğer siteler "varoluşu durdurduğunuzu" sanmaz; sadece sizin "müsait" olmadığınızı  ve böylece e-postaların bekletildiğini anlar (genellikle 4 günlük süre ile).
*  **3)** En son versiyonu kullanın.
*  **4)Giriş Kontrolü:** Ağınızda saldırıya açık olan veri miktarını azaltmak için alan değişimlerini kısıtlayın. İşlem imzası (TSIG) kullanmayı ve özyinelemeli sorguları kısıtlamayı düşünün.
*  **5)BIND’I en az ayrıcalık ile çalıştırın:** temel olmayan bir kullanıcı olarak, sıkı bir **umask** ile.
*  **6)Daha fazla izolasyon kaynakları:** BIND’i "chroot" kafesi ile çalıştırın, böylece bir BIND şeytanı için işletim sistemine zarar vermek ve diğer servisleri kötüye kullanmak daha da zor olur. 
*  **7)** BIND’i versiyon numarasını rapor etmemesi için ayarlayın. (aşağıda belirtilecek). Bazı insanlar bunun bir "gizlilik güvenliği" olduğu için versiyon numarasının gizlenmesine inanmayacak, ama bunun internette dolanıp açık hedef arayan çocuklara karşı işe yarayacağına eminim. Profesyonellere karşı korunma farklı bir konu.
*  **8)Keşif:** Monitör bütünlük denetleyicisi ile beklenmedik aktiviteler ve sistemdeki yetkisiz değişiklikler için keşif yapar.
*  **9)** Gözünüz uygun danışmalarda olsun, gelecek BIND problemlerinden güncel şekilde haberdar edildiğinizden emin olun.

# BIND8 ve BIND9’daki Farklılıklar
Çok işlemcili olma ve yeniden yazılmış kodların dolayısıyla daha stabil ve uzun dönem güvenlik vaad etmesi dışında başka farklılıkları da bulunuyor;
* Eğer named.conf’da bir yazım hatası olursa, BIND9 hatları bulur ve sunucuyu yenilemez. BIND hataları bulur ve şeytan ölür! 
* Ulaşım kontrolü için TSIG’in kapsamlı desteği (paylaşılan anahtarlar), mesela  "güncelleme poliçesi" dinamik güncellemelerde daha iyi öğütülmüş bir ulaşım kontrolü için kullanıla bilir.
* Başlama/durdurma/yeniden yükleme ve s. için olan araç, rndc ile v8 ndc arasında haberleşme, belgeleme ve diğer özelliklerde farklılıklar vardır.  Rndc kesitine bakınız.
* Bölge dosyalarındaki sentaks daha titizlikle denetlenir. (örneğin TTL satırı olmak zorunda)
* named.conf’ta:
  * v8’deki 'check-names' ve 'statistics-interval' seçenekleri v9’da henüz tamamlanmamıştır.
  * 'auth-nxdomain' için varsayılan seçenek şimdi 'no'dur. Eğer manüel olarak ayarlamazsanız, BIND 9 başlangıçta eş anlamlı bir mesaj keşfeder.
  * Kök sunucu listesi, BIND8’de named.root veya root.hints olarak ta bilinir, sunucunun içerisinde yer alsa bile BIND 9’da gerekli değildir.
  
 
# BIND’in Kurulumu ve Yapılandırılması
Solarisin iyi çalıştığı ve yeteri kadar sağlamlaştırıldığı ve birlikte gelen BIND’in aktif olmadığı farzedilir. Eğer hala Solarisi sağlamlaştırmadıysanız, ilk once Jass’ı control edin [7]. Bu bölüm bunlarla çalışır:
* Sağlamlaştırılmış bir DNS sunucunuz olmadığı için BIND’i bir uzman ev sahibine derleyin.
* BIND’i bir DNS sunucusuna kurun.
* Ayarlayın ve BIND’i çalıştırın.

## 1. BIND’in Derlenmesi ( derleyici ev sahibine )
Dağılımı indirin [1], onu subdirectorye çıkarın ve derleyin. Bu işlem kök kullanıcı olmayarak ta yapıla bilir.
* Önkoşullar: 
İlk olarak 'GNU make'i kurun, böylece altdaki rehbere geçici kurlumunuz doğru bir şekilde çalışır.
Ayrıca aşağıda  /usr/local/bin/make’e başvuruyoruz, Solarisin standart /usr/ccs/bin/make’e değil. 
Standart Solaris yacc’ın yeterli olmasına rağmen GNU bison’a eski test sistemimde ihtiyaç vardı. 
**GNU grep v9.5.1’e yükseltme için gerekti** 
SSL kütüphanesinin son versiyonunun kurulması gerek. Eğer SSL kütüphaneleri eski olursa BIND bundan hoşnut olmaz (eski versiyonların güvenlik zaafları mevcut). 
Yukarıdakiler için paketler SunFreeware.com’dan kolayca kurulabilir, mesela: 

  ```    
  wget ftp://ftp.sunfreeware.com/pub/freeware/sparc/8/grep-2.5.1a-sol8-sparc-local.gz
  gunzip grep-2.5.1a-sol8-sparc-local.gz
  pkgadd -d grep-2.5.1a-sol8-sparc-local
  ```
  
Yeni grep-i kurduktan sonra  'make'in bulmasından emin olun:
    	```
    	export GREP=/usr/local/bin/grep
    	```
* BIND 9.1.0’in sürüm notunda çok işlemliliğin Solaris 2.6-da bazı problemler yaratacağı not edilmiştir, bu yüzden çok işlemci desteği olmadan derlemeyi gerçekleştiriyoruz:
     ```
      ./configure --disable-threads
     ```
  
* Solaris 7/8’de çok işlemciyi active ede biliriz:
```      
./configure
```
     Şimdi ise GNU make’i kullanarak derleye biliriz:
     
     ```
      /usr/local/bin/make
     
     ```
     
    Şimdi kök hesabı değişin, onu geçici rehbere kurun ve ‘tarball’ yaratın:
    
       ```
       su - root
       #allow group, but not world access
       umask 027
       /usr/local/bin/make install DESTDIR=/tmp
       cd /tmp/usr/local
       strip bin/* sbin/* lib/*
       \rm -rf include
       tar cf - * | compress > bind9_dist.tar.Z
       ```
  
Daha sonra, bind9_dist.tar.Z’i daha güvenli bir yere taşıyın, /tmp/usr-i kaldırın ve BIND’i derlediğiniz rehberi temizleyin.
**Belgeleme:**
Yönetici Rehberi(html formatında) dağılıma doc/arm/Bv9ARM.html’de dahil edilmiştir ve okumakta yarar vardır. İnsanlar için olan sayfalar da mevcut fakat onları Solaris’e kurmak hayli zordur. Bir sonraki sürüm olan v9.2’de insan sayfaları düzgün bir şekilde kurulmalıdır.

## 2. Chroot’un ayarlanması ve BIND’in kurulumu (hedef sisteme)
Sonraki adımlar C-Shell kullanımını anlatıyor. Biz buna chroot ortam (kafes) lokasyonunu değişken olarak tanımlamakla başlıyoruz ve akabinde umask’i ayarlıyoruz ve böylece bütün kopyalanmış dosyalar hem gruplar hem de dünya tarafından okunabilir. Bu komutalar kopyalanmak ve yapıştırılmak üzere tasarlanmıştır.
* Chroot jail için hedef dizinlerini ayarlayın, herşey bu ağacın alt dizinlerie kurulacak.

     ```
      csh
      unset noclobber
      set jail='/home/dns';
      umask 022;
      ```
      
* Boş dizinleri ve bağlantıları chroot environment için ayarlayın:

     ```
     mkdir $jail;
     /dns-ten jail-e bir bağlantı yaratın, hayatı kolaylaştırmak için bu makalede "/dns" chroot ağacının en tepesi olarak kabul edilecektir.
     rm /dns
     ln -s $jail /dns
     cd /dns;
     mkdir -p {dev,opt,usr,var,etc};
     mkdir -p var/{run,log,named} usr/lib;
     mkdir -p usr/local/etc
     mkdir -p usr/share/lib/zoneinfo;
     ```
     
* Hesaplar:
BIND için bir kullanıcı ve grup hesabı yaratın,
     ```
groupadd named;
useradd -d /dns -s /bin/false -g named -c "BIND daemon" -m named
Chroot içinde aynı kullanıcı ve grup hesabı oluşturun:
grep named /etc/passwd >> /dns/etc/passwd
grep named /etc/shadow >> /dns/etc/shadow
grep named /etc/group >> /dns/etc/group
BIND hesabının ftp kullanmasına izin vermeyin:
echo "named" >> /etc/ftpusers
Add /dns/usr/local/bin to the root PATH in /root/.cshrc or /root/.profile.
     ```

* BIND dağılımını kurun – ilk önce dizini tarball-ın yerleşkesine değişin:

    ```
    cp bind9_dist.tar.Z /dns/usr/local;
    cd /dns/usr/local;
    zcat bind9_dist.tar.Z| tar xvf -
    ```
    
* chroot ortamı için gerekli system dosyalarını kopyalayın

   ```
   cp /etc/{syslog.conf,netconfig,nsswitch.conf,resolv.conf,TIMEZONE} /dns/etc
   ```
   
Obje kütüphanelerinin ne paylaştığını görmek için ldd kullanın:
  ```
ldd /dns/usr/local/sbin/named
  ```

ldd ile listelenen dosyaları kopyalayın, mesela Solaris 8’de:

  ```
cp -p /usr/lib/libnsl.so.1  \
/usr/lib/libsocket.so.1 /usr/lib/libc.so.1 \
/usr/lib/libthread.so.1 /usr/lib/libpthread.so.1 \
/usr/lib/libdl.so.1 /usr/lib/libmp.so.2 \
/usr/lib/ld.so.1 /usr/lib/nss_files.so.1 \
/usr/platform/SUNW,UltraAX-i2/lib/libc_psr.so.1 \
/dns/usr/lib
  ```

**Solaris 2.6:**

  ```
cp -p /usr/lib/libnsl.so.1 \
/usr/lib/libsocket.so.1 /usr/lib/libc.so.1 \
/usr/lib/libdl.so.1 /usr/lib/libmp.so.2 /dns/usr/lib
  ```

Solaris 2.6 UltraSPARC’da ldd aynı zamanda bunları da gerekli bilip listeler:

  ```
cp /usr/platform/SUNW,Ultra-250/lib/libc_psr.so.1  /dns/usr/lib
  ```

Deneyimler bunların da gerekli olduğunu göstermiştir:

  ```
cp /usr/lib/ld.so.1 /usr/lib/nss_files.so.1 /dns/usr/lib
  ```

("deneyim" ilk girişimlerin başarısız olduğu demektir, ama truss ile çalışan  BIND kütüphanenin neyi aradığını anlaya bilir.)
Timezone dosyalarını kopyalayın (mesela MET, burada Avrupa):

  ```
mkdir -p /dns/usr/share/lib/zoneinfo;
cp -p /usr/share/lib/zoneinfo/MET /dns/usr/share/lib/zoneinfo/MET
  ```

İletişim araçlarını kurun( konsol, syslog).
 
   ```
    cd /dns/dev
    mknod tcp c 11 42
    mknod udp c 11 41
    mknod log c 21 5
    mknod null c 13 2
    mknod zero c 13 12
    chgrp sys null zero
    chmod 666 null

    mknod conslog c 21 0
    mknod syscon c 0 0
    chmod 620 syscon
    chgrp tty syscon
    chgrp sys conslog
   ```
 
Bind v9.5.1 için /dev/poll oluşturun

  ```
   cd /dns/dev 
   mknod poll c 138 0 
   chgrp sys random
   chmod 644 random
  ```
Yerel syslog mesajları için opsiyoneldir: Syslog için bir döngü yaratın. Ben bunu gerekli bulmuyorum ama bir okuyucu bunu öneriyor:

  ```
mkdir /dns/etc/.syslog_door
mount -F lofs /etc/.syslog_door /dns/etc/.syslog_door
  ```

Solaris 8/9’da, /dev/random-a ulaşım /dns jail’a döngü oluşturarak temin edilebilir (ben bunu tarihi nedenlerden dolayı kullanıyorum...):

   ```
   mkdir /dns/dev/random
   mount -F lofs /dev/random /dns/dev/random
   veya DNS jail-in içinde bir cihaz yaratarak (önce cari minor/major cihaz numarasına bakılması gerek ls -al /devices/pseudo/random\@0\:random):
   cd /dns/dev
   mknod random c 240 0
   chgrp sys random
   chmod 644 random
   ```
 
DNS verisi için dizin oluşturun; bunun /var/named’de olduğunu varsayalım:

  ```
mkdir -p /dns/var/named;

  ```
## 3. DNS Veri Dosyalarının Ayarlanması

    ```
    cd /dns/etc
    touch named.conf
    chown root:named named.conf
    chmod 640 named.conf
    vi named.conf
    ```
    
Peki named.conf-a ne koyuyoruz? BIND-ı çalıştırmak için küçek bir örnek ile başlıyalım : lookups of 'localhost', reverse lookups of 127.0.0.1 and a simple domain test1.com
 * Basit bir öncül DNS sistemi (adresin bu olduğunu farzedelim 192.168.128.34):
    *  Buraya kopyalayın /dns/var/named: localhost.zone, localhost.rev, test1.com
    *  Buraya kopyalayın /dns/etc/named.conf: named.conf.primary
 * Basit bir ikincil DNS sistemi (adresin bu olduğunu farzedelim 192.168.128.33):
    *  Buraya kopyalayın /dns/var/named: localhost.zone, localhost.rev
    *  Buraya kopyalayın /dns/etc/named.conf: named.conf.secondary

Birazdan DNS yapılandırmasının detayına ineceğiz, şimdilik bu aşamada BIND’i çalıştırmaya odaklanıyoruz.
Bu dosyaları kopyaladıktan sonra yazılımı doğrulayın :

   ```
  Primary + Secondary:
  chroot /dns /usr/local/sbin/named-checkconf /etc/named.conf
  chroot /dns /usr/local/sbin/named-checkzone local /var/named/localhost.zone
  chroot /dns /usr/local/sbin/named-checkzone local /var/named/localhost.rev
   ```
  
localhost.zone dosyası eksik SOA and NS kayıtlarından deyinebilir. Buna aldırmayın.

Primary:

  ```
  /dns/usr/local/sbin/named-checkzone test1.com /dns/var/named/test1.com
  ```
## 4. Kafes İzinlerinin Ayarlanması
Şimdi dosya izinlerini ayarlıyoruz,böylece root dosyaları benimsiyor ve named bütün dosyaları okuyup bazılarını yaza biliyor. O zaman bütün SUID/SGID dosyalarını etkisiz hale getirin. 
PID dosyası /var/run-a konuldu /usr/local-a değil, çünki named kullanıcısının /usr/local/etc’a (ve named.conf’a) yazmasını istemiyoruz. PID dosyasının lokasyonu named.conf’ta belirleniyor.
 
  ```
  cd /dns
  chgrp -R named *
   ```
 > * grup yazımını var-dan kaldırın, opt ve usr’e ulaşım yazın
  
  ```
  chmod -R g-w var;
  chmod -R a-w opt usr;
  ```
> * Secondary İçin, named’e very dosyalarını oluşturma/değişim izni verin :

  ```
  chown -R root:named /dns/var/named;
  chmod 770 /dns/var/named;
  ```
> * Primary için, named’e yalnız okuma izni verin, veri dosyalarına yazma iznine gerek yok:
  
  ```
  chown -R root:named /dns/var/named;
  chmod 750 /dns/var/named;
  chmod -R go-w /dns/var/named;
  ```
> *  Not: Size bir beyaz yalan söyledim... eğer named onarım dosyası veya dökuman istatistiği yazma gereği duyarsa yazar
> * /dns/var/named’e ulaşın. Böylece isteğinize gore çok sıkı ya da rahat bir kurulum tercih edebilirsiniz:
  
  ```
  chmod 770 /dns/var/named;
  ```
  
> * Boş log ve pid dosyaları oluşturun:
  
  ```
  touch var/log/all.log var/run/named.pid;
  chown named:named var/log/all.log var/run/named.pid;
  ```

> * Named user/group’a logs ve piddosyaları yazma izni verin:
  
  ```
  chgrp -R named /dns/var/log /dns/var/run;
  chmod 770 /dns/var/run /dns/var/log;
  chmod -R o-rwx /dns/var/run /dns/var/log;
  ```
> * named’e BIND yapılanma dosyasına erişim izni verin:
  
  ```
  chgrp named /dns/etc;
  chown root:named /dns/etc/named.conf;
  chmod 640 /dns/etc/named.conf;
  chmod 755 /dns/etc;
  ```

> * Eğer varsa SUID veya SGID bitlerini kaldırın:
  
  ```
  find . -type f -exec chmod ug-s {} \;
  ```
> * Dünya erişimini kaldırın:
  
  ```
  chmod -R o-rwx * /dns/usr
  ```
  
"ls -alR"in üretim DNS öncülü üzerindeki örneği için dipnot [8]’e bakınız.
## 5. BIND Çalıştırma
Evet, /dns/etc/named.conf’da DNS yapılanmamız var, alan dosyaları /dns/var/named’de (/dns chroot ağacının başına bağlantıdır, öreneğin /export/home/dns), O zaman BIND’i çalıştırmayı deneyelim!
* BIND aktivitesini kontrol etmek için syslog(logs)’a bir kuyruk kurun, örneğin
 
 ```
 tail -f /var/adm/messages |grep named  &
 tail -f /var/log/daemonlog |grep named  &
 Logs /var/adm/messages-da veya /etc/syslog.conf yapılanmanızdan dolayı başka bir sunucuda olabilir.
 ```

* BIND chroot'ed-i başlatın: 

 ```
 /usr/sbin/chroot /dns /usr/local/sbin/named -u named
 ```

* Hatalarınızı kontrol edin:
  * Syslog’u inceleyin.
  * Örnek alanlarımızı test edin:

 ```
 /dns/usr/local/bin/dig @localhost 127.0.0.1
 /dns/usr/local/bin/dig @localhost localhost
 /dns/usr/local/bin/dig @localhost localhost mx
 /dns/usr/local/bin/dig @localhost localhost ns
 /dns/usr/local/bin/dig @localhost www.test1.com
 /dns/usr/local/bin/dig @localhost www1.test1.com
 /dns/usr/local/bin/dig @localhost test1.com ns
 /dns/usr/local/bin/dig @localhost test1.com mx
 ```

  * İkincilin alan transferleri yapa bildiğine emin olun: bizim örneğimizde 'test1.com' dosyasının /dns/var/named-de ortaya çıkması gerek.
  * Eğer yapılanmayi değişirseniz, named’e HUP işareti gönderin , yapılanmanın yeniden yüklendiğinden emin olmak için.
  
  ```
  kill -1 `cat /dns/var/run/named.pid`
  ```

  * Eğer internete bağlana biliyorsanız, IP-Plus tool 4 kullanan alanları inceleyiniz.
* Eğer herşey iyi görünüyorsa, sistem her önyükleme yaptığında BIND’i çalıştırın.
Sun'ın varsayılanını devredışı bırakmak için /etc/rc2.d/S72inetsvc girdilerini named-e değişin. Sonrasında bir başlama dosyası(/etc/init.d/dns)  oluşturun ve başlama bağlantıları şu şekildedir:

   ```
   ln -s /etc/init.d/dns /etc/rc2.d/S50dns
   ln -s /etc/init.d/dns /etc/rc2.d/K50dns
   ```
   
Örnek verdiğim başlama dosyasının /etc/init.d/dns kontrol etmek isteyeceğiniz birkaç nitelik ve ayrıntıları var, örenğin /dns chroot ortamı içinde /dev/random paketlemesi.

# Sorun Giderme Tavsiyeleri

* Client:
Sunucu sonuçlarını öğrenmek için dig veya host veya nslookup kullanın. Dig daha iyidir, çünki nslookup DNS sunucusu için PTR kayıtlarını; aksi takdirde başlamaz. Ayrıca nslookup-ın birçok uygulamasının IPv6 ile çalışmadığını göreceksiniz.

  ```    
  Check /etc/nsswitch.conf ve /etc/resolv.conf-u inceleyin.
  ```

Bir sürü hata ayıklama bilgisi için nslookup –u "-d2" seçeneği ile veya herhangi bir argümanla başlatmayın ve "help" yazın. Aynı zamanda burada etkileşimli istem kısmında "debug" komutası da mevcuttur.
Nscd şeytanını öldürmeye çalışın.

* Server:
Değişimlerden sonar config dosyasını tekrar okuması için named-e bir HUP sinyali gönderin. 

  ```
  kill -HUP `cat /dns/var/run/named.pid`
  ```

Syslog girdilerine bakın. Genellikle loglar syslog "şeytan" sekmesinde olur.
Yapılanmada bir denetim başlatın:

  ```
  chroot /dns /usr/local/sbin/named-checkconf /etc/named.conf
  ```

Özel alanda bir denetim başlatın:

  ```
  cd /dns/var/named; named-checkzone myzone.com zonefile
  ```

Named-in onarımı active eden bir "-d X" seçeneği vardır, (X onarım düzeyini gösteren bir rakamdır), örenğin:

  ```
  /usr/sbin/chroot /dns /usr/local/sbin/named -u named -d3
  ```

Named-i ön planda çalıştırın ve stderr-e itin (yani ekrana):

  ```
  /usr/sbin/chroot /dns /usr/local/sbin/named -u named -g
  ```

name sunucusundan /dns/named/named.stats içindeki istatistikleri elde etmek için:

  ```
  rndc stats
  ```

Eğer loglar izin problemleri belirtirse, dosya izinlerini üretim DNS öncülü [8] üzerindeki "ls -alR"-e karşın kontrol edin.
Eğer ikincildeki alan transferleri gerçekleşmiyorsa:
named kullanıcısının ikincildeki /dns/var/named-e erişim izni olduğundan emin olun. 
Manual alan değişimlerini deneyin:

  ```
  /dns/usr/local/bin/dig @SERVER DOMAIN.NAME axfr
  /dns/usr/local/bin/dig @192.168.128.34 test1.com axfr
  ```

named.conf-taki bir hata sonucu forward only seçeneğinin active edilmediyine emin olun.
chroot'ing-i yaptığınız filesystem-in nosuid oluşturmadığına emin olun, aksi takdirde /dev/zero çalışmayacak.
truss sıradaki program örneği için çok kullanışlıdır:

  ```
  truss /dns/usr/local/sbin/named -u named
  truss /usr/sbin/chroot /dns /usr/local/sbin/named -u named
  ```

IP-Plus tool 4 kullanan alanları kontrol edin.
Eğer chroot-un problem çıkardığını düşünüyorsanız BIND-ı chroot dışında çalıştırın ve onarın. Örneğin:

  ```
  ln -s /dns/var/named /var/named;
  /dns/usr/local/sbin/named -u named -c /dns/etc/named.conf
  ```

built-in BIND chroot özelliğini active eden '-t' seçeneğini kullanın. Bu BIND-in sorunsuz bir şekilde başladığını gösterir, kütüphaneleri yükleyin, bu zaman chroot() kendiliğinden belirecektir. Bu chroot'ing metodu hiçbir kütüphane gerektirmez, daha az /etc dosyaları ve daha az cihaz(/dev/null kafi olabilir). Şimdi, neden daha karmaşık bir kılavuz ile uğraştığımı sora bilirsiniz? Bu kılavuz –t seçeneği var olmadan once kullanılıyordu, bu metod tüm bind sürecini -t seçeneği ise yalnız kütüphane, cihaz ve yuvacıkların bağlanmasından sonraki süreci kapsar.
Aşağıdaki  Bilinen Problemler ve Yapılandırma Notları kesitlerini okuyun.
BIND-kullanıcıları e-posta listesini okuyun.
DNS ve BIND kitabını okuyun.

# Yapılandırma Örnekleri

##Örnek 1: test1.com (basit alan, ters döngü, alan transfer ACL)

* Primary  (bu adreste olduğunu farz ediyoruz 192.168.128.34):

  ```
  Buraya kopyala /dns/var/named:   test1.com, rev.192.168.128
  Buraya kopyala /dns/etc/named.conf: named.conf.primary
  ```

* Secondary (bu adreste olduğunu farz ediyoruz 192.168.128.33):
 
  ```
  Buraya kopyala /dns/etc/named.conf: named.conf.secondary
  ```

##Notlar:

* İkincil başladıktan sonra, secondary.test1.com ve secondary.rev.192.168.128 dosyaları BIND başladıktan sonra otomatik alan transferi tarafından /dns/var/named’de oluşturulmalı. 
* Alan tranferleri sadece öncül, ikincil ISP örneği ve ülkemizin kök alanı ile sınırlandırılmıştır. named.conf’daki cl "nameservers"  ve allow-transfer { nameservers; } bakınız. 
* 192.168.128.33 ve 192.168.128.34 ters döngülerinin çalışması gerek.
* test1.com’daki MX, NS döngüleri, www.test1.com, ns1.test1.com, www1.test1.com çalışması gerek.
* Dinamik güncellemelere izin verilmemektedir.

##Örnek 2: test2.com (Basit ACL ile Dinamik Güncellemeler)

Bu durumda, /dns/var/named/test1.com yapılandırmasını yukarıdaki test2.com-a kopyalıyoruz, fakat alan isimleri değişmek zorunda. Yeni alan dosyası /dns/var/named/test2.com named’e ait olmalı ve tarafından yazıla bilmelidir. 

  ```
  chown named.named /dns/var/named/test2.com;
  chmod 600 /dns/var/named/test2.com
  
  ```

named.conf’ta sadece 192.168.128.33 IP adresinden gelen dinamik güncellemelere izin veren birkaç çizgi eklemeliyiz.
   
    ```
    acl "updaters" {
    192.168.128.33;
    };
    zone "test2.com" {
    type master;
    file "test2.com";
    allow-update { updaters; };
    };
    
    ```
named’i tekrar başlattığımızda, syslog’ta yukarıda seçilmiş yöntemin dinamik güncellemeler için pek de güvenilir olmadığını belirten bir uyarı ile karşılaşacağız. Bir sonraki örneğimiz bunu geliştirme üzerine olacak.

   ```
   /usr/local/sbin/named: zone 'test2.com' IP adreslerinden gelen ve güvenli olmayan güncellemlere izin verir
   
   ```
##Test Etme:
Güncellemeler sadece 192.168.128.33’den alınır ve biz öncülün 192.168.128.34 olduğunu farzediyoruz, o zaman 192.168.128.33’den 'nsupdate' programını çalıştırmak zorundayız. Nsupdate programı bir dosya veya standart girdiden gelen komutaları okur, bu durumda bu örnekte "<<" sembollerini kullanmak durumundayız:
 domain’e "host1" ekliyoruz
  
   ```
   /dns/usr/local/bin/nsupdate <<EOF
   server 192.168.128.34 53
   update add host1.test2.com 3600 A 10.1.1.1

   EOF
   echo $status
   /dns/usr/local/bin/nslookup -sil host1.test2.com 192.168.128.34
   ```
 domain’den "host1"i kaldırıyoruz 
 
   ```
   /dns/usr/local/bin/nsupdate <<EOF
   server 192.168.128.34 53
   update delete host1.test2.com A

   EOF
   echo $status
   /dns/usr/local/bin/nslookup -sil host1.test2.com 192.168.128.34
   ```
 
 İlk önce host’u siliyoruz(eğer varsa), ve tekrar ekliyoruz:
 
   ```
   /dns/usr/local/bin/nsupdate <<EOF
   server 192.168.128.34 53
   update delete host1.test2.com A
   update add host1.test2.com 3600 A 10.1.1.1

   EOF
   echo $status
   /dns/usr/local/bin/nslookup -sil host1.test2.com 192.168.128.34
   ```
 
##Örnek 3: test3.com (TSIG kimlik doğrulama ile dinamik güncellemeler) 

Bir önceki örnekteki dinamik güncellemeler genellikle bir takım IP adreslerinedir (ACL mekanizması üzerinden) ve belli bir alandaki sunucularla haberleşir. Sadece IP adresleri kullanıldığı için bu mekanizma IP kandırmalarına açıktır. BIND ACL listesindeki sunuculara ek kimlik doğrulama izni verir. Her sunucuya özel anahtar ayarlanmıştır ve aralarındaki mesajları imzalamak için kullanılır. Sunucu saatlerinin senkronize olması çok önemlidir. Eğer haberleşme doğru kimlik doğrulama ile yapılmazsa güncellemeler gerçekleşmez.
Bu durumda,/dns/var/named/test2.com yapılandırmasını alan isimlerini değişerek yukarıda test3.com’a kopyalıyoruz. Şimdi güncellemelerde kimlik doğrulama için TSIG kullandığımız bir örneğe göz atalım.
 * a) Paylaşılmış bir sır olarak kullanılacak MD5 anahtarını oluşturuyoruz. "dnssec-keygen" aracı kullanılıyor. Anahtar bir dosyada yazılı.
 
   ```
   /dns/usr/local/sbin/dnssec-keygen -a HMAC-MD5 -b 128 -n HOST updater1

   ```

Sonuç olarak böyle dosyalar yaratılıyor: Kupdater1.+157+08531.key ve Kupdater1.+157+08531.private. Bizi ilgilendiren şey gizli dosyadaki 'Key' girdisi, bu girdi şöyle görünüyor: k2Pb7gEcbXg6ZosOqAbV8A==.
Daha sonra aşğıdakileri buraya ekliyoruz /dns/etc/named.conf:

 ```
 // TSIG keys
 key updater1 { algorithm hmac-md5; secret "k2Pb7gEcbXg6ZosOqAbV8A=="; };
 Ve test3.com için alan tanımına:
 allow-update { key updater1; };

 ```
Güncellemeler test ediliyor:

 ** Olağan bir şekilde domain’e "host1" eklemeye çalışıyoruz: başaramayacağız (öncül log’da "update denied" girdisi ile karşılaşıyoruz), nedeni ise TSIG anahtarını değişmeden güncelleme girşiminde olmamız.

  ```
  /dns/usr/local/bin/nsupdate <<EOF
  server 192.168.128.34 53
  update add host1.test3.com 3600 A 10.1.1.1

  EOF
  echo $status
  ```

 ** Bu sefer kuralına uygun şekilde yapıyoruz – domain’e "host1" ekliyor ve TSIG anahtarını komuta satırına yazıyoruz. 

  ```
  /dns/usr/local/bin/nsupdate -y "updater1:k2Pb7gEcbXg6ZosOqAbV8A=="   <<EOF
  server 192.168.128.34 53
  update add host1.test3.com 3600 A 10.1.1.1

  EOF
  echo $status

  ```
 ** Nsupdate dosya içinde tutulan TSIG anahtarını da kullana bilir, örneğin yukarıda oluşturduğumuz Kupdater1.+157+08531.private.Kupdater1.+157+08531.key dosyası da aynı dizinde ya da PATH’de olmalı.

  ```
  /dns/usr/local/bin/nsupdate -k Kupdater1.+157+08531.private <<EOF
  server 192.168.128.34 53
  update add host1.test3.com 3600 A 10.1.1.1

  EOF
  echo $status
  ```

##Dinamik Güncellemeler İçin Yorumlar, TSIG Güvenirliği ve ACL
* Anahtarın gizli tutulması çok önemli:
     * named.conf ve anahtar dosyalar named ya da nsupdate çalıştıran kullanıcıdan başka kimse tarafından okunamamalı.
     * Anahtar kriptosuz e-postalarla gönderilmemeli
     * Bu anahtarı paylaştığınız kişi kesinlikle güvenilir olmalı: yani sadece ihtiyacı olan kişilere verin, güvenilmeyenlere değil.
     * Anahtarınızı düzenli olarak değiştirin, personel değişiminden sonra veya güvenliğinin tehlikede olduğunu düşünürseniz.
* Eğer iki anasistem aynı alt ağda olursa, IP adres kandırması anahtarın bir kopyasını elde etemekten daha zordur(Örneğin sınır yönlendiricisi kandırılmış adresleri filtrelerse), bu yüzden IP ACL daha kullanışlıdır.
* Eğer hem ACL hem de TSIG anahtarları belirtildiyse, örneğin:
allow-update { key updater1; updaters};
Bu TSIG veya IP ACL güncellemeler için geçerli demektir.
* Aynı anda hem TSIG hem de IP erişim kontrolünü isteyemezsiniz. BIND gelişimcileri bunun yararlı olduöunu düşünmüyor, çünki onların odağı dinamik güncellemeler için ana sistem bazında değil kullanıcı bazında erişim. Buna katılmıyorum, her ikisinin kullanılması birçok durumda kullanışlı ola bilir ve ek güvenlik anlamına gelir, hatta IP ACL-lerin yerel olmayan alt ağlardaki IP adreleri için kandırılması durumunda bile. Rndc erişim kontrolü (aşağıda belirtilmiş) IP ve TSIG erişim kontrole izin verir.
* Dinamik güncellemeler alan adlarını ekleyip kaldıramaz, sadece bunların içindeki girdilere erişebilir.
* BIND sunucusunu güncellemek isteyen müşteri anasistemleri sadece nsupdate ikilisine ve uygun anahtarlara gerek duyar. Diğer ikili veya kütüphaneler gereksizdir.
* Nsupdate-in hata onarım için '-d' seçeneği vardır.
* nsupdate güncellemeler için udp yerine tcp de kullana bilir ('-v' seçeneği), bu güncellemeler çok olduğunda daha iyi bir performans ve tcp bağlantı amaçlı olduğu için daha güvenli ortam sağlar. Ek güvenlik amacıyla tcp bağlantısı kriptolu SSH tünelinden de geçirile bilir (kriptolama ve erişim kontrol).
* Güncelleme poliçesi yeni bir v9 özelliğidir ve sadece bireysel isimler için güncellemelere izin verir. Örneğin ADSL veya DHCP kullanıcısına kendi anasistem ismini güncellemeye izin verir (yani IP adresi deöişe bilir). Güncelleme poliçesi ile ana sistem anahtar listesi düzenlenebilir ve her anahtara sadece ilişkili anasistemi güncelleme izni verilebilir.

#İpuçları

##named.conf ipuçları
named.conf dosyası seçenekler,günlük tutma, ACL, sunucu ve alan kesitlerinden oluşur.Bazı direktifler şöyledir:
* Direktif BIND-e veri dosyaları için nereye bakmasını söyler.
* İnternet erişimi olmayan dahili DNS sunucuları tüm bilinmeyen sorguları forwarders kullanarak internet bağlantılı DNS sunucularına yönlendirir. 
* BIND işlem numarası pid-dosya direktifine uygun olarak depolanır. "named" kullanıcıları bu dosyaya okuma ve yazma erişimine ihtiyaç duyar. 
* BIND'in günlük tutması çok esnektir. Aşağıdaki örnek syslog olanaklarını tutar, sorguları yerel dosyaya tutarken onarır:
    
    ```
    logging {
    channel syslog_errors {syslog daemon; severity info; };
    channel debug_file {file "debuglog"; severity dynamic;};
    category queries {debug_file; };
    };
    
    ```
    
* Gerçek hata onarım günlüklemesini active etmek için (to /dns/var/named/debuglog), rndc ile named şeytan-a talimat verin:
    
    ```
    /dns/usr/local/sbin/rndc querylog
    ```
* Bind 9.5.1-deki huzursuz eden mesajları deaktive etmek için "disabling EDNS":
    
   ```
   category edns-disabled { null; };
   ```
* Eğer "ns_client_replace() hata: yeterli hafıza yok" mesajı alırsanız, herhangi bir "datasize" direktifi yazın.
* "12.66.185.10.in-addr.arpa için internetten RFC 1918 cevabı" uyarısını ala bilirsiniz. Ozaman onları bu türlü adresleri çözebilecek bir sunucuya yönlendirin (1.2.3.4-ü çözücü NS ile değişin):
    
    ```
    zone "10.IN-ADDR.ARPA" {
    type           forward;
    forwarders { 1.2.3.4; };
    forward only;
    }; 
    Veya boş bir alan ekleyin
    zone "10.IN-ADDR.ARPA" {
    type master;
    file "empty";
    };
    "empty" dosyası oluşur:
    @ 10800 IN SOA . . (1 3600 1200 604800 10800 )
    @ 10800 IN NS .
    
    ```
  
Bu 16.172.IN-ADDR.ARPA, 31.172.IN-ADDR.ARPA ve 168.192.IN-ADDR.ARPA için de yapılabilir.
* Erişim control listeleri (ACL-ler) sunucuların alan transferinde izin verdiklerini sınırlamak için kullanılmalıdır. Saldırganların ağ düzeninizin haritasını çıkarmasını zorlaştırmak için bu özelliği kullanmanız tavsiye edilir. Alan adı,sizing ISP ve ülkenizin NIC için izin verilen sunucular özellikle öncül/ikincil olur.  
* BIND-in müşterilere rapor ettiği versiyon numarası (mes. dig)versiyon direktifi ile değiştirile bilir. Bunu ayarlamak basit saldırganların spesifik BIND versiyonlarını(bilinen zayıflıkları ile) gözlemlemesini önlemek için iyi bir fikirdir. Uzak BIND-in versiyon numarasını sorgulamak için deneyin:

  ```
  dig @NAMESERVER version.bind chaos txt
  
  ```
  
* Görüşler: v9-daki yeni enterasan özelliklerden biri sorgu gönderene göre buna farklı şekilde yanıt vere bilmesidir, veya başka bir yolla – DNS namespace kısımlarını gözlemleyen spesifik uzak kullanıcıları kısıtlamasıdır. 
     * Sıradaki görüş ifadesi iki farklı DNS haritası örneğidir, biri dahili öbürü ise internet sorguları için. 
     * Not: öncül ve ikincilde dahili ve harici görüşler ile "split dns" kurmak için beni huzursuz eden iki ayrıntı var: 
** Dahili ve Harici görüşlere açık olan alanlar named.conf-da iki kere tanımlanır, her görüş için birer defa. Bütün alan tanımları görüşlerin içindedir (otomatik "varsayılan" diye bir görüş konsepti yoktur).
** Dahili namespace-i ikincilde istemeden de kolayca yayınlaya bilirsiniz. Problem ise öncülden ikincile transfer edilen alanların ikincilin kaynak adresine bağlı olması ve ikincilin göreceği görüşü belirlemesi.
İkincilin bağımsız dahili ve harici görüş oluşturduğundan emin olmak için:
    * ikincilde başka bir sanal ağ arayüzü daha oluşturun, ikincile bu yeni adresi öncülden gelen harici namespace transferler için kullanmasını söyleyin(transfer-kaynak A.B.C.D) . 
       * Bu yeni ikinci adresin ACL-de olduğuna ve alan trasferlerine izin verdiğine, ayrıca dahili görüş için match-clients-de olmadığına emin olun.
       * Ayrıca hiçbir yerde görünmeyen bu adresin sizin namespace olduğuna emin olun, yani harici veya dahili görüşlerde çözülmemelidir. 
     * Öncül ve ikincilin ilk arayüzlerinin her iki namespace-de çözüldüğüne emin olun.
     * Sıradaki örnek harici alan transferleri için  176.17.17.8 adresini kullandığımızı farzediyor.
   
   ```
   view "internal" {// Bu bizim dahili ağımızla örtüşmelidir.
   match-clients { !176.17.17.8; 10.0.0.0/8; }; // 176.17.17.8 –in dahili görüşten    çıkarılması önemli
   allow-transfer { internal-nameservers; };   
   // Dahili müşteriler için özyinelemeyi açın.
   recursion yes;

   // example.com alanı için bütün görüşü dahili anasistemler
   //-i dahil ederek ayarlayın.
   zone "example.com" {
   type master;
   file "example-internal.db";
   };
   zone "localhost" {
   type master;
   file "localhost.zone";
   notify no;
   allow-update { none; };
   };
   };
   view "external" {
   match-clients { any; };
   // Harici müşteriler için özyinelemeli servisleri reddedin.
   //transfer-kaynak 176.17.17.8; // İkincilde: Ağ arayüzleri
   for Internal ZoneTx
   recursion no;
// example.com alanı için sadece alenen ulaşılan anasistemleri 
// içeren sınırlandırılmış görüş sağlayın.
   zone "example.com" {
   type master;
   file "example-external.db";
   };
   zone "localhost" {
   type master;
   file "localhost.zone";
   notify no;
   allow-update { none; };
   }; 
   };
   
   ```
##rndc Araçalrının Kullanımı

Bind v9 named daemon-u durdurma, başlatma ve yeniden yükleme için rndc aracını kullanır. Bu kısımda rndc, belge problemleri ve kısıtlamaları kullanmayı inceliyoruz.
Bind v8 ndc aracını içerir, peki farkları nelerdir? Peki, rndc (v9) TCP soketlerini (varsayılan 953) ndc'nin (v8) UNIX-domain soketlerine karşın kullanır. Ndc chroot ortamında çalışmaz, rndc çalışır.
* Rndc-nin çalışması için, named rndc girişini dinleyecek şekilde ayarlanmalıdır. Bu girişe erişim kontrolü TSIG anahtarları ile sağlanmaktadır. Bu nedenle bu anahtarlar rndc çalışması için ayarlanmalıdır. O zaman aşağıdaki adımları uygulayarak çalıştıralım:
     *  rndc girişine erişimi sağlamak için yeni paylaşılan anahtar oluşturun:
   ```   
   /dns/usr/local/sbin/dnssec-keygen -a hmac-md5 -b 128 -n user rndc 
   ```
'private' dosyasından anahtarı kopyalıyoruz, buna benzer bir şey 'NsuYsQ0Pp7J3LaOsVHr0uw=='.
     *  Anahtarı buraya ekleyin /dns/etc/named.conf, örneğin:

   ```
   key key_rndc {algorithm hmac-md5; secret "NsuYsQ0Pp7J3LaOsVHr0uw=="; };
   
   ```
     *  Daha sonra named-e rndc girişini dinlemesini söyleyin, öncül'ün IP addresine ve doğru anahtarı isteyenlere cevap verin:
 
   ```
   controls {inet 192.168.128.34  port 953 allow {localhost;} keys {key_rndc;} ; };

   ```
Not: eğer control bölümünü değişirseniz, sunucuyu durdurup tekrar başlatmanızı öneririm, sadece yeniden yükleme veya 'kill -1' yapmayın.
     *	Named-i durdurun, yeniden başlatın (tabii ki, root olarak ve chroot'ed).
  
   ```
   sh /etc/init.d/dns stop
   sh /etc/init.d/dns start
   
   ```

kayıtlarda buna benzer bir mesaj göreceksiniz:
  
     ```
     /usr/local/sbin/named[12993]: command channel listening on 19     2.168.128.34#953
  
     ```
  
     *  Daha sonra /etc/rndc.conf-u uygun anahtar ve adresleri varsayılan sunucuda içermesi için başlatın.
  
   ```
  
   key key_rndc {
   algorithm hmac-md5;
   secret "NsuYsQ0Pp7J3LaOsVHr0uw==";
   };
   options {
   default-server 192.168.128.34; 
   default-key key_rndc; 
   };
   bu dosyayı korurun:
   chmod 600 /etc/rndc.conf
  
   ```
     *	Şimdi bazı testler için hazırız.
* Rndc test ediliyor:
* named sunucu yapılandırmasını yeniden yüklemek için:
  ```  
  /dns/usr/local/sbin/rndc reload

  ```
'rndc: yeniden yükleme başarılı' mesajını göreceksiniz.
* Sadece belirli bir alanı yenileyelim:

   ```  
   /dns/usr/local/sbin/rndc reload test1.com

   ```

* İkincili ustasını güncellemesine zorlayalım :
  
   ```
   /dns/usr/local/sbin/rndc refresh test1.com

   ```

* Bazı istatistikleri buraya yazın  /dns/var/named/named.stats:
  
   ```
   /dns/usr/local/sbin/rndc stats

   ```

* Sorguların tutulmasını + vey a – olarak değişin:
 
   ```
   /dns/usr/local/sbin/rndc querylog

   ```
* DNS önbelleğini bunu kapsaması için yazın /dns/var/named/named_dump.db:
   
   ```
   /dns/usr/local/sbin/rndc dumpdb

   ```
* Erişim kontrolü test ediliyor:
     * Eğer /etc/rndc.conf dosyasını başka bir anasisteme (örneğin ikincil 192.168.128.33-e) kopyalar ve 'rndc yenidne yükleme' çalıştırırsak, şifreli mesajlar alırız 'rndc: connect: dosyanın sonu' (sunucu syslog-ta hiçbir girdi görünmez). Aslında bu mesaj rndc bağlantısının erişiminin engellendiği demektir.
     * O zaman öncül'ün named.conf-a dönüyoruz ve erişim listesini ikincil IP adreslere izin verecek şekilde değişiyoruz:
inet 192.168.128.34 port 953 allow {localhost;192.168.128.33;} keys {key_rndc ;}
     * Şimdi 'rndc yeniden yükleme' ikincil bir anasistemden rahatça çalıştırılacak.


Rndc ile ilgili güzel şeyler:
* Bireysel alanlar yeniden yüklenebilir.
* chroot ortamında çalışır.

Dezavantajlar:
* Several features are planned but not yet implemented:
status: Display ps(1) status of named.
trace: Hata onarım seviyesini 1 kadar artırın.
notrace: Hata onarım seviyesini 0 olarak ayarlayın.
restart: sunucuyu tekrar başlatın.
* Azıcık karmaşıktır, erişim kontrolü için sadece IP adreslerini kullanmak güzel olurdu örneğin, yerel anasisteme erişimi engellemek gibi.
* Erişim control ihlalleri sunucu tarafından tutulmaz.
* Anahtarlar erişim kontrolü için kullanıldığından, /etc/rndc.conf ve named.conf üzerindeki kısıtlayıcı dosya izinleri kritiktir.




