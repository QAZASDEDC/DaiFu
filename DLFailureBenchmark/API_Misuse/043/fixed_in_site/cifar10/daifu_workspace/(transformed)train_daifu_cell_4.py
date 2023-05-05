def train_daifu_cell_4():
    try:
        global FLAGS, _, apply_gradient_op, checkpoint_path, cifar10, datetime, decay_steps, duration, examples_per_sec, format_str, global_step, grad, grads, i, init, loss, loss_value, lr, np, num_batches_per_epoch, num_examples_per_step, opt, os, saver, scope, sec_per_batch, sess, start_time, step, summaries, summary_op, summary_str, summary_writer, tf, time, tower_grads, train_op, var, variable_averages, variables_averages_op
        with tf.name_scope('%s_%d' % (cifar10.TOWER_NAME, i)) as scope:
            try:
                daifu_return_tag, daifu_return_item = train_daifu_cell_5()
            except Exception:
                while True:
                    try:
                        daifu.RP_MANAGER.repair()
                        daifu_return_tag, daifu_return_item = train_daifu_rest_5()
                        if daifu_return_tag is not None:
                            if daifu_return_tag == 'break':
                                break
                            else:
                                return daifu_return_tag, daifu_return_item
                        break
                    except Exception:
                        continue
    except Exception as train_exception_4:
        daifu.CT_MANAGER.save(locals())
        raise
    else:
        return None, None
