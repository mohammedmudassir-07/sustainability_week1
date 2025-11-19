import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import os

# Create models directory if it doesn't exist
os.makedirs('models', exist_ok=True)

# Define the model
def create_model():
    model = keras.Sequential([
        layers.Input(shape=(128, 128, 3)),
        layers.Conv2D(32, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(128, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Flatten(),
        layers.Dense(128, activation='relu'),
        layers.Dropout(0.5),
        layers.Dense(10, activation='softmax')  # 10 classes
    ])
    
    model.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )
    
    return model

# Create and save the model
model = create_model()
model.save('models/waste_classifier_model.h5')
print("✅ Model created and saved successfully!")
print(f"📁 Model location: models/waste_classifier_model.h5")