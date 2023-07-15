# WhatsApp Mesaj Toplayıcı ve Twitter'a Otomatik Tweetleme

Bu proje, WhatsApp grubunda belirli bir kullanıcının mesajlarını toplayan ve bu mesajları otomatik olarak Twitter hesabınızda paylaşan bir otomasyon aracıdır.

## Nasıl Çalışır?
Bu projede iki ana bileşen vardır:

- WhatsApp Mesaj Toplayıcı (py2txt): Bu bölüm, Python'un Selenium kütüphanesi kullanılarak WhatsApp Web'e giriş yapar ve belirlenen bir gruptaki belirli bir kullanıcının mesajlarını toplar. Toplanan mesajlar "collected_msgs.txt" adlı bir metin dosyasında saklanır.
- Twitter'a Otomatik Tweetleme (py2twitter): Bu bölüm, belirli bir metin mesajınızı Twitter hesabınızda paylaşmanıza olanak tanır. Bunun için tweepy adlı bir Twitter API kütüphanesi kullanılır.
  

## Gereksinimler

selenium ve tweepy kütüphaneleri. 
Kurulum için `pip install selenium tweepy` komutu kullanılır.

## Kullanım
keys_text.py adlı dosyanın içine Twitter API erişim anahtarlarınızı ve diğer gizli bilgilerinizi bu dosyada tanımlayın:\
`bearer_token = "YOUR_BEARER_TOKEN"`\
`api_key = "YOUR_API_KEY"`\
`api_key_secret = "YOUR_API_KEY_SECRET"`\
`access_token = "YOUR_ACCESS_TOKEN"`\
`access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"`\ 
main.py dosyasında `run_collector_and_tweet()` fonksiyonunu çağırarak uygulamayı çalıştırabilirsiniz.

## Notlar
- Kodun çalışması için bilgisayarınızda Google Chrome tarayıcısı ve **chromedriver** adlı sürücünün yüklü olması gerekmektedir. Ayrıca, chromedriver sürücüsünün PATH değişkenine eklenmesi gerekebilir.
- WhatsApp'a otomatik mesaj gönderme işlemi, kullanıcı deneyimini ve WhatsApp'ın hizmet şartlarını ihlal edebileceği için dikkatli kullanılmalıdır.
- Twitter API kullanımı için gizli bilgileri gizli tutun ve dosyanızı güvenli bir şekilde saklayın. Bu bilgileri paylaşmayın veya GitHub gibi ortak depolama alanlarında depolamayın.
