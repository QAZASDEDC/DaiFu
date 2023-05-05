def compute_loss(x, y):
    pred = model(x)
    return tf.reduce_mean(tf.square(tf.subtract(pred, y)))

grads, loss = compute_gradient(model, preds, data)
print(grads)