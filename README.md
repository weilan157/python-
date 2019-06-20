# python-

<pre><code class="lang-python">

class Solution:
    """
    @param ipLines: ip  address
    @return: return highestFrequency ip address
    
  	 返回次数最多的
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

</pre>
