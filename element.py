class element:
    """
    Create element object containing element name, atomic symbol, group, atomic number, and atomic weight.
    """
    def __init__(self, name=None, symbol=None, group=None, number=None, weight=None):
        self.name = name
        self.symbol = symbol
        self.group = group
        self.number = number
        self.weight = weight

    # Print Element object
    def __str__(self):
        return 'Element: {self.name} \nSymbol: {self.symbol} \nGroup: {self.group} \nNumber: {self.number} \nWeight: {self.weight}'.format(self=self)