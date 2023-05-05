@daifu.transform(globals())
def main():
    strategy = tf.distribute.MirroredStrategy()
    with strategy.scope():
        model = ConditionalNeuralProcess(encoder_dims, decoder_dims)
        model.compile(loss=loss, optimizer='adam')
    time = datetime.now().strftime('%Y%m%d-%H%M%S')
    log_dir = os.path.join('.', 'logs', 'cnp', args.task, time)
    tensorboard_clbk = tfk.callbacks.TensorBoard(log_dir=log_dir, update_freq='batch')
    plot_clbk = PlotCallback(logdir=log_dir, ds=test_ds, task=args.task)
    callbacks = [tensorboard_clbk, plot_clbk]
    model.fit(train_ds, epochs=EPOCHS, callbacks=callbacks)
    daifu.log_program_end()
