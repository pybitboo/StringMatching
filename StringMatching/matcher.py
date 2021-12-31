from abc import ABCMeta, abstractmethod


class Matcher(object):
    __meta_class__ = ABCMeta

    def __init__(self, p):
        self.p = p

    @abstractmethod
    def match(self, s):
        pass


class BruteForce(Matcher):

    def __init__(self, p):
        super(BruteForce, self).__init__(p)

    def match(self, s):
        matches = list()

        i = 0
        while i <= len(s) - len(self.p):
            j = 0
            while s[i + j] == self.p[j]:
                j += 1

                if j == len(self.p):
                    matches.append(i)
                    break
            i += 1

        return matches
