def main_daifu_cell_2():
    try:
        global W, X, Y, a, all, b, c, cost, hypothesis, nb_classes, optimizer, print_val, sess, step, tf, x_data, y_data
        sess.run(tf.global_variables_initializer())
        for step in range(2001):
            try:
                daifu_return_tag, daifu_return_item = main_daifu_cell_3()
            except Exception:
                while True:
                    try:
                        daifu.RP_MANAGER.repair()
                        daifu_return_tag, daifu_return_item = main_daifu_rest_3()
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
        print('--------------')
        a = sess.run(hypothesis, feed_dict={X: [[1, 11, 7, 9]]})
        print(a, sess.run(tf.arg_max(a, 1)))
        print('--------------')
        b = sess.run(hypothesis, feed_dict={X: [[1, 3, 4, 3]]})
        print(b, sess.run(tf.arg_max(b, 1)))
        print('--------------')
        c = sess.run(hypothesis, feed_dict={X: [[1, 1, 0, 1]]})
        print(c, sess.run(tf.arg_max(c, 1)))
        print('--------------')
        all = sess.run(hypothesis, feed_dict={X: [[1, 11, 7, 9], [1, 3, 4, 3], [1, 1, 0, 1]]})
        print(all, sess.run(tf.arg_max(all, 1)))
        print_val = sess.run(tf.argmax(all, 1))
    except Exception as main_exception_2:
        daifu.CT_MANAGER.save(locals())
        raise
    else:
        return None, None
