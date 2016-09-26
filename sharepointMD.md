> **İÇİNDEKİLER**

**BÖLÜM 1**

**Sharepoint**

**1-Sharepoint**

> **1-Nedir……………………………………………………………………….3**
>
> **2- Neden Sharepoint?………………………………………………….4**
>
> **3- SharePoint Açıklıkları ve Sıkılaştırılmaları……………….5**
>
> **3.a -[ASP.NET Güvenik
> Açığı](http://www.webhostingturkey.com/post/2010/09/23/ASPNET-Guvenik-Acikligi.aspx)
> ve Sıkılaştırması………………..5**
>
> **3.b- *Microsoft SharePoint ve FAST Arama sunucusu***
>
> ***Oracle Outside In Technology uygulaması açıklıkları ve sıkılaştırma
> adımları…*………………………………………………….6**
>
> ***3.c-* Harden SQL Server in SharePoint Environments…….7**
>
> ***3.*d-Database Hardening For SharePoint 2013…………...17**
>
> ***3.*e- SharePoint Security: Server Hardening……………….19**

**2- SHAREPOINT KURULUMU VE GEREKLİLİKLERİ…………………..24**

**SHAREPOINT**

![](media/image2.png){width="1.5625in" height="1.5625in"}

SharePoint Microsoft Firmasının geliştirmiş olduğu büyük ölçekli
firmaların kullandığı bir programdır. SharePoint genel olarak büyük
ölçekli şirketlerde şirket içerisindeki  farklı farklı depertmanlardaki
elemanların birbirleri ile çok rahat bir şekilde iletişime
geçebilmeşerini sağlayan bir yapıdır. Şirket içerisinde dosya paylaşımı
iletişim kurma vb herşeyi SharePoint sayesinde oturduğunuz yerden
kalkmadan gerçekleştirebilirsiniz.

Örneğin şirketinizin yazılım bölümünde çalışan 5 kişi aynı anda bir
proje geliştiriyorlar. SharePoint olmadan bunu nasıl yapacaklar onu bir
düşünelim. Bir kişi bir bölüm kodu yazacak ve diğer yazılımcıya mail
yolu ile gönderecek. Daha sonra diğer yazılımcı birşeyler daha ekleyecek
programa diğer yazılımcıya gönderecek. Yani çok karmaşık ve zaman
kayıbına sebep olan bir iş. Peki SharePoint sayesinde bu işlemi nasıl
gerçekleştirebiliriz ?. Hemen anlatalım : Projemizi oluşturduk ve
SharePoint üzerinde tuttuk. Yazılımcılardan biri girip projeyinin bir
kısmını geliştirecek ve işi bittiğinde projeyi kapatacak. Sonra diğer
yazılımcı SharePoint havuzundaki projeyi geliştirmeye devam edecek …
Yani daha da basit olarak anlatmak gerekirse : Projemiz bir bulut
üzerinde durmakta ve projeye erişme izni olan kişiler rahatlıkla girip
projeyi geliştirebilmektedir.

         Sharepoint genellikle büyük ölçekli şirketlerde
kullanılmaktadır. Yeni yeni bütün şirketler sistemlerini SharePoint
üzerine taşımaktadır. Fakat SharePoint ‘e taşımak için SharePoint uzmanı
bulmak o  kadarda kolay değildir.

Sharepoint Portal Server uygulaması altı önemli başlık altında
düşünülebilir;

-Bilgi paylaşımı

-Doküman yönetimi

-Gelişmiş arama fonksiyonları

-Form Servisleri

-Excel Servisleri

-BDC(Business Data Catalog)

*SharePoint Portal Server’ın özellikleri**;***

-Versiyon kontrolü

-Workflow sistemi (belgelerin dijital ortamda onaylanması ve
yayınlanması)

-Güvenlik

-İndeksleme ve arama

-Belgelerdeki değişikliklerden haberdar olma

**Neden Sharepoint?**

Microsoft Windows SharePoint Services 3.0 uygulaması, konuya hakim
kararlar almak ve yapılması gerekenleri yapmak için gereken kişilere,
belgelere ve bilgilere kolay erişim sağlayarak ekiplerin bağlı
kalmalarına ve üretken olmalarına yardımcı olur.

Gruplar daha verimli bir biçimde birlikte çalışabilir ve hızlı bir
biçimde siteler ve çalışma alanları kurabilir. SharePoint siteleri,
küçük bir ekipten küresel bir şirkete kadar her boyuttaki kuruluşlara
ölçeklenebilir.

SharePoint yapısının bize sağlayacağı temel avantajlar şunlardır;

· İşin bir bütün olarak tek bir çatı altında toplanması ve
görüntülenmesi.

· Kullanıcıya özel, ilişkili bilgi ve dökümanları biraraya toplayıp
onlara kolayca erişim.

· Bilgi paylaşımını kolay hale getirmek ve bilginin tüm organizasyon
tarafından paylaşılabilmesi

· Organizasyonun bilgi birikimi içinde, gelişmiş arama yöntemleri ile
bilgiyi kolayca bulabilme ve ona erişebilme.

· Portal bünyesinde sayfalar oluturulabilmesi, sayfaların bulunması ve
bir araya toplanabilmesi.

· Konuya özel portal sayfaları oluşturulabilmesi.

· İş süreçlerinin otomatikleştirilmesi.

· Bilgi yönetimi riskini düşürürken içeriği kontrol etme ve tekrar
kullanmayı mümkün kılmak.

· Daha hızlı ve doğru karar vermeye olanak sağlamak.

· Verimliliği arttırmak

· WSS ile hazır portalların kullanımı sayesinde uygulama geliştirme
zamanı ve maliyetini düşürme.

**SharePoint Açıklıkları ve Sıkılaştırılmaları**

**Güvenlik her zaman önemlidir.** Güvenlikle ilgili olan herkes bilir ki
evinizin kapısı kilitli olmasına rağmen eve hırsız girme olasılığı her
zaman vardır. Yani yüz de yüz güvenlik sağlamak her zaman çok da kolay
değil. Sharepoint içinde gerçerlidir bu durum. Aaşağıda 5 madde de
Sharepoint açıklıklarıyla sıkılaştırma adımları üzerine durulmuştur.

1-[***ASP.NET Güvenik
Açığı***](http://www.webhostingturkey.com/post/2010/09/23/ASPNET-Guvenik-Acikligi.aspx)

Microsoft Security Advisory ASP.NET'in tüm version'ları etkileyebilen
bir güvenlik açıklığı. Daha önce belirlenen fakat resmi olarak
tanımlanmamış bu güvenlik açığı ASP.NET'in Cryptography ile ilgili bir
zayıflığından faydalanıyor.

**Nasıl Etkiliyor?**

Açıklık cryptoplojik bilgileri tahmin yolu ile değerlendirip sunucudan
dönen hataya göre doğru değerleri bularak exploid ediyor, bu sayede
viewstate, session ve web.config bilgilerinize okuma, yazma mümkün
olabiliyor.

Açıklık ASO.NET Web Forms, SharePoint ve ASP.NET MVC Framewrok'lerini de
etkiliyor

**Saldırıya maruz kaldığımı nasıl anlarım?**

Açıklık web server sunucusunda HTTP 500 hata kodu oluşturup yorumlayarak
çalışıyor. Bu yorumlamayı yapabilemek için web sunucusuna binlerce http
isteği gönderiyor bu yüzden Web Server loglarında HTTP 500 hata kodunu
gözlemleyip yoğunluğuna göre rahatlıkla tespit etmeniz mümkün. Ayrıca
web suncusunda oluşan hata Windows'un Event Log'una da Application
seviyesinde yazılıyor.

**Açıklıktan Nasıl Korunabilirim?**

Açıklık binlerce http isteği gönderdiğinden bu doğrultuda web suncuusuna
gelen anlık http isteklerini sınırlayabilirsiniz. Örneğin: Bir IP
Adresinden'den 10 saniyede en fazla 50 istek alınabilir şeklinde
firewall kuralı girilebilir. Firewall kuralı girme imkanınız yoksa IIS7
ile blirlikte gelen [Dynamic IP
Restrictions](http://www.iis.net/download/DynamicIPRestrictions)
modülünü de rahatlıkla kullanabilirsiniz.

ASP.NET uygulamalarınızda ki CustomErrors özelliğini aktif etmenizde
resmi bir yama çıkana kadar durumu idare etmenizi sağlayabilir. Tabi
bunu atlayan bir exploid çıkana kadar demek'te gerekiyor ki konu ile
ilgili internet üzerinde henüz yayılmış bir exloid bulunmuyor.

ASP.NET Uygulamalarınızda CustomErrors'u aktif etmek için web.config
dosyanızı aşağıdaki şekilde düzenlemenzi yeterlidir.

&lt;configuration&gt;\
\
   &lt;system.web&gt;\
\
     &lt;customErrors mode="On" redirectMode="ResponseRewrite"
defaultRedirect="\~/error.aspx" /&gt;\
\
   &lt;/system.web&gt;\
\
&lt;/configuration&gt;

*\* Burda önemli olan redirectMode özelliğinin ResponseRewrite
olmasıdır.*

***2.* *Microsoft SharePoint ve FAST Arama sunucusu Oracle Outside In
Technology uygulamasından birden fazla açıklık tespit edilmiştir.***

**Kaynak:** Securelist

*Seviye:* Yüksek

*Açıklama zamanı:* 25.07.2012

*Etkilenen Sistemler:* Microsoft SharePoint Server için FAST Search
Server 2010 eklentisi

*CVE*: CVE-2012-1766 CVE-2012-1767 CVE-2012-1768 CVE-2012-1769
CVE-2012-1770 CVE-2012-1771 CVE-2012-1772 CVE-2012-1773 CVE-2012-3106
CVE-2012-3107 CVE-2012-3108 CVE-2012-3109 CVE-2012-3110

*Referanlar*:

Securelist:\
[*http://www.securelist.com/en/advisories/50049*](http://www.securelist.com/en/advisories/50049)\
Microsoft: -2\
[*http://technet.microsoft.com/en-us/security/advisory/2737111*](http://technet.microsoft.com/en-us/security/advisory/2737111)

Açıklama: Microsoft SharePoint Server ve SharePoint için FAST Arama
Sunucusu 2010 eklentisinde birden fazla açıklık tespit edilmiştir. Bu
açıklıkları suistimal eden kullanıcıların sistemi servis dışı bırakması
ve ele geçirmesinin mümkün olabileceği bildirilmiştir.\
Açıklığın gerçeklenebilmesi için Advanced Filter Pack kurulu FAST arama
eklentisinin aktif olması gerekmektedir. Bu ayar öntanımlı olarak kapalı
(disabled) gelmektedir.

*Etki:* Yetkisiz erişim ve servis dışı bırakma

*Çözüm:* Microsoft bu sorunu gidermek için aşağıdaki güvenlik
güncelleştirmelerini yayınladı:

• Microsoft Security Bulletin MS12-058 addresses this issue for
Microsoft Exchange.

• Microsoft Security Bulletin MS12-067 addresses this issue for
Microsoft FAST Search Server 2010 for SharePoint.

**3. Harden SQL Server in SharePoint Environments**

Sharepointte hassas veriler saklanır. Sql serverın güvenliği bu amaçla
çok önemli. Bu riski azaltmak içinde SQL Server için 3 adımda
hardenining yapılmış. Bu adımlar şu şekilde:

1.Encryption at Rest (sabit diskler üzerinde oturan verileri şifreleme)

2.Encrypt Connections (sunucular arasında ağ üzerinde uçuş verileri
şifreleme)

3.Server Isolation (Yapılandırma SQL Server'ın güvenlik duvarı yetkisiz
sunucularından gelen istekleri görmezden gelmek)

Not: Bu adımlar, tek bir sunucu örneği üzerinde yapılır.

**Encryption at Rest:***\
\
*Encryption at Rest:Şeffaf Veri Şifreleme (TDE) üzerinden
gerçekleştirilir. TDE raw veritabanı MDF / LDF dosyaları sayfa düzeyinde
şifreleme yapmak için bir sunucu düzeyinde sertifikası kullanır. TDE bir
sertifika şeklinde ana veritabanında saklanan bir simetrik anahtar
kullanır (veya EKM modülünde saklanan bir asimetrik anahtar, ama bu
tartışmanın kapsamı dışındadır). Veri AES veya 3DES ile şifrelenir ve
özgün sertifika veritabanına erişmek için gereklidir.\
\
Yüksek bir düzeyde, TDE sabit diskler veya yedekleri tehlikeye /
çalınması durumunda bizi korur; S. Kullanıcılar kavramlara alışık
değilseniz, TDE mantığı BitLocker mantığına benzer.

*Kurulumu:*

TDE 2 fazda dağıtılır: Örneği(instance) ve Veritabanı Yapılandırması.
Örnek yapılandırma sadece örnek başına bir kez yapılır, ancak veritabanı
yapılandırması her veritabanı için tekrar edilmesi gerekir\
Örnek(instance) yapılandırma:\
Bir ana anahtarı oluşturun (ve parola!)

USE\
\[master\]

GO

CREATE\
MASTER\
KEY\
ENCRYPTION\
BY\
PASSWORD=‘P@\$\$w0rd’

GO

 Master key ile korunan sertifika yarat:

USE\
\[master\]

CREATE\
CERTIFICATE\
TDECertificate\
WITH\
SUBJECT\
=\
‘TDE Certificate’

GO 

*Veri tabanı Konfigürasyonu:*

Sertifika adını al

SELECT\
name,pvt\_key\_encryption\_type\_desc\
FROM\
sys.certificates

GO

 

![](media/image3.png){width="3.75in" height="1.3541666666666667in"}

Veritabanı Şifreleme Anahtarını oluşturun önceki adımda sertifika adını
kullanarak

USE\
\[Test\]

GO

CREATE\
DATABASE\
ENCRYPTION\
KEY\
WITH\
ALGORITHM\
=\
AES\_256

ENCRYPTION\
BY\
SERVER\
CERTIFICATE\
TDECertificate

GO

 Şifreleme kullanmak için Veritabanı ayarlayın

USE\
\[master\]

ALTER\
DATABASE\
\[Test\]\
SET\
ENCRYPTION\
ON

*Yedekleme Sertifika:*\
Sen başka bir sunucuya DB geri sertifika gerekir. Geri hem dosyalarınızı
yedekleyin ve Şifreleme şifre kaydetmek yere sabitleyin!

BACKUP\
CERTIFICATE\
TDECertificate

TO\
FILE\
=\
‘C:\\TDECertificate.cert’

WITH\
PRIVATE\
KEY ( FILE\
=\
‘C:\\TDECertPrivateKey.key’,\
ENCRYPTION\
BY\
PASSWORD\
= ‘P@\$\$w0rd1234’)

GO

Test:

yedek veritabanı

BACKUP\
DATABASE\
\[Test\]

TO\
DISK=‘C:\\Test.bak’

GO

Dosya başka bir örneği (Örnek B) kopyalamak ve geri deneyin

RESTORE\
DATABASE\
\[Test\]

FROM\
DISK=‘C:\\Test.bak’

GO

Bu benzer bir iletisiyle başarısız olur

Msg 33111, Level 16, State 3, Line 1\
Cannot find server certificate with thumbprint ‘…….’.\
Msg 3013, Level 16, State 1, Line 1\
RESTORE DATABASE is terminating abnormally.

Başarı! Kullanıcılar keyfi sunucudan geçerli sertifika ve şifreleme
şifre olmadan veritabanını geri alamaz.

USE\
master

CREATE\
CERTIFICATE\
TDECertificate

FROM\
FILE\
=\
‘C:\\TDECertificate.cert’

WITH\
PRIVATE\
KEY (FILE =\
‘C:\\TDECertPrivateKey.key’,

DECRYPTION\
BY\
PASSWORD\
=\
‘P@\$\$w0rd1234’)

GO

Örnek B veritabanını geri yüklemek deneyin

RESTORE\
DATABASE\
\[Test\]

FROM\
DISK=‘C:\\Test.bak’

GO

Bu bizim TDE kurulumunu tamamlar ve disklerdeki bizim verileri şifreler.
Biz şimdi izni olmadan diskleri ve / veya veritabanı yedekleri kapma
bireylerin korunmasını garanti ediyoruz.

*Sıkıştırma hakkında Not:* Sıkıştırma uygulanabilir dosyanın ikili
biçimde desenleri bulma ve daha küçük bir desen onları dönüştürerek
yapılır (örneğin, '12345' 'a' ile temsil edilir). Şifreleme ham veride
desenler kaba kuvvet şifre çözme önlemek için kaldırır.

**Bağlantı Şifreleme**\
\
Bağlantıları Şifreleme Secure Socket Layer (SSL) üzerinden
gerçekleştirilir. SSL sunucu özgünlüğünü doğrulamak ve sunucular
arasında değiş tokuş verileri şifrelemek için bir sertifika değişim
sürecini kullanır.\
\
SSL sunucuları arasında iletilen bilgiyi şifreleyerek çevreyi korur.
Kötü niyetli bir kullanıcının Ağ dinleme ile (Netmon, WireShark ya da
benzer bir araç) keşfe çalışırsa, tüm veriler şifrelenir olacak ve
kullanıcı elde ettiği veriler anlamsız olacak.

**Kurulumu:**

Not: Bu örneklerde zaten uygulanabilir bir sunucu sertifikası dağıtılmış
varsayılır. VM kendinden imzalı sertifika kullanır; Tam üretim
yapılandırma 3. taraf güvenilir yetkisini kullanmalıdır.

1.  Sql Server Configuration Manager ‘I aç

2.  SQL Server Network Configuration’I genişlet

3.  *Protocols for &lt;Instance Name&gt;üzerine sağa tıkla* ve
    *Properties* ‘I seç

![](media/image4.png){width="3.8333333333333335in"
height="2.0208333333333335in"}

 

1.  *Force Encryption*’u *Yes* olarak değiştir.

![](media/image5.png){width="2.7916666666666665in"
height="3.1145833333333335in"}

 

1.  *Certificates* tab’I nı aç ve kendi sertifikanı seç
    ![](media/image6.png){width="2.7708333333333335in"
    height="3.1145833333333335in"}

 

1.  OK’e bas ve Sql server’I yeniden başlat

2.  Tamam

 

Test:

1.  Aşağıdaki komut çalıştırılır ve Encrypt\_Option seçeneği TRUE
    olarak ayarlanır.

SELECT\
net\_transport, auth\_scheme, encrypt\_option

FROM\
sys.dm\_exec\_connections

WHERE\
session\_id\
=\
@@SPID;

  Not: NTLM / Kerberos üzerinden SQL Server kimlik doğrulaması DAİMA
şifrelenir. Ama şifreleme sonra işlemlerde açık metin vardır.

**Sunucu İzolasyonu**\
\
Sunucu İzolasyon birkaç farklı şekilde yapılabilir, ancak sonuç aynıdır:
"Yetkili makine" bir yönetim organı (genellikle güvenlik ekibi ya da ağ
ekibi) tarafından kontrol edilen bir listesidir. SQL izole etmek en
basit ve en maliyet etkin yolu Gelişmiş Güvenlik Özellikli Windows
Güvenlik Duvarı yapılandırmasdır. Diğer yöntemler (VLAN, vb diğer
Firewall ürünleri,) mevcuttur.\
\
SQL izole ederek, ağ erişimi ötesinde ek bir güvenlik katmanı
zorlanarak, SQL server attackable alanını azaltır.

Kurulumu
--------

Not: Bu örneklerde, yerel makinenin güvenlik duvarını yapılandırır.
Windows Güvenlik Duvarı Grup İlkesi aracılığıyla yapılandırılabilir

1.Yönetimsel Araçlar Gelişmiş Güvenlik Özellikli Windows Güvenlik
Duvarı\
2. Bir kural ile eşleşmiyor Gelen Bağlantıları engelleniyor

![](media/image7.png){width="2.1979166666666665in" height="2.3125in"}

>  

1.  ***Inbound Rules ve New Rule’u seçin ***

2.  ***Rule Type*** ‘da ***Program***’I seç ve ***Next*** ile ilerle

3.  SQL Server EXE’I seç ve ***Next*** ile ilerle

    1.  Default path C:\\Program Files\\Microsoft SQL
        Server\\&lt;Instance Name&gt;\\MSSQL\\Binn\\sqlservr.exe

4.  ***Allow the Connection***’I seç ve ***Next*** ile ilerle

5.  3 domain types seç ve Next ile ilerle

6.  ***Finish***

7.  Yeni yarattığın kuralı seç ve ***Properties***’I seç

> ![](media/image8.png){width="3.3645833333333335in"
> height="4.010416666666667in"}
>
>  

1.  Test properties window’nda , ***Scope*** tab’I seç ve ***Remote IP
    Address*** ‘yi ***These IP Addresses*** olarak yaz.

> ![](media/image9.png){width="2.46875in" height="3.2708333333333335in"}
>
>  

1.  ***Add***’e bas and SharePoint Farm tüm IP adreslerini ekle

> ![](media/image10.png){width="2.4791666666666665in"
> height="3.28125in"}
>
>  

1.  OK tuşuna bas sayfayı kapat

### Test:

> 1.yetkili bir makine, açık SQL Server Management Studio ‘ya bağlanmayı
> deneyin. Bu başarılı olmalı.
>
> 2\. yetkisiz makinesi ,açık SQL Server Management Studio'yu bağlanmayı
> deneyin. Bu başarısız olmalıdır.![](media/image11.png){width="4.75in"
> height="1.6145833333333333in"} 
>
> Özet:\
> \
> \
> SQL Server'ın güvenlik SharePoint bilgi hassasiyetini eşleşmesi
> gerekir.Bu yapılanlarla sunucu performansı yük testleri +/-% 15
> performans düşüşü gösterdi. Birincil endişe eğer güvenlik ise tamam.
> **Bu üç aşamalı bir yaklaşım uygulanması önemli ölçüde istenmeyen veri
> erişimi için SQL'ın açığı azaltacaktır.**
>
> ***4.** **Database Hardening For SharePoint 2013***
>
> Bu kısımda, SQL Server iletişimi için kullanılan varsayılan bağlantı
> noktalarını engelleme ve SharePoint 2013, bunun yerine bu iletişim
> için özel bağlantı noktaları kurarak bir çiftlikte sunucular
> arasındaki iletişimin güvenliğini açıklar.
>
> SharePoint 2013 anahtarı için, SQL Server iletişimi için kullanılan
> varsayılan bağlantı noktalarını engelleme ve bunun yerine bu iletişim
> için özel bağlantı noktaları kurarak bir çiftlikte sunucular arasında
> iletişimi sağlamaktır. Hizmetleri için, veritabanı sunucuları
> tarafından gerekli olmayan herhangi bir hizmetini devre dışı bırakarak
> saldırı yüzey alanını azaltmak önemlidir.
>
> **Port ve Protokoller**
>
> Sharepoint yapılandırması ve servisleri için bazı port ve protokoller
> tanımlanmıştır. Bu tanımlamalar iyi güvenlik için modifiye
> edilmelidir.
>
> **Port ve Protokol Yapılandırma**\
> \
> Sunucular SharePoint 2013 çiftliğinde birbirleriyle iletişim kurmak
> için kullandıkları bağlantı noktaları güvenli olmalıdır. Farklı
> SharePoint sunucusu rolleri birbirleriyle iletişim kurmak için farklı
> bağlantı noktalarını kullanır.
>
> **Hizmet Uygulama İletişim Güvenliğini\
> \
> **Bir çiftlik ortamında web sunucuları ve hizmet uygulamalar arasında
> haberleşme varsayılan olarak aşağıdaki bağlantı noktalarını ve
> protokol bağlamaları kullanın:\
> • HTTP: TCP 32843 (HTTP varsayılan bağlayıcıdır)\
> • HTTPS: TCP 32844 (SSL)\
> • Net.tcp: TCP 32845 (bir üçüncü taraf geliştiricisi hizmet uygulaması
> için bu uygulamaya koydu ise)
>
> **Web Sunucusu İletişimi Güvenliğini**\
> \
> Aşağıdaki bir çiftlikte SharePoint web sunucuları tarafından
> kullanılan varsayılan port:\
> • HTTP: TCP 80\
> • HTTPS: TCP 443 (SSL)\
> \
> **Veritabanı Sunucusu İletişimi Güvenliğini**\
> \
> aşağıdaki SQL Server iletişimi için kullanılan varsayılan portlar:\
> • TCP 1433 (varsayılan)\
> • UDP 1434 (adlandırılmış örnekleri listesi için sunucusunu sorgulamak
> için kullanılır)\
> \
> SQL Server bilgisayardaki TCP 1433 portunu engelleyebilir ve yerine
> adlandırılmış örneğine bağlanmak için bir SQL Server istemci ad
> yapılandırmak için en iyi yöntemdir.
>
> **Arama Sunucusu İletişimi Güvenliğini**\
> \
> Aşağıdaki bir çiftlik içinde SharePoint Arama indeksleme bileşenleri
> tarafından kullanılan varsayılan portlar:\
> • TCP: dahil 16.500-16.519\
> \
> **Active Directory İletişim Güvenliğini**\
> \
> Varsayılan bağlantı noktaları Forefront Kimlik Yönetimi (FIM) ajanı
> çalıştıran sunucuda SharePoint 2013 ve Active Directory Etki Alanı
> Hizmetleri (AD DS) arasındaki kullanıcı profillerini eşitlemek için
> kullanılan portlar:\
> • TCP ve UDP: 389 (LDAP hizmeti)\
> • TCP ve UDP: 88 (Kerberos)\
> • TCP ve UDP: 53 (DNS)\
> • UDP 464: (Kerberos Parolayı Değiştir)\
> • TCP 5725: (FIM)
>
> **Harici Sunucu İletişimi Güvenliğini**\
> \
> Çiftlik harici sunucularda verilere erişmek için yapılandırılabilir
> bazı SharePoint 2013 özellikleri vardır. Bu senaryolarda, iletişim
> kanalları, yerel sunucu ve uzak sunucu arasında açık olmasını sağlamak
> gerekir. Tipik olarak, Office Web Uygulamaları ve İş Akışı Yöneticisi
> Liman hususlar bağlıdır kullanılan bağlantı noktaları ve protokolleri.
> Office Web Uygulamaları Server düzenli bu bağlantı noktalarında web
> uygulamaları kaldırır çünkü, Office Web Uygulamaları Server çalıştıran
> herhangi bir sunucuda aşağıdaki bağlantı noktalarını engellemek
> gerekir:
>
> -HTTPS trafiğini Limanı 443.\
> -HTTP trafiği için Port 80\
> -Office Web Uygulamaları Server çalışan sunucular arasında özel
> trafiği için bağlantı noktası 809 (Multi-sunucu grubundaki)\
> \
> Ayrıca bunlar da kullanılabilir olduğundan emin olmak için İş Akışı
> Yöneticisi tarafından kullanılan bağlantı noktalarını görmek için IIS
> Yöneticisi gözden geçirmelidir.
>
> **Yapılandırma Bağlantı Noktaları**\
> \
> Yapılandırmak ve açmak için SharePoint 2013, önceden tanımlanmış gelen
> ve giden kurallar otomatik olarak oluşturulur yüklediğinizde Gelişmiş
> Güvenlik Özellikli Windows Güvenlik Duvarı kullanıyorsanız, ancak
> SharePoint 2013 için bağlantı noktalarını ve protokolleri
> yapılandırmak için kullanabileceğiniz çeşitli araçlar ve teknolojiler
> vardır.
>
> ***5. SharePoint Security: Server Hardening***
>
> Güvenlik adımlarından bir taneside parolalardır.

*Güçlü parola ne demektir, nasıl oluşturulur? *

> Oluşturulan bir parolanın "güçlü" kabul edilebilmesi için aşağıdaki
> özellikleri göstermelidir.  En az 8 karakterden oluşur.  Harflerin
> yanı sıra, rakam ve "?, @, !, \#, %, +, -, \*, %" gibi özel
> karakterler içerir.  Büyük ve küçük harfler bir arada kullanılır.
>
> Bu kurallara uygun parola oluştururken genelde yapılan hatalardan
> dolayı saldırganların ilk olarak denedikleri parolalar vardır. Bu
> nedenle parola oluştururken aşağıdaki önerileri de dikkate almak
> gerekir. Kişisel bilgiler gibi kolay tahmin edilebilecek bilgiler
> parola olarak kullanılmamalıdır. (Örneğin doğum tarihiniz, çocuğunuzun
> adı, soyadınız, … gibi) Sözlükte bulunabilen kelimeler parola olarak
> kullanılmamalıdır.  Çoğu kişinin kullanabildiği aynı veya çok benzer
> yöntem ile geliştirilmiş parolalar kullanılmamalıdır.

*Parolamızı korumak için ne yapmalıyız ? *

Kağıt ya da elektronik, harhangi bir ortamda açıkça yazılmış olarak
bulundurulmamalıdır. Yazılı bulundurulması gerektiğinde saklanan ortamın
güvenliği sağlanmalı ve parolalar kilit altında saklanmalıdır.

 Farklı sistemlerde farklı parola kullanılması olası riskleri
azaltacaktır.

 Parolalar belirli aralıklarla değiştirilmelidir.

 Antivirüs yazılımları güncel tutulmalıdır.

 Parola girilirken başkaları tarafından görülmediğine emin olunmalıdır.
 Bilgisayarınıza ve/veya işletim sistemine şifre tanımlamalı

 Bilgisayarınızın başından kalkarken mutlaka oturumunuzu kilitlemeli ve
şifreli ekran koruyucu özelliği kullanılmalı

 Uzaktan erişimleri engellemek için, işletim sistemi ve anti-virüs
yazılımları güncel tutulmalı ve güvenlik duvarı yapılandırılmalıdır.

> **\
> Hesap Güvenliği**\
> \
> Eğer saldırganlara karşı SharePoint çiftlik sertleşmesine için
> yapabileceğiniz ilk şeylerden biri yüklemek ve en az ayrıcalık
> yaklaşımı ile yapılandırma yapmaktır.\
> \
> Bu sayede saldırgan sadece küçük bir ayak izi erişimine sahip
> olacaktır. Saldırgaın Makinenin tamamını devralması mümkün
> olmayacaktır muhtemelen sunucu üzerinde sınırlı izinlere sahip
> olacaktır.\
> \
> Sık sık hizmet hesabı parolalarını değiştirme - her üç aydan altı aya
> - SharePoint çiftlik daha güvenli hale getirmek için iyi bir yoldur.\
> \
> **Makine Güvenliği**\
> \
> Windows Microsoft IIS, SQL Server ve Active Directory (AD) de dahil
> olmak üzere - - SharePoint karakter büyük döküm gerektirir. Bu
> karakterleri önemli olmakla birlikte, bunlardan herhangi biri ile
> güvenlik sorunları SharePoint grubu için felaket olabilir. Bu parçalar
> güvenli tutmak çok iyi bir SharePoint yönetici işinin bir parçasıdır.\
> \
> Ne yazık ki, Windows Update ayarlama ve daha sonra walking away kadar
> kolay değildir. Windows Update sunucuları güncellenen tutmanın önemli
> bir parçasıdır, ancak SharePoint sunucuları ile kullanırken dikkatli
> olmak gerekir.\
> \
> Güvenli ve operasyonel SharePoint altyapısı tutmak için, Windows
> Update gerekir, ayrıca zamanda her yama araştırma konusunda bilgili
> olmak gerekir. Örneğin, SQL Server yama önce, yama olumsuz SharePoint
> etkilememesinden emin olunmalıdır. Yama bir sunucu sertleştirmenin
> önemli bir parçasıdır ancak dikkate alınarak yapılmalıdır.\
> \
> İyi bir yama sürecinin bir parçası test ortamıDIR. Test ortamı tam
> olarak üretim ortamını yansıtmasa da, mümkün olduğunca yakın
> olmalıdır: Aynı Windows sürümünü kullanılmalıdır, SharePoint aynı
> sürümünü kullanılmalı ve mümkün olduğunca üretim ortamı gibi olması
> için test ortamı yapılandırılmalıdır.\
> \
> SharePoint her ay toplu güncelleştirmeleri alır. Bu güncellemeler
> genellikle hata düzeltmeleri, güvenlik düzeltmeleri vardır. Bir
> güvenlik sorununa SharePoint ile yaşıyorsanız belirli bir sorunu
> çözmek bu yamaları yükleyin.\
> \
> \
> \
> \
> Güvenli SharePoint sunucusu tutmak için başka bir yolu, SharePoint
> kullanmıyor bağlantı noktalarını bloke edilmelidir. Bunu yapmak
> rastgele sunucunuzu nüfuz için kullanılabilir yararlanma olasılığını
> azaltır. Tablo 1 SharePoint sunucuları kullanmak yaygın gelen
> limanlarından bazılarını gösterir.
>
> **Table 1: Commonly Used Inbound Ports **

  > **Port**                                                                                > **SharePoint Purpose**
  ----------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------
  > TCP 80, TCP 443, central admin port and any custom ports on which you publish content   > Web connections
  > TCP 32843, TCP 32844, TCP 32845                                                         > Communication to service applications
  > TCP 32846                                                                               > Used by the User Code service (sandbox solutions)
  > TCP/UDP 445, TCP 137, UDP 138, TCP/UDP 139                                              > File and print services, used by Search
  > TCP/UDP 88, UDP 464                                                                     > Needed if Kerberos authentication is used by SharePoint
  > TCP 5725, TCP/UDP 389, TCP/UDP 88, TCP/UDP 53, UDP 464                                  > Used by User Profile service application
  > UDP 1434, TCP 1433                                                                      > Default ports for SQL Server; consider running on nonstandard ports and blocking the default ports
  > TCP 25                                                                                  > SMTP if incoming email is in use
  > TCP 3389                                                                                > RDP if that's being used to access the server

> Ref:
> [*http://sharepointpromag.com/sharepoint-2010/sharepoint-security-server-hardening*](http://sharepointpromag.com/sharepoint-2010/sharepoint-security-server-hardening)
>
> Windows 2008 ve Windows 2008 R2 SharePoint sunucusunda Windows
> bölümünü kilitlemek yardımcı olabilecek bir Güvenlik Yapılandırma
> Sihirbazı (SCW) içerir. Yönetimsel Araçlar altında veya Sunucu
> Yöneticisi SCW bir bağlantı bulabilirsiniz. SCW sunucu
> gerçekleştiriyor hangi rolleri ve kullanıyor hangi bağlantı
> noktalarını belirleme sürecinde size yol gösterir.\
> \
> SharePoint yüklü ve yapılandırılmış sonra SCW'yi çalıştırın. SCW
> çalışmasını bitirdiğinde, o size sunucusu için geçerli olabilir bir
> güvenlik profili verir. Bu sunucu kilitlenir, ama dikkatli olmak için
> nispeten kolay bir yoludur: Çok sıkı bir şekilde kilitleyebilirsiniz.\
> \
> SCW'yi kullanmamayı seçerseniz, SharePoint sunucuları uygun gelen ve
> giden bağlantı noktaları açık olduğundan emin olun.\
> \
> Eğer bir seviye ağ güvenliğini almak istiyorsanız, sunucular ve son
> kullanıcılar arasında bir ters proxy tanıtılabilir.Ters proxy (veya
> başka bir ağ aygıtı) aynı zamanda kötü niyetli olup olmadığını
> belirlemeye yardımcı olmak için, gelip istekleri daha karmaşık tarama
> gerçekleştirmek mümkün olabilir. Bu gereksiz görünebilir rağmen,
> SharePoint ortamı daha güvenli hale getirebilirsiniz ve SharePoint
> sunucuları kapalı bazı hesaplama yükünü alabilir.\
> hesap Güvenliği\
> \
> Eğer saldırganlara karşı SharePoint çiftlik sertleşmesine için
> yapabileceğiniz ilk şeylerden biri yüklemek ve en az ayrıcalık
> yaklaşımı ile yapılandırmak için olduğunu. SharePoint kendi hesabını
> yapar, her fonksiyon vermek ve her işini yapması gereken tek izinleri
> hesap vermek - başka bir şey.\
> \
> hesabı tehlikeye eğer bu şekilde, saldırgan sadece küçük bir ayak izi
> erişimine sahip olacaktır. (Başlamak için, SharePoint hizmet hesapları
> benim blog yazısı okudum.) Burada başlattığınızda, süreçleri iyi
> izolasyonu olacak; Herhangi hesaplar tehlikeye eğer, hasar
> bulunabilir. senin sp\_serviceapps kesmek hesabı Örneğin, saldırgan
> Makinenin tamamını devralması mümkün olmayacaktır muhtemelen sunucu
> üzerinde sınırlı izinlere sahip olacak ve.\
> \
> Bu yöntem, her şey için bir hesap kullanarak daha az uygundur, ama iyi
> bir güvenlik sınırlarını içerir. en küçük ayrıcalık yaklaşımı gelen
> büyük rahatsızlık tüm bu belâ şifreleri takip edilir.\
> \
> Eğer daha önce bahsettiğim blog yazısı izlerseniz, dokuz şifreleri
> anlamına dokuz hesapları ile başlayacağız. böylece, word1 @ geçmesi
> WORD2 @ geçmek değildir ve dokuz şifreleri ile geliyor yeterince
> zordur, ama sonra bunları değiştirmeniz gerekir. (Tabii ki, sık sık
> hizmet hesabı parolalarını değiştirme - her üç aydan altı aya -
> SharePoint çiftlik daha güvenli hale getirmek için iyi bir yoldur.)\
> \
> Ben parola üretimi ile çok yardımcı olamaz rağmen, ben değişim
> sürecinde yardımcı olabilir. Başka bir blog yazısı, ben hesapları ve
> nasıl en az kesinti ile her parolayı değiştirmek için her yürümek.\
> \
> genel idari görevleri yaparken Çiftliği hesabı olarak oturum Dur: Biz
> hesaplardan hareket etmeden önce, sisteminizi daha güvenli hale
> getirmek için yapabileceğiniz başka bir şey var. Hepimizin içine almak
> kötü bir alışkanlık var, ama bu saldırı bizim SharePoint çiftlikleri
> açılır.\
> \
> Biz gün-gün yönetici faaliyetleri yapmak, biz orada olan patlatır
> herhangi bir sayıda vurma riski vardır. normal bir kullanıcı olarak bu
> patlatır Koşu yeterince kötü; SharePoint yükseltilmiş ayrıcalıklarla
> bir kullanıcı olarak çalışan daha da kötüdür. Ayrıca, denetim
> zorlaştırır. Bunun yerine, her bir SharePoint sunucusu yöneticisi
> grubundaki görevleri yerine kullanılacak ayrıcalıklı bir hesap
> olmalıdır.\
> \
> Ne yazık ki, SharePoint hesabı izinleri yönetimi için sağlanmalıdır
> çok küçük yerler vardır. (Benim blog bu yaklaşımın tam yol tarifi
> alabilirsiniz.)\
> \
> **Antivirüs Yazılımı**\
> \
> Güvenli Windows sunucu koruma konusunda antivirüs gereklidir.
> SharePoint bağlamda, iki kez bu konuyu konuşmak gerekir. Bir kez
> sunucu için ve bir kez SharePoint içerik için.\
> \
> Makine antivirüs hakkında konuşmaya başlayalım. Bu hepimiz Windows
> PC'ler ve sunucular üzerindeki antivirüs yazılımıdır. Genellikle bir
> işletme düzeyinde yönetilen ve tüm SharePoint sunucuları üzerinde
> çalıştırıyor olmalıdır.\
> \
> Bir SharePoint sunucusunda dosya sistemi antivirüs çalıştırdığınızda
> Ancak, taramaları bazı SharePoint dizinleri ayırmak için önemlidir.\
> \
> Antivirüs yazılımı ikinci yönü de yüklenen ve indirilen gibi
> dokümanları taramak için SharePoint sunucuları üzerinde
> çalıştırabilirsiniz SharePoint ile uyumlu virüsten koruma yazılımıdır.
> SharePoint kendisi antivirüs yazılımı ile gelmiyor.\
> \
> Özet:
>
> Güvenlik SharePoint birçok köşelerine uzanan, geniş bir konudur. Bu
> kısımda, portları kilitleyerek hizmet hesaplarını güvence ve virüsten
> koruma yazılımı çalıştırarak, SharePoint sunucuları daha güvenli hale
> getirmenin bazı yolları anlatılmıştır. (Microsoft makale "Plan
> Güvenlik Artırma (2010 SharePoint Foundation" ek ayrıntılar sunuyor.)
>
> **SHAREPOINT KURULUMU VE GEREKLİLİKLERİ**

[SharePoint](http://www.mshowto.org/tag/sharepoint) kurulumu ilk bakışta
basit gibi görünse de kurulumdan önce dikkatle planlanması gereken bazı
adımlar var.

Bunlardan en önemlileri kapasite planlama ve ön gereklileri bu yazıda
inceleyeceğiz.

Ön gereklilikleri aşağıdaki alt başlıklarda gruplayabiliriz.

1.  Donanımsal Gereksinimler

2.  Yazılımsal Gereksinimler

3.  Tarayıcı Desteği

4.  Kurulum gereksinimleri

**1- [SharePoint 2013](http://www.mshowto.org/tag/sharepoint-2013)
Donanımsal Gereksinimler:**

SharePoint 2013 Farm yapısı önceki versiyonda olduğu gibi 3 rolde
inceleniyor bunlar:

1.  **Web sunucusu rolü:** Web sayfalarını, web servislerini ve web
    bölümlerini sunar-çalıştırır, IIS te bu sunucuda yer alır.

2.  **Uygulama sunucusu rolü:** Central Administration’nın ve web
    servislerinin üzerinde çalıştığı sunucu rolü.

3.  **Veri tabanı sunucusu rolü:**
    [Microsoft](http://www.mshowto.org/tag/microsoft) SQL
    [Server](http://www.mshowto.org/tag/server) ve veri tabanlarının
    üzerinde barındığı sunucu rolü.

Bu roller kapasite planlamasının gerekliliklerine göre farklı altyapı
mimarileri ile kurulabiliyorlar, sık kullanılan topolojileri aşağıdaki
tabloda anlatmaya çalıştım.

![](media/image12.png){width="6.0in" height="9.625in"}\
**Resim-1**

SharePoint 2013’de Web ve Uygulama sunucuları için minimum donanımsal
gereksinimler aşağıdaki gibi:

![](media/image13.png){width="4.875in" height="1.1979166666666667in"}\
**Resim-2**

Database sunucusu için ise:

![](media/image14.png){width="4.875in" height="1.1979166666666667in"}\
**Resim-3**

**2- SharePoint 2013 Yazılımsal Gereksinimler:**

Yazılımsal gereksinimleri yine sunucu rollerine göre inceleyeceğiz, tabi
bu noktada birde kullanıcı tarafındaki ön gereklilikleri göz ardı
etmemek gerek.

1.  **Veri tabanı sunucuları için yazılımsal gereksinimler:**

Aşağıdaki tablodan inceleyebileceğiniz gibi SharePoint 2013 versiyonunda
SQL Server 2005 ve 2008 desteği kaldırılmış durumda, **SQL Server 2008
R2 SP1** ve sonrası versiyonlar destekleniyor.

**SQL Server 2012 RTM** versiyonuda SharePoint 2013 tarafından
destekleniyor.

![](media/image15.png){width="6.6875in" height="0.8125in"}\
**Resim-4**

1.  **Web ve Uygulama sunucuları için yazılımsal gereksinimler:**

Web ve uygulama sunucuları için işletim sistemi ve bazı ön
gereksinimleri içeren bir listemiz var.

Web ve uygulama sunucularında işletim sistemi olarak **Windows Server
2008 R2 SP1** minimum gereklilik iken **Windows Server 2012 RC** de
destekleniyor.

SharePoint 2013 kurulumundan önce aşağıdaki tabloda inceleyebileceğiniz
bazı uygulamaların/ürünlerin yüklenmesi gerekmekte, bu kurulumları
SharePoint 2013 kurulum ekranındaki “**Install software prerequisites**”
bağlantısına tıklanarak internet üzerinden kurulabilir durumda.

Internet bağlantımızın olmadığı ortamlarda ise bu kurulumları yapmamız
yine mümkün.

Internet olmadan ön gereklilikleri yüklemek için kurulum dosyaları
arasında görebileceğiniz “**PrerequisitesInstallerFiles**” klasörüne
kurulum dosyalarını kopyalayıp, prerequisiteInstaller. Arguments isminde
bir dosya oluşturmalı ve ön gerekliliklerin PrerequisitesInstallerFiles
klasörü içindeki adreslerini yazmalıyız.

Daha sonra prerequisiteInstaller.exe de yapacağımız küçük bir değişiklik
ile kurulumu gerçekleştirebiliriz.

İnternet olmadan SharePoint için ön gerekliliklerin kurulması konusunda
detaylı bilgiye
<http://technet.microsoft.com/en-us/library/ff686793(v=office.15).aspx>
adresinden erişebilirsiniz.

![](media/image16.png){width="5.65625in" height="2.8020833333333335in"}\
**Resim-5**

![](media/image17.png){width="3.1770833333333335in" height="3.40625in"}\
**Resim-6**

![](media/image18.png){width="6.979166666666667in" height="1.34375in"}\
**Resim-7**

**3- Tarayıcı Desteği:**

SharePoint 2013 tarayıcı desteği tablosunu aşağıda inceleyeceğiniz gibi
**IE9 (32-Bit)** , **IE8 (32-Bit)’**e**\
**tüm özellikler için desteklerken diğer tarayıcılarda limitli destek
olduğunu görüyoruz, sınırlı destek ibaresinde ActiveX nesnelerinin
desteklenmeyebileceğini çıkarabiliriz.

![](media/image19.png){width="7.052083333333333in"
height="2.7083333333333335in"}\
**Resim-8**

**3- Kurulum Gereksinimleri:**

Her üründe olduğu gibi SharePoint 2013 içinde kuruluma başlamadan önce
bazı kullanıcıların tanımlanması ve yetki atamalarının yapılması
gerekir.

Kullanıcılara ait bilgileri aşağıda bulabilirsiniz, kullanıcı
isimlendirmelerini istediğiniz gibi tanımlayabilirsiniz, fakat
genellikle SharePoint ile ilgili kullanıcı isimleri “SP” ön eki ile
başlatırız.

Not: Tüm kullanıcıların domain kullanıcıları olması gerekiyor

**SQL Server service account(SQL\_Admin) :**

-   SQL sunucusu üzerinde yönetici yetkilerine sahip kullanıcı, SQL
    kurulumunuda bu kullanıcı ile gerçekleştirebilirsiniz.

-   SQL kurulumu yapılacak sunucuda local admin olmalıdır.

**Setup User account (SP\_Admin): **

-   SharePoint kurulumunu gerçekleştireceğimiz kullanıcı.

-   [SharePoint
    kurulumu](http://www.mshowto.org/tag/sharepoint-kurulumu) yapılacak
    sunucuda local admin olmalıdır.

-   SharePoint SQL Sunucusu üzerinde yeni veritabanları oluşturacağı ve
    yetki atamaları yapacağı için SQL sunucusunda bu kullanıcı
    “**securityadmin**” ve “**dbcreator**” rollerine sahip olmalıdır.

**Search crawler account (SP\_Crawl):**

-   Search servisi içerik kaynaklarına erişirken (SharePoint siteleri,
    harici siteler, paylaşılan dosyalar, file Serverlar v.b.)
    kullanacağı kullanıcı.

-   Erişim sağlanan datalar bu kullanıcının yetkileri ile indexlenir.

-   Bu kullanıcının erişmek istediği kaynaklarda okuma yetkisi
    olması gerekir.

**User Profile Synchronization account (SP\_ADSync):**

-   Active Directoryden kullanıcı bilgilerini okurken
    kullanacağımız kullanıcı.

-   Bu kullanıcının Active Directoryden data okumaya yetkisi
    olması gerekmekte.

NOT: Kullanıcı sayıları için kesin bir kısıtlama yoktur, her ne kadar
doğru olmasada istenildiği taktirde özellikle development ortamları için
tüm işler local admin olan tek bir kullanıcı üzerinden de
gerçekleştirilebilir. Ancak doğru ve güvenli olan yetkileri farklı
kullanıcılara dağıtmaktır.

**B- SHAREPOINT 2013 KURULUM ADIMLARI**

Kurulum öncesi ön gereklilikleri tamamlayıp kapasite planlamasını
tamamladıktan sonra kuruluma başlayabiliriz.

Kurulum ekranları SharePoint 2010 ile hemen hemen aynı.

Kurulum ekranında ilk olarak Ön gereklilikleri yükleyerek başlıyoruz.

Burada unutulmaması gereken nokta: **Farm’a dahil edeceğimiz tüm Web ve
Uygulama sunucularımıza bu ön gerekliliklerin yüklenmesi gerekiyor.**

![](media/image20.png){width="5.510416666666667in"
height="4.114583333333333in"}\
**Resim-9**

![](media/image21.png){width="5.510416666666667in"
height="4.197916666666667in"}\
**Resim-10**

![](media/image22.png){width="5.510416666666667in"
height="4.416666666666667in"}\
**Resim-11**

Ön gerekliliklerin yüklenmesi tamamladıktan sonra SharePoint 2013
kurulumuna başlayabiliriz.

İnternet bağlantısı olmayan ortamlarda ön gereklilikleri
yükleyebiliyoruz yazının üst bölümünde bahsettiğim **Web ve Uygulama
sunucuları için yazılımsal gereksinimler** başlığını inceleyebilirsiniz.

![](media/image23.png){width="5.510416666666667in"
height="4.114583333333333in"}\
**Resim-12**

Ürün anahtarını yazıp devam ediyoruz.

![](media/image24.png){width="5.510416666666667in"
height="4.510416666666667in"}\
**Resim-13**

SharePoint 2013 de eski versiyonda olduğu gibi varsayılan olarak Program
Files’ın altındaki Office Servers klasörüne kuruluyor.

Install Now diyerek kurulum işlemini başlatıyoruz, dilersek bu adresi
değiştirebiliriz.

![](media/image25.png){width="5.510416666666667in"
height="4.489583333333333in"}\
**Resim-14**

Kurulum tamamlandıktan sonra bizim en önemli adım olan Farm
yapılandırmasına başlıyoruz.

Bu bölümde kuracağımız topolojiye uygun Farm tipini, veri tabanı
sunucularına erişebileceğimiz bağlantı bilgilerini tanımlıyor olacağız.

![](media/image26.png){width="5.510416666666667in"
height="4.739583333333333in"}\
**Resim-15**

Wizard sırasında “**IIS**“, “**SharePoint Administration**” ve
“**SharePoint Timer**” servislerinin yeniden başlatılabileceği uyarısı
alıyoruz.

IIS üzerinde farklı bir uygulama yok ise sitemi henüz yeni kurduğumuz
için şu aşamada üzerinde düşünülmesi gereken bir konu değil ancak farklı
uygulamalar var ise IIS servisinin yeniden başlatılması sırasında bu
uygulamaların geçici süre cevap veremeyeceğini unutmamak gerekir.

![](media/image27.png){width="3.9479166666666665in"
height="2.3020833333333335in"}\
**Resim-16**

Yeni bir Farm kuruyorsak “**Create New Farm**” seçeneği ile devam
ediyoruz.

Eğer mevcut bir Farma ekleme yapacaksak yani birden fazla web uygulama
sunucusunun olduğu bir topolojiye karar verdiysek bu sunucuları eklemek
için “**Connect to an existing Server Farm**” seçeneği ile devam etmemiz
gerekiyor.

Eğer mevcut bir Farm’a sunucu eklemek istersek bizden daha önceden
tanımlanmış olan passphrase’i isteyecektir. Passphrase ile ilgili detaya
yazının devamından erişebilirsiniz.

![](media/image28.png){width="5.510416666666667in"
height="4.791666666666667in"}\
**Resim-17**

Sonraki adımda SharePoint Central Administration ve ilerleyen süreçte
diğer service ve web uygulamalara ait veri tabanlarının konumlanacağı
SQL sunucumuzu belirtiyoruz.

Buradaki alanlara ait bilgiler şu şekilde,

**Specify Configuration Database Settings**

**Database Server:** bağlanılacak SQL sunucusunun adı

**Database Name:** Central Administration’a ait veri tabanının adı

**Specify Database Access Account**

**User Name:** Sunucuya bağlanırken kullanılacak kullanıcı adı, etki
alanı (domain) ile birlikte yazılmalı.

**Password:** Sunucuya bağlanırken kullanılacak kullanıcının şifresi

\*Hatırlayacağınız gibi kullanıcılara ait yetki tanımlamalarının nasıl
olması gerektiğini ön gerekliler bölümünde bahsetmiştik.

![](media/image29.png){width="5.510416666666667in"
height="4.770833333333333in"}\
**Resim-18**

Bu ekranda bizden bir parola oluşturmamızı istiyor SharePoint 2010
sürümünde gelen bu yenilik Farm’a daha sonra bir sunucu eklemek
istediğimizde bizden bu parolayı istiyor böylece güvenliği bir seviye
daha yukarı çekmiş oluyordu.

SharePoint 2013’de de aynen devam ediyor bu gelenek.

![](media/image30.png){width="5.510416666666667in"
height="4.770833333333333in"}**\
Resim-19**

**! Küçük bir hatırlatma:** Bir çok kez kurulum sırasında tanımlanan
passphrase’nin sonradan unutulma durumu ile karşılaştım, bu durumda
passphrase resetlemek için aşağıdaki küçük kod bloğunu “**SharePoint
Management Shell**” ile kullanabilirsiniz.

\$passphrase = ConvertTo-SecureString -String “YeniPassphrase”
-asPlainText –Force

Set-SPPassPhrase -PassPhrase \$passphrase –Confirm

Configuration Wizard’ın bu bölümünde ise SharePoint Central
Administration’nın IIS üzerinde konumlanacağı portu ve kullanacağı
authentication provider’ı seçiyoruz.

Authentication provider olarak mevcut etki alanımız ne kullanıyor ise
onu seçmemiz gerekiyor.

![](media/image31.png){width="5.510416666666667in"
height="4.760416666666667in"}\
**Resim-20**

Yapılandırmaya başlamadan tanımladığımız bilgilerin kısa bir özetini bu
ekrandan inceleyebilirsiniz.

Next’e tıklayıp yapılandırma işlemini başlatıyoruz.

![](media/image32.png){width="5.510416666666667in" height="4.75in"}\
**Resim-21**

Configuration Wizard yapılandırma işlemini tamamladığında aşağıdaki gibi
bir ekran görüntüsü ile karşılaşmanız gerekiyor.

Bu aşamada SharePoint ürününün yapılandırmasını tamamlamış buluyoruz,
sonraki adımda Farm yapılandırmasına yönlendireceğiz.

![](media/image33.png){width="5.510416666666667in"
height="4.729166666666667in"}\
**Resim-22**

Bu bölümde az önce konfigürasyonunu tanımladığımız Central
Administration bizi karşılıyor.

“Start the Wizard” butonu ile Farm konfigürasyonunu başlatacağız.

![](media/image34.png){width="6.927083333333333in"
height="4.416666666666667in"}\
**Resim-23**

Bu ekrandan Farm’a konumlandırılacak ve kullanıma açılacak “Service
uygulamalarını” seçiyoruz, seçtiğimiz uygulamalar için IIS’de birer
uygulama oluşturulacak ve gerek duyan uygulamalar için Veri Tabanı
sunucumuzda kendilerine özel veri tabanları oluşturulacak.

\*Bu ekrandan seçmediklerimizi daha sonra Central Administration
&gt;&gt; Application Management &gt;&gt; Manage Service Application
bölümünden oluşturabiliriz.

![](media/image35.png){width="6.541666666666667in"
height="8.458333333333334in"}\
**Resim-24**

Service uygulamalarının kurulumdan sonra SharePoint kurulumunu
tamamlamış oluyoruz,

> **\
> **

**KAYNAKÇA**

[*https://tr.wikipedia.org/wiki/SharePoint*](https://tr.wikipedia.org/wiki/SharePoint)

[*http://tayfundemirbas.net/sharepoint-nedir-nerelerde-kullanilir/*](http://tayfundemirbas.net/sharepoint-nedir-nerelerde-kullanilir/)

[*https://www.ceyhuncamli.com/sinir-guvenligi-cihazlarinin-sikilastirilmasinda-test-ve-denetim-araclarinin-kullanilmasi-nipper/*](https://www.ceyhuncamli.com/sinir-guvenligi-cihazlarinin-sikilastirilmasinda-test-ve-denetim-araclarinin-kullanilmasi-nipper/)

[*http://www.webhostingturkey.com/post/2010/09/23/ASPNET-Guvenik-Acikligi.aspx*](http://www.webhostingturkey.com/post/2010/09/23/ASPNET-Guvenik-Acikligi.aspx)

[*http://www.iso-27001.net/microsoft-sharepoint-ve-fast-arama-sunucusu-oracle-outside-in-technology-coklu-acikliklari/*](http://www.iso-27001.net/microsoft-sharepoint-ve-fast-arama-sunucusu-oracle-outside-in-technology-coklu-acikliklari/)

[*https://technet.microsoft.com/tr-tr/library/cc262849.aspx*](https://technet.microsoft.com/tr-tr/library/cc262849.aspx)

[*https://technet.microsoft.com/en-us/library/cc288143(v=office.14).aspx*](https://technet.microsoft.com/en-us/library/cc288143(v=office.14).aspx)

[*https://blogs.technet.microsoft.com/rycampbe/2013/10/14/securing-sharepoint-harden-sql-server-in-sharepoint-environments/*](https://blogs.technet.microsoft.com/rycampbe/2013/10/14/securing-sharepoint-harden-sql-server-in-sharepoint-environments/)

[*http://www.c-sharpcorner.com/UploadFile/Roji.Joy/database-hardening-for-sharepoint-2013/*](http://www.c-sharpcorner.com/UploadFile/Roji.Joy/database-hardening-for-sharepoint-2013/)

[*http://sharepointpromag.com/sharepoint-2010/sharepoint-security-server-hardening*](http://sharepointpromag.com/sharepoint-2010/sharepoint-security-server-hardening)

[*http://www.mshowto.org/sharepoint-2013-kurulumu-on-gereklilikler-ve-sik-kullanilan-topolojiler.html*](http://www.mshowto.org/sharepoint-2013-kurulumu-on-gereklilikler-ve-sik-kullanilan-topolojiler.html)
