import cv2
import numpy as np
import matplotlib.pyplot as plt


video_path = #video input path

cap = cv2.VideoCapture(video_path)
ret, frame = cap.read()

frame_height, frame_width, _ = frame.shape

fps = cap.get(cv2.CAP_PROP_FPS)

#mask 1. 50% cove
mask_1 = np.zeros((frame_height, frame_width), dtype=np.uint8)
cv2.rectangle(mask_1, (0, 0), (frame_width//2, frame_height), 255, -1)

#mask 2. 40% cover
mask_2 = np.zeros((frame_height, frame_width), dtype=np.uint8)
cv2.rectangle(mask_2, (500, 0), (frame_width, frame_height), 255, -1)

frame_number = 0 

cv2.imshow('mask', mask_1)
cv2.waitKey(0)

# fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# output_path = 'dataset\\test_data\\masked_output4.mp4'
# out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

brightness_value = 0


# while True:
#     ret, frame = cap.read()

#     if not ret:
#         break

#     if frame_number <= 190:
#         mask = mask_2
#     else:
#         mask = mask_1
    
#     bright_image = cv2.convertScaleAbs(frame, alpha=1, beta=brightness_value)

#     masked_frame = cv2.bitwise_and(bright_image, bright_image, mask=mask)

#     cv2.imshow('video playback', masked_frame)

#     # out.write(masked_frame)

#     key = cv2.waitKey(25)&0xFF

#     if key == ord('q'):
#         break

#     frame_number += 1

cap.release()
# out.release()
cv2.destroyAllWindows()
