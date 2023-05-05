def main_daifu_cell_1():
    try:
        global batch_size, data, epoch, epochs, grads, itr, loss, model, np, optimizer, preds, tf, train_dataset, x, y
        model = make_model()
        optimizer = tf.train.AdamOptimizer(0.0001)
        x = np.linspace(0, 1, 1000)
        y = x + np.random.normal(0, 0.3, 1000)
        y = y.astype('float32')
        train_dataset = tf.data.Dataset.from_tensor_slices(y.reshape(-1, 1))
        epochs = 10
        batch_size = 25
        itr = y.shape[0] // batch_size
        for epoch in range(epochs):
            try:
                daifu_return_tag, daifu_return_item = main_daifu_cell_2()
            except Exception:
                while True:
                    try:
                        daifu.RP_MANAGER.repair()
                        daifu_return_tag, daifu_return_item = main_daifu_rest_2()
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
    except Exception as main_exception_1:
        daifu.CT_MANAGER.save(locals())
        raise
    else:
        return None, None
