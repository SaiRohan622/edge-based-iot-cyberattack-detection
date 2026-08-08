# ================================================================
# IoT Cyberattack Detection
# Raspberry Pi Pico + DHT Sensor
# ================================================================

import network
import time
import json
import machine

import config

from sensor import DHT11Sensor
from mqtt_client import PicoMQTTClient


# ------------------------------------------------
# On-board LED
# ------------------------------------------------

led = machine.Pin("LED", machine.Pin.OUT)


def blink(times=1, delay_ms=200):

    for _ in range(times):

        led.on()
        time.sleep_ms(delay_ms)

        led.off()
        time.sleep_ms(delay_ms)


# ------------------------------------------------
# Wi-Fi
# ------------------------------------------------

def connect_wifi():

    wlan = network.WLAN(network.STA_IF)

    wlan.active(True)

    if wlan.isconnected():

        print("[WIFI] Already connected")
        print(wlan.ifconfig()[0])

        return True

    print("[WIFI] Connecting...")

    wlan.connect(
        config.WIFI_SSID,
        config.WIFI_PASSWORD
    )

    for attempt in range(config.WIFI_RETRY_COUNT):

        if wlan.isconnected():

            print("[WIFI] Connected")
            print("[WIFI] IP:", wlan.ifconfig()[0])

            blink(3, 150)

            return True

        print(
            "[WIFI] Waiting...",
            attempt + 1
        )

        time.sleep_ms(
            config.RETRY_DELAY_MS
        )

    return False


# ------------------------------------------------
# Main
# ------------------------------------------------

def main():

    print("=" * 50)
    print("IoT Cyberattack Detection")
    print("Device:", config.DEVICE_ID)
    print("=" * 50)

    # Wi-Fi
    if not connect_wifi():

        print("[MAIN] Wi-Fi connection failed")

        while True:

            blink(5, 100)

            time.sleep(5)

    # Sensor
    sensor = DHT11Sensor(
        config.DHT_PIN,
        config.DEVICE_ID
    )

    print(
        "[SENSOR] Initialized on GPIO",
        config.DHT_PIN
    )

    # MQTT
    mqtt = PicoMQTTClient()

    retry = 0

    while not mqtt.connect():

        retry += 1

        if retry > config.MQTT_RETRY_COUNT:

            print("[MAIN] MQTT failed")

            machine.reset()

        time.sleep_ms(
            config.RETRY_DELAY_MS
        )

    # Online status
    status = {
        "device_id": config.DEVICE_ID,
        "status": "online",
        "timestamp": time.time()
    }

    mqtt.publish(
        config.TOPIC_STATUS,
        json.dumps(status),
        qos=1
    )

    blink(2, 300)

    # ------------------------------------------------
    # Sensor loop
    # ------------------------------------------------

    while True:

        data = sensor.read()

        if data is not None:

            payload = json.dumps(data)

            mqtt.publish(
                config.TOPIC_SENSOR,
                payload
            )

            print("[SENSOR]", payload)

        time.sleep_ms(
            config.PUBLISH_INTERVAL_MS
        )


main()