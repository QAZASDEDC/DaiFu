def _generate_filter_image(input_img,
                            layer_output,
                            filter_index):
    """Generates image for one particular filter.

    # Arguments
        input_img: The input-image Tensor.
        layer_output: The output-image Tensor.
        filter_index: The to be processed filter number.
                        Assumed to be valid.

    #Returns
        Either None if no image could be generated.
        or a tuple of the image (array) itself and the last loss.
    """
    s_time = time.time()

    # we build a loss function that maximizes the activation
    # of the nth filter of the layer considered
    if K.image_data_format() == 'channels_first':
        loss = K.mean(layer_output[:, filter_index, :, :])
    else:
        loss = K.mean(layer_output[:, :, :, filter_index])

    # we compute the gradient of the input picture wrt this loss
    grads = K.gradients(loss, input_img)[0]

    # normalization trick: we normalize the gradient
    grads = normalize(grads)

    # this function returns the loss and grads given the input picture
    iterate = K.function([input_img], [loss, grads])

    # we start from a gray image with some random noise
    intermediate_dim = tuple(
        int(x / (upscaling_factor ** upscaling_steps)) for x in output_dim)
    if K.image_data_format() == 'channels_first':
        input_img_data = np.random.random(
            (1, 3, intermediate_dim[0], intermediate_dim[1]))
    else:
        input_img_data = np.random.random(
            (1, intermediate_dim[0], intermediate_dim[1], 3))
    input_img_data = (input_img_data - 0.5) * 20 + 128

    # Slowly upscaling towards the original size prevents
    # a dominating high-frequency of the to visualized structure
    # as it would occur if we directly compute the 412d-image.
    # Behaves as a better starting point for each following dimension
    # and therefore avoids poor local minima
    for up in reversed(range(upscaling_steps)):
        # we run gradient ascent for e.g. 20 steps
        for _ in range(epochs):
            loss_value, grads_value = iterate([input_img_data])
            input_img_data += grads_value * step

            # some filters get stuck to 0, we can skip them
            if loss_value <= K.epsilon():
                return None

        # Calculate upscaled dimension
        intermediate_dim = tuple(
            int(x / (upscaling_factor ** up)) for x in output_dim)
        # Upscale
        img = deprocess_image(input_img_data[0])
        img = np.array(pil_image.fromarray(img).resize(intermediate_dim,
                                                        pil_image.BICUBIC))
        input_img_data = np.expand_dims(
            process_image(img, input_img_data[0]), 0)

    # decode the resulting input image
    img = deprocess_image(input_img_data[0])
    e_time = time.time()
    print('Costs of filter {:3}: {:5.0f} ( {:4.2f}s )'.format(filter_index,
                                                                loss_value,
                                                                e_time - s_time))
    return img, loss_value