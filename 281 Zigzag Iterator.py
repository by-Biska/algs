class ZigzagIterator:
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
        self.i, self.j = 0, 0  # Индексы для каждого списка
        self.turn = 0  # Для чередования между списками

    def next(self):
        if self.turn % 2 == 0:
            if self.i < len(self.v1):
                result = self.v1[self.i]
                self.i += 1
            else:
                result = self.v2[self.j]
                self.j += 1
        else:
            if self.j < len(self.v2):
                result = self.v2[self.j]
                self.j += 1
            else:
                result = self.v1[self.i]
                self.i += 1
        self.turn += 1
        return result

    def hasNext(self):
        return self.i < len(self.v1) or self.j < len(self.v2)