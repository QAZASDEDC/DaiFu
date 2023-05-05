def plot_img_daifu_cell_1():
    try:
        global ax, fig, image, plt, self, tf
        fig, ax = plt.subplots(nrows=1, ncols=1)
        image = tf.cast(image, tf.int32)
        if image.shape[-1] == 1:
            image = tf.squeeze(image, axis=-1)
        ax.imshow(image, vmin=0.0, vmax=1.0, cmap=plt.cm.Greys)
        ax.axis('off')
        return 'plot_img_daifu_cell_1', fig
    except Exception as plot_img_exception_1:
        daifu.CT_MANAGER.save(locals())
        raise
    else:
        return None, None
