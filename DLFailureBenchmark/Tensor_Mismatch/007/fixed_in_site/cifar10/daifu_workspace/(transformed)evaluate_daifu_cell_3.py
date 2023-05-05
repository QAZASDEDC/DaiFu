def evaluate_daifu_cell_3():
    try:
        global FLAGS, cifar10, eval_data, g, images, labels, logits, saver, summary_op, summary_writer, tf, time, top_k_op, variable_averages, variables_to_restore
        eval_once(saver, summary_writer, top_k_op, summary_op)
        if FLAGS.run_once:
            return 'break', None
        time.sleep(FLAGS.eval_interval_secs)
    except Exception as evaluate_exception_3:
        daifu.CT_MANAGER.save(locals())
        raise
    else:
        return None, None
