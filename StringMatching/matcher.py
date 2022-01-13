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


class Horspool(Matcher):

    def __init__(self, pattern):
        super(Horspool, self).__init__(pattern)
        self.last_chars = self.__last_chars(pattern)

    def match(self, text):
        matches = list()

        i = 0
        while i <= len(text) - len(self.pattern):
            j = len(self.pattern) - 1

            while j >= 0 and text[i + j] == self.pattern[j]:
                j -= 1

            if j == -1:
                matches.append(i)
                i += 1
            else:
                i += self.__shift(text[i + j], j)

        return matches

    @staticmethod
    def __last_chars(pattern):
        last_chars = dict()

        for i in range(1, len(pattern)):
            chars = dict()

            for j in range(i):
                chars[pattern[j]] = j

            last_chars[i] = chars

        return last_chars

    def __shift(self, c, j):
        if j not in self.last_chars.keys():
            return j + 1

        if c not in self.last_chars.get(j).keys():
            return j + 1

        return j - self.last_chars.get(j).get(c)
