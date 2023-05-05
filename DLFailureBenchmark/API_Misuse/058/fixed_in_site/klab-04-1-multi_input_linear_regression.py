from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import RMSprop
import numpy as np

import sys
sys.path.append('../../../..')
import daifu

@daifu.transform(globals())
def main():
    x_data = [[73., 80., 75.],
            [93., 88., 93.],
            [89., 91., 90.],
            [96., 98., 100.],
            [73., 66., 70.]]
    y_data = [[152.],
            [185.],
            [180.],
            [196.],
            [142.]]

    model = Sequential()
    model.add(Dense(input_dim=3, units=1))
    model.add(Activation('linear'))

    rmsprop = RMSprop(lr=0.1)
    model.compile(loss='mse', optimizer=rmsprop, metrics=['accuracy'])
    model.fit(x_data, y_data, epochs=1000)

    y_predict = model.predict(np.array([[95., 100., 80]]))
    print(y_predict)

main()
daifu.log_program_end()