def main_daifu_cell_3():
    try:
        global W, X, Y, a, all, b, c, cost, hypothesis, nb_classes, optimizer, print_val, sess, step, tf, x_data, y_data
        sess.run(optimizer, feed_dict={X: x_data, Y: y_data})
        if step % 200 == 0:
            print(step, sess.run(cost, feed_dict={X: x_data, Y: y_data}))
    except Exception as main_exception_3:
        daifu.CT_MANAGER.save(locals())
        raise
    else:
        return None, None
