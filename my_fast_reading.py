# import cv2
# import numpy as np
# import threading
# import sys
# import time
#
# start = time.time()
#
# label = ''
# frame = None
#
# class MyThread(threading.Thread):
# 	def __init__(self):
# 		threading.Thread.__init__(self)
#
# 	def run(self):
# 		global label
# 		print("Converting frame.")
# 		image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         cv2.imshow("Classification", image)
#
#
# cap = cv2.VideoCapture('output.mp4')
# if (cap.isOpened()):
# 	print("Camera OK")
# else:
# 	cap.open()
#
# keras_thread = MyThread()
# keras_thread.start()
#
# while (True):
#     ret, original = cap.read()
#
#     if not ret:
#         break
#
#     # cv2.putText(original, "Label: {}".format(label), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
#
#     # cv2.imshow("Classification", original)
#
#     if (cv2.waitKey(1) & 0xFF == ord('q')):
#         break;
#
# cap.release()
# frame = None
# cv2.destroyAllWindows()
# sys.exit()
# print(time.time()-start)



import numpy as np
import cv2
import sys
import threading
import time

frame = None

class myThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        # print("Converting frame")
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # cv2.imshow("gray", gray)
        cap = cv2.VideoCapture('jurassic_park_intro.mp4')
        return cap


cap = cv2.VideoCapture('jurassic_park_intro.mp4')

thread = myThread()
thread.start()

while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("gray", gray)
    if (cv2.waitKey(1) & 0xFF == ord('q')):
        break

cap.release()
frame = None
cv2.destroyAllWindows()
sys.exit()
