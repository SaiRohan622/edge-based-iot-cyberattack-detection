import argparse
import json
import time

import paho.mqtt.client as mqtt


BROKER = "localhost"
PORT = 1883

TOPIC = "sensors/home/temperature"


def run(rate, duration):

    print("=" * 55)
    print("MQTT FLOOD SIMULATION")
    print("=" * 55)

    print("Rate:", rate, "messages/second")
    print("Duration:", duration, "seconds")

    client = mqtt.Client(
        client_id="flood_simulator"
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

    client.loop_start()

    interval = 1.0 / rate

    start = time.monotonic()

    count = 0

    try:

        while time.monotonic() - start < duration:

            payload = {
                "device_id": "pico-001",
                "timestamp": int(time.time()),
                "temperature": 25.0,
                "humidity": 50.0,
                "unit": "C"
            }

            result = client.publish(
                TOPIC,
                json.dumps(payload),
                qos=0
            )

            if result.rc == mqtt.MQTT_ERR_SUCCESS:

                count += 1

            time.sleep(interval)

    except KeyboardInterrupt:

        print("\nSimulation stopped.")

    client.loop_stop()
    client.disconnect()

    print("\nTotal messages:", count)
    print("Flood simulation completed.")


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--rate",
        type=int,
        default=150
    )

    parser.add_argument(
        "--duration",
        type=int,
        default=10
    )

    args = parser.parse_args()

    run(
        args.rate,
        args.duration
    )