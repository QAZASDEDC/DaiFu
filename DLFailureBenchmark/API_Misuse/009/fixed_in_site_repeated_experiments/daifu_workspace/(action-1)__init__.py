def new_dis(self):
    model = Sequential()
    model.add(Flatten(input_shape=self.shape))
    model.add(Dense((self.width * self.height * self.channels), input_shape=self.shape))
    model.add(LeakyReLU(alpha=0.2))
    model.add(Dense(np.int64((self.width * self.height * self.channels)/2)))
    model.add(LeakyReLU(alpha=0.2))
    model.add(Dense(1, activation='sigmoid'))
    model.summary()

    return model

GAN.discriminator.__code__ = new_dis.__code__