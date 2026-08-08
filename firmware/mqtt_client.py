# ================================================================
# MQTT Client for Raspberry Pi Pico
# ================================================================

import config

try:
    from umqtt.simple import MQTTClient
except ImportError:
    from umqtt_simple import MQTTClient


class PicoMQTTClient:

    def __init__(self):

        self.client = None
        self.connected = False

    def connect(self):

        try:

            self.client = MQTTClient(
                client_id=config.DEVICE_ID,
                server=config.MQTT_BROKER,
                port=config.MQTT_PORT,
                user=config.MQTT_USERNAME,
                password=config.MQTT_PASSWORD,
                keepalive=60
            )

            self.client.connect()

            self.connected = True

            print(
                "[MQTT] Connected:",
                config.MQTT_BROKER,
                config.MQTT_PORT
            )

            return True

        except Exception as error:

            print("[MQTT] Connection failed:", error)

            self.connected = False

            return False

    def publish(self, topic, payload, qos=0):

        if not self.connected:

            if not self.connect():
                return False

        try:

            self.client.publish(
                topic,
                payload,
                qos=qos
            )

            print("[MQTT] Published:", topic)
            print(payload)

            return True

        except Exception as error:

            print("[MQTT] Publish error:", error)

            self.connected = False

            return False

    def disconnect(self):

        if self.client and self.connected:

            try:
                self.client.disconnect()
            except:
                pass

        self.connected = False