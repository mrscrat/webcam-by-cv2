import cv2
import keyboard as kb 
import numpy as np


is_gray = False


def cnvt_to_gray(frame):
    kb.KeyboardEvent = "d"
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return gray_frame


def toggle_gray():
    global is_gray
    is_gray = not is_gray





kb.add_hotkey("d", toggle_gray)


cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 2000)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1500)



while True:
    ret, frame = cap.read()

    frame = cv2.flip(frame, 1)



    if not ret:
        print("no video")
        break
    #write functions here


    if is_gray:
        frame = cnvt_to_gray(frame)



    cv2.imshow("webcam", frame)


    if cv2.waitKey(1) & 0xFF == ord("q"):
        break




cap.release()
cv2.destroyAllWindows()

            
