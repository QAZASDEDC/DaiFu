def main_daifu_cell_1():
    try:
        global EPOCHS, args, callbacks, datetime, decoder_dims, encoder_dims, log_dir, loss, model, os, plot_clbk, strategy, tensorboard_clbk, test_ds, tf, tfk, time, train_ds
        strategy = tf.distribute.MirroredStrategy()
        with strategy.scope():
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
        time = datetime.now().strftime('%Y%m%d-%H%M%S')
        log_dir = os.path.join('.', 'logs', 'cnp', args.task, time)
        tensorboard_clbk = tfk.callbacks.TensorBoard(log_dir=log_dir, update_freq='batch')
        plot_clbk = PlotCallback(logdir=log_dir, ds=test_ds, task=args.task)
        callbacks = [tensorboard_clbk, plot_clbk]
        model.fit(train_ds, epochs=EPOCHS, callbacks=callbacks)
    except Exception as main_exception_1:
        daifu.CT_MANAGER.save(locals())
        raise
    else:
        return None, None
