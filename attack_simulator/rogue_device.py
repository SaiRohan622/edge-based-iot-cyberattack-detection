import argparse
import json
import time

import paho.mqtt.client as mqtt


BROKER = "localhost"
PORT = 1883

TOPIC = "sensors/home/temperature"

DEFAULT_DEVICE = "rogue-device-99"


def run(device_id, count, interval):

    print("=" * 55)
    print("UNAUTHORIZED DEVICE SIMULATION")
    print("=" * 55)

    client = mqtt.Client(
        client_id=device_id
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
            "device_id": device_id,
            "timestamp": int(time.time()),
            "temperature": 25.0,
            "humidity": 50.0,
            "unit": "C"
        }

        client.publish(
            TOPIC,
            json.dumps(payload)
        )

        print(
            "[ROGUE] Message:",
            i + 1,
            "Device:",
            device_id
        )

        time.sleep(interval)

    client.disconnect()

    print("\nSimulation completed.")


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--device-id",
        default=DEFAULT_DEVICE
    )

    parser.add_argument(
        "--count",
        type=int,
        default=10
    )

    parser.add_argument(
        "--interval",
        type=float,
        default=3
    )

    args = parser.parse_args()

    run(
        args.device_id,
        args.count,
        args.interval
    )