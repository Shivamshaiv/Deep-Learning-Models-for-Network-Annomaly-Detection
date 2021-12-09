import tensorflow as tf
import numpy as np



def rmse(predictions, targets):
	return np.sqrt(np.mean((predictions - targets) ** 2))

def diff_convert(time_steps,num_nodes,diff_dict):
	num_samples = len(diff_dict)
	diff = np.zeros((num_samples,time_steps,num_nodes,num_nodes))
	for m in range(num_samples):
		if diff_dict[m] == {}:
			continue # no anomalous pixels
		else:
			coord = diff_dict[m]["coord"]
			value = diff_dict[m]["value"]
			for s in range(len(coord[0])):
				i,j,k = coord[0][s],coord[1][s],coord[2][s]
				diff[m,i,j,k] = value[s]
	return diff
