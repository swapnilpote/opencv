# import threading
# import numpy as np
# import cv2
# import time

# frame_count = 1
# frame = None

# class myThread(threading.Thread):

# 	def __init__(self):
# 		threading.Thread.__init__(self)

# 	def run(self):
# 		global frame_count

# 		while (~(frame is None)):
# 			frame_count += 1

# cap = cv2.VideoCapture('jurassic_park_intro.mp4')

# thread1 = myThread()
# thread1.start()

# while True:
# 	ret, original = cap.read()

# 	frame = cv2.resize(original, (224, 224))

# 	cv2.putText(original, "Frame Count: {}".format(frame_count), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
# 	cv2.imshow("Frame Count", original)

# 	if (cv2.waitKey(1) & 0xFF == ord('q')):
# 		break;

# cap.release()
# frame = None
# cv2.destroyAllWindows()


# import os
# import threading
# import numpy as np
# import cv2

# # my_opencv_path = "C:/opencv2.4.3"
# # video_path_1 = os.path.join(my_opencv_path, "samples", "cpp", "tutorial_code",
# #                             "HighGUI", "video-input-psnr-ssim", "video",
# #                             "Megamind.avi")
# # video_path_2 = os.path.join(my_opencv_path, "samples", "c", "tree.avi")
# # assert os.path.isfile(video_path_1)
# # assert os.path.isfile(video_path_2)

# video_path_1 = os.path.abspath('output.mp4')
# video_path_2 = os.path.abspath('jurassic_park_intro.mp4')

# class MyThread (threading.Thread):
#     maxRetries = 20

#     def __init__(self, thread_id, name, video_url, thread_lock):
#         threading.Thread.__init__(self)
#         self.thread_id = thread_id
#         self.name = name
#         self.video_url = video_url
#         self.thread_lock = thread_lock

#     def run(self):
#         print("Starting " + self.name)
#         print(self.video_url)

#         window_name = self.name
#         cv2.namedWindow(window_name)
#         video = cv2.VideoCapture(self.video_url)
        
#         while True:
#             # self.thread_lock.acquire()  # These didn't seem necessary
#             got_a_frame, image = video.read()
#             # self.thread_lock.release()
#             if not got_a_frame:  # error on video source or last frame finished
#                 break
#             cv2.imshow(window_name, image)
#             key = cv2.waitKey(50)
#             if key == 27:
#                 break
#         cv2.destroyWindow(window_name)
#         print(self.name + " Exiting")


# def main():
#     thread_lock = threading.Lock()
#     thread1 = MyThread(1, "Thread 1", video_path_1, thread_lock)
#     thread2 = MyThread(2, "Thread 2", video_path_2, thread_lock)
#     thread1.start()
#     thread2.start()
#     print("Exiting Main Thread")

# if __name__ == '__main__':
#     main()


# import threading
# import time
# import os
# import numpy as np
# import cv2


# video_path_1 = os.getcwd() + '/jurassic_park_intro.mp4'

# class myThread(threading.Thread):
# 	def __init__(self, thread_id, name, video_url, thread_lock):
# 		threading.Thread.__init__(self)
# 		self.thread_id = thread_id
# 		self.name = name
# 		self.video_url = video_url
# 		self.thread_lock = thread_lock

# 	def run(self):
# 		print("Starting " + self.name)

# 		window_name = self.name
# 		cv2.namedWindow(window_name)
# 		video = cv2.VideoCapture(self.video_url)

# 		count = 0
        
# 		while True:
# 			got_a_frame, image = video.read()

# 			if not got_a_frame:  # error on video source or last frame finished
# 				break

# 			cv2.imwrite("./images/" + "frame%d.jpg" % count, image)
# 			cv2.imshow(window_name, image)

# 			if (cv2.waitKey(1) & 0xFF == ord('q')):
# 				break;

# 			count += 1

# 		cv2.destroyWindow(window_name)
# 		print(self.name + " Exiting")


# def main():
# 	thread_lock = threading.Lock()
# 	thread1 = myThread(1, "Thread 1", video_path_1, thread_lock)
# 	thread1.start()
# 	print("Exiting Main Thread")

# if __name__ == '__main__':
# 	main()


import threading
from queue import Queue
import time, os
import cv2
import numpy as np

video_lock = threading.Lock()


def exampleJob(worker):
	print("Starting")
	cap = cv2.VideoCapture(worker)

	while True:
		ret, frame = cap.read()

		if not ret:
			break

		cv2.imshow('frame', frame)

		if (cv2.waitKey(1) & 0xFF == ord('q')):
			break

# The threader thread pulls an worker from the queue and processes it
def threader():
	while True:
		# gets an worker from the queue
		worker = q.get()
		# Run the example job with the avail worker in queue (thread)
		exampleJob(worker)
		# completed with the job
		q.task_done()

# Create the queue and threader 
q = Queue()

# how many threads are we going to allow for
for x in range(1):
	t = threading.Thread(target=threader)
	# classifying as a daemon, so they will die when the main dies
	t.daemon = True
	# begins, must come after daemon definition
	t.start()


worker = os.getcwd() + '/jurassic_park_intro.mp4'
q.put(worker)

q.join()

print("Existing")






















