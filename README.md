# Distributed TensorFlow
Examples that show how to distribute computations using tensorflow

# single_device.py
Simple example that shows how TensorFlow executes computation graphs.

# multiple_devices.py
Example to show how constraints can be used to use the CPU or GPU to execute
computations of the graph.

## Notes
### How to plot the graph
To plot the graph using tensorboard simply add the following lines of code:
```python
...
with tf.Session() as sess:
    writer = tf.summary.FileWriter('logs', sess.graph)
    ...
    writer.close()
```
Then execute ```tensorboard --logdir logs``` in the terminal.