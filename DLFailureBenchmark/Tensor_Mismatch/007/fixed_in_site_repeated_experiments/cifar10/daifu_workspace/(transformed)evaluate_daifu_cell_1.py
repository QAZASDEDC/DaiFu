def evaluate_daifu_cell_1():
    try:
        global FLAGS, cifar10, eval_data, g, images, labels, logits, saver, summary_op, summary_writer, tf, time, top_k_op, variable_averages, variables_to_restore
        """Eval CIFAR-10 for a number of steps."""
        with tf.Graph().as_default() as g:
            try:
                daifu_return_tag, daifu_return_item = evaluate_daifu_cell_2()
            except Exception:
                while True:
                    try:
                        daifu.RP_MANAGER.repair()
                        daifu_return_tag, daifu_return_item = evaluate_daifu_rest_2()
                        if daifu_return_tag is not None:
                            if daifu_return_tag == 'break':
                                break
                            else:
                                return daifu_return_tag, daifu_return_item
                        break
                    except Exception:
                        continue
    except Exception as evaluate_exception_1:
        daifu.CT_MANAGER.save(locals())
        raise
    else:
        return None, None
