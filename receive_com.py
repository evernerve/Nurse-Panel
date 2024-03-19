import paho.mqtt.client as mqtt

# MQTT settings
MQTT_BROKER = "10.183.214.97"
MQTT_PORT = 1883
MQTT_TOPIC = "button/pressed"

def on_message(client, userdata, msg):
    print(f"Received message: {msg.payload.decode()}")

# Set up MQTT client
client = mqtt.Client()
client.on_message = on_message
client.connect(MQTT_BROKER, MQTT_PORT)
client.subscribe(MQTT_TOPIC)

# Keep the script running
client.loop_forever()
