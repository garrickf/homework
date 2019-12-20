"""
Presents a simple RNN for running sentiment analysis.
"""

import tensorflow.keras as K
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing import sequence
import tensorflow as tf
import numpy as np

# Set random seeds for reproducibility
np.random.seed(1)
tf.random.set_seed(1)

def get_model():
    """
    Creates and returns the RNN model.
    """
    vocabulary_size = 5000
    embedding_size = 64
    input_length = 500
    rnn_activations = 128

    X = K.layers.Input(shape=(input_length,))

    Embedded = K.layers.Embedding(vocabulary_size, embedding_size)(X)

    LSTM = K.layers.LSTM(rnn_activations)(Embedded)

    Y = K.layers.Dense(1, activation='sigmoid')(LSTM)

    model = K.models.Model(inputs=X, outputs=Y)
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model


def get_data():
    vocabulary_size = 5000
    input_length = 500
    
    (x_train, y_train), (x_test, y_test) = imdb.load_data(num_words = vocabulary_size)
    print('Loaded dataset with {} training samples, {} test samples'.format(len(x_train), len(x_test)))

    x_train = sequence.pad_sequences(x_train, maxlen=input_length)
    x_test = sequence.pad_sequences(x_test, maxlen=input_length)

    return (x_train, y_train), (x_test, y_test)


def train(model, x_train, y_train):
    batch_size = 64
    num_epochs = 3

    model.fit(x_train, y_train, batch_size=batch_size, epochs=num_epochs)


def test(model, x_test, y_test):
    model.evaluate(x_test, y_test)


def main(): 
    model = get_model()
    model.summary()
    
    (x_train, y_train), (x_test, y_test) = get_data()

    train(model, x_train, y_train)

    test(model, x_test, y_test)


if __name__ == '__main__':
    main()
