# ================================================================
# Raspberry Pi Pico W / Pico 2W Configuration
# ================================================================

# Wi-Fi
WIFI_SSID = "YOUR_WIFI_NAME"
WIFI_PASSWORD = "YOUR_WIFI_PASSWORD"

# MQTT Broker
# Use the IP address of the computer running Mosquitto
MQTT_BROKER = "192.168.1.100"
MQTT_PORT = 1883

# MQTT credentials
# Leave blank if your local Mosquitto broker has no authentication
MQTT_USERNAME = ""
MQTT_PASSWORD = ""

# Device identity
DEVICE_ID = "pico-001"

# MQTT topics
TOPIC_SENSOR = "sensors/home/temperature"
TOPIC_STATUS = "sensors/home/status"

# DHT sensor
DHT_PIN = 15

# Publish every 5 seconds
PUBLISH_INTERVAL_MS = 5000

# Connection retry settings
WIFI_RETRY_COUNT = 10
MQTT_RETRY_COUNT = 5
RETRY_DELAY_MS = 2000