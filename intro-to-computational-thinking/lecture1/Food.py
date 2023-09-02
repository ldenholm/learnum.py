class Food(object):
    def __init__(self, n, v, w) -> None:
        self.name = n
        self.value = v
        self.calories = w

    def getValue(self):
        return self.value
    
    def getCost(self):
        return self.calories
    
    def density(self):
        return self.getValue()/self.getCost()
    
    def __str__(self) -> str:
        return self.name + ': ' + str(self.value)\
                + ', ' + str(self.calories) + '>'
    
    @staticmethod
    def buildMenu(names: list[str], values: list[int], calories: list[int]) -> list:
        """names, values, calories lists of same length.
        name a list of strings
        values and calories lists of numbers"""
        menu = []
        for i in range(len(values)):
            menu.append(Food(names[i], values[i], calories[i]))
        return menu