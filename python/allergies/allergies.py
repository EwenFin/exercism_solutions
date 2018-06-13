
class Allergies(object):

    SCORES = [
        'eggs',
        'peanuts',
        'shellfish',
        'strawberries',
        'tomatoes',
        'chocolate',
        'pollen',
        'cats',
    ]


    def __init__(self, score):
        while score > 255:
            score = score - 256
        self._score = str(bin(score))[2:][::-1]
        self._lst = self.build_allergies_list()


    def is_allergic_to(self, item):
        return item in self.lst

    def build_allergies_list(self):
        allergy_list = []
        for index, char in enumerate(self.score):
            if char == '1':
                allergy_list.append(self.SCORES[index])
        return allergy_list

    @property
    def lst(self):
        return self._lst

    @lst.setter
    def lst(self, lst):
        self._lst = lst

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        self._score = score

