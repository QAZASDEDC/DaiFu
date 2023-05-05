@daifu.transform(globals())
def __init__(self, width=28, height=28, channels=1):
    self.width = width
    self.height = height
    self.channels = channels
    self.shape = self.width, self.height, self.channels
    self.optimizer = Adam(lr=0.0002, beta_1=0.5, decay=8e-08)
    self.G = self.generator()
    self.G.compile(loss='binary_crossentropy', optimizer=self.optimizer)
    self.D = self.discriminator()
    self.D.compile(loss='binary_crossentropy', optimizer=self.optimizer, metrics=['accuracy'])
    self.stacked_generator_discriminator = self.stacked_generator_discriminator()
    self.stacked_generator_discriminator.compile(loss='binary_crossentropy', optimizer=self.optimizer)
