class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split(' ')
        wordArr = []
        for i in arr:
            if i != '':
                wordArr.append(i)
        wordArr.reverse()

        return ' '.join(wordArr)