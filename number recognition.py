import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.utils import to_categorical
import matplotlib.pyplot as plt
import numpy as np
import random

print('Training AI model...\n')
# Load the MNIST dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalize the pixel values from [0, 255] to [0, 1]
x_train, x_test = x_train / 255.0, x_test / 255.0

# One-hot encode the labels
y_train_cat = to_categorical(y_train)
y_test_cat = to_categorical(y_test)

# Build a simple neural network
model = Sequential([
    Flatten(input_shape=(28, 28)),
    Dense(128, activation='relu'),
    Dense(10, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Train the model
model.fit(x_train, y_train_cat, epochs=5, validation_split=0.1)

# Evaluate the model
print('Evaluating model accuracy...\n')
loss, accuracy = model.evaluate(x_test, y_test_cat)

print(f"Test accuracy: {accuracy:.4f}\n")

# Pick random test images and predict
num_samples = 10
indices = random.sample(range(len(x_test)), num_samples)

for idx in indices:
    img = x_test[idx]
    actual = y_test[idx]
    prediction = model.predict(np.expand_dims(img, axis=0), verbose=0)
    predicted = np.argmax(prediction)

    plt.imshow(img, cmap='gray')
    plt.title(f"Predicted: {predicted}")
    plt.axis('off')
    plt.show()
