import cv2
import time

capture = cv2.VideoCapture("C:/Users/DELL/Desktop/apex2z.mp4")
frameNr = 0
frameRate = 20  # multiple 10 means take frame number 10
interval = 1 / frameRate  # Interval between frame captures
SaveFrameNr = 1500

while True:
    success, frame = capture.read()

    if not success:
        break

    if frameNr % frameRate == 0:

        cv2.imwrite(f'C:/Users/DELL/Desktop/sample/frame_{SaveFrameNr}.jpg', frame)
        print(SaveFrameNr)
        SaveFrameNr += 1
    frameNr += 1
    time.sleep(interval)
print("done")
capture.release()
