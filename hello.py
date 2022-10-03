#save this file as hello.py in your repo
import tensorflow as tf

# Simple hello world using TensorFlow
hello = 'Hello, TensorFlow!'

# Start tf session
#sess = tf.Session()

# Run the op
#print(sess.run(hello))
fpOut = open(r'/outputs/data/test.txt',"w")
print(hello,file=fpOut)
fpOut.close() 
