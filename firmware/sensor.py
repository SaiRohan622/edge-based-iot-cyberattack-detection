# ================================================================
# DHT11 Sensor Driver
# ================================================================

import dht
import machine
import json
import time


class DHT11Sensor:

    def __init__(self, pin, device_id):

        self.pin = machine.Pin(pin)
        self.sensor = dht.DHT11(self.pin)
        self.device_id = device_id

    def read(self):

        try:

            self.sensor.measure()

            temperature = self.sensor.temperature()
            humidity = self.sensor.humidity()

            return {
                "device_id": self.device_id,
                "timestamp": time.time(),
                "temperature": temperature,
                "humidity": humidity,
                "unit": "C"
            }

        except OSError as error:

            print("[SENSOR] Read error:", error)

            return None

    def read_json(self):

        data = self.read()

        if data is not None:
            return json.dumps(data)

        return None