#!/usr/bin/python3
import paho.mqtt.client as mqtt
import time
import json
import serial
from datetime import datetime



iot_hub = "104.40.7.210"
port = 1883

Trung1 ="ble1Token"
Trung2 ="ble2Token"
Trung3 ="ble3Token"

Tung1 ="ble4Token"
Tung2 ="ble5Token"
Tung3 ="ble6Token"
Tung4 ="ble7Token"

password =""
topic ="v1/devices/me/telemetry"

client = mqtt.Client()


print("Connection success")

bleSer = serial.Serial('/dev/ttyAMA0', baudrate = 9600, stopbits = serial.STOPBITS_ONE)
#bleSer = serial.Serial('/dev/ttyUSB0', baudrate = 9600, stopbits = serial.STOPBITS_ONE)
#bluetoothSerial.open() '/dev/ttyAMA0'  /dev/ttyUSB0

data=dict()
dataTrung2 = dict()
dataTrung3 = dict()

dataTung2 = dict()
dataTung3 = dict()
dataTung4 = dict()
while True:
     now = datetime.now()
     time = now.strftime("%d/%m/%Y %H:%M:%S")
     info = bleSer.readline()
     data2 = info.decode()
     data2 = data2.rstrip()

     if data2.rfind("xx")==0:
        data2 = data2.lstrip("xx")
        print("Tem: " + data2)
        client.username_pw_set(Trung1,password)       
        client.connect(iot_hub,port)
        data["temperature"] = data2
        data_out = json.dumps(data)
        client.publish(topic,data_out,0)
        #client.disconnect()

     if data2.rfind("zz")==0:
        data2 = data2.lstrip("zz")
        print("TDS: " + data2)
        print(time)
        print("-------------------------------------------")
        client.username_pw_set(Trung1,password)
        client.connect(iot_hub,port)
        data["tds"] = data2
        data_out = json.dumps(data)
        client.publish(topic,data_out,0)
        #client.disconnect()
     if data2.rfind("yy")==0:
        data2 = data2.lstrip("yy")
        print("pH: " + data2)
        client.username_pw_set(Trung1,password)
        client.connect(iot_hub,port)
        data["ph"] = data2
        data_out = json.dumps(data)
        client.publish(topic,data_out,0)
        #client.disconnect()
     if data2.rfind("aa")==0:
        data2 = data2.lstrip("aa")
        print("NH4: " + data2)
        client.username_pw_set(Trung2,password)
        client.connect(iot_hub, port, 60)
        client.loop_start()
        dataTrung2["nh4"] = data2
        time.sleep(5)
        data_out = json.dumps(dataTrung2)
        client.publish(topic, data_out, 1)
        client.loop_stop()
        client.disconnect()   
     if data2.rfind("ab")==0:
        data2 = data2.lstrip("ab")
        print("CO2: " + data2)
        client.username_pw_set(Trung2,password)
        client.connect(iot_hub,port)
        dataTrung2["co2"] = data2
        data_out = json.dumps(dataTrung2)
        client.publish(topic,data_out,0)
        #client.disconnect()
     if data2.rfind("ac")==0:
        data2 = data2.lstrip("ac")
        print("Rain: " + data2)
        print(time)
        print("-------------------------------------------")
        client.username_pw_set(Trung2,password)
        client.connect(iot_hub,port)
        dataTrung2["rain"] = data2
        data_out = json.dumps(dataTrung2)
        client.publish(topic,data_out,0)
        #client.disconnect() 
     if data2.rfind("ad")==0:
        data2 = data2.lstrip("ad")
        print("CO: " + data2)
        client.username_pw_set(Trung3,password)
        client.connect(iot_hub,port)
        dataTrung3["co"] = data2
        data_out = json.dumps(dataTrung3)
        client.publish(topic,data_out,0)
        #client.disconnect()
     if data2.rfind("ae")==0:
        data2 = data2.lstrip("ae")
        print("Tem: " + data2)
        client.username_pw_set(Trung3,password)
        client.connect(iot_hub,port)
        dataTrung3["temperature"] = data2
        data_out = json.dumps(dataTrung3)
        client.publish(topic,data_out,0)
        #client.disconnect()
     if data2.rfind("af")==0:
        data2 = data2.lstrip("af")
        print("Hum: " + data2)
        print(time)
        print("-------------------------------------------")
        client.username_pw_set(Trung3,password)
        client.connect(iot_hub,port)
        dataTrung3["humidity"] = data2
        data_out = json.dumps(dataTrung3)
        client.publish(topic,data_out,0)
        #client.disconnect()
     if data2.rfind("ca")==0:
        data2 = data2.lstrip("ca")
        print("LPG: "+data2)
        client.username_pw_set(Tung2,password)
        client.connect(iot_hub,port)
        dataTung2["lpg"] = data2
        data_out = json.dumps(dataTung2)
        client.publish(topic,data_out,0)
        #client.disconnect()
     if data2.rfind("cb")==0:
        data2 = data2.lstrip("cb")
        print("NH4: "+data2)
        client.username_pw_set(Tung2,password)
        client.connect(iot_hub,port)
        dataTung2["nh4"] = data2
        data_out = json.dumps(dataTung2)
        client.publish(topic,data_out,0)
        #client.disconnect()
     if data2.rfind("cc")==0:
        data2 = data2.lstrip("cc")
        print("CO2: "+data2)
        print(time)
        print("-------------------------------------------")
        client.username_pw_set(Tung2,password)
        client.connect(iot_hub,port)
        dataTung2["co2"] = data2
        data_out = json.dumps(dataTung2)
        client.publish(topic,data_out,0)
        #client.disconnect()
     if data2.rfind("cd")==0:
        data2 = data2.lstrip("cd")
        print("Lux: "+data2)
        client.username_pw_set(Tung3,password)
        client.connect(iot_hub,port)
        dataTung3["lux"] = data2
        data_out = json.dumps(dataTung3)
        client.publish(topic,data_out,0)
        #client.disconnect()
     if data2.rfind("ce")==0:
        data2 = data2.lstrip("ce")
        print("Rain: "+data2)
        client.username_pw_set(Tung3,password)
        client.connect(iot_hub,port)
        dataTung3["rain"] = data2
        data_out = json.dumps(dataTung3)
        client.publish(topic,data_out,0)
        #client.disconnect()
     if data2.rfind("cf")==0:
        data2 = data2.lstrip("cf")
        print("Temperature: "+data2)
        client.username_pw_set(Tung3,password)
        client.connect(iot_hub,port)
        dataTung3["temperature"] = data2
        data_out = json.dumps(dataTung3)
        client.publish(topic,data_out,0)
        #client.disconnect()
     if data2.rfind("cg")==0:
        data2 = data2.lstrip("cg")
        print("Humidity: "+data2)
        print(time)
        print("-------------------------------------------")
        client.username_pw_set(Tung3,password)
        client.connect(iot_hub,port)
        dataTung3["humidity"] = data2
        data_out = json.dumps(dataTung3)
        client.publish(topic,data_out,0)
        #client.disconnect()
     if data2.rfind("ch")==0:
        data2 = data2.lstrip("ch")
        print("PM 2.5: "+data2)
        print(time)
        print("-------------------------------------------")
        client.username_pw_set(Tung4,password)
        client.connect(iot_hub,port)
        dataTung4["pm25"] = data2
        data_out = json.dumps(dataTung4)
        client.publish(topic,data_out,0)
        #client.disconnect()
     if data2.rfind("ci")==0:
        data2 = data2.lstrip("ci")
        print("CO: "+data2)
        client.username_pw_set(Tung4,password)
        client.connect(iot_hub,port)
        dataTung4["co"] = data2
        data_out = json.dumps(dataTung4)
        client.publish(topic,data_out,0)
        #client.disconnect()

        
