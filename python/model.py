from tensorflow.keras import layers, models

def residual_block(x, filters):

    shortcut = x

    x = layers.Conv2D(
        filters,
        3,
        padding="same",
        activation="relu"
    )(x)

    x = layers.BatchNormalization()(x)

    x = layers.Conv2D(
        filters,
        3,
        padding="same",
        activation="relu"
    )(x)

    x = layers.BatchNormalization()(x)

    if shortcut.shape[-1] != filters:
        shortcut = layers.Conv2D(
            filters,
            1,
            padding="same"
        )(shortcut)

    return layers.Add()([x, shortcut])


def build_modified_unet(
        input_shape=(256, 256, 3)):

    inputs = layers.Input(input_shape)

    c1 = residual_block(inputs, 64)

    p1 = layers.MaxPooling2D(
        (2, 2)
    )(c1)

    b1 = residual_block(
        p1,
        128
    )

    u1 = layers.UpSampling2D(
        (2, 2)
    )(b1)

    u1 = layers.Concatenate()(
        [u1, c1]
    )

    c2 = residual_block(
        u1,
        64
    )

    outputs = layers.Conv2D(
        1,
        1,
        activation="sigmoid"
    )(c2)

    return models.Model(
        inputs,
        outputs,
        name="Modified_UNet"
    )