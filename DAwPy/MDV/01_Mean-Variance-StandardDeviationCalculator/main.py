import numpy as np

def calculate(alista):

    if not len(alista) == 9 :
        raise ValueError('List must contain nine numbers.')

    else:
        np_arr = np.asarray(alista).reshape(3,3)
        np_funcs = [np.mean,np.var,np.std,np.max,np.min,np.sum]

        result_ax0 = [f(np_arr,axis=0).tolist() for f in np_funcs]
        result_ax1 = [f(np_arr,axis=1).tolist() for f in np_funcs]
        result_flat = [f(np_arr) for f in np_funcs]

        final = {
            'mean':[],
            'variance': [],
            'standard deviation': [],
            'max': [],
            'min': [],
            'sum': [],
        }

        for k,ax0,ax1,flat in zip(final.keys(),result_ax0,result_ax1,result_flat):
            final[k] = [ax0,ax1,flat]

        return final


