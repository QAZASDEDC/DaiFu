def on_epoch_end_daifu_cell_1():
    try:
        global epoch, fig, i, images, imgs, logs, self, tf
        images = self.model.sample(self.nex)
        imgs = []
        for i in range(self.nex):
            try:
                daifu_return_tag, daifu_return_item = (
                    on_epoch_end_daifu_cell_2())
            except Exception:
                while True:
                    try:
                        daifu.RP_MANAGER.repair()
                        daifu_return_tag, daifu_return_item = (
                            on_epoch_end_daifu_rest_2())
                        if daifu_return_tag is not None:
                            if daifu_return_tag == 'break':
                                break
                            else:
                                return daifu_return_tag, daifu_return_item
                        break
                    except Exception:
                        continue
                if daifu_return_tag == 'break':
                    break
        imgs = tf.concat(imgs, axis=0)
        with self.file_writer.as_default():
            try:
                daifu_return_tag, daifu_return_item = (
                    on_epoch_end_daifu_cell_3())
            except Exception:
                while True:
                    try:
                        daifu.RP_MANAGER.repair()
                        daifu_return_tag, daifu_return_item = (
                            on_epoch_end_daifu_rest_3())
                        if daifu_return_tag is not None:
                            if daifu_return_tag == 'break':
                                break
                            else:
                                return daifu_return_tag, daifu_return_item
                        break
                    except Exception:
                        continue
    except Exception as on_epoch_end_exception_1:
        daifu.CT_MANAGER.save(locals())
        raise
    else:
        return None, None
