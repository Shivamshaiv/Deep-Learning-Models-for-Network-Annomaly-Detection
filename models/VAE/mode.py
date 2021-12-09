import tensorflow as tf
tf.random.set_seed(42)
import tensorflow.keras.backend as K
import tensorflow.keras.layers as layers
from tensorflow.keras.callbacks import Callback, ReduceLROnPlateau, ModelCheckpoint, EarlyStopping

def VAE(object):
    def __init__(self,df):
        self.df = df

    def generate_model(self,num_columns, num_labels, hidden_units, dropout_rates, ls = 1e-2, lr = 1e-3):

        inp = tf.keras.layers.Input(shape = (num_columns, ))
        x0 = tf.keras.layers.BatchNormalization()(inp)

        #Encoder
        encoder = tf.keras.layers.GaussianNoise(dropout_rates[0])(x0)
        encoder = tf.keras.layers.Dense(hidden_units[0])(encoder)
        encoder = tf.keras.layers.BatchNormalization()(encoder)
        encoder = tf.keras.layers.Activation('swish')(encoder)

        #Decoder
        decoder = tf.keras.layers.Dropout(dropout_rates[1])(encoder)
        decoder = tf.keras.layers.Dense(num_columns, name = 'decoder')(decoder)


        x_ae = tf.keras.layers.Dense(hidden_units[1])(decoder)
        x_ae = tf.keras.layers.BatchNormalization()(x_ae)
        x_ae = tf.keras.layers.Activation('swish')(x_ae)
        x_ae = tf.keras.layers.Dropout(dropout_rates[2])(x_ae)

        out_ae = tf.keras.layers.Dense(num_labels, activation = 'sigmoid', name = 'ae_action')(x_ae)

        #Multi Layer perceptron
        x = tf.keras.layers.Concatenate()([x0, encoder])
        x = tf.keras.layers.BatchNormalization()(x)
        x = tf.keras.layers.Dropout(dropout_rates[3])(x)

        for i in range(2, len(hidden_units)):
            x = tf.keras.layers.Dense(hidden_units[i])(x)
            x = tf.keras.layers.BatchNormalization()(x)
            x = tf.keras.layers.Activation('swish')(x)
            x = tf.keras.layers.Dropout(dropout_rates[i + 2])(x)

        out = tf.keras.layers.Dense(num_labels, activation = 'sigmoid', name = 'action')(x)

        model = tf.keras.models.Model(inputs = inp, outputs = [out_ae, out])
        model.compile(optimizer = tf.keras.optimizers.Adam(learning_rate = lr),
                      loss = {
                              'ae_action': tf.keras.losses.BinaryCrossentropy(label_smoothing = ls),
                              'action': tf.keras.losses.BinaryCrossentropy(label_smoothing = ls),
                             },
                      metrics = {
                                 'ae_action': tf.keras.metrics.AUC(name = 'AUC'),
                                 'action': tf.keras.metrics.AUC(name = 'AUC'),
                                },
                     )

        return model
