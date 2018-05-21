#
# Examples from 
#   https://www.tensorflow.org/deploy/distributed
#   https://github.com/tensorflow/models/blob/master/tutorials/image/cifar10/cifar10_multi_gpu_train.py

# In-graph replication
with tf.device("/job:ps/task:0/cpu:0")
    W = tf.Variable(...)
    b = tf.Variable(...)
inputs = tf.split(0, num_workers, input)
outputs = []
for i in range(num_workers):
    with tf.device("/job:worker/task:%d/gpu:0" % i):
    outputs.append(tf.mtmul(input[i], W) + b)
loss = cross_entropy(outputs)


# Between-graph replication
# Note: Start on every client for different
# worker task id
with tf.device("/job:ps/task:0/cpu:0")
    W = tf.Variable(...)
    b = tf.Variable(...)
with tf.device("/job:worker/task:0/gpu:0"):
    output = tf.mtmul(input[i], W) + b
loss = cross_entropy(output)


# Asynchronous
loss = ...
optimizer = tf.train.GradientDescentOptimizer(
    learning_rate=0.01) 
    
train_op = optimizer.minimize(
    loss, global_step=global_step)


# Synchronous
loss = ...
optimizer = tf.train.GradientDescentOptimizer(
    learning_rate=0.01) 

# At each step the optimizer collects 50 gradients 
# before applying to variables.
optimizer = tf.train.SyncReplicasOptimizer(
    optimizer, replicas_to_aggregate=50)
train_op = optimizer.minimize(
    loss, global_step=global_step)


# Data parallelism 
for i in xrange(FLAGS.num_gpus):
  with tf.device('/gpu:%d' % i):
    with tf.name_scope('%d' % i) as scope:
      image_batch, label_batch = batch_queue.dequeue()
      loss = tower_loss(scope, image_batch, label_batch)
      grads = opt.compute_gradients(loss)
      tower_grads.append(grads)

grads = average_gradients(tower_grads)