def train_daifu_cell_1():
    try:
        global X_train, batch, cnt, d_loss, epochs, g_loss, gen_noise, legit_images, noise, np, random_index, save_interval, self, syntetic_images, x_combined_batch, y_combined_batch, y_mislabled
        for cnt in range(epochs):
            try:
                daifu_return_tag, daifu_return_item = train_daifu_cell_2()
            except Exception:
                while True:
                    try:
                        daifu.RP_MANAGER.repair()
                        daifu_return_tag, daifu_return_item = (
                            train_daifu_rest_2())
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
    except Exception as train_exception_1:
        daifu.CT_MANAGER.save(locals())
        raise
    else:
        return None, None
