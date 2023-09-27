class Solution(object):
    # main function
    def RomanToInt(self,s: str) -> int:
        
        #  dictionary of all the roman no. and their cossesponding values
        info: dict = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        int_value = 0    # main output will be stored here
        previous_value = None
        for i in range(len(s)-1):
            if s[i] in info:
                if (s[i] == previous_value):
                    previous_value = None
                    if i == len(s)-2:
                        int_value += info[s[i+1]]
                
                elif(info[s[i]] < info[s[i+1]]) :
                    int_value += (info[s[i+1]] - info[s[i]])
                    previous_value = s[i+1]
                    
                else:
                        if i == len(s)-2:
                             int_value += info[s[i]]
                             int_value += info[s[i+1]]
                            
                        else:
                            int_value += info[s[i]]
        if len(s) == 1 and s[0] in info:
             int_value += info[s[0]]
        return int_value
