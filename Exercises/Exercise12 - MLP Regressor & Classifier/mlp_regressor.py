import numpy as np
from utils import *
import math 
import time
from sklearn.neural_network import MLPRegressor

if __name__ == "__main__":
    plt.close('all')
    
    data_path = 'C:\\Users\\npizz\\Desktop\\Machine-Learning\\Exercises\\Exercise12\\'  # Use your own path here
    
    X = np.load(data_path+'particles_X.npy').astype(np.float32)
    y = np.load(data_path+'particles_y.npy').astype(np.float32)
  
    X_train, X_test, y_train, y_test = split_train_test(X,y,seed=20)
    '''
    MLPRegressor(hidden_layer_sizes=(100, ), activation='relu', *, solver='adam', 
                 alpha=0.0001, batch_size='auto', learning_rate='constant', learning_rate_init=0.001, 
                 power_t=0.5, max_iter=200, shuffle=True, random_state=None, tol=0.0001, verbose=False, 
                 warm_start=False, momentum=0.9, nesterovs_momentum=True, early_stopping=False, 
                 validation_fraction=0.1, beta_1=0.9, beta_2=0.999, epsilon=1e-08, n_iter_no_change=10, 
                 max_fun=15000)
    '''
    model = MLPRegressor(solver='adam', alpha=1e-5, batch_size = 100 ,learning_rate='adaptive',momentum=0.95,  hidden_layer_sizes=(300), verbose=True, random_state=1)
    
    start = time.time()
    model.fit(X_train, y_train)
    elapsed_time = time.time()-start
    print('Elapsed_time training  {0:.6f} '.format(elapsed_time))  
    print('Training iterations  {} '.format(model.n_iter_))  
    
    start = time.time()       
    pred = model.predict(X_test)
    elapsed_time = time.time()-start
    print('Elapsed_time testing  {0:.6f} '.format(elapsed_time))   
    print('Mean-squared error: {0:.6f}'.format(mse(y_test,pred)))
          
'''
Iteration 1, loss = 0.03309577
Iteration 2, loss = 0.01980742
Iteration 3, loss = 0.01960576
Iteration 4, loss = 0.01958716
Iteration 5, loss = 0.01957387
Iteration 6, loss = 0.01956098
Iteration 7, loss = 0.01955044
Iteration 8, loss = 0.01953929
Iteration 9, loss = 0.01953229
Iteration 10, loss = 0.01952428
Iteration 11, loss = 0.01951844
Iteration 12, loss = 0.01951340
Iteration 13, loss = 0.01951421
Iteration 14, loss = 0.01951209
Training loss did not improve more than tol=0.000100 for 10 consecutive epochs. Stopping.
Elapsed_time training  44.123978 
Training iterations  14 
Elapsed_time testing  0.025989 
Mean-squared error: 0.039072
   '''