def train_daifu_cell_5():
    try:
        global FLAGS, _, apply_gradient_op, checkpoint_path, cifar10, datetime, decay_steps, duration, examples_per_sec, format_str, global_step, grad, grads, i, init, loss, loss_value, lr, np, num_batches_per_epoch, num_examples_per_step, opt, os, saver, scope, sec_per_batch, sess, start_time, step, summaries, summary_op, summary_str, summary_writer, tf, time, tower_grads, train_op, var, variable_averages, variables_averages_op
        loss = tower_loss(scope)
        tf.get_variable_scope().reuse_variables()
        summaries = tf.get_collection(tf.GraphKeys.SUMMARIES, scope)
        grads = opt.compute_gradients(loss)
        tower_grads.append(grads)
    except Exception as train_exception_5:
        daifu.CT_MANAGER.save(locals())
        raise
    else:
        return None, None
