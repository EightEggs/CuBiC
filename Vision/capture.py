import os

os.system('fswebcam -d /dev/video0 --no-banner\
            -q /home/pi/Documents/CuBiC/Vision/1.jpg')

os.system('fswebcam -d /dev/video2 --no-banner\
            -q /home/pi/Documents/CuBiC/Vision/2.jpg')

os.system('fswebcam -d /dev/video4 --no-banner\
            -q /home/pi/Documents/CuBiC/Vision/3.jpg')

os.system('fswebcam -d /dev/video6 --no-banner\
            -q /home/pi/Documents/CuBiC/Vision/4.jpg')

print('capture done.')
