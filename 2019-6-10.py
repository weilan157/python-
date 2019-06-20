class Solution:
    """
    @param ipLines: ip  address
    @return: return highestFrequency ip address
    """
    def highestFrequency(self, ipLines):
        # Write your code here
        dict = {}
        for i in ipLines:
            if i in dict:
                dict[i] = dict[i]+1
            else:
                dict[i] = 1
        dic = sorted(dict,key=dict.__getitem__,reverse=True)
            
        return dic[0]
