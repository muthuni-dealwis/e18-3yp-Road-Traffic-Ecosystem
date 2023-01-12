# import cv2
# # from playsound import playsound
# # from pydub import AudioSegment
# # from pydub.playback import play
# # playsound('stop.mp3')
# import os
#
# #
# # Stop Sign Cascade Classifier xml
# stop_sign = cv2.CascadeClassifier('cascade_stop_sign.xml')
# yieldsigns = cv2.CascadeClassifier('yeildstages.xml')
# speedlimit_sign= cv2.CascadeClassifier('speedlimit.xml')
# trafficlight_sign= cv2.CascadeClassifier('trafficlights.xml')
# left_turn= cv2.CascadeClassifier('left.xml')
#
# cap = cv2.VideoCapture(0)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
# while cap.isOpened():
#     _, img = cap.read()
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     stop_sign_scaled = stop_sign.detectMultiScale(gray, 1.3, 5)
#     stop_sign_scaled1 = yieldsigns.detectMultiScale(gray, 1.3, 5)
#     speedlimit_scaled = speedlimit_sign.detectMultiScale(gray, 1.3, 5)
#     trafficlight_scaled = trafficlight_sign.detectMultiScale(gray, 1.3, 5)
#     left_scaled = left_turn.detectMultiScale(gray, 1.3, 5)
#
#     # Detect the stop sign, x,y = origin points, w = width, h = height
#     for (x, y, w, h) in stop_sign_scaled:
#         # Draw rectangle around the stop sign
#         stop_sign_rectangle = cv2.rectangle(img, (x,y),
#                                             (x+w, y+h),
#                                             (0, 255, 0), 3)
#         # Write "Stop sign" on the bottom of the rectangle
#         stop_sign_text = cv2.putText(img=stop_sign_rectangle,
#                                      text="Stop Sign",
#                                      org=(x, y+h+30),
#                                      fontFace=cv2.FONT_HERSHEY_SIMPLEX,
#                                      fontScale=1, color=(0, 0, 255),
#                                      thickness=2, lineType=cv2.LINE_4)
#
#         # song = AudioSegment.from_wav("stop.mp3")
#         # play(song)
#         # os.system("/Users/hari/PycharmProjects/RoadTrafficCommunityTest/stop.mp3")
#
#     for (x, y, w, h) in stop_sign_scaled1:
#         # Draw rectangle around the stop sign
#         stop_sign_rectangle1 = cv2.rectangle(img, (x,y),
#                                             (x+w, y+h),
#                                             (0, 255, 0), 3)
#         # Write "Stop sign" on the bottom of the rectangle
#         stop_sign_text1 = cv2.putText(img=stop_sign_rectangle1,
#                                      text="Yield",
#                                      org=(x, y+h+30),
#                                      fontFace=cv2.FONT_HERSHEY_SIMPLEX,
#                                      fontScale=1, color=(0, 0, 255),
#                                      thickness=2, lineType=cv2.LINE_4)
#         # song = AudioSegment.from_wav("yeild.mp3")
#         # play(song)
#         # os.system("yeild.mp3")
#     for (x, y, w, h) in speedlimit_scaled:
#         # Draw rectangle around the stop sign
#         speedlimit_rectangle = cv2.rectangle(img, (x,y),
#                                             (x+w, y+h),
#                                             (0, 255, 0), 3)
#         # Write "Stop sign" on the bottom of the rectangle
#         speedlimit_text1 = cv2.putText(img=speedlimit_rectangle,
#                                      text="speed limit",
#                                      org=(x, y+h+30),
#                                      fontFace=cv2.FONT_HERSHEY_SIMPLEX,
#                                      fontScale=1, color=(0, 0, 255),
#                                      thickness=2, lineType=cv2.LINE_4)
#
#     for (x, y, w, h) in trafficlight_scaled:
#         # Draw rectangle around the stop sign
#         trafficlights_rectangle = cv2.rectangle(img, (x, y),
#                                              (x + w, y + h),
#                                              (0, 255, 0), 3)
#         # Write "Stop sign" on the bottom of the rectangle
#         trafficlights_text1 = cv2.putText(img=trafficlights_rectangle,
#                                        text="traffic_light",
#                                        org=(x, y + h + 30),
#                                        fontFace=cv2.FONT_HERSHEY_SIMPLEX,
#                                        fontScale=1, color=(0, 0, 255),
#                                        thickness=2, lineType=cv2.LINE_4)
#
#     for (x, y, w, h) in left_scaled:
#         # Draw rectangle around the stop sign
#         left_rectangle = cv2.rectangle(img, (x, y),
#                                              (x + w, y + h),
#                                              (0, 255, 0), 3)
#         # Write "Stop sign" on the bottom of the rectangle
#         left_text1 = cv2.putText(img=left_rectangle,
#                                        text="Left Turn",
#                                        org=(x, y + h + 30),
#                                        fontFace=cv2.FONT_HERSHEY_SIMPLEX,
#                                        fontScale=1, color=(0, 0, 255),
#                                        thickness=2, lineType=cv2.LINE_4)
#
#
#     cv2.imshow("img", img)
#     key = cv2.waitKey(30)
#     if key == ord('q'):
#         cap.release()
#         cv2.destroyAllWindows()
#         break
#
# # # import numpy as np
# # # import cv2
# # # import pickle
# # #
# # # #############################################
# # #
# # # frameWidth = 640  # CAMERA RESOLUTION
# # # frameHeight = 480
# # # brightness = 180
# # # threshold = 0.75  # PROBABLITY THRESHOLD
# # # font = cv2.FONT_HERSHEY_SIMPLEX
# # # ##############################################
# # #
# # # # SETUP THE VIDEO CAMERA
# # # cap = cv2.VideoCapture(0)
# # # cap.set(3, frameWidth)
# # # cap.set(4, frameHeight)
# # # cap.set(10, brightness)
# # # # IMPORT THE TRANNIED MODEL
# # # pickle_in = open("model_trained.p", "rb")  ## rb = READ BYTE
# # # model = pickle.load(pickle_in)
# # #
# # #
# # # def grayscale(img):
# # #     img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# # #     return img
# # #
# # #
# # # def equalize(img):
# # #     img = cv2.equalizeHist(img)
# # #     return img
# # #
# # #
# # # def preprocessing(img):
# # #     img = grayscale(img)
# # #     img = equalize(img)
# # #     img = img / 255
# # #     return img
# # #
# # #
# # # def getCalssName(classNo):
# # #     if classNo == 0:
# # #         return 'Speed Limit 20 km/h'
# # #     elif classNo == 1:
# # #         return 'Speed Limit 30 km/h'
# # #     elif classNo == 2:
# # #         return 'Speed Limit 50 km/h'
# # #     elif classNo == 3:
# # #         return 'Speed Limit 60 km/h'
# # #     elif classNo == 4:
# # #         return 'Speed Limit 70 km/h'
# # #     elif classNo == 5:
# # #         return 'Speed Limit 80 km/h'
# # #     elif classNo == 6:
# # #         return 'End of Speed Limit 80 km/h'
# # #     elif classNo == 7:
# # #         return 'Speed Limit 100 km/h'
# # #     elif classNo == 8:
# # #         return 'Speed Limit 120 km/h'
# # #     elif classNo == 9:
# # #         return 'No passing'
# # #     elif classNo == 10:
# # #         return 'No passing for vechiles over 3.5 metric tons'
# # #     elif classNo == 11:
# # #         return 'Right-of-way at the next intersection'
# # #     elif classNo == 12:
# # #         return 'Priority road'
# # #     elif classNo == 13:
# # #         return 'Yield'
# # #     elif classNo == 14:
# # #         return 'Stop'
# # #     elif classNo == 15:
# # #         return 'No vechiles'
# # #     elif classNo == 16:
# # #         return 'Vechiles over 3.5 metric tons prohibited'
# # #     elif classNo == 17:
# # #         return 'No entry'
# # #     elif classNo == 18:
# # #         return 'General caution'
# # #     elif classNo == 19:
# # #         return 'Dangerous curve to the left'
# # #     elif classNo == 20:
# # #         return 'Dangerous curve to the right'
# # #     elif classNo == 21:
# # #         return 'Double curve'
# # #     elif classNo == 22:
# # #         return 'Bumpy road'
# # #     elif classNo == 23:
# # #         return 'Slippery road'
# # #     elif classNo == 24:
# # #         return 'Road narrows on the right'
# # #     elif classNo == 25:
# # #         return 'Road work'
# # #     elif classNo == 26:
# # #         return 'Traffic signals'
# # #     elif classNo == 27:
# # #         return 'Pedestrians'
# # #     elif classNo == 28:
# # #         return 'Children crossing'
# # #     elif classNo == 29:
# # #         return 'Bicycles crossing'
# # #     elif classNo == 30:
# # #         return 'Beware of ice/snow'
# # #     elif classNo == 31:
# # #         return 'Wild animals crossing'
# # #     elif classNo == 32:
# # #         return 'End of all speed and passing limits'
# # #     elif classNo == 33:
# # #         return 'Turn right ahead'
# # #     elif classNo == 34:
# # #         return 'Turn left ahead'
# # #     elif classNo == 35:
# # #         return 'Ahead only'
# # #     elif classNo == 36:
# # #         return 'Go straight or right'
# # #     elif classNo == 37:
# # #         return 'Go straight or left'
# # #     elif classNo == 38:
# # #         return 'Keep right'
# # #     elif classNo == 39:
# # #         return 'Keep left'
# # #     elif classNo == 40:
# # #         return 'Roundabout mandatory'
# # #     elif classNo == 41:
# # #         return 'End of no passing'
# # #     elif classNo == 42:
# # #         return 'End of no passing by vechiles over 3.5 metric tons'
# # #
# # #
# # # while True:
# # #
# # #     # READ IMAGE
# # #     success, imgOrignal = cap.read()
# # #
# # #     # PROCESS IMAGE
# # #     img = np.asarray(imgOrignal)
# # #     img = cv2.resize(img, (32, 32))
# # #     img = preprocessing(img)
# # #     cv2.imshow(img)
# # #     img = img.reshape(1, 32, 32, 1)
# # #     cv2.putText(imgOrignal, "CLASS: ", (20, 35), font, 0.75, (0, 0, 255), 2, cv2.LINE_AA)
# # #     cv2.putText(imgOrignal, "PROBABILITY: ", (20, 75), font, 0.75, (0, 0, 255), 2, cv2.LINE_AA)
# # #     # PREDICT IMAGE
# # #     predictions = model.predict(img)
# # #     predict_x = model.predict(img)
# # #     classes_x = np.argmax(predict_x, axis=1)
# # #     probabilityValue = np.amax(predictions)
# # #     if probabilityValue > threshold:
# # #         print(getCalssName(classes_x))
# # #         cv2.putText(imgOrignal, str(classes_x) + " " + str(getCalssName(classes_x)), (120, 35), font, 0.75,
# # #                     (0, 0, 255), 2, cv2.LINE_AA)
# # #         cv2.putText(imgOrignal, str(round(probabilityValue * 100, 2)) + "%", (180, 75), font, 0.75, (0, 0, 255), 2,
# # #                     cv2.LINE_AA)
# # #         cv2.imshow("Result", imgOrignal)
# # #
# # #     if cv2.waitKey(1) and 0xFF == ord('q'):
# # #         break
#
#

import time
import math

oldx = 0
oldy = 0
oldz = 0

sensitivity = 20

while (True):

    print("Running")

    # Set the value for curx, cury, curz according to the current readings of the accelerometer
    curx = (int)(input("Enter curx: "))
    cury = (int)(input("Enter cury: "))
    curz = (int)(input("Enter curz: "))

    deltx = curx - oldx
    delty = cury - oldy
    deltz = curz - oldz

    magnitude = math.sqrt(math.pow(deltx, 2) + math.pow(delty, 2) + math.pow(deltz, 2))

    # Accident is detected if the magnitude is greater than the sensitivity
    if magnitude > sensitivity:

        # include the procedure need to be done when an accident is detected
        print("Accident detected")
    else:
        magnitude = 0

    time.sleep(0.5)
