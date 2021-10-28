import numpy as np
import time
import cv2
import requests
from PIL import Image



def yolo_dection_dogcat(INPUT_FILE='fire.jpg'):
	url = 'https://incontrol-sys.com/image_api/runClassify'
	url2 = 'https://incontrol-sys.com/image_api/runClassifyPoop'
	url3 = 'https://incontrol-sys.com/image_api/vanilaOrNot'
	url4 = 'https://incontrol-sys.com/image_api/poopOrNot'
	# INPUT_FILE='dogpoof.png'
	# INPUT_FILE='dogcat.jpg'
	OUTPUT_FILE='./yolo_recongized/predicted.jpg'
	LABELS_FILE='./yolo_recongized/coco.names'
	CONFIG_FILE='./yolo_recongized/yolov3.cfg'
	WEIGHTS_FILE='./yolo_recongized/yolov3.weights'
	print('test_yolo_1')
	arrDogCat=[]
	recognizeDog=[]
	pooping=[]
	CONFIDENCE_THRESHOLD=0.3

	LABELS = open(LABELS_FILE).read().strip().split("\n")
	print('test_yolo_2')
	np.random.seed(4)
	COLORS = np.random.randint(0, 255, size=(len(LABELS), 3),
		dtype="uint8")


	net = cv2.dnn.readNetFromDarknet(CONFIG_FILE, WEIGHTS_FILE)

	image = cv2.imread(INPUT_FILE)
	(H, W) = image.shape[:2]

	# determine only the *output* layer names that we need from YOLO
	ln = net.getLayerNames()
	ln = [ln[i[0] - 1] for i in net.getUnconnectedOutLayers()]


	blob = cv2.dnn.blobFromImage(image, 1 / 255.0, (416, 416),
		swapRB=True, crop=False)
	net.setInput(blob)
	start = time.time()
	layerOutputs = net.forward(ln)
	end = time.time()


	print("[INFO] YOLO took {:.6f} seconds".format(end - start))


	# initialize our lists of detected bounding boxes, confidences, and
	# class IDs, respectively
	boxes = []
	confidences = []
	classIDs = []




	# loop over each of the layer outputs
	for output in layerOutputs:
		# loop over each of the detections
		for detection in output:
			# extract the class ID and confidence (i.e., probability) of
			# the current object detection
			scores = detection[5:]
			classID = np.argmax(scores)
			confidence = scores[classID]

			# filter out weak predictions by ensuring the detected
			# probability is greater than the minimum probability
			if confidence > CONFIDENCE_THRESHOLD:
				# scale the bounding box coordinates back relative to the
				# size of the image, keeping in mind that YOLO actually
				# returns the center (x, y)-coordinates of the bounding
				# box followed by the boxes' width and height
				box = detection[0:4] * np.array([W, H, W, H])
				(centerX, centerY, width, height) = box.astype("int")

				# use the center (x, y)-coordinates to derive the top and
				# and left corner of the bounding box
				x = int(centerX - (width / 2))
				y = int(centerY - (height / 2))

				# update our list of bounding box coordinates, confidences,
				# and class IDs
				boxes.append([x, y, int(width), int(height)])
				confidences.append(float(confidence))
				classIDs.append(classID)

	# apply non-maxima suppression to suppress weak, overlapping bounding
	# boxes
	idxs = cv2.dnn.NMSBoxes(boxes, confidences, CONFIDENCE_THRESHOLD,
		CONFIDENCE_THRESHOLD)

	# ensure at least one detection exists
	if len(idxs) > 0:
		
		# loop over the indexes we are keeping
		for i in idxs.flatten():
			lableClass=LABELS[classIDs[i]]
			if(lableClass=="dog"):
				with open(INPUT_FILE, 'rb') as imageClassify:
				# imageClassify = open(INPUT_FILE, 'rb')
					my_img = {'image': imageClassify}
					r = requests.post(url, files=my_img)

				with open(INPUT_FILE, 'rb') as imageClassify:
					my_img = {'image': imageClassify}
					r2 = requests.post(url2, files=my_img)

				with open(INPUT_FILE, 'rb') as imageClassify:
					my_img = {'image': imageClassify}
					r3 = requests.post(url3, files=my_img)

				with open(INPUT_FILE, 'rb') as imageClassify:
					my_img = {'image': imageClassify}
					r4 = requests.post(url4, files=my_img)

				lableClass2=r2.json()['poopOrNot']
				pooping.append(lableClass2)
				print(r)
				print(r2)
				print(r.json()['score'])
				print(r3.json()['vanilaOrNot'])
				print(r4.json()['poopOrNot'])

				if(r3.json()['vanilaOrNot']=='vanila' or r4.json()['poopOrNot']=='poop'):
					if(int(r.json()['score'])>60):
						lableClass=r.json()['name']
						print(r.json()['name'])
						recognizeDog.append(lableClass)
					else:
						recognizeDog.append('Unknown')
				else:
					recognizeDog.append('Unknown')





			else:
				continue	
			# extract the bounding box coordinates
			(x, y) = (boxes[i][0], boxes[i][1])
			(w, h) = (boxes[i][2], boxes[i][3])

			color = [int(c) for c in COLORS[classIDs[i]]]

			cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
			text = "{}: {:.4f}".format(lableClass, confidences[i])
			# print(LABELS[classIDs[i]])
			arrDogCat.append(LABELS[classIDs[i]])
			cv2.putText(image, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX,
				0.5, color, 2)

	# show the output image
	print(arrDogCat)
	print(recognizeDog)
	try:
		print('i in try')
		cv2.imwrite("example.png", image)
	except:
		print('we have a problem with save the expample.png')
	if 'dog' in arrDogCat:
		if(len(recognizeDog)>0):
			text='We recognize dogs'
			if len(pooping)>0:
				text+="\nThe dog is {}".format(pooping[0])
			text += "\n The names:\n"
			counter=1		
			for name in recognizeDog:
				text+="{}) name:{}\n".format(counter, name)
				counter+=1
			return text
	# 	if 'cat' in arrDogCat:
	# 		return 'we reconigzed dog and cat'
	# 	else: return 'we reconigzed dog'
	# elif 'cat' in arrDogCat:
	# 	return 'we reconigzed cat'

	return 'not reconigzed dog or cat'
