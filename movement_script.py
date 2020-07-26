import cv2
import imutils
from movement_script_utils import *

#Capture video from webcam
cap = cv2.VideoCapture(1)
#Movement ie left,right,up,down
query = ""
#When nose move only one time arrow pressed. So need to bring back nose back in circle. To control it boolean
press = True
#Coordinates of nose
nose = ()
#Coorinates of box out of which movement detected
cord = []

while cap.isOpened():
	succ,frame = cap.read()
	if succ:
		# flip the captured frame
		frame = cv2.flip(frame, 1)

		# resizing the frame
		frame = imutils.resize(frame,width = 400)

		# get the height,width,channels from frame
		h,w,a = frame.shape

		# detect face then detect nose coordinates
		frame,nose = detectFaceAndNose(frame)

		# drawing the basic circle for getting the movement when out of this circle
		frame,cord = drawCircle(frame,h//2,w//2)

		cv2.putText(frame,query,(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(125,255,0),2,cv2.LINE_AA)

		# when movement detected in nose coordinates and if nose coordinates found then move action performed
		if press and len(nose)>0:
			query = command(nose,cord,query)	
		
		press,query = changeFlag(nose,cord,query)
		cv2.imshow("Frame",frame)
		if cv2.waitKey(1) == ord('q'):
			break
	else:
		break
cap.release()
cv2.destroyAllWindows()
