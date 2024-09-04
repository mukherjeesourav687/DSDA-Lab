import tensorflow as tf
from tensorflow.keras.applications import VGG16, DenseNet201
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, GlobalAveragePooling2D
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Load and preprocess data
train_datagen = ImageDataGenerator(rescale=1.0/255)
train_data = train_datagen.flow_from_directory('path/to/train/data', target_size=(224, 224), batch_size=32, class_mode='binary')

# VGG-16 Model
vgg16 = VGG16(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
model_vgg16 = Sequential([
    vgg16,
    Flatten(),
    Dense(256, activation='relu'),
    Dense(1, activation='sigmoid')
])

model_vgg16.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train VGG-16 model
model_vgg16.fit(train_data, epochs=10)

# DenseNet-201 Model
densenet = DenseNet201(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
model_densenet = Sequential([
    densenet,
    GlobalAveragePooling2D(),
    Dense(256, activation='relu'),
    Dense(1, activation='sigmoid')
])

model_densenet.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train DenseNet-201 model
model_densenet.fit(train_data, epochs=10)
