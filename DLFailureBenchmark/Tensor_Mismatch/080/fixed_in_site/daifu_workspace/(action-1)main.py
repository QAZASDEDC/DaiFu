from keras.layers import Flatten
model = Sequential([
    Conv2D(8, kernel_size=(3, 3), padding="same", activation=activations.relu, input_shape=(28, 28, 1)),
    Flatten(),
    Dense(64, activation=activations.relu),
    Dense(64, activation=activations.relu),
    Dense(10, activation=activations.softmax)
])

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)