import subprocess
import sys
from pathlib import Path
import time


BASE_DIR = Path(__file__).resolve().parent


ATTACKS = [

    (
        "Unauthorized Device",
        "rogue_device.py",
        [
            "--device-id",
            "rogue-device-99",
            "--count",
            "10",
            "--interval",
            "1"
        ]
    ),

    (
        "Fake Sensor Data",
        "fake_sensor_data.py",
        [
            "--temp",
            "999",
            "--humidity",
            "150",
            "--count",
            "5"
        ]
    ),

    (
        "MQTT Flood",
        "flood_attack.py",
        [
            "--rate",
            "150",
            "--duration",
            "10"
        ]
    )
]


def run_attack(name, script, arguments):

    print("\n" + "=" * 60)
    print("Running:", name)
    print("=" * 60)

    script_path = BASE_DIR / script

    subprocess.run(
        [
            sys.executable,
            str(script_path)
        ] + arguments,
        check=False
    )

    print("\nFinished:", name)

    time.sleep(2)


def main():

    print("=" * 60)
    print("IoT CYBERATTACK TEST SUITE")
    print("=" * 60)

    print("\nThese simulations are intended for your own")
    print("local MQTT lab environment.")

    for name, script, arguments in ATTACKS:

        run_attack(
            name,
            script,
            arguments
        )

    print("\n" + "=" * 60)
    print("ALL SIMULATIONS COMPLETED")
    print("=" * 60)


if __name__ == "__main__":
    main()