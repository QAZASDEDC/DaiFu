@daifu.transform(globals())
def on_epoch_end(self, epoch, logs=None):
    images = self.model.sample(self.nex)
    imgs = []
    for i in range(self.nex):
        fig = self.plot_img(images[i])
        imgs.append(plot_to_image(fig))
    imgs = tf.concat(imgs, axis=0)
    with self.file_writer.as_default():
        tf.summary.image(name='Samples', data=imgs, step=epoch, max_outputs=self.nex)
