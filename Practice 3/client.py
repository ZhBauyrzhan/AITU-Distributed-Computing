from email import message
from http import client
from threading import Thread
import paho.mqtt.client as mqtt


class Client:
    def __init__(self, host, mqtt_port, keepalive):
        self.host = host
        self.mqtt_port = mqtt_port
        self.keepalive = keepalive
        self.mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
        
        self.mqttc.on_connect = self._on_connect
        self.mqttc.on_message = self._on_message

    
    def _on_connect(self, client, userdata, flags, reason_code, properties):
        if reason_code.is_failure:
            print(f"Failed to connect: {reason_code}.")
        else:
            print("Connected")

    def _on_message(self, client, userdata, message):
        print(f'we got thos messages {message.payload}')

    def write(self):
        while True:
            message = input("Type message: ")
            if message == "EXIT":
                self.mqttc.disconnect()
                break
            else:
                self.mqttc.publish('chat/general', message, 2)

    def connect(self):
        self.mqttc.connect(self.host, self.mqtt_port, self.keepalive)
        self.mqttc.loop_start()
        self.mqttc.subscribe('chat/general', 2)
        write = Thread(target=self.write)
        write.run()
   
client = Client("localhost", 1885, 60)
client.connect()
