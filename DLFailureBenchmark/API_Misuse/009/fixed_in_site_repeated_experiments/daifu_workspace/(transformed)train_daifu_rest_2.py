@daifu.with_goto
def train_daifu_rest_2():
    try:
        global X_train, batch, cnt, d_loss, epochs, g_loss, gen_noise, legit_images, noise, np, random_index, save_interval, self, syntetic_images, x_combined_batch, y_combined_batch, y_mislabled
        goto .restart
        random_index = np.random.randint(0, len(X_train) - batch / 2)
        legit_images = X_train[random_index:random_index + np.int64(batch / 2)].reshape(np.int64(batch / 2), self.width, self.height, self.channels)
        gen_noise = np.random.normal(0, 1, (np.int64(batch / 2), 100))
        syntetic_images = self.G.predict(gen_noise)
        x_combined_batch = np.concatenate((legit_images, syntetic_images))
        label .restart
        y_combined_batch = np.concatenate((np.ones((np.int64(batch / 2), 1)), np.zeros((np.int64(batch / 2), 1))))
        d_loss = self.D.train_on_batch(x_combined_batch, y_combined_batch)
        noise = np.random.normal(0, 1, (batch, 100))
        y_mislabled = np.ones((batch, 1))
        g_loss = self.stacked_generator_discriminator.train_on_batch(noise, y_mislabled)
        print('epoch: %d, [Discriminator :: d_loss: %f], [ Generator :: loss: %f]' % (cnt, d_loss[0], g_loss))
        if cnt % save_interval == 0:
            self.plot_images(save2file=True, step=cnt)
    except Exception as train_exception_2:
        daifu.CT_MANAGER.save(locals())
        raise
    else:
        return None, None
