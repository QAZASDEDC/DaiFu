@daifu.transform(globals())
def plot_img(self, image):
    fig, ax = plt.subplots(nrows=1, ncols=1)
    image = tf.cast(image, tf.int32)
    if image.shape[-1] == 1:
        image = tf.squeeze(image, axis=-1)
    ax.imshow(image, vmin=0.0, vmax=1.0, cmap=plt.cm.Greys)
    ax.axis('off')
    return fig
