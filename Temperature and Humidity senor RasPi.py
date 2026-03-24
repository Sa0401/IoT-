import time
import adafruit_dht
import board

dht_device = adafruit_dht.DHT11(board.D11)

while True:
    try:
        temperature = dht_device.temperature
        humidity = dht_device.humidity
        print(f"Temp: {temperature}°C Humidity: {humidity}%")
    except RuntimeError as error:
        print(error.args[0])
    time.sleep(2)
