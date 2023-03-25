import sys
import numpy as np
import Random as rng
import matplotlib.pyplot as plt


seed = 5052
random = rng.Random(seed)


n_true_values = 100
n_tests = 100
n_cups= 100
n_trials = n_true_values * n_tests

x_arr = [0]*n_trials
y_arr = [0]*n_trials
i_trial = 0

for i in range (1, n_true_values):
    true_alpha = i*0.01
    for j in range (1, n_tests):
        n_cups_correct = 0 
        for cup in range (0,n_cups):
            y = random.rand()
            if y< true_alpha:
                n_cups_correct += 1
            
        measured_alpha = n_cups_correct/n_cups
        i_trial += 1 
        x_arr[i_trial] = true_alpha
        y_arr[i_trial] = measured_alpha


true_values = [0]*n_true_values

for j in range (1, n_trials):
    if y_arr[j] == 0.7:
        ibin_x = int(x_arr[j]*n_true_values)
        true_values[ibin_x] += 1

###summing true_values so we can normalize it

total_true_values = sum(true_values)
total_true_values_inv =  (1/total_true_values)

    


probability = [0] * len(true_values)
for i in range(len(true_values)):
    probability[i] = true_values[i] * total_true_values_inv
print(probability)

true_value_x = np.arange(0, 100, 1)
plt.bar(true_value_x, probability)
plt.xlabel('alpha as percentage correct guesses')
plt.ylabel('normalized probability')
plt.show()
