from abc import abstractmethod, ABCMeta


class Matcher(metaclass=ABCMeta):

    def __init__(self, pattern):
        self.pattern = pattern

    @abstractmethod
    def match(self, text):
        pass


class BruteForce(Matcher):

    def __init__(self, pattern):
        super(BruteForce, self).__init__(pattern)

    def match(self, text):
        matches = list()

        i = 0
        while i <= len(text) - len(self.pattern):
            j = 0

            while j < len(self.pattern) and text[i + j] == self.pattern[j]:
                j += 1

            if j == len(self.pattern):
                matches.append(i)

            i += 1

        return matches


class Sunday(Matcher):

    def __init__(self, pattern):
        super(Sunday, self).__init__(pattern)
        self.shift = self.__shift(pattern)

    def match(self, text):
        matches = list()

        i = 0
        while i <= len(text) - len(self.pattern):
            j = 0

            while j < len(self.pattern) and text[i + j] == self.pattern[j]:
                j += 1

            if j == len(self.pattern):
                matches.append(i)

            next_index = i + len(self.pattern)

            if next_index < len(text):
                shift = self.__do_shift(text[next_index])
                i += shift
            else:
                break

        return matches

    @staticmethod
    def __shift(pattern):
        shift = dict()

        for i in range(len(pattern)):
            shift[pattern[i]] = len(pattern) - i

        return shift

    def __do_shift(self, c):
        if c in self.shift.keys():
            return self.shift[c]
        else:
            return len(self.pattern) + 1
