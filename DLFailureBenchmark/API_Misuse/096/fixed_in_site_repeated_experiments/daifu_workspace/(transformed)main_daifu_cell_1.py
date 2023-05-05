def main_daifu_cell_1():
    try:
        global X, X_list, Y, Y_list, dataframe, dataset, float, model
        dataframe = read_csv('sonar.all-data', header=None)
        dataset = dataframe.values
        X = dataset[:, 0:60].astype(float)
        Y = dataset[:, (60)]
        Y[Y == 'R'] = 0
        Y[Y == 'M'] = 1
        X_list = X.tolist()
        Y_list = Y.tolist()
        model = Sequential()
        model.add(Dense(5, input_dim=len(X_list[0]), activation='sigmoid'))
        model.add(Dense(1, activation='sigmoid'))
        model.compile(loss='mean_squared_error', optimizer='adam', metrics=['acc'])
        model.fit(np.array(X_list), np.array(Y_list), epochs=20, batch_size=10)
    except Exception as main_exception_1:
        daifu.CT_MANAGER.save(locals())
        raise
    else:
        return None, None
