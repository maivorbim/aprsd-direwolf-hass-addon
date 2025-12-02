import paho.mqtt.client as mqtt
import os
import sys
import json
import time
import subprocess

MQTT_HOST = os.getenv("MQTT_HOST", "core-mosquitto")
MQTT_PORT = int(os.getenv("MQTT_PORT", "1883"))
MQTT_USER = os.getenv("MQTT_USER", "")
MQTT_PASS = os.getenv("MQTT_PASS", "")

client = mqtt.Client()

if MQTT_USER:
    client.username_pw_set(MQTT_USER, MQTT_PASS)

client.connect(MQTT_HOST, MQTT_PORT, 60)
client.loop_start()

# Subscribe to aprsd log stream via subprocess
proc = subprocess.Popen(
    ["aprsd", "logwatch"],
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    text=True
)

for line in proc.stdout:
    client.publish("aprs/raw", line.strip())
