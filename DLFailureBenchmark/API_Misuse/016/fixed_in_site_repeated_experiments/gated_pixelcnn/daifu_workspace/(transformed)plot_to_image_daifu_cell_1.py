def plot_to_image_daifu_cell_1():
    try:
        global buf, figure, image, io, plt, tf
        """Converts the matplotlib plot specified by 'figure' to a PNG image and
    returns it. The supplied figure is closed and inaccessible after this call."""
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        plt.close(figure)
        buf.seek(0)
        image = tf.image.decode_png(buf.getvalue(), channels=4)
        image = tf.expand_dims(image, 0)
        return 'plot_to_image_daifu_cell_1', image
    except Exception as plot_to_image_exception_1:
        daifu.CT_MANAGER.save(locals())
        raise
    else:
        return None, None
