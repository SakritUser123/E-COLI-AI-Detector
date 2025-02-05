import pandas as pd
import os 
import numpy as np
import cv2
import tensorflow as tf
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.utils import to_categorical
import kagglehub
# Download latest version
! pip install opendatasets
import opendatasets as od
od.download("https://www.kaggle.com/datasets/avk256/cnmc-leukemia")
import os

import os
import cv2
import numpy as np
from sklearn.model_selection import train_test_split

path = "/content/cnmc-leukemia"
categories = {"hem": 0, "all": 1}
IMG_SIZE = (150, 150)
X = []
y = []

folds = ["fold_0", "fold_1", "fold_2"]
for fold in folds:
    fold_path = os.path.join(path, fold)
for category in categories:
    category_path = os.path.join(fold_path, category)
    images = os.listdir(category_path)
    X.extend([cv2.resize(cv2.imread(os.path.join(category_path, img)), IMG_SIZE) / 255.0 for img in images if cv2.imread(os.path.join(category_path, img)) is not None])
    y.extend([categories[category]] * len(images))

X = np.array(X)
y = np.array(y)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(f"Dataset Loaded: {len(X)} images (Train: {len(X_train)}, Test: {len(X_test)})")

from keras import layers
from keras import models

model = models.Sequential()
model.add(layers.Conv2D(32,(3,3),activation = 'relu',input_shape=(150,150,3)))
model.add(layers.MaxPooling2D((2,2)))
model.add(layers.Conv2D(64,(3,3),activation='relu'))

model.add(layers.MaxPooling2D((2,2)))
model.add(layers.Conv2D(128,(3,3),activation='relu'))
model.add(layers.MaxPooling2D((2,2)))


model.add(layers.Flatten())
model.add(layers.Dense(512,activation='relu'))
model.add(layers.Dense(1,activation='sigmoid'))

model.summary()

from keras import optimizers
model.compile(loss='binary_crossentropy',optimizer = optimizers.RMSprop(),metrics=['acc'])
model.fit(X_train, y_train, epochs=10, validation_data=(X_test, y_test))
model.save("cancer.h5")
import tensorflow as tf
import cv2
from google.colab import files
from google.colab.patches import cv2_imshow
cancerde = tf.keras.models.load_model('cancer.h5')
import numpy as np
img=files.upload()
filename = list(img.keys())[0]
img = cv2.imread(filename)

if img is not None:

  cv2_imshow(img)
else:
  print("Sorry This file Does not exist.")

IMG_SIZE = (150, 150)

new = cv2.resize(img,IMG_SIZE)
print(f"Resized image shape: {new.shape}")  

img_normalized = new.astype('float32') / 255.0

img_normalized = np.expand_dims(img_normalized, axis=0)
prediction = cancerde.predict(img_normalized)
print(prediction)
if prediction >= 0.50:

  print("It is : cancer")
else:
  print("It is not  : cancer")
