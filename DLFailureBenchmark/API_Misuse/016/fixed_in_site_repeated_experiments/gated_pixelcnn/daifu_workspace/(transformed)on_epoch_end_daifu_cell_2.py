def on_epoch_end_daifu_cell_2():
    try:
        global epoch, fig, i, images, imgs, logs, self, tf
        fig = self.plot_img(images[i])
        imgs.append(plot_to_image(fig))
    except Exception as on_epoch_end_exception_2:
        daifu.CT_MANAGER.save(locals())
        raise
    else:
        return None, None
