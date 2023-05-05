def main_daifu_cell_2():
    try:
        global batch_size, data, epoch, epochs, grads, itr, loss, model, np, optimizer, preds, tf, train_dataset, x, y
        for data in tf.contrib.eager.Iterator(train_dataset.batch(25)):
            try:
                daifu_return_tag, daifu_return_item = main_daifu_cell_3()
            except Exception:
                while True:
                    try:
                        daifu.RP_MANAGER.repair()
                        daifu_return_tag, daifu_return_item = main_daifu_rest_3()
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
    except Exception as main_exception_2:
        daifu.CT_MANAGER.save(locals())
        raise
    else:
        return None, None
