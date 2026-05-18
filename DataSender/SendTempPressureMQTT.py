import time
import json
import paho.mqtt.client as mqtt


def send_sensor_data(client, sensor_topic):
    temperature = 25.0
    pressure = 100.0

    client.loop_start()
    try:
        while True:
            temperature += 0.5
            pressure += 1.0

            payload = {"temperature": temperature, "pressure": pressure}

            client.publish(sensor_topic, json.dumps(payload))

            print(f"Sent sensor data to {sensor_topic}: {payload}")

            time.sleep(5)
    finally:
        client.loop_stop()
        client.disconnect()


if __name__ == "__main__":
    broker_host = "localhost"
    broker_port = 1883
    sensor_topic = "states/sensor_data"

    client = mqtt.Client(client_id="data-sender-mqtt")
    client.connect(broker_host, broker_port, keepalive=60)

    send_sensor_data(client, sensor_topic)
