@daifu.with_goto
def main_daifu_rest_1():
    try:
        global K, argparse, args, batch_size, cloudpickle, conda_env, epochs, img_cols, img_rows, input_shape, int, keras, mlflow, mnist, model, num_classes, parser, score, tf, x_test, x_train, y_test, y_train
        goto .restart
        parser = argparse.ArgumentParser(description='Train a Keras CNN model for MNIST classification in PyTorch')
        parser.add_argument('--batch-size', '-b', type=int, default=128)
        parser.add_argument('--epochs', '-e', type=int, default=4)
        args = parser.parse_args()
        batch_size = args.batch_size
        epochs = args.epochs
        num_classes = 10
        mlflow.log_param('batch_size', batch_size)
        mlflow.log_param('epochs', epochs)
        img_rows, img_cols = 28, 28
        (x_train, y_train), (x_test, y_test) = mnist.load_data()
        if K.image_data_format() == 'channels_first':
            x_train = x_train.reshape(x_train.shape[0], 1, img_rows, img_cols)
            x_test = x_test.reshape(x_test.shape[0], 1, img_rows, img_cols)
            input_shape = 1, img_rows, img_cols
        else:
            x_train = x_train.reshape(x_train.shape[0], img_rows, img_cols, 1)
            x_test = x_test.reshape(x_test.shape[0], img_rows, img_cols, 1)
            input_shape = img_rows, img_cols, 1
        x_train = x_train.astype('float32')
        x_test = x_test.astype('float32')
        x_train /= 255
        x_test /= 255
        print('x_train shape:', x_train.shape)
        print(x_train.shape[0], 'train samples')
        print(x_test.shape[0], 'test samples')
        y_train = keras.utils.to_categorical(y_train, num_classes)
        y_test = keras.utils.to_categorical(y_test, num_classes)
        model = Sequential()
        label .restart
        model.add(Conv2D(64, (3, 3), activation='relu', input_shape=input_shape))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Dropout(0.25))
        model.add(Flatten())
        model.add(Dense(128, activation='relu'))
        model.add(Dense(num_classes, activation='softmax'))
        model.compile(loss=keras.losses.categorical_crossentropy, optimizer=keras.optimizers.Adadelta(), metrics=['accuracy'])
        model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, verbose=1, validation_data=(x_test, y_test))
        score = model.evaluate(x_test, y_test, verbose=0)
        mlflow.log_metric('cross_entropy_test_loss', score[0])
        mlflow.log_metric('test_accuracy', score[1])
        print('Test loss:', score[0])
        print('Test accuracy:', score[1])
        mlflow.keras.log_model(model, artifact_path='keras-model')
        conda_env = _mlflow_conda_env(additional_conda_deps=['keras=={}'.format(keras.__version__), 'tensorflow=={}'.format(tf.__version__)], additional_pip_deps=['cloudpickle=={}'.format(cloudpickle.__version__), 'mlflow=={}'.format(mlflow.__version__)])
        mlflow.pyfunc.log_model(artifact_path='keras-pyfunc', python_model=KerasMnistCNN(), artifacts={'keras-model': mlflow.get_artifact_uri('keras-model')}, conda_env=conda_env)
        print(mlflow.active_run().info.run_uuid)
    except Exception as main_exception_1:
        daifu.CT_MANAGER.save(locals())
        raise
    else:
        return None, None
