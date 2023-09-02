from Food import *

@staticmethod
def greedy(items: list[Food], maxcost, keyFunction):
    """Assumed  items a list, maxCost constraint => 0,
    keyFunction informs which keys to use for the arguments (weight, value, density)
    This function takes O(n) to iterate through items, and O(n log n) for the sorted(),
    a total computation complexity of O(n log n)"""
    itemsCopy = sorted(items, key=keyFunction, reverse=True)
    # reverse = True for descending order, and keyFunc is the key index to sort by.
    result = []
    totalValue = totalCost = 0.0
    for i in range(len(itemsCopy)):
        if (totalCost + itemsCopy[i].getCost() <= maxcost):
            result.append(itemsCopy[i])
            totalCost += itemsCopy[i].getCost()
            totalValue += itemsCopy[i].getValue()
    return (result, totalValue)

@staticmethod
def testGreedy(items, constraint, keyFunction):
    taken, val = greedy(items, constraint, keyFunction)
    print('Total valye of items taken =', val)
    for item in taken:
        print('     ', item)

@staticmethod
def testGreedys(foods, maxUnits):
    print('Use greedy by value to allocate', maxUnits, 'calories')
    testGreedy(foods, maxUnits, Food.getValue)
    print('\nUse greedy by cost to allocate', maxUnits, 'calories')
    # Use 1/cost to order by foods with fewest calories first since.
    testGreedy(foods, maxUnits, lambda x: 1/Food.getCost(x))
    print('\nUse greedy by density to allocate', maxUnits, 'calories')
    testGreedy(foods, maxUnits, Food.density)