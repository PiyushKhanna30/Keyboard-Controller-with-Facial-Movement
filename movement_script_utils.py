import cv2
import keyboard

cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
def detectFaceAndNose(frame,face_cascade=cascade):
	gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray_frame,scaleFactor=1.1,minNeighbors=8)
	nose = ()
	for (x,y,w,h) in faces:
		# cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
		cv2.circle(frame,(x+w//2,y+h//2),5,(0,255,0),-1)
		nose = (x+w//2,y+h//2)
	return frame,nose
def drawCircle(frame,h,w):
	size = 20
	x1 = w - size
	y1 = h - size
	x2 = w + size
	y2 = h + size
	# cv2.circle(frame, (x1,y1),10,(0,255,255),-1)
	# cv2.circle(frame, (x2,y2),10,(0,255,255),-1)

	cv2.circle(frame, (w,h),size,(255,255,255),2)
	return frame,[(x1,y1),(x2,y2)]

def command(nose,cord,query):
	[(x1,y1),(x2,y2)] = cord
	nx,ny = nose
	if nx > x2:
		query = "right"
	elif nx < x1:
		query = "left"
	elif ny > y2:
		query = "down"
	elif ny < y1:
		query = "up"
	if query:
		keyboard.press_and_release(query)
		# print(query)
	return query
def changeFlag(nose,cord,query):
	try:
		[(x1,y1),(x2,y2)] = cord
		nx,ny = nose
	except:
		# print("except")
		return True,query
	if x1<nx and nx<x2 and y1<ny and ny<y2:
		return True,""
	return False,query 
