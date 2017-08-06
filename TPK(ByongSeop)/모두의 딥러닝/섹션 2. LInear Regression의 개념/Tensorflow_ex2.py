import tensorflow as tf

#Linear Regression 구현

#H(x) = Wx + b

x_train = [1,2,3]
y_train = [1,2,3]

w = tf.Variable(tf.random_normal([1]), name = 'weight') # tensorflow 가 사용 하는 변수로 tensorflow가 변경 시키는 변수
b = tf.Variable(tf.random_normal([1]), name = 'bias')

hypothesis  = x_train * w + b

#cost(W,b)

cost = tf.reduce_mean(tf.square(hypothesis - y_train)) # square = 제곱
                                                       # reduce_maen = 평균 내주는 함수

#Minimize

optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
train = optimizer.minimize(cost)

#Session

sess = tf.Session()

#Initializes

sess.run(tf.global_variables_initializer())

#Fit the Line

for step in range(2001):
    sess.run(train)
    if step%20 == 0:
        print(step, sess.run(cost), sess.run(w), sess.run(b))

#Linear Regression 구현 Placeholder 사용

X = tf.placeholder(tf.float32, shape=[None])
Y = tf.placeholder(tf.float32, shape=[None])

W = tf.Variable(tf.random_normal([1]), name = 'weight')
b = tf.Variable(tf.random_normal([1]), name = 'bias')

hypothesis  = X * W + b

cost = tf.reduce_mean(tf.square(hypothesis - Y))

optimizer  = tf.train.GradientDescentOptimizer(learning_rate=0.01)
train = optimizer.minimize(cost)

sess = tf.Session()

sess.run(tf.global_variables_initializer())

for step in range(2001):
    cost_val, W_val, b_val, _ = sess.run([cost, W, b, train],
                                         feed_dict={X:[1,2,3,4,5], Y:[2.1, 3.1, 4.1, 5.1, 6.1]})
    if step%20 == 0:
        print(step, cost_val, W_val, b_val)

print(sess.run(hypothesis, feed_dict={X:[5]}))
print(sess.run(hypothesis, feed_dict={X:[2.5]}))
print(sess.run(hypothesis, feed_dict={X: [1.5, 3.5]}))