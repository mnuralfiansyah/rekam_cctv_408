import cv2
from datetime import datetime


vidcap = cv2.VideoCapture('rtsp://admin:@192.168.1.13:2300/live')
success,image = vidcap.read()
count = 0
while success:
    success,image = vidcap.read()

    if count % 250 == 0:
        cv2.imwrite("gambar\\408_frame_"+str(count)+"_"+str(datetime.now().strftime('%Y_%m_%d_%H_%M_%S'))+".png", image)     # save frame as JPEG file      
        print('Read a new frame: ', success)
        print("gambar\\408_frame_"+str(count)+"_"+str(datetime.now().strftime('%Y_%m_%d_%H_%M_%S'))+".png")
    count += 1