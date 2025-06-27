class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        integerToRoman = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M'
        }

        roman = []
        for key in sorted(integerToRoman.keys(), reverse=True):
            if num == 0:
                break

            count = num//key
            num = num%key

            roman.append(integerToRoman[key] * count)
            

        return ''.join(roman)