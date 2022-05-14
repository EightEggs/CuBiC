import pigpio

GPIO=4

pi = pigpio.pi()
if not pi.connected:
   exit()

level = pi.read(GPIO)

print("GPIO {} is {}".format(GPIO, level))

pi.stop()