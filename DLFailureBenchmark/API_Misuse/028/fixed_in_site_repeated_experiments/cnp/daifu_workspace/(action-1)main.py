train_ds, test_ds = mnist['train'], mnist['test']
def encode(element):
    # element should be already batched
    img = tf.cast(element['image'], tf.float32) / 255.
    batch_size = tf.shape(img)[0]
    num_context = tf.random.uniform(
        shape=[], minval=10, maxval=100, dtype=tf.int32)
    context_x = tf.random.uniform(
        shape=(batch_size, num_context, 2),
        minval=0, maxval=27, dtype=tf.int32)
    context_y = tf.gather_nd(img, context_x, batch_dims=1)  # TODO check
    context_x = tf.cast(context_x, tf.float32)  /27.  # normalize
    cols, rows = tf.meshgrid(tf.range(28.), tf.transpose(tf.range(28.)))
    grid = tf.stack([rows, cols], axis=-1)  # (28, 28, 2)
    batch_grid = tf.tile(
        tf.expand_dims(grid, axis=0),
        [batch_size, 1, 1, 1])  # (batch_size, 28, 28, 2)
    target_x = tf.reshape(
        batch_grid, (batch_size, 28 * 28, 2)) / 27.  # normalize
    target_y = tf.reshape(img, (batch_size, 28 * 28, 1))
    return (context_x, context_y, target_x), target_y

train_ds = train_ds.batch(BATCH_SIZE).map(encode)
test_ds = test_ds.batch(1).map(encode)

plot_clbk = PlotCallback(logdir=log_dir, ds=test_ds, task=args.task)
callbacks = [tensorboard_clbk, plot_clbk]
