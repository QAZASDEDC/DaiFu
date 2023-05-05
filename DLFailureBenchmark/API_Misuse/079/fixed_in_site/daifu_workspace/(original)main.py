@daifu.transform(globals())
def main():
    model = make_model()
    optimizer = tf.train.AdamOptimizer(0.0001)
    x = np.linspace(0, 1, 1000)
    y = x + np.random.normal(0, 0.3, 1000)
    y = y.astype('float32')
    train_dataset = tf.data.Dataset.from_tensor_slices(y.reshape(-1, 1))
    epochs = 10
    batch_size = 25
    itr = y.shape[0] // batch_size
    for epoch in range(epochs):
        for data in tf.contrib.eager.Iterator(train_dataset.batch(25)):
            preds = model(data)
            grads, loss = compute_gradient(model, preds, data)
            print(grads)
            apply_gradients(optimizer, grads, model.variables)
