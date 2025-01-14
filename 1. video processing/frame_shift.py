import cv2
import os
import numpy as np

folder_in = 'dataset\\raw data\\blind\\batch 5'
folder_out = 'dataset\\additional data\\blind\\batch 5'

shift_value = 300

fourcc = cv2.VideoWriter_fourcc(*'X264')

for file in os.listdir(folder_in):
    if file.endswith('.mp4'):
        video_path = os.path.join(folder_in, file)

        cap = cv2.VideoCapture(video_path)
        ret, frame = cap.read()
        height, width, channels = frame.shape

        fps = cap.get(cv2.CAP_PROP_FPS)
        
        file_name = video_path.split("\\")
        save_path = os.path.join(folder_out, f"shifted_{file_name[4]}")
        out = cv2.VideoWriter(save_path, fourcc, fps, (width, height))

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            shifted_frame = np.zeros_like(frame)

            if shift_value < width:
                shifted_frame[:, shift_value:] = frame[:, :width - shift_value]

            cv2.imshow("shifted frame", shifted_frame)

            out.write(shifted_frame)

            if cv2.waitKey(25) & 0xFF == ord('q'):
                break


        print(f"{save_path} done")
        out.release()
        cap.release()
        cv2.destroyAllWindows()
