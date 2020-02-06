# -*- coding: UTF-8 -*-



# your code
# you may need import some package
import random



x = ['快递太慢了！','不好吃','特别难吃','要齁死我了','很划算','下次还来','味道很不错！','香']
y = ['差评','差评','差评','差评','好评','好评','好评','好评']



def shuffle(x,y):
    # your code here
    seed = 0

    seed = random.random()

    random.seed(seed)
    random.shuffle(x)

    random.seed(seed)
    random.shuffle(y)

    return x,y



x, y = shuffle(x, y)

# print result for certify
for i,j in zip(x,y):
    print(i,':',j)
