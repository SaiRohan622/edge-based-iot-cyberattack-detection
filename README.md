# Edge-Based IoT Cyberattack Detection and Automated Response System

An edge-oriented IoT cybersecurity system for monitoring MQTT-based sensor communication, detecting abnormal or malicious activity, and triggering automated responses through a Node-RED dashboard.

The project combines a Raspberry Pi Pico 2W-based sensing device, DHT sensor, MQTT communication, a local Mosquitto broker, Node-RED, and Python-based attack simulators to demonstrate detection of common IoT network attacks.

---

## 📌 Overview

IoT devices continuously exchange sensor data over lightweight communication protocols such as MQTT. Because MQTT is widely used in resource-constrained IoT environments, unauthorized devices, abnormal sensor values, and excessive message traffic can become security risks.

This project implements an edge-based monitoring and response pipeline:

```text
┌──────────────────────┐
│   IoT Sensor Device  │
│ Raspberry Pi Pico 2W │
│      + DHT Sensor    │
└──────────┬───────────┘
           │
           │ MQTT
           ▼
┌──────────────────────┐
│   Mosquitto Broker   │
│      Port: 1883      │
└──────────┬───────────┘
           │
           │ sensors/#
           ▼
┌──────────────────────┐
│      Node-RED        │
│ Detection + Response │
└──────────┬───────────┘
           │
           ├──────────────► Dashboard
           │
           ├──────────────► Alerts
           │
           └──────────────► Automated Response
```

Python attack simulators generate controlled test traffic against the local MQTT environment to evaluate the detection pipeline.

---

# 🎯 Objectives

- Monitor IoT sensor communication in real time.
- Detect abnormal MQTT traffic at the edge.
- Identify unauthorized or rogue devices.
- Detect abnormal or fake sensor values.
- Detect MQTT flooding based on message rate.
- Generate security alerts.
- Maintain attack logs and statistics.
- Provide automated response mechanisms.
- Visualize IoT security information through a Node-RED dashboard.
- Provide a reproducible environment for IoT cybersecurity experimentation.

---

# 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Raspberry Pi Pico 2W | IoT edge device |
| DHT Sensor | Temperature and humidity sensing |
| MicroPython | Pico firmware |
| MQTT | IoT communication protocol |
| Mosquitto | Local MQTT broker |
| Node-RED | Detection, processing and automation |
| FlowFuse Dashboard | Security monitoring dashboard |
| Python | Attack simulation and testing |
| Paho MQTT | Python MQTT communication |
| Git/GitHub | Version control and project hosting |

---

# 🏗️ System Architecture

```text
                    ┌─────────────────────┐
                    │     DHT Sensor      │
                    │ Temperature/Humidity│
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Raspberry Pi Pico 2W│
                    │    Edge Device      │
                    └──────────┬──────────┘
                               │
                               │ MQTT
                               ▼
                    ┌─────────────────────┐
                    │ Mosquitto MQTT      │
                    │ Broker              │
                    │ Port 1883           │
                    └──────────┬──────────┘
                               │
                               │ sensors/#
                               ▼
                    ┌─────────────────────┐
                    │      Node-RED       │
                    │                     │
                    │ • MQTT Monitoring   │
                    │ • JSON Processing   │
                    │ • Attack Detection │
                    │ • Response Logic    │
                    └──────────┬──────────┘
                               │
              ┌────────────────┼────────────────┐
              ▼                ▼                ▼
       ┌────────────┐   ┌────────────┐   ┌────────────┐
       │ Dashboard  │   │   Alerts   │   │ Response   │
       └────────────┘   └────────────┘   └────────────┘
```

---

# 🔐 Attack Detection

The current implementation contains three controlled attack simulations.

## 1. Unauthorized / Rogue Device

A simulated device publishes MQTT messages using an unauthorized device ID.

Example:

```json
{
  "device_id": "rogue-device-99",
  "temperature": 25,
  "humidity": 50
}
```

The detection system checks the device identity against the authorized device list.

### Detection Concept

```text
Incoming MQTT message
        │
        ▼
Extract device_id
        │
        ▼
Check authorized device list
        │
   ┌────┴────┐
   │         │
Known      Unknown
   │         │
Normal     ALERT
             │
             ▼
       Automated Response
```

---

## 2. Fake Sensor Data

The simulator publishes abnormal temperature or humidity values.

Example:

```json
{
  "device_id": "pico-001",
  "temperature": 999,
  "humidity": 150
}
```

The system checks whether the sensor values fall within the expected operating range.

This demonstrates how manipulated sensor data can be detected before it is treated as legitimate telemetry.

---

## 3. MQTT Flood Attack

The flood simulator generates a high rate of MQTT messages against the sensor topic.

The Node-RED flow monitors incoming MQTT traffic and calculates message frequency.

```text
Normal traffic
      │
      ▼
Message rate monitoring
      │
      ▼
Below threshold ─────► Normal


High traffic
      │
      ▼
Message rate monitoring
      │
      ▼
Above threshold ─────► MQTT Flood Alert
```

The project uses controlled high-rate test traffic to demonstrate MQTT flooding detection.

---

# 🖥️ Dashboard

The Node-RED dashboard provides a centralized security monitoring interface.

The dashboard can display information such as:

- Temperature
- Humidity
- Security status
- Latest security alert
- Attack count
- Network traffic
- Device activity
- Attack logs

Screenshots of the dashboard and project flow are available in the `images/` directory.

---

# 📂 Project Structure

```text
edge-based-iot-cyberattack-detection/
│
├── attack_simulator/
│   ├── fake_sensor_data.py
│   ├── flood_attack.py
│   ├── rogue_device.py
│   └── run_all_attacks.py
│
├── firmware/
│   ├── config.py
│   ├── main.py
│   ├── mqtt_client.py
│   └── sensor.py
│
├── images/
│   ├── architecture.png
│   ├── dashboard.png
│   └── flow.png
│
├── node-red/
│   └── flow IOT CYBERATTACK.json
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

# ⚙️ MQTT Configuration

The project uses MQTT topics for communication between the IoT device, broker, and Node-RED.

### Sensor Data

```text
sensors/home/temperature
```

### Device Status

```text
sensors/home/status
```

### Node-RED Subscription

```text
sensors/#
```

The wildcard subscription allows Node-RED to monitor sensor-related MQTT topics.

---

# 🚀 Installation

## 1. Clone the Repository

```bash
git clone https://github.com/SaiRohan622/edge-based-iot-cyberattack-detection.git
```

Move into the project directory:

```bash
cd edge-based-iot-cyberattack-detection
```

---

# 🐍 Python Environment

Install the required Python dependency:

```bash
pip install -r requirements.txt
```

The project currently uses:

```text
paho-mqtt
```

---

# 📡 MQTT Broker Setup

Install and run a local Mosquitto MQTT broker.

The MQTT broker uses:

```text
Port: 1883
```

The Raspberry Pi Pico configuration can be changed in:

```text
firmware/config.py
```

Example:

```python
MQTT_BROKER = "192.168.1.100"
MQTT_PORT = 1883
```

Replace the example IP address with the IP address of the computer running the MQTT broker.

> Do not commit real Wi-Fi passwords, credentials, or private keys to a public repository.

---

# 🔴 Node-RED Setup

Import the Node-RED flow:

```text
node-red/flow IOT CYBERATTACK.json
```

In Node-RED:

```text
Menu
  ↓
Import
  ↓
Select flow IOT CYBERATTACK.json
  ↓
Deploy
```

The flow subscribes to:

```text
sensors/#
```

and processes incoming IoT messages for monitoring and security analysis.

---

# 🔬 Running the Attack Simulators

The attack simulators are designed for testing the project's own local MQTT environment.

## Unauthorized Device

```bash
python attack_simulator/rogue_device.py
```

---

## Fake Sensor Data

```bash
python attack_simulator/fake_sensor_data.py
```

---

## MQTT Flood

```bash
python attack_simulator/flood_attack.py
```

---

## Run All Simulations

To execute the attack simulations:

```bash
python attack_simulator/run_all_attacks.py
```

---

# 🔄 Data Flow

The normal IoT data path is:

```text
DHT Sensor
    │
    ▼
Raspberry Pi Pico 2W
    │
    │ MQTT
    ▼
Mosquitto Broker
    │
    ▼
Node-RED
    │
    ├── Parse JSON
    │
    ├── Monitor Device
    │
    ├── Analyze Sensor Values
    │
    ├── Monitor Message Rate
    │
    └── Generate Security Events
              │
              ▼
         Dashboard
```

During security testing:

```text
Python Attack Simulator
          │
          │ MQTT
          ▼
   Mosquitto Broker
          │
          ▼
       Node-RED
          │
          ▼
   Attack Detection
          │
          ├── Alert
          ├── Log
          └── Response
```

---

# 🧪 Testing

The project can be tested using the following scenarios:

| Test | Expected Result |
|---|---|
| Normal sensor data | Normal monitoring status |
| Unauthorized device | Rogue-device detection |
| Extreme sensor values | Fake-data detection |
| High MQTT message rate | Flood detection |
| Multiple attacks | Multiple security events |

---

# 📊 Example Sensor Payload

A normal sensor message follows this structure:

```json
{
  "device_id": "pico-001",
  "timestamp": 1720000000,
  "temperature": 28,
  "humidity": 65,
  "unit": "C"
}
```

This payload is published through MQTT and processed by Node-RED.

---

# 🛡️ Security Response

When suspicious behavior is detected, the system can:

- Generate a security alert.
- Update the dashboard security status.
- Record the event in the attack log.
- Increment attack counters.
- Identify the suspicious device.
- Trigger automated response logic.

The project demonstrates how security monitoring and response can be moved closer to IoT edge infrastructure rather than relying entirely on cloud processing.

---

# 📈 Advantages

- Edge-oriented security monitoring.
- Low-cost hardware.
- MQTT-based IoT communication.
- Real-time monitoring.
- Automated detection and response.
- Visual security dashboard.
- Controlled attack simulation.
- Easy to extend with additional detection algorithms.
- Suitable for IoT cybersecurity experimentation and academic demonstrations.

---

# 🔮 Future Enhancements

Future versions can include:

- Machine-learning-based anomaly detection.
- Additional MQTT attack scenarios.
- Device authentication using certificates.
- MQTT TLS encryption.
- More sophisticated behavioral analysis.
- Persistent attack databases.
- Advanced automated blocking.
- Distributed IoT monitoring.
- Edge-based ML inference.
- Integration with SIEM platforms.
- Real-time security notifications.

---

# 👨‍💻 Author

**Sai Rohan**

Kakatiya Institute of Technology and Science, Warangal

GitHub:  
https://github.com/SaiRohan622

---

# 📜 Disclaimer

This project is intended for educational, research, and controlled cybersecurity testing purposes.

The attack simulators should only be used against MQTT infrastructure that you own or have explicit permission to test.

Do not use the attack simulators against unauthorized systems or networks.

---

# ⭐ Project

If this project is useful for your IoT cybersecurity research or learning, consider starring the repository.

**Edge-Based IoT Cyberattack Detection and Automated Response System**
