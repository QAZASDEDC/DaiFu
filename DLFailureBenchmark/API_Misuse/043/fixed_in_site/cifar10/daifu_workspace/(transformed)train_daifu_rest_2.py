@daifu.with_goto
def train_daifu_rest_2():
    try:
        global FLAGS, _, apply_gradient_op, checkpoint_path, cifar10, datetime, decay_steps, duration, examples_per_sec, format_str, global_step, grad, grads, i, init, loss, loss_value, lr, np, num_batches_per_epoch, num_examples_per_step, opt, os, saver, scope, sec_per_batch, sess, start_time, step, summaries, summary_op, summary_str, summary_writer, tf, time, tower_grads, train_op, var, variable_averages, variables_averages_op
        goto .restart
        global_step = tf.get_variable('global_step', [], initializer=tf.constant_initializer(0), trainable=False)
        num_batches_per_epoch = cifar10.NUM_EXAMPLES_PER_EPOCH_FOR_TRAIN / FLAGS.batch_size
        decay_steps = int(num_batches_per_epoch * cifar10.NUM_EPOCHS_PER_DECAY)
        lr = tf.train.exponential_decay(cifar10.INITIAL_LEARNING_RATE, global_step, decay_steps, cifar10.LEARNING_RATE_DECAY_FACTOR, staircase=True)
        opt = tf.train.GradientDescentOptimizer(lr)
        tower_grads = []
        manager = tf.variable_scope(tf.get_variable_scope())
        enter = type(manager).__enter__
        exit = type(manager).__exit__
        value = enter(manager)
        for i in xrange(FLAGS.num_gpus):
            try:
                daifu_return_tag, daifu_return_item = train_daifu_cell_3()
            except Exception:
                while True:
                    try:
                        daifu.RP_MANAGER.repair()
                        daifu_return_tag, daifu_return_item = train_daifu_rest_3()
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
        exit(manager, None, None, None)
        grads = average_gradients(tower_grads)
        summaries.append(tf.summary.scalar('learning_rate', lr))
        for grad, var in grads:
            try:
                daifu_return_tag, daifu_return_item = train_daifu_cell_6()
            except Exception:
                while True:
                    try:
                        daifu.RP_MANAGER.repair()
                        daifu_return_tag, daifu_return_item = train_daifu_rest_6()
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
        apply_gradient_op = opt.apply_gradients(grads, global_step=global_step)
        for var in tf.trainable_variables():
            try:
                daifu_return_tag, daifu_return_item = train_daifu_cell_7()
            except Exception:
                while True:
                    try:
                        daifu.RP_MANAGER.repair()
                        daifu_return_tag, daifu_return_item = train_daifu_rest_7()
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
        variable_averages = tf.train.ExponentialMovingAverage(cifar10.MOVING_AVERAGE_DECAY, global_step)
        label .restart
        variables_averages_op = variable_averages.apply(tf.trainable_variables())
        train_op = tf.group(apply_gradient_op, variables_averages_op)
        saver = tf.train.Saver(tf.global_variables())
        summary_op = tf.summary.merge(summaries)
        init = tf.global_variables_initializer()
        sess = tf.Session(config=tf.ConfigProto(allow_soft_placement=True, log_device_placement=FLAGS.log_device_placement))
        sess.run(init)
        tf.train.start_queue_runners(sess=sess)
        summary_writer = tf.summary.FileWriter(FLAGS.train_dir, sess.graph)
        for step in xrange(FLAGS.max_steps):
            try:
                daifu_return_tag, daifu_return_item = train_daifu_cell_8()
            except Exception:
                while True:
                    try:
                        daifu.RP_MANAGER.repair()
                        daifu_return_tag, daifu_return_item = train_daifu_rest_8()
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
    except Exception as train_exception_2:
        daifu.CT_MANAGER.save(locals())
        raise
    else:
        return None, None
