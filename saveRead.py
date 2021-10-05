import cv2
print(cv2.__version__)
dispW =1280
dispH =960
flip =2
#camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
#cam = cv2.VideoCapture(camset) for raspberry pi camera
cam = cv2.VideoCapture('/dev/video0')
fourcc =cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('videos/myCam4.avi',fourcc,21,(640,480))
while True:
    ret, frame = cam.read()
    cv2.imshow('picam',frame)
    cv2.moveWindow('picam',0,0)
    out.write(frame)
    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
out.release()
cv2.destroyAllWindows()