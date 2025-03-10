# IOT Kettle
Evdeki kettle'ı internete bağlayan bir projedir.
Micropython ile yazıldı.
ESP8266 ile deneme gerçekleştirildi.
Tek röle bağlandı, röle GPIO0 pinine bağlandı.
WifiManager kütüphanesi ile kurulum modu eklendi.

## Özellikler
* Ilk çalışmada Access Point olarak çalışacaktır. WifiKettle adı ile ve şifresi yoktur, bu AP'ye bağlanıp "192.168.4.1" adresine giderek herhangi bir modeme bağlayın, daha sonra konsoldan ip adresini alın. http://ipadresi:3001 portu üzerinden web sayfası yayını yapacaktır cihaz.
* 3001 portundan bağlanılan web sayfası ile belirtilen pin açılıp kapatılabiliyor. Ben bu pine bir röle bağlayıp açıp, kapatma işlemini gerçekleştirdim.
* 3001 portundan girilen web sayfasından saat kurularak yine aynı pinin o saatte çalışması sağlanabiliyor.
* saat.py dosyasından NTP ile internetten saat çekilir, Türkiye için olduğundan UTC +3 olarak ayarlıdır.

## Kaynaklar 
[NODEMCU Pinout](https://i0.wp.com/randomnerdtutorials.com/wp-content/uploads/2019/05/ESP8266-NodeMCU-kit-12-E-pinout-gpio-pin.png?quality=100&strip=all&ssl=1) <br>
[ESP-01 Pinout](https://raw.githubusercontent.com/AchimPieters/ESP8266-12F---Power-Mode/master/ESP8266_01X.jpg) <br>
[ESP-01 Bootloader Mode](https://i.stack.imgur.com/l5rRA.jpg) <br>
[Micropython ESP8266](https://docs.micropython.org/en/latest/esp8266/tutorial/intro.html) <br>
[tzapu /WiFiManager](https://github.com/tzapu/WiFiManager) <br>
