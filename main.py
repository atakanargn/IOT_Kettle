import wifimgr
from time import sleep
import machine
from machine import Pin
import os

led = Pin(0, Pin.OUT)
led.value(0)

wlan = wifimgr.get_connection()
if wlan is None:
    print("Could not initialize the network connection.")
    while True:
        pass  

wlan.config(dhcp_hostname = 'wifikettle')

print("ESP OK")

from saat import gettime
try:
  import usocket as socket
except:
  import socket
  
alarm = [8, 0]
calisti=False

def web_page():
  if led.value() == 1:
    gpio_state="AÇIK"
  else:
    gpio_state="KAPALI"
  
  html = """<html><head> <meta charset="UTF-8"><title>WiFi Kettle</title> <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="icon" href="data:,"> <style>html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
  h1{color: #0F3376; padding: 2vh;}p{font-size: 1.5rem;}.button{display: inline-block; background-color: #e7bd3b; border: none; 
  border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
  .button2{background-color: #4286f4;} .button3{background-color: #42f454;}</style></head><body style="margin-top:200px;"> <h1>WiFi Kettle</h1> 
  <p>Kettle Durum: <strong>""" + gpio_state + """</strong></p><p><a href="/?kettle=1"><button class="button">AÇ</button></a>
  <a href="/?kettle=0"><button class="button button2">KAPAT</button></a></p>
  <p>
  <form method="get" action="/">
  <input type="number" min="0" max="23" name="saat" value="{}" />
  <br/>
  <button class="button button3">KAYDET</button>
  </form>
  </p>
  </body></html>""".format(alarm[0],alarm[1])
  return html

def params(request,query):
    try:
        try:
            return request.split("/?{}=".format(query))[1].split("&")[0].split(" ")[0].rstrip().strip()
        except:
            return request.split("/?{}=".format(query))[1].split(" ")[0].rstrip().strip()
    except Exception as e:
        return -1
    
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 3001))
s.listen(5)

def alarmKontrol():
    global calisti
    while True:
        if gc.mem_free() < 102000:
          gc.collect()
        saatData = gettime()
        if saatData != -1:
            saat, dakika = saatData[4],saatData[5]
            print(saat,dakika)
        
        if alarm[0] == saat and calisti==False:
            calisti=True
            led.value(1)
            for i in range(0,90):
                sleep(1)
            led.value(0)
            break
        
        if saat >= alarm[0]+1:
            calisti=False
            break
        sleep(1)

while True:
    if gc.mem_free() < 102000:
      gc.collect()
    conn, addr = s.accept()
    request = conn.recv(1024)
    request = str(request)
    
    try:
        if params(request,"kettle")!=-1:
          led.value(int(params(request,"kettle")))
    except:
        pass
    
    try:
        if params(request, "saat")!=-1:
            alarm[0] = int(params(request, "saat"))
            calisti=False
            alarmKontrol()
    except:
        pass
    
    response = web_page()
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)
    conn.close()
    sleep(0.05)