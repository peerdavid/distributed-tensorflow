import numpy as np
import tensorflow as tf

# Build computation graph
x = tf.placeholder(tf.int32, name="x")
y = tf.constant(5, name="y")
z = x * y

# Start computation
with tf.Session() as session:
    input_data = { x: 7 }
    result = session.run(z, input_data)
    print("Result: %d" % result)