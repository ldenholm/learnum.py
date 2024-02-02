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