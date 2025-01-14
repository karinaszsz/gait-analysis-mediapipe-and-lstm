import os
import cv2
import numpy as np

video_path = 'dataset\\raw data\\blind\\batch 5\\blind (239).mp4'

frame_count = 0

cap = cv2.VideoCapture(video_path)

while True:
    ret, frame = cap.read()
    if not ret: 
        break

    cv2.putText(frame, f"Frame: {frame_count}", (10, 30), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
    cv2.imshow('video playback', frame)

    if cv2.waitKey(0) & 0xFF == ord('q'):
        break

    frame_count +=  1

cap.release()
cv2.destroyAllWindows()