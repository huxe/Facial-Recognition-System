from sklearn.utils import shuffle
import numpy as np
import os
from keras.models import model_from_json
import cv2

def LoadModel():
    # load json and create model
    json_file = open('model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights("model.h5")
    return loaded_model

def get_classlabel(class_code):
    labels = {0:'Hamza', 1:'Anas',2:'Osama'}
    return labels[class_code]

def runModel(LM,img):
    return get_classlabel(LM.predict_classes(np.expand_dims(cv2.resize(img,(100,100)), axis=0))[0])