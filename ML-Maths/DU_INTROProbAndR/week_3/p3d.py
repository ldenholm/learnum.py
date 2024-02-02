from math import comb

conf1 = (comb(20, 4) * comb(15, 1) * comb(10, 1)) + comb(20, 1) * comb(15, 4) * comb(10, 1) + comb(20, 1) * comb(15, 1) * comb(10, 4)
print(conf1)

conf2 = comb(20, 2) * comb(15, 2) * comb(10, 2)
print(conf2)

conf3 = (comb(20, 3) * comb(15, 2) * comb(10, 1)) + (comb(20, 2) * comb(15, 3) * comb(10, 1)) + (comb(20, 1) * comb(15, 2) * comb(10, 3)) + (comb(20, 2) * comb(15, 1) * comb(10, 3)) + (comb(20, 1) * comb(15, 3) * comb(10, 2)) + (comb(20, 3) * comb(15, 1) * comb(10, 2))
print(conf3)

conf_sum = conf1 + conf2 + conf3
probability_of_all_represented = conf_sum / (comb(45, 6))

print(probability_of_all_represented)
print('probability of at least 1 not represented = ', 1 - probability_of_all_represented)

print("probability of at least 14 correct ans in MC quiz of 20 q's")

series = (comb(20, 14)*(1/5)**14 * (4/5)**6) + (comb(20, 15)*(1/5)**15 * (4/5)**5) + (comb(20, 16)*(1/5)**16 *(4/5)**4) + (comb(20, 17)*(1/5)**17 * (4/5)**3) + (comb(20, 18)*(1/5)**18 * (4/5)**2) + (comb(20, 19)*(1/5)**19 * (4/5)**1) + (comb(20, 20)*(1/5)**20 * (4/5)**0)
print('2c ans: ', series)

# ~ 1.84500
# this is the correct ans (rounded to 7th decimal) = 0.00000184500

# Now we apply the same formula except using p = 0.9, (1-p) = 0.1
second_series = (comb(20, 14)*(0.9)**14 * (0.1)**6) + (comb(20, 15)*(0.9)**15 * (0.1)**5) + (comb(20, 16)*(0.9)**16 *(0.1)**4) + (comb(20, 17)*(0.9)**17 * (0.1)**3) + (comb(20, 18)*(0.9)**18 * (0.1)**2) + (comb(20, 19)*(0.9)**19 * (0.1)**1) + (comb(20, 20)*(0.9)**20 * (0.1)**0)
print('2d ans: ', second_series)

# ~ 0.9976
# this is the correct ans (rounded to 4th decimal) = 0.9976