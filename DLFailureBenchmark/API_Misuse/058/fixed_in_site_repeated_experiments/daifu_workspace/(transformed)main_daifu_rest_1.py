@daifu.with_goto
def main_daifu_rest_1():
    try:
        global model, np, rmsprop, x_data, y_data, y_predict
        goto .restart
        x_data = [[73.0, 80.0, 75.0], [93.0, 88.0, 93.0], [89.0, 91.0, 90.0], [96.0, 98.0, 100.0], [73.0, 66.0, 70.0]]
        y_data = [[152.0], [185.0], [180.0], [196.0], [142.0]]
        model = Sequential()
        model.add(Dense(input_dim=3, units=1))
        model.add(Activation('linear'))
        rmsprop = RMSprop(lr=0.1)
        model.compile(loss='mse', optimizer=rmsprop, metrics=['accuracy'])
        label .restart
        model.fit(x_data, y_data, epochs=1000)
        y_predict = model.predict(np.array([[95.0, 100.0, 80]]))
        print(y_predict)
    except Exception as main_exception_1:
        daifu.CT_MANAGER.save(locals())
        raise
    else:
        return None, None
