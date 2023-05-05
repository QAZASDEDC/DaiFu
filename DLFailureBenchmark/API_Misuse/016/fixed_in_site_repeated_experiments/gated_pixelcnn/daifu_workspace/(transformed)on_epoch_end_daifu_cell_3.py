def on_epoch_end_daifu_cell_3():
    try:
        global epoch, fig, i, images, imgs, logs, self, tf
        tf.summary.image(name='Samples', data=imgs, step=epoch, max_outputs=self.nex)
    except Exception as on_epoch_end_exception_3:
        daifu.CT_MANAGER.save(locals())
        raise
    else:
        return None, None
