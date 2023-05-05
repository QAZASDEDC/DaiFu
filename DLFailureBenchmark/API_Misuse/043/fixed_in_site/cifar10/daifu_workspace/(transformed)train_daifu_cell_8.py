def train_daifu_cell_8():
    try:
        global FLAGS, _, apply_gradient_op, checkpoint_path, cifar10, datetime, decay_steps, duration, examples_per_sec, format_str, global_step, grad, grads, i, init, loss, loss_value, lr, np, num_batches_per_epoch, num_examples_per_step, opt, os, saver, scope, sec_per_batch, sess, start_time, step, summaries, summary_op, summary_str, summary_writer, tf, time, tower_grads, train_op, var, variable_averages, variables_averages_op
        start_time = time.time()
        _, loss_value = sess.run([train_op, loss])
        duration = time.time() - start_time
        assert not np.isnan(loss_value), 'Model diverged with loss = NaN'
        if step % 10 == 0:
            num_examples_per_step = FLAGS.batch_size * FLAGS.num_gpus
            examples_per_sec = num_examples_per_step / duration
            sec_per_batch = duration / FLAGS.num_gpus
            format_str = '%s: step %d, loss = %.2f (%.1f examples/sec; %.3f sec/batch)'
            print(format_str % (datetime.now(), step, loss_value, examples_per_sec, sec_per_batch))
        if step % 100 == 0:
            summary_str = sess.run(summary_op)
            summary_writer.add_summary(summary_str, step)
        if step % 1000 == 0 or step + 1 == FLAGS.max_steps:
            checkpoint_path = os.path.join(FLAGS.train_dir, 'model.ckpt')
            saver.save(sess, checkpoint_path, global_step=step)
    except Exception as train_exception_8:
        daifu.CT_MANAGER.save(locals())
        raise
    else:
        return None, None
