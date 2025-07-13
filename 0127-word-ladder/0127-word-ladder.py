class Pair:
    def __init__(self, word, dis):
        self.word = word
        self.dis = dis

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        dictionary = set(wordList)

        q = deque()
        q.append(Pair(beginWord, 1))
        if beginWord in dictionary:
            dictionary.remove(beginWord)

        while q:
            size = len(q)

            for _ in range(size):
                curr = q.popleft()

                if curr.word == endWord:
                    return curr.dis

                for i in range(0, len(curr.word)):
                    for c in string.ascii_lowercase:
                        new_word = curr.word[:i] + c + curr.word[i+1:]
                        if new_word in dictionary:
                            q.append(Pair(new_word, curr.dis + 1))
                            dictionary.remove(new_word)

        return 0





        

        