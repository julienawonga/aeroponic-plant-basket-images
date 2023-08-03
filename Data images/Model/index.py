import os
import numpy as np

from tflite_model_maker.config import ExportFormat, QuantizationConfig
from tflite_model_maker import model_spec
from tflite_model_maker import object_detector

from tflite_support import metadata

import tensorflow as tf
assert tf.__version__.startswith('2')

tf.get_logger().setLevel('ERROR')
from absl import logging
logging.set_verbosity(logging.ERROR)

# Load data
train_data = object_detector.DataLoader.from_pascal_voc(
    './train',
    './train',
    ['basket']
)

val_data = object_detector.DataLoader.from_pascal_voc(
    './test',
    './test',
    ['basket']
)

# Train the model

spec = model_spec.get('efficientdet_lite0')

model = object_detector.create(train_data, model_spec=spec, batch_size=8, train_whole_model=True, validation_data=val_data)


# Evaluate the model
model.evaluate(val_data)

# Export the model
model.export(export_dir='.')

