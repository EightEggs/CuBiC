import os


def capture_one(cam_id: int):
    '''Capture one image using the specified camera.
    Save to /home/pi/Desktop/CuBiC/Vision/pictures/
    :param cam_id: Camera id. Can be only 0, 1, 2, or 3.
    '''
    if cam_id in [0, 1, 2, 3]:
        os.system(f'fswebcam -d /dev/video{cam_id*2} --no-banner\
            -q /home/pi/Desktop/CuBiC/Vision/pictures/{cam_id}.jpg')
        # print(f'Camera {cam_id} capture done.')
    else:
        raise ValueError(f'Invalid Camera {cam_id}.')


def capture_all():
    '''Capture all the 4 images. Save to /home/pi/Desktop/CuBiC/Vision/pictures/
    '''
    for cam_id in range(4):
        capture_one(cam_id)


if __name__ == '__main__':
    capture_all()
