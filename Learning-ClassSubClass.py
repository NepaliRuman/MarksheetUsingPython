class Country:
    def __init__(self, Name, Population):
        self.name = Name
        self.population = Population

    def describe(self):
        print(f'My country is {self.name} \nand it has {self.population} population')


class Language(Country):
    def __init__(self, Name, Population, speak):
        super().__init__(Name, Population)
        self.speak = speak

    def describe(self):
        super().describe()
        print(f'The language spoken is {self.speak}')


Name = "Nepal"
Population = "30 Millions"
speak = "Nepali"
language = Language(Name, Population, speak)
language.describe()
