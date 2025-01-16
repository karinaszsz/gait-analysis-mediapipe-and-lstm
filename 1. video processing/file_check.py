import os
import cv2

# to check if there's duplicate data

folder_in = ''

file_details = {}

i = 0

for file in os.listdir(folder_in):
    if file.endswith('.mp4'):
        file_path = os.path.join(folder_in, file)
        # print(file_path)
        if os.path.exists(file_path):
            file_stat = os.stat(file_path)
            cap = cv2.VideoCapture(file_path)
            file_size = file_stat.st_size
            frame_total = int(cap.get(cv2.CAP_PROP_FPS))
            file_details[i] = [file_path, file_size, frame_total]
            cap.release()
            i += 1

print(len(file_details))


k = 0

for j in range(len(file_details)):
    # if file_details[j][0] != file_details[k][0]:
    if (file_details[j][1] == file_details[k][1]) and (file_details[j][2] == file_details[k][2]):
        print(f"{file_details[j][0]} same as {file_details[k][0]}")
        k += 1
    else:
        print(f"{file_details[j][0]} no duplicate")