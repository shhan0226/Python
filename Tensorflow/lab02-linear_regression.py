# Lab 2 Linear Regression
# import tensorflow as tf
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

tf.set_random_seed(777)  # for reproducibility

# X and Y data
x_train = [1, 2, 3]
y_train = [1, 2, 3]

# Try to find values for W and b to compute y_data = x_data * W + b
# We know that W should be 1 and b should be 0
# But let TensorFlow figure it out
W = tf.Variable(tf.random_normal([1]), name="weight")
b = tf.Variable(tf.random_normal([1]), name="bias")
# Variable은 텐서플로우가 알아서 변경하는 값을 말한다.

# Our hypothesis XW+b
hypothesis = x_train * W + b

# cost/loss function
cost = tf.reduce_mean(tf.square(hypothesis - y_train))

# reduce_mean은 평균을 내주는 함수
# t = [1., 2., 3., 4.]
# tf.reduce_mean(t) ==> 2.5



#GradientDescent / Minimize
# optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
# train = optimizer.minize(cost)
train = tf.train.GradientDescentOptimizer(learning_rate=0.01).minimize(cost)

# Launch the graph in a session.
with tf.Session() as sess:
    # Initializes global variables in the graph.
    sess.run(tf.global_variables_initializer())
    # W, b를 초기화하기 위해

    # Fit the line
    for step in range(2001):
        #_, cost_val, W_val, b_val = sess.run([train, cost, W, b])
        sess.run(train)

        if step % 20 == 0:
            #print(step, cost_val, W_val, b_val)
            print(step, sess.run(cost), sess.run(W), sess.run(b))

# Learns best fit W:[ 1.],  b:[ 0.]
