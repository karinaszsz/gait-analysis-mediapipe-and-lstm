import os
import cv2
import numpy as np

path = 'dataset\\raw data\\blind\\batch 5\\blind (205).mp4'
folder_path = 'dataset\\raw data\\processed'

cap = cv2.VideoCapture(path)

fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

frame_number = 0

fourcc = cv2.VideoWriter_fourcc(*'X264')
filename = path.split("\\")
save_path = os.path.join(folder_path, f"cut_{filename[3]}")
out = cv2.VideoWriter(save_path, fourcc, fps, (width, height))

while True:
    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow('video', frame)

    frame_number += 1

    if frame_number == 190:
        break

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

    out.write(frame)

out.release()
cap.release()
cv2.destroyAllWindows()
