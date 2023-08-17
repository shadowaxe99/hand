```python
import tensorflow as tf
from tensorflow.keras import layers
from data_preprocessing import processedSVGData
from feature_extraction import extractedFeatures

class ModelParameters:
    def __init__(self):
        self.latent_dim = 50
        self.batch_size = 128
        self.epochs = 100

def build_model(latent_dim):
    model = tf.keras.Sequential()
    model.add(layers.Dense(512, activation='relu', input_shape=(latent_dim,)))
    model.add(layers.Dense(256, activation='relu'))
    model.add(layers.Dense(latent_dim, activation='relu'))
    model.add(layers.Dense(len(extractedFeatures), activation='softmax'))
    return model

def trainModel():
    model_params = ModelParameters()
    model = build_model(model_params.latent_dim)
    model.compile(optimizer='adam', loss='categorical_crossentropy')
    model.fit(processedSVGData, extractedFeatures, epochs=model_params.epochs, batch_size=model_params.batch_size)
    return model

trainedModel = trainModel()
```