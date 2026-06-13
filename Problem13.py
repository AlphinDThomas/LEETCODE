class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        list1=[]
        sum =0
        i=0
        while i<len(s):
            if i == len(s)-1:
                substring =s[i]
            else:
                substring =s[i] +s[i+1]
            if substring in ["IV","IX","XL","XC","CD","CM"]:
                list1.append(substring)
                i = i +2
            else:
                list1.append(substring[0])
                i= i +1
            
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }
        for item in list1:
            sum+= values[item]
        return sum