class Model:

	def __init__(self, weights=[1,2], threshold=-1, level=0.5):
		self.weights = weights
		self.threshold = threshold
		self.level = level

	def fit(self, data, label):
		i = 0
		train_accurate = 0
		iteration = 1
		while i < len(data):
			net = 0
			for j in range(len(data[i])):
				net += data[i][j] * self.weights[j]
			if net > self.threshold:
				result = 1
			else:
				result = 0
			if result != label[i]:
				if (result - label[i]) > 0:
					for j in range(len(self.weights)):
						self.weights[j] -= self.level * data[i][j]
				else:
					for j in range(len(self.weights)):
						self.weights[j] += self.level * data[i][j]
			else:
				train_accurate += 1

			i += 1

			if (i == len(data)):
				train_accurate /= float(i)
				print("training for %d. iteration" % iteration)
				print(
					"performance of training data for %d. iteration: %f" % 
					(iteration, train_accurate))
				if int(train_accurate) != 1:
					i = 0
					train_accurate = 0
				iteration += 1

	def evaluate(self, data, label):
		accuracy = 0
		for i in range(len(data)):
			net = 0
			for j in range(len(data[i])):
				net += data[i][j] * self.weights[j]
			if net > self.threshold:
				result = 1
			else:
				result = 0

			if result == label[i]:
				accuracy += 1

		accuracy /= float(len(data))
		return accuracy