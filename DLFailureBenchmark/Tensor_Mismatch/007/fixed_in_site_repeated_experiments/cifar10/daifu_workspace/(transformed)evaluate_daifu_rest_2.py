@daifu.with_goto
def evaluate_daifu_rest_2():
    try:
        global FLAGS, cifar10, eval_data, g, images, labels, logits, saver, summary_op, summary_writer, tf, time, top_k_op, variable_averages, variables_to_restore
        goto .restart
        eval_data = FLAGS.eval_data == 'test'
        label .restart
        images, labels = cifar10.inputs(eval_data=eval_data)
        logits = cifar10.inference(images)
        top_k_op = tf.nn.in_top_k(logits, labels, 1)
        variable_averages = tf.train.ExponentialMovingAverage(cifar10.MOVING_AVERAGE_DECAY)
        variables_to_restore = variable_averages.variables_to_restore()
        saver = tf.train.Saver(variables_to_restore)
        summary_op = tf.summary.merge_all()
        summary_writer = tf.summary.FileWriter(FLAGS.eval_dir, g)
        while True:
            try:
                daifu_return_tag, daifu_return_item = evaluate_daifu_cell_3()
                if daifu_return_tag is not None:
                    if daifu_return_tag == 'break':
                        break
                    else:
                        return daifu_return_tag, daifu_return_item
            except Exception:
                while True:
                    try:
                        daifu.RP_MANAGER.repair()
                        daifu_return_tag, daifu_return_item = evaluate_daifu_rest_3()
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
    except Exception as evaluate_exception_2:
        daifu.CT_MANAGER.save(locals())
        raise
    else:
        return None, None
