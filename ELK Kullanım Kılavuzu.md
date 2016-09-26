# 1. ELK Stack Nedir?
ELK Stack üç tane açık kaynak kodlu ürünün (Elasticsearch, Logstash ve Kibana) birleşimidir. ELK Stack dünyanın en popüler log yönetim programlarından birisidir. ELK Stack iş zekası, güvenlik, uyum ve web analitiği alanlarında en çok kullanılan araçlardan birisidir. Logstash logları toplar ve ayrıştırır, sonrasında Elasticsearch bu logları endeksler ve saklar. Kibana ise görsel bir şekilde bu logları kullanıcılara sunar.
## 1.1. Elasticsearch
Elasticsearch çoğu zaman bir arama sunucusu olarak da anılmaktadır. Normalde insanlar arama işlevini kendilerinin yaptıkları basit bir işlem olarak görürler. Oysa ki arama işlemi çok karmaşık bir işlem olup bizlere hizmet olarak sunulmaktadır. Elasticsearch bu hizmeti sunan arama sunucularından bir tanesidir. Fakat bildiğimiz SQL veritabanlarından farklı olarak veriyi belirli bir düzen içerisinde tutmaz. Elasticsearch verinin ne kadar düzenli tutulduğundan çok aramalara karşı ne kadar iyi performansa sahip olduğuna önem verir.
## 1.2. Logstash
Logstash ELK Stack’in tam ortasında bulunan olmazsa olmaz parçalardan biridir. Elasticsearch verileri ne kadar iyi endekslerse endekslesin, bu verilerin öncelikle bir yerden ELK sunucusuna gelmesi gerekmektedir. Çeşitli kaynaklardan bu verilerin gelmesi işlemini Logstash gerçekleştirmektedir. Yani kısaca Logstash çeşitli uygulama ve sunuculardan logları alıp Elasticsearch e saklaması için iletmektedir.

Bunlardan farklı olarak Logstash ayrıca veriyi filtreleme ve şekillendirme görevini de yerine getirmektedir. Bu sayede gelen veriler anlamlandırılmakta ve kullanıcının kolayca anlayabileceği bir hale gelmektedir.
##1.3. Kibana
Her sistemde olduğu gibi ELK Stack için de görsellik çok önemlidir. Kibana ELK Stack’de tutulan logların görselleştirilmesi görevini üstlenmektedir. Kibana ile loglar kategorilere göre ayırılabilmekte, belirli kriterlere göre daraltılabilmekte ve istenilen formatta görsel grafikler şeklinde kullanıcıya gösterilebilmektedir.
# Çalışma Prensipleri
## 2.1. Elasticsearch 
### 2.1.1. Terminoloji
Elasticsearch arama işlemini kolaylaştırmak ve verileri düzenli bir şekilde tutabilmek için farklı bir mimari yapı kullanmaktadır. Bu yapıda en üstte dizi (cluster) gelmektedir. Dizi bir veya daha fazla düğümün (node) birleşmesinden oluşan ve tüm bu düğümler arasında endeksleme ve arama yetenekleri sağlanan birimdir. Düğüm ise verileri saklayan tek bir sunucudur. Bir düğüm istenilen diziye ait olacak şekilde ayarlanabilmektedir. Endeks (index) benzer özellikler içeren dökümanların birleşiminden oluşmaktadır. Farklı veri kategorileri için farklı endeksler oluşturabilmek mümkündür. Tip (type) benzer yapı içeren verilere verilen genel bir yapıdır. Döküman (document) ise endekslenebilen en temel bilgi birimidir.

Bir endeksteki verilerin boyutu çok büyük olabileceği için, donanımsal problemler yaşamamak adına endeksteki veriler zarflara (shards) ayırılmaktadır. Bu sayede içerik hacmi yatay olarak ayrılırken aynı zamanda bir arama işlemi zarflar üzerinde paralel olarak gerçekleştirilebilmektedir. Sistemde beklenmeyen problemlerin yaşanması durumlarda veri kaybı yaşamamak için bu zarfların kopyaları (replicas) da ayrıca tutulabilmektedir. Bu kopyaların sayısı her bir endeks için kullanıcılar tarafından ayarlanabilmektedir.
### 2.1.2. Kurulum
Bu çalışma kapsamında anlatılan bütün kurulumlar CentOS 7 üzerinde yapılacaktır. Ayrıca makine kurulurken ‘Server with GUI’ seçeneği seçilmelidir. Bu seçeneğin seçilmesi gerekli olan pek çok kütüphane ve uygulamanın yüklü olarak gelmesini sağlayacaktır (örn. Java, EPEL repository). 
* Öncelikle GPG imza anahtarını indirip yükleyiniz:
```sh
rpm –import https://packages.elastic.co/GPG-KEY-elasticsearch
```
* Elasticsearch’ün yüklenebilmesi için gerekli olan repo dosyasını aşağıdaki gibi oluşturunuz ve elasticsearch.repo olarak /etc/yum.repos.d klasörü altına kaydediniz:

![alt text](images/1.png)

* Oluşturduğunuz repo dosyasını kullanarak elasticsearch’ü yükleyiniz:
```sh
yum -y install elasticsearch
```
* Elasticsearch’ün sistem açılışında servis olarak çalışması için aşağıdaki komutları çalıştırınız:
```sh
systemctl daemon-reload
systemctl enable elasticsearch.service
systemctl start elasticsearch.service
```
* Elasticsearch’ün düzgün çalışıp çalışmadığını kontrol etmek için aşağıdaki komutu çalıştırabilirsiniz. Çıkan sonuçta elasticsearch versiyonunu, dizi adını (varsayılan olarak elasticsearch) ve diğer varsayılan değerleri görebilirsiniz.

![alt text](images/2.png)

### 2.1.3. Konfigürasyon
Elasticsearch konfigürasyon dosyaları /etc/elasticsearch/conf dizini altında bulunmaktadır. Bu dizin altında elasticsearch.yml ve logging.yml dosyaları bulunmaktadır. Genel olarak elasticsearch ayarları elasticsearch.yml dosyası üzerinden yapılmaktadır. Logging.yml dosyası ise Elasticsearch loglama ayarlarını içermektedir. Elasticsearch.yml dosyası uzantısından da anlaşılacağı üzere yaml formatında yazılmıştır. Buradaki alanlardan en çok kullanılanlar veya değiştirilmesi gerekenler aşağıda listelenmiştir.
Path.log, path.plugin, path.conf: logların, pluginlerin ve konfigürasyon dosyalarının hangi dizin altında olduğunu gösterir.
Cluster.name, node.name: Dizi ve düğümün isminin girilebilmesini sağlar. Verilmezse elasticsearch varsayılan değerlerden atamaktadır.
İndex.number_of_shards, index.number_of_replicas: Bir endeks için zarf ve kopya sayısının girilebilmesini sağlar. Varsayılan olarak zarf sayısı 5 ve kopya sayısı 1’dir.
Plugin.mandatory: Bir düğümün çalışması için yüklenmesi zorunlu olan pluginlerin belirtilmesini sağlar. Eğer burada yazan bir plugin yüklü değilse o düğüm başlayamaz.
Network.host: Diğer düğümlerin bu düğümle konuşmak için kullanacağı ve bind adresi olan IP adresinin belirtilmesini sağlar.
Transport.tcp.port: Düğümler arası iletişimde kullanılacak port numarasını belirtir. Varsayılan olarak 9300’dür.
http.port: http trafiğinin dinleneceği port numarasını belirtir. 
http.enabled: false verildiğinde http’nin olarak kullanılmamasını sağlar.
Logging.yml Elasticsearch için loglama ayarlarını içerir. Genel olarak logging.yml hakkında bilinmesi gereken logger.level alanındaki değerdir. Bu değere bağlı olarak elasticsearch loglama seviyesi belirlenir. Bu değer ERROR, WARN, INFO, DEBUG ve TRACE değerlerinden herhangi biri olabilir. Varsayılan olarak INFO seçilidir, fakat daha fazla log istendiğinde DEBUG veya TRACE seçilebilir, aynı şekilde sadece hatalar gösterilmek istendiğinde ERROR olarak seçilebilir.

### 2.1.4. Elasticsearch REST API
ELK Stack kurulum ve yönetimi için çok gerekli olmasa da, oluşabilecek hataları çözebilmek ve Elasticsearch i ayrı olarak kullanabilmek için API’lerini öğrenmek faydalı olacaktır. Elasticsearch REST API  genel olarak endeks ve doküman ekleme, çıkarma ve değiştirme işlemleri için ve dizilerin durumlarını ve istatistiklerini kontrol edebilmek için kullanılmaktadır. Ayrıca REST API ile beraber arama, filtreleme, sıralama gibi daha pek çok fonksiyon yerine getirilebilmektedir. Bu çalışma kapsamında, REST API ile yapılabilecek belli başlı temel fonksiyonlar aşağıda örneklendirilmiştir:

* Elasticsearch’de bulunan dizilerin durumunu öğrenmek için ```curl ‘localhost:9200/_cat/health?v’``` komutu çalıştırılabilir. Çıkan sonuçta yeşil (green) herhangi bir sorun olmadığını, sarı (yellow) verilerin tamamen operasyonel olduğunu fakat bazı kopyaların henüz ayrılmadığını, kırmızı (red) ise bazı verilerin erişilebilir olmadığını ifade etmektedir. Ayrıca çıkan cevapta kaç tane düğüm ve zarf olduğunu da görebilirsiniz.

* Elasticsearch’de dizide bulunan düğümlerin listesini öğrenmek için ```curl ‘localhost:9200/_cat/nodes?v’``` komutu çalıştırılabilir. Aynı şekilde tüm endeksleri listelemek için curl ‘localhost:9200/_cat/indices?v’ komutu çalıştırabilir.

* Komut satırından yeni bir endeks oluşturmak için ```curl -XPUT ‘localhost:9200/endeksAdi?pretty’``` komutu çalıştırılabilir.

* Var olan bir endekse yeni bir doküman eklemek için
```sh
curl -XPUT ‘localhost:9200/endeksAdi/tipAdi/1?pretty -d ‘
{
	“alanAdi”: “değeri”
}’
```
şeklinde komut girilebilir. Doküman üzerinde değişiklik yapılmak istendiğinde aynı komut istenilen değerlerle birlikte tekrar çalıştırılabilir. Burada ayırt edici unsur id değeri yani bu örnek için 1’dir. Id değeri 1 olarak girilen tüm komutlar bu doküman üzerinde değişiklik yapacaktır, fakat id değeri 2 olarak girilen başka bir komut yeni bir doküman oluşturacaktır. Bu dokümana da ulaşmak için ```curl -XGET ‘localhost:9200/endeksAdi/tipAdi/2?pretty’``` komutu çalıştırılabilir.

* Var olan bir endeksi komut satırından silmek için ```curl -XDELETE ‘localhost:9200/endeksAdi?pretty’``` komutu çalıştırılabilir.

* Var olan bir dokümanı komut satırından silmek için ```curl -XDELETE ‘localhost:9200/endeksAdi/tipAdi/id?pretty’``` komutu çalıştırılabilir.

* Dokümanları elle girmek yerine tek bir komut satırıyla bir dosyadan endekslenmek istediğinde ```curl -XPOST ‘localhost:9200/endeksAdi/tipAdi/_bulk?pretty’ --data-binary “@fileName.json”``` komutu çalıştırılabilir. Dosyanın json formatına sahip olduğu önceden kontrol edilmelidir.

* Bir endeksteki tüm dokümanları getirmek için
```sh
curl ‘localhost:9200/endeksAdi/_search?q=*&pretty’
```
komutu veya
```sh
curl -XPOST ‘localhost:9200/endeksAdi/_search?pretty’ -d ‘
{
	“query”: { “match_all”: {}}
}’
```
komutu çalıştırılabilir.

* Üstteki komutta geçen query kısmı, dokümanların istenilen alanlarının istenilen filtreden geçirildikten sonra getirilebilecek şekilde değiştirilebilmektedir. Bu işlemlerin nasıl yapılacağı Elasticsearch’ün sitesinden bulunabilir.

### 2.1.5. Örnek Kullanım Senaryosu

Bu kısımda daha önceki Kurulum ve REST API kısımlarında sağlanan bilgiler ışığında basit bir örnek canlandırılacaktır. 

Öncelikle Elasticsearch için aşağıdaki gibi basit bir durum kontrolü yapalım.

![alt text](images/3.png)

Gelen cevaptan da anlaşılacağı üzere elasticsearch isimli dizi yeşil yani çalışır durumda. Ayrıca bu dizimizin içerisindeki düğümlerin listesini de getirelim.

![alt text](images/4.png)

Son olarak da Elasticsearch içerisinde bulunan endekslerin bir listesini getirelim.
 
![alt text](images/5.png)
 
Henüz kurulumdan sonar bir şey eklemediğimiz için gelen cevaptan da anlaşılacağı üzere Elasticsearch üzerinde herhangi bir endeks bulunmamaktadır.

Daha önce bahsedildiği gibi Elasticsearch birden fazla endekse sahip olabilir ve bu endekslerin altında birden fazla tip olabilir. Her bir tip için de birden fazla doküman denilen kayıtlar bulunabilir. Buradaki öğrenciler ile ilgili bilgileri barındıran bir okul endeksi kuracağız. Bu endeksin altında da ogrenci tipinde dokümanlar oluşturacağız. Bunun için oluşturmuş olduğumuz json formatındaki dosyayı elasticsearch e yeni bir endeks olarak aşağıdaki gibi yüklüyoruz.

![alt text](images/6.png)

Düzgün bir şekilde yüklenip yüklenmediğini kontrol etmek için dokümanlardan bir tanesini çekelim.

![alt text](images/7.png)

Çıkan sonuçtan da görüleceği üzere her bir ogrenci dokümanı ad, soyad, yaş, sınıf, kayıt tarihi ve bölüm bilgilerinden oluşmaktadır. Verilerimizin elasticsearch de düzgün bir şekilde tutulduğundan emin olduktan sonra bir sonraki işlemimiz bu veriler üzerinde arama yapmak. Öncelikle soyadı Hester olan öğrencilerin kayıtlarını getirelim.

![alt text](images/8.png)

Yukarıda görüleceği üzere q parametresi alan adı ve değerini alarak bunlar için sorgulama yapmaktadır. Fakat ileri seviye aramaların q parametresi ile yapılabilmesi gerçekten çok zor, bu yüzden elasticsearch DSL (Domain-Specific Language) dilinde aramalar yapabilmeyi mümkün kılmıştır. Örneğin yukarıda yaptığımız aramanın aynısını şu şekilde yapmamız da mümkündür.

![alt text](images/9.png)

Görüleceği üzere iki arama da aynı sonuçları getirdi. Bu örnek için DSL kullanımı gereksiz gibi dursa da, ismi Susanna olan ve yaşı 20 den büyük olan kişileri aramak istediğimiz de DSL in ne kadar önemli olduğunu anlıyoruz. Bahsettiğimiz aramayı şimdi DSL ile yapalım.

![alt text](images/50.png)

Yukarıdaki aramada yazılan range filtresi belirli bir aralık için arama yapılırken kullanılmaktadır. Daha önce de kullandığımız match ise direk bir eşleşme aramaktadır.

Şimdi ise mühendislik okuyan öğrencilerin kaydını getirmeye çalışalım. Bunun için birden fazla bölüm olduğu için, direk bölüm alanında mühendis ifadesini içeren kayıtları getirelim.

![alt text](images/10.png)

Görüldüğü gibi bu şekilde mühendislik bölümlerinde okuyan öğrencilerin kayıtlarını getirmiş olduk. Bu aramada öncekilerden farklı olarak bolum alanında muhendis ifadesi içeren tüm kayıtlar getirildi. Buradaki _score alanı aratılan ifadenin alan içerisinde ne kadarının eşleştiğinin normalize edilmiş halidir. Şimdi sadece Bilgisayar mühendisliği bölümünde okuyan öğrencilerin kayıtlarını getirmeye çalışalım.

![alt text](images/11.png)

Görüleceği üzere Bilgisayar Mühendisliği ifadesi iki kelime içerdiği için match filtresi değil onun yerine match_phrase filtresi kullanıldı.

Şimdiye kadar elasticsearch üzerinde bulunan bir endekste kayıtlı dokümanlar üzerinde arama ve filtreleme işlemi nasıl yapılır onlara değindik. Şimdi ise elasticsearch’ün tercih edilme sebeplerinden birisi olan analiz yeteneğini biraz inceleyelim. Elasticsearch, SQL’deki GROUP BY özelliği gibi birleştirme (aggregation) özelliğine sahiptir. Bu özelliği kullanmak için şimdi okulda kayıtlı öğrencilerin kaçının hangi bölümde okuduğunu öğrenmeye çalışalım.

![alt text](images/51.png)

Gelen cevabın alt satırlarına bakıldığında örneğin iktisat bölümünde toplam 28 öğrenci bulunmaktadır. Bu aramamızı geliştirerek Iktisat bölümünde okuyan öğrencilerin kayıt yılına göre sayılarına bakalım.

![alt text](images/12.png)

Yine gelen cevabın alt satırlarına bakıldığında örneğin 2015 yılında kayıt olmuş İktisat bölümünde okuyan öğrenci sayısı altıdır. Bu şekilde birleştirme işlemi sadece belirli bir kriteri sağlayan kayıtlar üzerinden de yapılabilmektedir. Şimdi biraz daha farklı bir örnek yapalım ve her bir bölümdeki öğrencilerin ortalama yaşına bakalım.

![alt text](images/14.png)

Bu kısımda bahsettiğimiz örnekler Elasticsearch ile yapılabileceklerin sadece ufak bir kısmıydı. Fakat, elasticsearch ile karmaşık aramaların ne kadar hızlı bir şekilde yapılabildiğinin ve nasıl yapıldığının bir gösterimi olarak düşünülebilir. Daha detaylı aramaların nasıl yapılabileceği ve aramalarda kullanılan DSL dilinin yazım biçimleri için elastic.co sayfasına bakabilirsiniz.

## 2.2. Logstash
Logstash gerçek zamanlı veri toplama motorudur. Pek çok farklı kaynaktan topladığı verileri birleştirip istenilen hedef konuma kaydedebilmektedir. Herhangi bir yapıya sahip veri Logstash filtre ve output pluginleriyle istenildiği gibi işlenebilmektedir. Logstash sayesinde istenilen türe sahip loglar toplanabilmekte ve ayrıca çeşitli pluginler aracılığıyla bilgisayar üzerinde gerçekleşen pek çok olayın kayıtları tutulabilmektedir. 

Belirli bir verinin logstash ile toplanabilmesi için, Logstash bir veya daha fazla input, filter veya output plugini kullanmaktadır. Bunlardan filter plugini opsiyonel olsa da, input ve output pluginlerini kullanmak zorunludur. İnput plugini bir kaynaktan verilerin çekilmesini, filter plugini istenilen şekilde verinin değiştirilmesini ve output plugini ise bu verinin bir hedefe yazılmasını sağlar. Bu pluginler konfigürasyon dosyalarına yazılarak kullanılmaktadır. Bu dosyaların nasıl yazılacağı konfigürasyon kısmında ve kullanım senaryoları kısmında detaylı olarak işlenecektir. 
### 2.2.1. Kurulum
Centos üzerinde Logstash kurulumunun en basit yöntemi hazır depoları kullanarak yüklemektir. Bu yüzden ilk olarak /etc/yum.repos.d/ klasörü altında logstash.repo dosyası oluşturuyoruz ve aşağıdaki gibi içini dolduruyoruz.

![alt text](images/15.png)

Dosyayı kaydettikten sonra aşağıdaki komut ile otomatik olarak yüklüyoruz.
```sh
Yum install logstash -y
```
Bundan sonra başlatılmaya hazır bir servis olarak logstash yüklenmiş oluyor. Aşağıdaki komutu girerek servisi başlatabilirsiniz.
```sh
systemctl start logstash.service
```
Bu aşamada Logstash lokal ortamda çalışır vaziyete gelmiş bulunuyor. Fakat kullanım senaryolarında bahsedeceğimiz bazı durumlarda dışarıdan loglar alınırken lumberjack protokolü kullanmamız gerekecek. Lumberjack protokolü veya yeni adıyla logstash-forwarder bağlantı kurarken SSL sertifikaları kullanmakta. Bu yüzden  ilk olarak /etc/pki/tls/openssl.conf dosyasında birkaç değişiklik yapmamız gerekiyor. ELK Stack’i static bir IP ile kullanacağımız için, bu dosya içerisinde [ v3_ca ] diye başlayan satırın altına aşağıdaki satırı ekliyoruz.
```
SubjectAltName = IP: yourIPAdress
```
Bundan sonra sertifika ve anahtar dosyalarını üretmek için aşağıda verilen komutu çalıştırıyoruz.
```sh
openssl req -config /etc/pki/tls/openssl.cnf -x509 -days 3650 -batch -nodes -newkey rsa:2048 -keyout /etc/pki/tls/private/logstash-forwarder.key -out /etc/pki/tls/certs/logstash-forwarder.crt
```
Opsiyonel olarak Logstash’in GeoIP veritabanı kullanması isteniyorsa aşağıdaki komutlar çalıştırılmalıdır.
```sh
cd /etc/logstash
curl -O "http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz"
gunzip GeoLiteCity.dat.gz
```
### 2.2.2. Konfigürasyon
Logstash konfigürasyon dosyaları üç çeşit konfigürasyon dosyasından oluşmaktadır. Bunlardan input ve output konfigürasyonları kesinlikle gerekmekteyken filter konfigürasyonu opsiyoneldir. Bu konfigürasyon dosyaları eksikken Logstash pek bir işe yaramaktadır. Aşağıdaki görüntüden anlaşılacağı üzere logstash konfigürasyon dosyaları yokken Logstash uyarı vermektedir.

![alt text](images/16.png)

Logstash konfigürasyon dosyaları, alınmak istenen log dosyalarına göre değişmektedir. Fakat, senaryoya bağlı olarak bir sonraki kısımda bahsedilen pluginler kullanılmaktadır. Bu pluginlerin nasıl kullanılacağı ve konfigürasyon dosyalarının nasıl yapılandırılacağı kullanım senaryoları kısmında detaylı olarak anlatılacaktır.
### 2.2.3. Pluginler
#### 2.2.3.1. Input Pluginleri
Input pluginleri sayesinde Logstash çok sayıda farklı kaynaktan verileri başarılı bir şekilde çekebilmektedir. Bu çalışma kapsamında bu pluginlerden bazıları kullanalacak olup bunlara kullanım senaryoları kısmında erişebilirsiniz. Bunların dışında kalan pluginler için sadece genel bilgi sağlanacak olup, detaylı bilgi Logstash sitesinden edinilebilir.

* beats: Elastic Beats çerçevesinden olayların alınabilmesini sağlar. 
* couchdb_changes: CouchDB _changes URI’sinden olayların alınabilmesini sağlar.
* elasticsearch: Bir elasticsearch dizisinden belirli bir arama sonucunadayanarak kayıtların alınabilmesini sağlar.
* exec: Periyodik olarak bir komutun çalıştırılabilmesini ve çıkan sonucun alınabilmesini sağlar.
* eventlog: Windows Event Log’dan olayların alınabilmesini sağlar.
* file: İstenilen dosyadan veri alınabilmesini sağlar.
* generator: Genellikle pluginlerin performansını test etmek için rastgele log olayları üretir.
* heartbeat: Logstash performansını ve erişilebilirliğini test etmek için heartbeat mesajları üretir.
* http: HTTP veya HTTPS üzerinden olayların alınabilmesini sağlar.
* irc: IRC sunucudan olayların alınabilmesini sağlar.
* imap: IMAP sunucusundan maillerin okunabilmesini sağlar.
* jdbc: JDBC arayüzü olan veritabanlarından verilerin alınabilmesini sağlar.
* lumberjack: Lumberjack protokolü üzerinden olayların alınabilmesini sağlar.
* snmptrap: SNMP trap mesajlarının alınabilmesini sağlar.
* stdin: Standart inputtan olayların okunabilmesini sağlar.
* sqlite: Sqlite veritabanından bilgilerin alınabilmesini sağlar.
* syslog: Ağ üzerinden syslog mesajlarının alınabilmesini sağlar.
* tcp: Bir TCP soket üzerinden olayların alınabilmesini sağlar.
* twitter: Twitter Streaming API’den olayların alınabilmesini sağlar.
* unix: UNIX soket üzerinden olayların alınabilmesini sağlar.
* udp: Bir UDP port üzerinden olayların alınabilmesini sağlar.

#### 2.2.3.2. Output Pluginleri
ELK Stack kapsamında sadece elasticsearch plugini kullanılmaktadır. Detaylı kullanımı konfigürasyon kısmından incelenebilir. Diğer pluginlerin detaylı açıklaması sağlanmayacak olsa da isimleri ve genel işlevleri aşağıda listelenmiştir.
* Boundary: Logstash olaylarına dayanarak Boundary’e uyarılar yollar.
* Circonus: Logstash olaylarına dayanarak Circonus’a uyarılar yollar.
* Csv: Ayrılmış bir şekilde olayların diske yazılmasını sağlar.
* Cloudwatch: Metrik verilerin AWS CloudWatch’a gönderilmesini sağlar.
* Datadog: Logstash olaylarına dayanarak DataDogHQ’a olayların gönderilmesini sağlar.
* Email: Output ulaştığında belirlenen mail adresine mail gönderilmesini sağlar.
* Elasticsearch: Logların Elasticsearch’de saklanmasını sağlar.
* Exec: Eşleşen bir olay durumunda belirlenen komutun çalıştırılmasını sağlar.
* File: Olayların diskteki bir dosyaya yazılmasını sağlar.
* İrc: Olayların IRC sunucuya atılmasını sağlar.
* Lumberjack: Olayların lumberjack protokolü ile yollanmasını sağlar.
* Loggly: Logların loggly’e yollanmasını sağlar.
* MongoDB: Olayların MongoDB’ye yazılmasını sağlar.
* Nagios: Pasif kontrol sonuçlarının Nagios’a gönderilmesini sağlar.
* Null: Test amaçlı null output oluşturur.
* Riemann: Metriklerin Riemann’a yollanmasını sağlar.
* Redmine: Redmine API kullanarak biletlerin oluşturulmasını sağlar.
* Stomp: Olayların STOMP protokolü kullanılarak yollanmasını sağlar.
* Syslog: Olayların bir syslog sunucuya yollanabilmesini sağlar.
* Stdout: Olayların standart outputa yazılmasını sağlar.
* Tcp: Olayların bir TCP soket üzerinden atılmasını sağlar.
* Udp: Olayların UDP üzerinden yollanmasını sağlar.

#### 2.2.3.3. Filter Pluginleri
Filter pluginleri input pluginleri aracılığıyla alınan olayların output pluginine yollanmadan önce istenilen şekilde değiştirilmesini sağlar. Gelen verilerin yapısına göre kullanılacak filter plugini de değişiklik gösterebilmektedir. Bu çalışma kapsamında filter pluginlerinden bazıları kullanılmıştır, bunların kullanımı için kullanım senaryoları kısmına bakabilirsiniz. Bu kısmın geri kalanında diğer filter pluginleri hakkında kısa bilgi verilecektir.

* aggregate: Tek bir görev sonrası farklı olaylardan gelen bilgilerin toplanmasını sağlar.
* alter: mutate plugininin yapamadığı alanlarda genel değişikliklerin yapılmasını sağlar.
* anonymize: Alan değerlerini tutarlı bir hash değeri ile değiştirir.
* collate: Olayları zaman veya toplam bakımından sıralar.
* csv: Virgülle ayrılmış değerleri ayrı alanlara yazar.
* cidr: Bloklanmış IP listesiyle IP adreslerini kontrol eder.
* clone: Olayları kopyalar.
* cipher: Bir olaya şifreleme uygular ve uygulanan şifreyi çözer.
* checksum: Bir olaydaki alanlara dayanarak checksum oluşturur.
* date: Logstash timestamp olarak kullanılmak üzere alanlardan tarihleri çeker.
* de_dot: Bir alan adından noktaların kaldırılmasını sağlar.
* dns: Standart veya ters DNS sorgusu yapar.
* drop: Tüm olayları düşürür.
* extractnumbers: Bir string ifadeden sayıları çeker.
* elapsed: İki olay arasında geçen süreyi hesaplar.
* geoip: Bir IP adresi hakkında coğrafik bilgi ekler.
* grok: Belirli bir yapıya sahip olmayan olay verisini alanlara ayırır.
* i18n: Bir alandan özel karakterlerin kaldırılmasını sağlar.
* json: JSON formatındaki olayları ayırır.
* kv: Anahtar-değer formatındaki verileri ayırır.
* mutate: Alanlar üzerinde dönüşüm sağlar.
* metrics: Metrikleri toplar.
* metaevent: Bir olaya isteğe bağlı alanlar ekler.
* ruby: istenilen Ruby kodunu çalıştırır.
* range: Belirlenen alanların istenilen aralıkta veya boyutta olup olmadığını kontrol eder.
* sleep: Belirlenen süre kadar uyumasını sağlar.
* split: Birden fazla satırlı mesajları farklı olaylar olarak ayırır.
* uuid: Olaylara UUID ekler.
* urldecode: URL olarak kodlanmış alanları çözer.
* xml: XML formatını alanlara çevirir.

## 2.3. Kibana
Kibana, Elasticsearch ile beraber çalışabilecek şekilde tasarlanmış bir analiz ve görselleştirme platformudur. Elasticsearch endekslerinde tutulan veriler Kibana ile aranabilir ve gösterilebilir. İleri veri analizlerinin sonuçları Kibana ile görsel grafikler şeklinde sunulabilmektedir.
### 2.3.1. Kurulum
Önceki kurulumlarda olduğu gibi önce Kibana için uygun bir repo dosyası oluşturunuz. Dosyanın adı kibana.repo olmalı ve /etc/yum.repos.d/ klasörü altında yer almalıdır.

![alt text](images/17.png)

Repo dosyası oluşturulduktan sonra yum install kibana komutunu çalıştırınız. Sonrasında kibanayı servis olarak sistem başladığında çalıştırmak için aşağıdaki komutları çalıştırınız.
```sh
chkconfig –add kibana
systemctl daemon-reload
systemctl enable kibana.service
systemctl start kibana.service
```
Bu komutlar çalıştırıldıktan sonra internet tarayıcınıza localhost:5601 yazdığınızda Kibana sayfası açılacaktır. Henüz herhangi bir endeks ayarlanmadığı için herhangi bir log göremeyeceksiniz. Elasticsearch ve logstash ile entegrasyonu için Elasticsearch-Logstash-Kibana Entegrasyonu kısmına bakabilirsiniz.
### 2.3.2. Görselleştirme
Kibana logların görselleştirilmesi için 5601 portundan bir http arayüz sunmaktadır. Bu arayüzün Discover kısmında logları interaktif bir şekilde görebilirsiniz. Discover kısmında sağ üst kısımdaki tarih kısmını değiştirerek en son bir aylık, bir haftalık ve benzeri şekilde logları sınırlandırabilirsiniz. Aynı şekilde üst tarafta bulunan ve varsayılan olarak * karakteri bulunan yere istediğiniz arama kriterini yazarak o kriteri sağlayan logların gözükmesini sağlayabilirsiniz. Çıkan arama sonuçlarını kaydedip daha sonra tekrar bakabilirsiniz. Aynı zamanda Auto-refresh özelliği ile istenilen aralıkta sayfanın tekrar yüklenmesini ve yeni logların gelmesini sağlayabilirsiniz. Sol kısımda yer alan adlarına tıklayarak belirli bir alan adına veya belirli bir alanın belirli bir değerine göre logları filtreleyebilirsiniz. 

Discover tabıdan farklı olarak ayrıca Visualize kısmında kaydettiğiniz bir arama sonucu üzerinde istediğiniz görsel grafikleri hazırlayabilirsiniz. Kibana aşağıda listelenen grafik ve görsel çeşitlerini desteklemektedir.
* Area Chart: Farklı serilerin toplama katkısını gösteren alan grafiği.
* Data Table: Verileri görselleştirmek için kullanılan veri tablosu.
* Line chart: Farklı serileri karşılaştırmaya yarayan çizgi grafik.
* Markdown Widget: Belirli bir değeri veya hazırlanan Dashboard hakkında bilgiyi göstermek için kullanılan kutucuk.
* Metric: Dashboard üzerinde tek bir sayısal değeri göstermek için kullanılan metrik.
* Pie Chart: Her kaynağın toplama katkısını gösteren yuvarlak diyagram.
* Tile map: Coğrafik koordinatlar içeren verinin harita üzerinde gösterimini sağlayan harita.
* Vertical bar chart: Genel veri amaçlı kullanılan dikey çubuk grafik.

Yukarıda bahsedilen görselleri birleştirerek Dashboard kısmında kullanıcıların direk olarak görebileceği bir gösterge paneli oluşturabilirsiniz. 

Bu kısımda bu görsellere kasıtlı olarak örnekler verilmemiştir, çünkü ne tür görsellerin oluşturulabileceği kullanım senaryoları kısmında detaylı olarak anlatılacaktır.

# 3. Elasticsearch-Logstash-Kibana Entegrasyonu
Bu kısımdaki adımların gerçekleştirilebilmesi için Elasticsearch, Logstash ve Kibana’nın kurulum kısımlarında bahsedildiği gibi kurulması gerekmektedir. 

Entegrasyon için ilk olarak Logstash’in aldığı logları Elasticsearch’e vermesini sağlamamız gerekmektedir. Bunun için Logstash output konfigürasyon dosyası oluşturmamız gerekiyor. Aşağıda verilen dosyayı /etc/logstash/conf.d/30-output.conf olarak oluşturalım.

![alt text](images/18.png)

Yukarıdaki konfigürasyon dosyası içerisinde elasticsearch ve stdout pluginleri kullanıldı. Elasticsearch plugini gelen logların localhostta çalışan elasticsearch’e logstash-yıl.ay.gün şeklinde endekslenmesini ve bu endekslemenin http protokolü üzerinden yapılmasını söylemektedir. Stdout plugini ise bu logların aynı zamanda /var/log/logstash/logstash.stdout dosyasına da yazılmasını söylemektedir. Logların elasticsearch’e taşınmasının ardından bir sonraki adım Kibana’ya bu endeksin verilmesidir. Bunun için Kibana arayüzüne girin ve endeks adı istenilen kısma logstash-* ifadesini giriniz. Bu sayede logstash- ile başlayan tüm endeksler Kibana tarafından alınıp görselleştirilecektir. Fakat şu aşamada bu endekslerde herhangi bir veri olmadığı için Kibana bu endeksi oluşturamayacak, bu yüzden Logstash e örnek bir input sağlayalım ve Kibana’nın düzgün olarak ayarlanmış olup olmadığını kontrol edelim. Bunun için Logstash’e aşağıdaki input-output konfigürasyonunu girelim.

![alt text](images/19.png)

Bu konfigürasyon dosyasını kullanmak için aşağıdaki komutu girelim.
```sh
./opt/logstash/bin/logstash -f /etc/logstash/conf.d/deneme.conf
```
Burada bahsedilen deneme.conf dosyası yukarıda içeriği verilen dosyadır. Burada input olarak standart inputu kullanmasını ve bunu elasticsearche yollamasını söyledik. Şimdi ise aşağıdaki gibi birkaç girdi sağlayalım.

![alt text](images/20.png)

Bu şekilde elasticsearch’e girdiler sağlandıktan sonra logstash- ile başlayan bir endeks otomatik olarak oluşturulmuş oluyor. Kibana sayfasında artık bu endeksi kaydedip girdiğimiz kayıtları görebiliriz. Bunun için Kibana anasayfasında çıkan sayfada create butonuna basarak endeksi oluşturun. Bundan sonra Discover tabına basıldığında aşağıdaki gibi kayıtlar gelecektir.

![alt text](images/21.png)

Böylece Elasticsearch-Logstash-Kibana entegrasyonunu tamamlamış oluyoruz. Bundan sonraki kısımlarda ELK Stack’in gerçek hayatta nerelerde kullanabileceğini örneklerle inceleyeceğiz.

# 4. Kullanım Senaryoları
Bu kısımda kullanılam tüm yazılımlar Centos 7 işletim sistemi üzeride kurulmuştur. Tüm uygulamalar için tek bir ELK sunucusu kullanılmıştır. Bunun dışında Bro IDS, Suricata ve pfSense için farklı sunucular kurulmuştur. PfSense dışındaki sanal makineler aşağıda linki verilen zip dosyasının içinde bulunabilir.

## 4.1. ELK ile Bro IDS Loglarının Yönetimi
Bro IDS anormallik tabanlı bir saldırı tespit sistemidir. Ağda oluşan trafiği inceleyerek, anormalliklere bakmakta ve buna göre saldırıları tespit etmektedir. Fakat sadece saldırıları loglamamakta aynı zamanda HTTP, SSH, FTP, DNS gibi protokollere ait trafikleri de loglamaktadır. Bunun dışında indirilen dosyalara ait bir log dosyası, beklenmedik ağ trafikleri için bir log dosyası gibi protokollerden bağımsız log dosyaları da içermektedir. Bu açıdan sadece saldırı tespit sistemi olarak değil, aynı zamanda ağ faaliyetleri takip etmek için de kullanılabilmektedir. Bro IDS için ayrıca bir doküman hazırlanması gerekmektedir. Bu çalışma kapsamında sadece Bro IDS ve ELK Stack entegrasyonu anlatılacak olup, Bro IDS hakkında detaylı bilgi internetten edinilebilir.

### 4.1.1. Bro IDS Kurulumu
Bro IDS trafiği dinlediği ve dinlediği trafik üzerinde işlemler yaptığı için dışarıdan bazı kütüphanelere ihtiyaç duymaktadır. Bu yüzden ilk olarak gereken kütüphaneleri ve programları yüklüyoruz.
```sh
yum install cmake make gcc gcc-c++ flex bison libpcap-devel openssl-devel python-devel swig zlib-devel perl
```
Bro IDS’in de GeoIP veritabanını kullanması için aşağıdaki komutları çalıştırıyoruz.
```sh
yum install GeoIP-devel
wget http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz
gunzip GeoLiteCity.dat.gz
mv GeoLiteCity.dat /usr/share/GeoIP/GeoIPCity.dat
```
Bro IDS trafiği sürekli olarak dinlediği ve bu trafik üzerinde pek çok analiz işlemi gerçekleştirdiği için yüksek performans gereksinimlerine sahiptir. Var olan kaynakların daha verimli kullanılabilmesi için bazı performans geliştirici araçların yüklenmesi faydalı olacaktır. Bunun için aşağıdaki komutlarda yer alan araçları yüklüyoruz.
```sh
yum install gawk
yum install gperftools
wget http://www.read.seas.harvard.edu/~kohler/ipsumdump/ipsumdump-1.85.tar.gz
tar -xvf ipsumdump-1.85.tar.gz
cd ipsumdump-1.85
./configure --prefix=/usr/
make 
make install
```
Bu aşamaya kadar Bro IDS kurulumu için gerekli ve tavsiye edilen araç ve kütüphaneleri eklemiş bulunuyoruz. Şimdi ise sıra Bro IDS’i indirip kurmakta. Öncelikle sitesinden en güncel versiyonunu öğrenip bu versiyon için yükleme dosyasını indiriyoruz ve kuruyoruz.
```sh
cd /usr/share
wget https://www.bro.org/downloads/release/bro-2.4.1.tar.gz
tar -xvf bro-2.4.1
./configure
make
make install
```
Bro yüklendikten sonra ilgili dosyalar /usr/local/bro dizini altında bulunmaktadır. Bu dizinde /bin klasörünün altında Bro nun betikleri bulunmaktadır. Bu betikler sayesinde Bro için gereken ayarlar hızlı bir şekilde yapılabilmektedir. Bu betiklere her yerden ulaşabilmek için çevre değişkenlerine bu betiklerin bulunduğu klasörün yolunu aşağıdaki gibi ekleyelim.
```sh
export PATH=/usr/local/bro/bin:$PATH
```
Bu komut tek seferlik olarak çalışmaktadır. Yani bilgisayarı kapatıp tekrar açtığınızda yeniden eklemeniz gerekecektir. Bunu engellemek için bu komutu ~/.bashrc dosyasına yazabilirsiniz.
Bro yüklendikten sonra düzgün çalışabilmesi için bazı ayarların değiştirilmesi gerekmektedir. Bro konfigürasyon dosyaları /usr/local/bro/etc klasörü altında bulunmaktadır. Bu klasördeki node.cfg dosyası içerisinde trafiğin dinleneceği interface adı yer almaktadır. Buraya uygun değeri giriniz. Aynı şekilde networks.cfg dosyası içerisinde de izlenecek IP adres aralığı yer almaktadır. Buraya da uygun değerleri giriniz. Bunların dışında broctl.cfg dosyası içerisinde mail seçenekleri, loglama seçenekleri bulunmaktadır. Bro için genel kontrol ve ayarlama işlemleri broctl sayesinde yapılabilmektedir. Bunun için daha önce eklediğimiz betiklerden broctl’yi kullanıyoruz. Komut satırına broctl yazdığınızda aşağıdaki gibi size ayrı bir kontrol satırı getirecektir.

![alt text](images/22.png)

Bro kontrol satırında ilk önce install komutu çalıştırınız, bu sayede konfigürasyon dosyaları yüklenmiş olacak. Bundan sonra start komutunu yazdığınızda Bro çalışmaya başlamış olacak. Bunlara ek olarak Bro’nun genel bakım işlerinin yapılması için bir cronjob oluşturunuz. Bunun için crontab -e komutunu çalıştırdıktan sonra gelen ekranda 
```
0-59/5 * * * * /usr/local/bro/bin/broctl cron
``` ifadesini ekleyiniz. Başlangıçtaki süreyi kendi isteğinize göre ayarlayabilirsiniz. Bundan sonra Bro’nun oluşturduğu logları /usr/local/bro/logs/current klasörü altında görebilirsiniz. Log üretmek için internet tarayıcınızda birkaç site gezebilirsiniz. Logları http.log dosyasına ve diğer ilgili dosyalara düşecektir.

### 4.1.2. Logstash-forwarder Kurulumu
Bro IDS’in oluşturduğu log dosyalarını ELK sunucusuna aktarılabilmesi için ELK tarafındaki Logstash ile Bro IDS çalışan makinenin iletişim halinde olması gerekmektedir. Bu iletişimi logstash-forwarder sağlamaktadır. Logstash-forwarder ı kullanmak için öncelikle yüklememiz gerekiyor ve yüklemek için de yine öncelikle repo dosyasını /etc/yum.repos.d klasörü altına kaydetmemiz gerekiyor. Logstash-forwarder.repo dosyasını aşağıda görüldüğü gibi oluşturunuz ve daha sonra yum install logstash-forwarder komutunu çalıştırınız.

![alt text](images/23.png)

Logstash-forwarder yüklendikten sonra hangi dosyalarını nereye yollayacağını öğrenmesi için konfigürasyon dosyasında bazı yerlerin değiştirilmesi gerekiyor. Aşağıdaki resimde bu senaryo için gereken konfigürasyon dosyası verilmiştir.

![alt text](images/24.png)

Bu dosya içerisinde servers kısmı ELK Stack’in çalıştığı sunucunun IP adresi ve portudur. Burada verilen 5043 portu Logstash tarafından açılıp dinlenmesi gerekmektedir. Bunun nasıl yapılacağı bir sonraki kısım olan Logstash konfigürasyonunda anlatılacaktır. Ssl key ve ssl ca diye ifade edilen alanlar Logstash ile iletişim kurarken kullanılacak olan SLL anahtar ve sertifika dosyalarının yoludur. Bu dosyalar uyuşmazsa arada herhangi bir iletişim kurulamayacaktır. Dosyanın en alt kısmında yer alan kısımda logstash-forwarder’ın ileteceği dosyalar belirtilmektedir. *.log ifadesi ile Bro’nun ürettiği tüm logların ELK Stack’e atılması sağlanmaktadır. Her bir log dosyasının içeriği farklı olduğu için Logstash tarafında her bir log dosyası için ayrı bir filtre oluşturmak gerekmektedir. Fakat, bu zahmetten kurtulmak için Bro’nun logları json formatında alması sağlanabilmektedir. Bu sayede hangi dosya olursa olsun Logstash json formatını kullanarak logları alanlara ve değerlere ayırabilmektedir. Bu konfigürasyon kısmında yazan codec ile de logların json formatında olduğu belirtilmiş olmaktadır. En sonda yazan type kısmı ise Logstash tarafında pek çok kaynaktan veri geleceği için bu verilen ayırt edilmesi adına oluşturulmuştur. Bro logları Logstash tarafından bro_logs türünde kaydedilecektir. Böylece arama yapılırken hızlıca Bro logları ayırt edilebilir.
Bro’nun logları json formatında hazırlaması için Bro’nun kendine özgü betiklerinden hazırlamak gerekmektedir. Bro kendine has bir dil ile betik yazılmasını desteklemektedir. Bu sayede isteğe göre yeni log türleri veya saldırı analizleri yapılabilmektedir. Biz bu çalışma kapsamında sadece Bro’nun json formatında log almasını sağlayacak betikle ilgileneceğiz. Bro betik dili bu çalışma kapsamı dışında olduğu için bu betiğin nasıl hazırlandığı anlatılmaksızın direk olarak verilecektir. 

![alt text](images/25.png)

Oluşturduğumuz bu betiği /usr/local/bro/share/bro/policy/tuning dizini altında json-logs.bro olarak kaydediniz. Bro’nun hangi betikleri kullanıp hangilerini kullanmayacağını belirleyen dosya /usr/local/bro/share/bro/site/local.bro dosyasıdır. Bu dosya içerisine yazılan betikler Bro tarafından çalıştırılmaktadır. Hazırlanan betiğin eklenmesi için bu dosyanın herhangi bir satırına ```@load  /usr/local/bro/share/bro/policy/tuning/json-logs.bro``` ifadesini ekleyiniz. Yapılan değişikliklerin uygulanması için broctl ile Bro kontrol satırını açın ve check komutunu girerek betiklerde herhangi bir sorun olup olmadığını kontrol ediniz. Kontrol ettikten install komutuyla betikleri yükleyiniz ve restart ile de Bro’yu tekrar başlatınız. Artık log dosyalarının json formatında tutulduğunu gözlemleyebilirsiniz.

### 4.1.3. Logstash Konfigürasyonu
Öncelikle Logstash’in logstash-forwarder’dan logları alabilmesi için aşağıdaki konfigürasyon dosyasını /etc/logstash/conf.d dizini altında oluşturun.

![alt text](images/26.png)

Buradaki lumberjack plugini logstash-forwarder üzerinden log alımını sağlamaktadır. Logstash-forwarder lumberjack protokolünü kullandığı için bu plugin tercih edilmektedir. Buradaki port değeri Logstash’in logları dinleyeceği portun numarasıdır. Type değeri logstash-forwarder konfigürasyonunda da belirtildiği gibi gelen logların ayırt edilebilmesi için kullanılmaktadır. Ssl_certificate ve ssl_key alanları ise iki sistem arasındaki iletişimde SSL bağlantısında kullanılacak SSL sertifika ve anahtar dosyasının yolunu ifade etmektedir.
İnput konfigürasyonundan sonra bro loglarının anlamlandırılabilmesi için bir de filter konfigürasyon dosyası oluşturalım. Bu dosyaya da 10-broFilter.conf adını verelim.

![alt text](images/27.png)

Dosyanın en üstündeki if ifadesi bu filtrenin sadece bro\_logs türündeki verilere uygulanmasını sağlamaktadır. Ondan sonra gelen data plugini loglarla beraber gelen timestamp I Unix işletim sistemi timestampine çevirmektedir. Ondan sonraki geoip pluginleri loglarla beraber gelen IP bilgilerine bakarak konum bilgisi elde etmeyi sağlamaktadır. Translate plugini varsayılan olarak yüklü değildir. Bu plugin conn\_state alanındaki değerlerin yorumlanmasını ve yeni oluşturulan conn_state_full alanına yazılmasını sağlamaktadır. Bu plugini yüklemek için ```/opt/logstash/bin/plugin install logstash-filter-translate``` komutunu çalıştırınız. Translate plugininden sonra gelen mutate plugini bazı alanlar üzerinde değişim yapabilmemizi sağlamaktadır. Convert ile başlayan satırlar verilen alandaki verilerin istenilen tür şeklinde kaydedilmesini sağlamaktadır. Örneğin id.orig\_p alanı kaynak portu ifade etmektedir ve bir sayı değeridir. Bu yüzden onun integer olarak kaydedilmesi söylenmektedir. En alttaki rename ise belirli bir alanın adının değiştirilmesini sağlamaktadır. Örneğin daha anlaşılır olması için id.orig\_p id.orig\_port olarak değiştirilmiştir. Dosya oluşturulduktan sonra her zaman bir yanlışlık olup olmadığı aşağıdaki gibi kontrol edilmelidir.

![alt text](images/28.png)

Yapılan konfigürasyon değişikliklerinin uygulanması için logstash servisi yeniden başlatılmalıdır. Bunun için systemctl restart logstash.service komutu çalıştırılabilir. Logstash servisi yeniden başlatıldıktan sonra ```netstat -nlpt``` komutu ile açık portlar incelendiğinde 5043 numaralı portun artık açık olduğu gözlemlenebilir. Eğer port ipv6 trafiği için açılmışsa sistemde ipv6’yı kaldırmak için /etc/sysctl.conf dosyasına ```net.ipv6.conf.all.disable_ipv6 = 1``` satırını ekleyin ve sonrasında sysctl -p komutunu çalıştırın. Şimdi bu port üzerinden trafiğin başlaması için ELK sunucusundaki SSL sertifika ve anahtarlarını Bro’nun çalıştığı makineye kopyalayalım.
```sh
scp /etc/pki/tls/certs/logstash-forwarder.crt root@192.168.0.27:/etc/pki/tls/certs/
scp /etc/pki/tls/private/logstash-forwarder.key root@192.168.0.27:/etc/pki/tls/private/
```
Ayrıca ELK ile Bro makineleri arasında iptables in paketleri engellememesi için iptables’ı da kapatalım.
```sh
systemctl disable firewalld
systemctl stop firewalld
```
Yukarıda bahsedilen adımları doğru bir şekilde takip ettiyseniz ELK Stack’in Bro loglarını alması gerekmektedir. Eğer bir sorun varsa /var/log/logstash-forwarder.err dosyası incelenebilir. Eğer burada bir sorun yoksa loglar Bro makinesinden düzgün bir şekilde gönderiliyor fakat ELK sunucusu logları alamıyor demektir. Bunun için de ağ problemlerini gidermeye çalışınız.

### 4.1.4. Kibana ile Görselleştirme
Yukarıdaki konfigürasyon adımlarından sonra aşağıdaki gibi loglar Kibana'ya gelecektir.

![alt text](images/29.png)

Ve bu kayıtlar incelendiğinde aşağıdaki gibi tüm alanların doğru bir şekilde Logstash tarafından ayırt edildiği görülecektir.

![alt text](images/30.png)

Bu alanlardaki bilgiler kullanılarak Kibana Visualize kısmından çeşitli grafikler hazırlanabilir. Burada birkaç örnek vereceğiz fakat burada verilenlerin dışında daha pek çok kullanışlı grafik kolayca üretilebilir.
Örneğin aşağıdaki grafik Bro IDS loglarının id.orig_h yani kaynak ip adresi alanındaki değerlere göre çıkartılabilir. Böylece en çok hangi IP adresinden trafik üretildiği grafikle gözlemlenebilir.

![alt text](images/31.png)

Aynı şekilde Bro’nın ürettiği http loglarına bakılarak aşağıdaki gibi en çok ziyaret edilen internet sayfaları görselleştirilebilir.

![alt text](images/32.png)

Aşağıdaki grafikte de hangi log kaynağından ne kadar log geldiği tarih bazında incelenebilir. Bu aşamada sadece bro loglarıyla ilgilenildiği için çıkan sonuçta da sadece bro logları gözükmektedir.

![alt text](images/33.png)

## 4.2. ELK ile Suricata Loglarının Yönetimi
Suricata açık kaynak kodlu bir saldırı tespit ve engelleme sistemidir. Suricata da Bro IDS gibi saldırıları tespit edip loglamaktadır. Suricata saldırıları anormallik tabanlı değil de imza tabanlı olarak tespit etmektedir. Suricata’nın farklı loglama seçenekleri mevcuttur. Fakat ELK ile entegrasyonu için hem json formatında olan hem de en detaylı loglamayı yapan eve.json dosyası ELK sunucusuna aktarılacaktır. Bro IDS de olduğu gibi öncelikle Suricata kurulumu ve sonrasında logstash-forwarder ve logstash konfigürasyonu anlatılacaktır. 

### 4.2.1. Suricata Kurulumu
Öncelikle Suricata’nın çalışacağı yeni bir Centos sanal makine kurunuz. Kurulum tamamlandıktan sonra Suricata’yı yüklemek için aşağıdaki komutları çalıştırınız.
```sh
yum update
yum -y install gcc libpcap-devel pcre-devel libyaml-devel file-devel zlib-devel jansson-devel nss-devel libcap-ng-devel libnet-devel tar make libnetfilter_queue-devel lua-devel epel-release
yum install wget
wget http://www.openinfosecfoundation.org/download/suricata-3.1.1.tar.gz
tar -xvf suricata-3.1.1.tar.gz
cd suricata-3.1.1
./configure –prefix=/usr –sysconfdir=/etc –localstatedir=/var –enable-nfqueue –enable-lua
make
make install
ldconfig
make install-conf
make install-rules
make install-full
```
Suricata konfigürasyon dosyası /etc/suricata/suricata.yml dosyasıdır. Bu dosya içerisinde hangi log dosyalarının tutulacağı belirlenebilmektedir. Bu komutları başarıyla çalıştırdıktan sonra aşağıdaki komutu çalıştırarak Suricata’yı başlatabilirsiniz. 
```sh
suricata -c /etc/suricata/suricata.yml -i enp0s3
```
Suricata loglarının ELK sunucusuna aktarımı için yine logstash-forwarder kullanılacaktır. Bunun için daha önce bahsedildiği gibi öncelikle logstash-forwarder.repo dosyası oluşturulup yum install logstash-forwarder komutu çalıştırılmalıdır. Daha sonra logstash-forwarder.conf dosyası aşağıdaki gibi düzenlenmelidir.

![alt text](images/34.png)

Daha sonra SSL iletişimi için gerekli olan anahtar ve sertifika dosyalarını daha önce olduğu gibi ELK sunucusundan kopyalayınız.

### 4.2.2. Logstash Konfigürasyonu
Bro IDS için olduğu gibi Suricata için de logstash-forwarder yani lumberjack protokolü seçilmiştir. Bunun için aşağıdaki gibi yeni bir input konfigürasyon dosyası oluşturulmalıdır.

![alt text](images/35.png)

Aynı şekilde aşağıdaki gibi filter konfigürasyonunu da oluşturunuz.

![alt text](images/36.png)

 Yukarıdaki konfigürasyon dosyası en üstte bulunan if ifadesi sayesinde sadece suricata_logs türündeki kayıtlara uygulanacaktır. Bro IDS örneğinde bahsedildiği gibi geoip ve mutate pluginleri orada bahsedilen işlevlerini yerine getirmektedir.  

### 4.2.3. Kibana ile Görselleştirme

![alt text](images/37.png)

Yine görüldüğü üzere loglar Kibana arayüzünde gözüküyor. Yine Kibana ile bu loglardan bazı anlamlı grafikler çıkarmaya çalışalım. Örneğin aşağıdaki grafik saldırıların gelen kaynak IP lerinin geoip plugini ile yorumlanmasının ardından saldırı kaynaklarının coğrafik koordinatlarını gösteren bir haritadır.

![alt text](images/38.png)

Aynı grafik harita yerine yuvarlak diyagram olarak aşağıdaki gibi de gösterilebilir.

![alt text](images/39.png)

Benzer bir şekilde suricata loglarına bakılarak kullanılan user agentların bir listesi de çıkarılabilir.

![alt text](images/40.png)

Kibana ile daha pek çok görsel yapmak mümkündür, fakat bu kısımda sadece bu kadarıyla yetinilecektir.

## 4.3. ELK ile pfSense Loglarının Yönetimi
PfSense FreeBSD işletim sistemi üzerine kurulmuş bir güvenlik duvarı uygulamasıdır. Güvenlik duvarı her ağ için son derece yüksek bir öneme sahiptir. Bu yüzden güvenlik duvarının ürettiği loglar da son derece önem taşımaktadır. Çalışmanın bu kısmında pfSense güvenlik duvarı tarafından üretilen logların ELK sunucuya nasıl aktarılacağını anlatacağız. Ayrıca pfSense üzerinde de suricata kurarak onun da loglarını ELK sunucusuna nasıl aktarılacağını anlatacağız.

### 4.3.1. pfSense Syslog Loglarının Yönetimi
pfSense syslog loglarının aktarımı için log mesajlarını uzak bir syslog sunucusuna gönder seçeneğinin seçilip, ELK sunucusunun ip adresi ve logların alınacağı port numarasının girilmesi yeterli olacaktır. Bunun için pfSense yönetim arayüzünde Status/System Logs/Settings kısmına geliniz. Bu kısımda versiyona bağlı olarak aşağıda gördüğünüz ekrana benzer bir göreceksiniz. Buraya uygun ip adresi ve port değerlerini giriniz.

![alt text](images/41.png)

Burada ayrıca hangi logların aktarılacağını da seçebilirsiniz. Fakat seçtiğiniz loglara uygun logstash filtreleri yazmayı unutmayınız. PfSense tarafında sadece bu işlemlerin yapılması yeterli olacaktır. Bundan sonra logstash için input ve filter konfigürasyon dosyaları oluşturacağız.

![alt text](images/42.png)

Filter konfigürasyon dosyası ise aşağıya kopyalanmıştır.

```
filter {  
  if [type] == "syslog" {

    #change to pfSense ip address
    if [host] =~ /192\.168\.0\.2/ {
      mutate {
        add_tag => ["PFSense", "Ready"]
      }
    }

    if "Ready" not in [tags] {
      mutate {
        add_tag => [ "syslog" ]
      }
    }
  }
}

filter {  
  if [type] == "syslog" {
    mutate {
      remove_tag => "Ready"
    }
  }
}

filter {  
  if "syslog" in [tags] {
    grok {
      match => { "message" => "%{SYSLOGTIMESTAMP:syslog_timestamp} %{SYSLOGHOST:syslog_hostname} %{DATA:syslog_program}(?:\[%{POSINT:syslog_pid}\])?: %{GREEDYDATA:syslog_message}" }
      add_field => [ "received_at", "%{@timestamp}" ]
      add_field => [ "received_from", "%{host}" ]
    }
    syslog_pri { }
    date {
      match => [ "syslog_timestamp", "MMM  d HH:mm:ss", "MMM  dd HH:mm:ss" ]
      locale => "en"
    }

    if !("_grokparsefailure" in [tags]) {
      mutate {
        replace => [ "@source_host", "%{syslog_hostname}" ]
        replace => [ "@message", "%{syslog_message}" ]
      }
    }

    mutate {
      remove_field => [ "syslog_hostname", "syslog_message", "syslog_timestamp" ]
    }
#    if "_grokparsefailure" in [tags] {
#      drop { }
#    }
  }
}
filter {  
  if "PFSense" in [tags] {
    grok {
      add_tag => [ "firewall" ]
      match => [ "message", "<(?<evtid>.*)>(?<datetime>(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)\s+(?:(?:0[1-9])|(?:[12][0-9])|(?:3[01])|[1-9]) (?:2[0123]|[01]?[0-9]):(?:[0-5][0-9]):(?:[0-5][0-9])) (?<prog>.*?): (?<msg>.*)" ]
    }
    mutate {
      gsub => ["datetime","  "," "]
    }
    date {
      match => [ "datetime", "MMM dd HH:mm:ss" ]
      timezone => "UTC"
    }
    mutate {
      replace => [ "message", "%{msg}" ]
    }
    mutate {
      remove_field => [ "msg", "datetime" ]
    }
}
if [prog] =~ /^filterlog$/ {  
    mutate {
      remove_field => [ "msg", "datetime" ]
    }
    grok {
      patterns_dir => "/etc/logstash/conf.d/patterns"
      match => [ "message", "%{PFSENSE_LOG_DATA}%{PFSENSE_IP_SPECIFIC_DATA}%{PFSENSE_IP_DATA}%{PFSENSE_PROTOCOL_DATA}",
         "message", "%{PFSENSE_LOG_DATA}%{PFSENSE_IPv4_SPECIFIC_DATA_ECN}%{PFSENSE_IP_DATA}%{PFSENSE_PROTOCOL_DATA}" ]
    }
    mutate {
      lowercase => [ 'proto' ]
    }
    geoip {
      add_tag => [ "GeoIP" ]
      source => "src_ip"
      # Optional GeoIP database
      database => "/etc/logstash/GeoLiteCity.dat"
    }
  }
}
```

Konfigürasyon dosyası diğerlerine göre daha uzun olsa da aslında diğerlerinden farklı plugin içermemektedir. Tek farkı filter konfigürasyonu bir pattern dosyası kullanmaktadır. Pattern dosyaları sunucuya gelen logların formatının regex kullanılarak tanımlandığı dosyalardır. Her bir log türü için farklı bir pattern dosyası oluşturmak mümkündür. Ticari ürünlerin logları toplanırken uygun pattern dosyasının oluşturulması önem taşımaktadır. Burada kullanılan pattern dosyası /etc/logstash/patterns dizini altında bulunmaktadır ve içeriği aşağıdaki gibidir.

```
PFSENSE_LOG_DATA (%{INT:rule}),(%{INT:sub_rule}),,(%{INT:tracker}),(%{WORD:iface}),(%{WORD:reason}),(%{WORD:action}),(%{WORD:direction}),(%{INT:ip_ver}),
PFSENSE_IP_SPECIFIC_DATA (%{PFSENSE_IPv4_SPECIFIC_DATA}|%{PFSENSE_IPv6_SPECIFIC_DATA})
PFSENSE_IPv4_SPECIFIC_DATA (%{BASE16NUM:tos}),,(%{INT:ttl}),(%{INT:id}),(%{INT:offset}),(%{WORD:flags}),(%{INT:proto_id}),(%{WORD:proto}),
PFSENSE_IPv4_SPECIFIC_DATA_ECN (%{BASE16NUM:tos}),(%{INT:ecn}),(%{INT:ttl}),(%{INT:id}),(%{INT:offset}),(%{WORD:flags}),(%{INT:proto_id}),(%{WORD:proto}),
PFSENSE_IPv6_SPECIFIC_DATA (%{BASE16NUM:class}),(%{DATA:flow_label}),(%{INT:hop_limit}),(%{WORD:proto}),(%{INT:proto_id}),
PFSENSE_IP_DATA (%{INT:length}),(%{IP:src_ip}),(%{IP:dest_ip}),
PFSENSE_PROTOCOL_DATA (%{PFSENSE_TCP_DATA}|%{PFSENSE_UDP_DATA}|%{PFSENSE_ICMP_DATA}|%{PFSENSE_CARP_DATA})
PFSENSE_TCP_DATA (%{INT:src_port}),(%{INT:dest_port}),(%{INT:data_length}),(%{WORD:tcp_flags}),(%{INT:sequence_number}),(%{INT:ack_number}),(%{INT:tcp_window}),(%{DATA:urg_data}),(%{DATA:tcp_options})
PFSENSE_UDP_DATA (%{INT:src_port}),(%{INT:dest_port}),(%{INT:data_length})
PFSENSE_ICMP_DATA (%{PFSENSE_ICMP_TYPE}%{PFSENSE_ICMP_RESPONSE})
PFSENSE_ICMP_TYPE (?<icmp_type>(request|reply|unreachproto|unreachport|unreach|timeexceed|paramprob|redirect|maskreply|needfrag|tstamp|tstampreply)),
PFSENSE_ICMP_RESPONSE (%{PFSENSE_ICMP_ECHO_REQ_REPLY}|%{PFSENSE_ICMP_UNREACHPORT}| %{PFSENSE_ICMP_UNREACHPROTO}|%{PFSENSE_ICMP_UNREACHABLE}|%{PFSENSE_ICMP_NEED_FLAG}|%{PFSENSE_ICMP_TSTAMP}|%{PFSENSE_ICMP_TSTAMP_REPLY})
PFSENSE_ICMP_ECHO_REQ_REPLY (%{INT:icmp_echo_id}),(%{INT:icmp_echo_sequence})
PFSENSE_ICMP_UNREACHPORT (%{IP:icmp_unreachport_dest_ip}),(%{WORD:icmp_unreachport_protocol}),(%{INT:icmp_unreachport_port})
PFSENSE_ICMP_UNREACHPROTO (%{IP:icmp_unreach_dest_ip}),(%{WORD:icmp_unreachproto_protocol})
PFSENSE_ICMP_UNREACHABLE (%{GREEDYDATA:icmp_unreachable})
PFSENSE_ICMP_NEED_FLAG (%{IP:icmp_need_flag_ip}),(%{INT:icmp_need_flag_mtu})
PFSENSE_ICMP_TSTAMP (%{INT:icmp_tstamp_id}),(%{INT:icmp_tstamp_sequence})
PFSENSE_ICMP_TSTAMP_REPLY (%{INT:icmp_tstamp_reply_id}),(%{INT:icmp_tstamp_reply_sequence}),(%{INT:icmp_tstamp_reply_otime}),(%{INT:icmp_tstamp_reply_rtime}),(%{INT:icmp_tstamp_reply_ttime})

PFSENSE_CARP_DATA (%{WORD:carp_type}),(%{INT:carp_ttl}),(%{INT:carp_vhid}),(%{INT:carp_version}),(%{INT:carp_advbase}),(%{INT:carp_advskew})
```

Konfigürasyon dosyaları oluşturulduktan sonra logstash servisinin yeniden başlatılması yeterli olacaktır.

### 4.3.2. pfSense Suricata Loglarının Yönetimi
Öncelikle Suricata’yı pfSense üzerinde yüklemek için System/Package Manager/Available Packages tabına gidiniz. Burada Suricata’yı bulup install butonuna basarak yüklenmesini sağlayınız. Services/Suricata/Interfaces tabından bir arayüz seçerek Log Options kısmına geliniz. Aşağıdakine benzer bir ekran karşınıza gelecektir. Bu ekranda istediğiniz loglama ayarlarını seçebilirsiniz.

![alt text](images/43.png)

Bundan sonra Global Settings kısmından kuralları ekleyebilirsiniz. Kuralları almak için Updates kısmından güncelleyerek en yeni imzaları alabilirsiniz. Interfaces tabında Suricata’nın çalışır vaziyette olduğundan emin olunuz. Bunun için aşağıda da görebileceğiniz gibi Suricata yazan kısmın altında yeşil bir tik işareti olmalıdır.

![alt text](images/44.png)

Suricata loglarını konsoldan erişim sağlayarak veya arayüzden Logs View tabından görebilirsiniz. Arayüzdeki gerekli ayarlamalardan sonra pfSense’ e konsoldan erişim sağlayınız. Konsolda aşağıdaki komutları giriniz.
```sh
cd ~
fetch https://beats-nightlies.s3.amazonaws.com/jenkins/filebeat/426-79bd08a8db4487c0ddf72486cb1553ded7528df8/filebeat-freebsd-386
mkdir /etc/filebeat
mv filebeat-freebsd-386 /etc/filebeat/filebeat
chmod +x /etc/filebeat/filebeat
```
Önceki örneklerde logların ELK sunucusuna gönderilmesi için logstash-forwarder kullanılmıştı. Bunun dışında logların gönderimi için yine Elatic şirketinin geliştirdiği beat programları mevcut. Bu senaryomuzda filebeat kullanarak logların ELK sunucusuna gönderimini sağlayacağız. Fakat filebeat için de konfigürasyon dosyası oluşturmak gerekiyor. Bunun için aşağıdaki gibi filebeat.yml dosyasını oluşturunuz.

![alt text](images/45.png)

Aşağıdaki komutla konfigürasyon dosyasında herhangi bir hata olup olmadığını kontrol edebilirsiniz.
```sh
/etc/filebeat/filebeat -configtest
```
Filebeat’in pfSense üzerinde sistem açıldığında direk çalışması için shellcmd paketinin pfSense de yüklü olması gerekmektedir. Bunun için yine System/Package Manager/Available Packages tabından shellcmd’yi bulup install butonuna basınız. Shellcmd yüklendikten sonra Services/shellcmd tabına geçerek aşağıdaki gibi ```/etc/filebeat/filebeat``` komutunu ekleyiniz.

![alt text](images/46.png)

PfSense üzerinde bu adımların yapılması yeterli olacaktır. Bundan sonra yine Logstash konfigürasyon dosyalarının oluşturulması gerekmektedir. Öncelikle aşağıdaki input konfigürasyonunu oluşturunuz.

![alt text](images/47.png)

Görüleceği üzere diğer örneklerden farklı olarak burada beats plugini kullanıldı. Filebeat gibi beat çerçevesi programlarının input konfigürasyonlarında beats plugini kullanılmaktadır. Daha önce Suricata senaryosunda oluşturduğumuz konfigürasyon dosyasına çok benzer bir şekilde aşağıdaki filter konfigürasyon dosyasını da oluşturunuz.

![alt text](images/48.png)

Bundan sonra daha önce belirtildiği gibi konfigürasyon dosyalarını kontrol ettikten sonra logstash servisini tekrar başlatabilirsiniz. Bu adımları başarılı bir şekilde takip ettiyseniz aşağıdaki gibi Kibana arayüzü üzerinde logları görebilirsiniz.

![alt text](images/49.png)
