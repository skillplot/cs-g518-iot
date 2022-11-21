import time
import adafruit_dht
import psutil

import board

def init():
  # We first check if a libgpiod process is running. If yes, we kill it!
  for proc in psutil.process_iter():
    if proc.name() == 'libgpiod_pulsein' or proc.name() == 'libgpiod_pulsei':
      proc.kill()

def trigger(sensor):
  temp = sensor.temperature
  humidity = sensor.humidity
  # print("Temperature: {}*C   Humidity: {}% ".format(temp, humidity))
  res = {
    'temperature_in_deg': temp,
    'humidity': humidity
  }
  return res


def main():
  sensor = adafruit_dht.DHT11(board.D23)
  while True:
    try:
      res = trigger(sensor)
      print("res: {}".format(res))
    except RuntimeError as error:
      print(error.args[0])
      time.sleep(2.0)
      continue
    except Exception as error:
      sensor.exit()
      raise error
    time.sleep(1.0)


if __name__ == '__main__':
  init()
  main()
