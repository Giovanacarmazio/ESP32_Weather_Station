#Giovanaisabel Souza Carmazio
#2 periodo de analise e desenvolvimento de sistemas


import network
import time
import urequests
import dht
import machine

d = dht.DHT11(machine.Pin(13))
r = machine.Pin(2,machine.Pin.OUT)

def conecta(ssid, senha):
    import network
    import time
    station = network.WLAN(network.STA_IF)
    station.active(True)
    station.connect(ssid, senha)
    for t in range(50):
        if station.isconnected():
            break
        time.sleep(0.1)
    return station



while True:
    print("Conectando....")
    station = conecta("Carlos Suzuki","31415926")
    if not station.isconnected():
        print("Não conectado")
        time.sleep(2)
        
    else:
        print("Conectado!!!")
        d.measure()
        print("Temp={}  Umid{}".format(d.temperature(), d.humidity()))
        if ((d.temperature() > 31) or (d.humidity() > 70)):
            r.value(1)
            rele = 1
        else:
            r.value(0)
            rele = 0        
        print("Acessando o site....")
        #resposta = urequests.get("https://api.thingspeak.com/update?api_key=AH3LFDI1WBF8MJKV&field1=0")      
        resposta = urequests.get("https://api.thingspeak.com/update?api_key=AH3LFDI1WBF8MJKV&field1={}&field2={}&field3={}".format(d.temperature(), d.humidity(), rele))
        print(resposta.text)
        station.disconnect()
    time.sleep(5)   
