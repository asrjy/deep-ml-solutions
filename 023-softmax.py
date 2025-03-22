import math

def softmax(scores: list[float]) -> list[float]:
	denom = sum([math.exp(i) for i in scores])
	probabilities = [round(math.exp(i)/denom, 4) for i in scores]
	return probabilities