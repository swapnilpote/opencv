import cv2
import numpy as np


cap = cv2.VideoCapture(0)

w=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH ))
h=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT ))

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (w, h))

while True:
	ret, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	out.write(frame)
	cv2.imshow('frame', frame)
	cv2.imshow('gray', gray)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

		
cap.release()
out.release()
cv2.destroyAllWindows()
