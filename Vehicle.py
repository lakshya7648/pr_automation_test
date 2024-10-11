class Vehicle:
    def __init__(self,category, name, color):
        self.category = category
        self.name = name
        self.color = color

    def setName(self):
        self.name = name

    def getName(self):
        return self.name

    def setColor(self):
        self.color = color

    def getColor(self):
        return self.color

    def details(self):
        return f'Vehicle of category {self.category} is of identity : Name = {self.name} & color = {self.color}'
