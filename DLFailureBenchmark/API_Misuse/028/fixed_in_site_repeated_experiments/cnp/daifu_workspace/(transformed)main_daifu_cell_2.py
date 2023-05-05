def main_daifu_cell_2():
    try:
        global EPOCHS, args, callbacks, datetime, decoder_dims, encoder_dims, log_dir, loss, model, os, plot_clbk, strategy, tensorboard_clbk, test_ds, tf, tfk, time, train_ds
        model = ConditionalNeuralProcess(encoder_dims, decoder_dims)
        model.compile(loss=loss, optimizer='adam')
    except Exception as main_exception_2:
        daifu.CT_MANAGER.save(locals())
        raise
    else:
        return None, None
