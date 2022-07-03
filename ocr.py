import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import numpy as np
import cv2
from keras.models import load_model
model=load_model('resources/TRAINED_MODEL.h5')


def OCR_digits(digits):
    digits_numerical=[]
    for i in digits:

        i = np.asarray(i)
        i = i / 255
        i = i[4:i.shape[0] - 4, 4:i.shape[1] - 4]
        i = cv2.resize(i, (28, 28))
        #j=i.copy()
        #j=cv2.adaptiveThreshold(j,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,39,11)
        i = i.reshape(1, 28, 28, 1)
        pred = model.predict(i)
        prediction = model.predict_classes(i)
        p = np.amax(pred)

        '''if np.sum(j)<20000:
            digits_numerical.append(0)'''

        if p > 0.75:
            digits_numerical.append(model.predict_classes(i)[0])
        else:
            digits_numerical.append(0)

    for i in range(len(digits)):
        c=digits[i].copy()
        c=c[4:c.shape[0] - 4, 4:c.shape[1] - 4]
        ct = cv2.threshold(c, 0, 255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
        cnts,heirarchy = cv2.findContours(ct.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        cont=cnts[0]
        max_area=cv2.contourArea(cnts[0])
        for z in cnts:
            if cv2.contourArea(z)>max_area:
                max_area=cv2.contourArea(z)
                cont=z

        mask=np.zeros(ct.shape,np.uint8)
        cv2.drawContours(mask, [cont], -1, 255, -1)
        (h,w)=ct.shape
        percentFilled = cv2.countNonZero(mask) / float(w * h)

        if percentFilled<=0.05:
            digits_numerical[i]=0





    return digits_numerical

