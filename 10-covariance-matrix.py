def mean_variance(vector: list[float]):
	mean = 0
	for i in vector:
		mean += i
	mean /= len(vector)
	
	variance = 0
	for i in vector:
		variance += (i - mean)**2
	variance /= (len(vector) - 1)

	return mean, variance

def covariance(vector_1, vector_2, mean_1, mean_2):
	covariance = 0
	for i in range(len(vector_1)):
		covariance += ((vector_1[i] - mean_1) * (vector_2[i] - mean_2))
	covariance /= (len(vector_1) - 1)
	return covariance

def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
	n_rows = len(vectors)
	n_cols = len(vectors[0])
	mean_list, variance_list = [], []
	for vector in vectors:
		mean, variance = mean_variance(vector)
		mean_list.append(mean)
		variance_list.append(variance)
	
	covariance_list = [[0 for i in range(n_rows)] for j in range(n_rows)]
	for i in range(n_rows):
		for j in range(n_rows):
			if i != j:
				covariance_ = covariance(vectors[i], vectors[j], mean_list[i], mean_list[j])
				covariance_list[i][j] = covariance_
			if i == j:
				covariance_list[i][j] = variance_list[i]
	
	return covariance_list
