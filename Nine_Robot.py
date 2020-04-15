import numpy as np
import pandas as pd

'''
Logistic Regression:
	f(x) = 1 / 1+e^(-z)
	z = W * X + B
Log Loss:
	-y * ln (y_predict) - (1-y) * ln (1-y_predict)
	
How to learn it? Maybe you should to make train data.
this 3 dimensions data should to into 1 dimensions 
'''
Flame = pd.DataFrame(np.zeros((9, 3), dtype=np.float), index=range(9), columns=['Empty', 'Player', 'Robot'])
Weight = np.zeros((9, 9, 3), dtype=np.float)
Biases = np.zeros((9, 9, 3), dtype=np.float)
Weight2 = np.zeros((9, 9), dtype=np.float)
Biases2 = np.zeros((9, 9), dtype=np.float)
Memory = pd.DataFrame(index=['Empty', 'Player', 'Robot'])
step = 0.005
step2 = 0.05
threshold = 0.01
learn_times = 10

'''
print(Flame.values)
print(Weight)
print('b')
print(Biases)
print(Memory)
'''


def robot_main(data):
	read_data(data)
	target = teacher(data)
	first = hidden_layer1()
	second = hidden_layer2(first)
	print('-- Learning --')
	for k in range(learn_times):
		layer2_update(target, second, first)
		layer1_update(target, second)
		first = hidden_layer1()
		second = hidden_layer2(first)
	print('result:', second)
	print('--- All Finish ---')
	return choice(second)


def teacher(data):
	target = np.array([0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5], dtype=float)
	for i in range(9):
		if data[i] != 0:
			target[i] = 0
		else:
			target[i] = 0.8
	return target


# 3 to 2 y=wx+b Linear
def hidden_layer1():
	pred_y = np.zeros((9, 9), dtype=float)
	for i in range(9):
		for j in range(9):
			pred_y[i][j] = np.sum(Weight[i][j] * Flame.values[j] + Biases[i][j])
	return pred_y


# 2 to 1 t=wx+b y=1/1+e^(-t) Logistic
def hidden_layer2(x):
	pred_y = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0], dtype=float)
	for i in range(9):
		pred_y[i] = 1 / (1 + np.e ** (-np.sum(Weight2[i] * x[i] + Biases2[i])))
	return pred_y


# target 9x1  predict 9x1  t=hidden_layer1() 9x9  hidden_layer2(t) 9x1
def layer1_update(target, predict):
	hidden_layer2(hidden_layer1())
	for i in range(9):
		loss = abs(target[i]-predict[i])
		if loss <= threshold:
			continue
		for j in range(9):
			for k in range(3):
				log = loss_log(target, hidden_layer2(hidden_layer1()))
				Weight[i][j][k] += step2
				w_g = loss_log(target, hidden_layer2(hidden_layer1()))
				Weight[i][j][k] -= step2
				Biases[i][j][k] += step2
				b_g = loss_log(target, hidden_layer2(hidden_layer1()))
				Biases[i][j][k] -= step2
				# judge
				if w_g <= log:
					# print('+', end='')
					Weight2[i][j] += step2
				else:
					# print('-', end='')
					Weight2[i][j] -= step2
				if b_g <= log:
					# print('+,', end='')
					Biases2[i][j] += step2
				else:
					# print('-,', end='')
					Biases2[i][j] -= step2


# target 9x1  predict 9x1  t(x)=hidden_layer1() 9x9  hidden_layer2(t) 9x1
def layer2_update(target, predict, x):
	for i in range(9):
		loss = abs(target[i]-predict[i])
		if loss <= threshold:
			continue
		for j in range(9):
			# count
			log = loss_log(target, hidden_layer2(x))
			Weight2[i][j] += step
			w_g = loss_log(target, hidden_layer2(x))
			Weight2[i][j] -= step
			Biases2[i][j] += step
			b_g = loss_log(target, hidden_layer2(x))
			Biases2[i][j] -= step
			# judge
			if w_g <= log:
				Weight2[i][j] += step
			else:
				Weight2[i][j] -= step
			if b_g <= log:
				Biases2[i][j] += step
			else:
				Biases2[i][j] -= step


# get log loss
def loss_log(target, predict):
	return np.sum(-target*np.log(predict)-(1-target)*np.log(1-predict))


def train_data():
	a = int(input('Please help robot to choice 0~8'))
	y = [0, 0, 0, 0, 0, 0, 0, 0, 0]
	y[a] = 1
	return y


# get max choice
def choice(predict):
	m = np.max(predict)
	for i in range(9):
		if predict[i] == m:
			return i
	return 0


# let data(Board) into Flame
def read_data(data):
	for i in range(9):
		if data[i] == 0:
			Flame.loc[i, 'Empty'] = 1
			Flame.loc[i, 'Player'] = 0
			Flame.loc[i, 'Robot'] = 0
		elif data[i] == 1:
			Flame.loc[i, 'Empty'] = 0
			Flame.loc[i, 'Player'] = 1
			Flame.loc[i, 'Robot'] = 0
		elif data[i] == 2:
			Flame.loc[i, 'Empty'] = 0
			Flame.loc[i, 'Player'] = 0
			Flame.loc[i, 'Robot'] = 1
	return
