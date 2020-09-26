from time import sleep
import json
from gpiozero import LED

class Curtain:
    def __init__(self):
        self.sun_info_json_file = 'suninfo.json'
        self.status = ''
        self.drive1 = LED(20)
        self.drive2 = LED(16)
        self.drive1.off()
        self.drive2.off()

    def set_status_to_json_file(self):
        with open(self.sun_info_json_file, 'r') as json_file:
            json_data = json.load(json_file)
            json_data['status'] = self.status
        
        with open(self.sun_info_json_file, 'w') as json_file:
            json.dump(json_data,json_file, indent=4)

    def get_status(self):
        with open(self.sun_info_json_file, 'r') as json_file:
            return json.load(json_file)['status']

    def open(self):
        self.status = 'open'
        self.set_status_to_json_file()
        sleep(0.1)
        self.drive1.on()
        self.drive2.off()
        sleep(3)

    def close(self):
        self.status = 'close'
        self.set_status_to_json_file()
        sleep(0.1)
        self.drive1.off()
        self.drive2.on()
        sleep(3)
