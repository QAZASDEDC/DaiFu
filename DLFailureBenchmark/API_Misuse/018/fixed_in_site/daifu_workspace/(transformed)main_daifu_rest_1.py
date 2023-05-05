@daifu.with_goto
def main_daifu_rest_1():
    try:
        global batch_size, beta_schedule, callbacks, conv, datagen, epoch, f, gibbs_pruning, init, input_shape, inputs, keras, ks, kwargs, layers, lr_scheduler, m, model, n_classes, n_epochs, np, opt, outputs, p, reg, s, score, test_gen, train_gen, x, x_test, x_train, y_test, y_train
        goto .restart
        (x_train, y_train), (x_test, y_test) = keras.datasets.cifar10.load_data()
        n_classes = 10
        input_shape = x_train.shape[1:]
        x_train = x_train.astype('float32')
        x_test = x_test.astype('float32')
        m = np.mean(x_train)
        s = np.std(x_train)
        x_train = (x_train - m) / (s + 1e-07)
        x_test = (x_test - m) / (s + 1e-07)
        label .restart
        gibbs_stretch = 1
        lr_schedule = lambda epoch: 0.001 if epoch // gibbs_stretch <= 80 else 0.0001 if epoch // gibbs_stretch <= 120 else 1e-05 if epoch // gibbs_stretch <= 160 else 1e-06
        n_epochs = 1 * gibbs_stretch
        batch_size = 128
        opt = keras.optimizers.Adam(learning_rate=lr_schedule(0))
        lr_scheduler = keras.callbacks.LearningRateScheduler(lr_schedule, verbose=1)
        callbacks = [lr_scheduler]
        callbacks.append(keras.callbacks.TensorBoard(log_dir='./logs/tensorboard'))
        p = 0.9
        beta_schedule = np.logspace(0, 4, num=128 * gibbs_stretch)
        conv = lambda f, ks, **kwargs: gibbs_pruning.GibbsPrunedConv2D(f, ks, p=p, **kwargs)
        callbacks.append(gibbs_pruning.GibbsPruningAnnealer(beta_schedule, verbose=1))
        datagen = keras.preprocessing.image.ImageDataGenerator(width_shift_range=0.1, height_shift_range=0.1, horizontal_flip=True)
        datagen.fit(x_train)
        train_gen = datagen.flow(x_train, y_train, batch_size=batch_size)
        reg = keras.regularizers.l2(0.0001)
        init = keras.initializers.he_normal()
        inputs = keras.Input(shape=input_shape)
        x = layers.Conv2D(16, 3, padding='same', kernel_initializer=init, kernel_regularizer=reg, use_bias=False)(inputs)
        x = layers.BatchNormalization()(x)
        x = layers.Activation('relu')(x)
        x = resnet_block(16, conv, False, x)
        x = resnet_block(16, conv, False, x)
        x = resnet_block(16, conv, False, x)
        x = resnet_block(32, conv, True, x)
        x = resnet_block(32, conv, False, x)
        x = resnet_block(32, conv, False, x)
        x = resnet_block(64, conv, True, x)
        x = resnet_block(64, conv, False, x)
        x = resnet_block(64, conv, False, x)
        x = layers.GlobalAveragePooling2D()(x)
        outputs = layers.Dense(n_classes, activation='softmax', kernel_initializer=init)(x)
        model = keras.Model(inputs, outputs)
        model.compile(loss=keras.losses.SparseCategoricalCrossentropy(), optimizer=opt, metrics=['accuracy'])
        model.summary()
        model.fit(train_gen, steps_per_epoch=x_train.shape[0] // batch_size, epochs=n_epochs, validation_data=(x_test, y_test), callbacks=callbacks)
        score = model.evaluate(x_test, y_test)
        print('Test loss:', score[0])
        print('Test accuracy:', score[1])
    except Exception as main_exception_1:
        daifu.CT_MANAGER.save(locals())
        raise
    else:
        return None, None
