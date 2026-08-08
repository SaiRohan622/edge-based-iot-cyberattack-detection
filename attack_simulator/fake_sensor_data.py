import argparse
import json
import time

import paho.mqtt.client as mqtt


BROKER = "localhost"
PORT = 1883

TOPIC = "sensors/home/temperature"


def run(temperature, humidity, count, interval):

    print("=" * 55)
    print("FAKE SENSOR DATA SIMULATION")
    print("=" * 55)

    client = mqtt.Client(
        client_id="fake_sensor"
    )

    try:

        client.connect(
            BROKER,
            PORT,
            60
        )

    except Exception as error:

        print("[ERROR] MQTT connection failed:", error)
        return

    for i in range(count):

        payload = {
            "device_id": "pico-001",
            "timestamp": int(time.time()),
            "temperature": temperature,
            "humidity": humidity,
            "unit": "C"
        }

        client.publish(
            TOPIC,
            json.dumps(payload)
        )

        print(
            "[FAKE DATA]",
            i + 1,
            payload
        )

        time.sleep(interval)

    client.disconnect()

    print("\nSimulation completed.")


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--temp",
        type=float,
        default=999
    )

    parser.add_argument(
        "--humidity",
        type=float,
        default=150
    )

    parser.add_argument(
        "--count",
        type=int,
        default=5
    )

    parser.add_argument(
        "--interval",
        type=float,
        default=1
    )

    args = parser.parse_args()

    run(
        args.temp,
        args.humidity,
        args.count,
        args.interval
    )
