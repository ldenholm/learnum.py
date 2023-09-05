def maxVal(itemsToConsider, weightAvailable):
    """Accepts a list of items, and a weight available.
    Returns a tuple of total value of a solution, 
    and the list of items within that solution."""

    if itemsToConsider == 0 or weightAvailable == 0:
        # return empty tuple
        result = (0, ())
    elif itemsToConsider[0].getUnits() > weightAvailable:
        result = maxVal(itemsToConsider[1:], weightAvailable)
    else:
        nextItem = itemsToConsider[0]
        withVal, withToTake = maxVal(itemsToConsider[1:],
        weightAvailable - nextItem.getUnits())
        withVal += nextItem.getValue()
        withoutVal, withoutToTake = maxVal(itemsToConsider[1:], weightAvailable)
    if withVal > withoutVal:
        result = (withVal, withToTake + (nextItem,))
    else:
        result = (withoutVal, withoutToTake)
    return result

# Note this does not generate a tree, it merely keeps track
# of the best generated node. If a new node is better than the
# previous then that node becomes the best.