def main_daifu_cell_1():
    try:
        global W, X, Y, a, all, b, c, cost, hypothesis, nb_classes, optimizer, print_val, sess, step, tf, x_data, y_data
        x_data = [[1, 2, 1, 1], [2, 1, 3, 2], [3, 1, 3, 4], [4, 1, 5, 5], [1, 7, 5, 5], [1, 2, 5, 6], [1, 6, 6, 6], [1, 7, 7, 7]]
        y_data = [[0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 1, 0], [0, 1, 0], [0, 1, 0], [1, 0, 0], [1, 0, 0]]
        X = tf.placeholder('float', [None, 4])
        Y = tf.placeholder('float', [None, 3])
        nb_classes = 3
        W = tf.Variable(tf.random_normal([4, nb_classes]), name='weight')
        b = tf.Variable(tf.random_normal([nb_classes]), name='bias')
        hypothesis = tf.nn.softmax(tf.matmul(X, W) + b)
        cost = tf.reduce_mean(-tf.reduce_sum(Y * tf.log(hypothesis), axis=1))
        optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.1).minimize(cost)
        with tf.Session() as sess:
            try:
                daifu_return_tag, daifu_return_item = main_daifu_cell_2()
            except Exception:
                while True:
                    try:
                        daifu.RP_MANAGER.repair()
                        daifu_return_tag, daifu_return_item = main_daifu_rest_2()
                        if daifu_return_tag is not None:
                            if daifu_return_tag == 'break':
                                break
                            else:
                                return daifu_return_tag, daifu_return_item
                        break
                    except Exception:
                        continue
    except Exception as main_exception_1:
        daifu.CT_MANAGER.save(locals())
        raise
    else:
        return None, None
