import cv2
import os, sys
import face_recognition
import numpy as np
import math
import arduino

WINDOW_TITLE = 'Face Recognition'

class FaceRecognition:
    face_locations = []
    face_encodings = []
    face_names = []
    process_current_frame = True

    def __init__(self):
        pass 

    def run_recognition(self):
        video_capture = cv2.VideoCapture(0)

        if not video_capture.isOpened():
            sys.exit('Video source not found.')

        while True:
            ret, frame = video_capture.read()

            if self.process_current_frame:
                small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
                # no needed
                # rgb_small_frame = small_frame[:, :, ::-1]

                self.face_locations = face_recognition.face_locations(small_frame)

            self.process_current_frame = not self.process_current_frame

            for (top, right, bottom, left) in self.face_locations:
                if left > 0:
                    arduino.rotate_horizontal(180 - (60 / (120 / left)))
                    
                if bottom > 0:
                    arduino.rotate_vertical((180 / (120 / bottom)))

                top *= 4
                right *= 4
                bottom *= 4
                left *= 4

                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            cv2.namedWindow(WINDOW_TITLE, cv2.WINDOW_NORMAL)
            cv2.imshow(WINDOW_TITLE, frame)

            if cv2.waitKey(1) == ord('q'):
                break

        video_capture.release()
        cv2.destroyWindow(WINDOW_TITLE)

if __name__ == '__main__':
    fr = FaceRecognition()
    fr.run_recognition()
