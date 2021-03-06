import numpy as np
import time
import utils

class knn(object):
    def __init__(self,k=3,weighted=True,classify=True, distance = 'Euclidean'):  
        self.k = k
        self.weighted = weighted
        self.classify = classify
        self.distance = distance
    
    def euclidean_distance(self,X_test):
        # Returns 2D array dist
        # where dist[i,j] is the Euclidean distance from training example i to test example j
        dist = np.sum(self.X_train**2,axis=1).reshape(-1,1) # dist = X_train**2
        dist = dist - 2*np.matmul(self.X_train,X_test.T) # dist = X_train**2  - 2*X_train*X_test
        dist = dist + np.sum(X_test.T**2,axis=0).reshape(1,-1) # dist = X_train**2  - 2*X_train*X_test + X_test**2 - Not really necessary
        dist = np.sqrt(dist) 
        return  dist
    
    def manhattan_distance(self,X_test):
        # Returns 2D array dist
        # where dist[i,j] is the Manhattan distance from training example i to test example j
        dist = np.zeros((self.X_train.shape[0],X_test.shape[0]))
        for i,x in enumerate(X_test):
            dist[:,i] = np.sum(np.abs(self.X_train - x),axis=1)
        return  dist
    
    def fit(self,x,y): 
        # K-nn just stores the training data
        self.X_train = x
        self.y_train = y
        self.num_classes = np.max(self.y_train)+1
    
    def predict(self,X_test):
        if self.distance=='Euclidean':
            dist  = self.euclidean_distance(X_test)     
            dist = dist**2
        else:
            dist  = self.manhattan_distance(X_test)     
        
        nn = np.argsort(dist,axis=0)[:self.k]
        dist = np.sort(dist,axis=0)[:self.k]
        ind = np.arange(len(X_test))
        if self.weighted:
            w = 1/(dist+1e-10)
            sum_w = np.sum(w,axis=0)
            w = w/sum_w
        else:
            w = np.zeros_like(nn,dtype=np.float32)+1/self.k
        if self.classify:
            vote = np.zeros((len(X_test),self.num_classes))
            for i in range(self.k):
                vote[ind,self.y_train[nn[i,:]]] += w[i,:]
            pred = np.argmax(vote,axis=1)
        else:
            pred = np.sum(self.y_train[nn]*w,axis=0)
        return pred
   

if __name__ == "__main__":  
    print('MNIST dataset')
   
    X = np.load('mnist_X.npy').astype(np.float32).reshape(-1,28*28)
    y = np.load('mnist_y.npy')
    
    n = X.shape[0] # Use all examples
    n = 10000      # Use a few examples
    
    ind = np.random.permutation(len(y))
    X=X[ind[:n]]
    y=y[ind[:n]]
    
    X_train, X_test, y_train, y_test = split_train_test(X,y)
    
    
    model = knn(distance = 'Euclidean')
    start = time.time()
    model.fit(X_train, y_train)
    elapsed_time = time.time()-start
    
    print('Elapsed_time training  {0:.6f} '.format(elapsed_time))  
    
    start = time.time()       
    pred = model.predict(X_test)
    elapsed_time = time.time()-start
    print('Elapsed_time testing  {0:.6f} '.format(elapsed_time))   
    print('Accuracy:',np.sum(pred==y_test)/len(y_test))
    
    model = knn(distance = 'Manhattan')
    start = time.time()
    model.fit(X_train, y_train)
    elapsed_time = time.time()-start
    
    print('Elapsed_time training  {0:.6f} '.format(elapsed_time))  
    
    start = time.time()       
    pred = model.predict(X_test)
    elapsed_time = time.time()-start
    print('Elapsed_time testing  {0:.6f} '.format(elapsed_time))   
    print('Accuracy:',np.sum(pred==y_test)/len(y_test))
    
    dist =  model.manhattan_distance(X_test)
