import keras
import numpy as np
import cv2

model = keras.models.load_model('cifar/model.h5')
labels = ["airplane", "ship", "bird", "cat", "deer", "dog", "frog", "horse", "automobile", "truck"]

def classificate(image):
	img = cv2.imread(image.url[1:])
	img = cv2.resize(img, (32, 32))

	img_arr = np.expand_dims(img, axis=0)
	img_arr = 1 - img_arr/255.0
	img_arr = img_arr.reshape((1, 32, 32, 3))

	predict = list(model.predict(img_arr)[0])
	result = predict.index(max(predict))
	return labels[result]
