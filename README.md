# Distributed TensorFlow
Examples that show how to distribute computations using tensorflow

## Notes
### How to plot the graph
To plot the graph using tensorboard simply add the following lines of code:
```python
...
with tf.Session() as session:
    writer = tf.summary.FileWriter('logs', session.graph)
    ...
    writer.close()
```
Then execute ```tensorboard --logdir logs``` in the terminal.