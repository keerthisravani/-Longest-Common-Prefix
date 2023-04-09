
class Solution:
    def longestCommonPrefix(self, strs):
        l=sorted(strs)
        s1=l[0]
        s2=l[-1]
        result=""
        m=min(len(l[0]),len(l[-1]))
        i=0
        while i<m :
            if s1[i]!=s2[i]:
                return result
            else:
                result=result+s1[i]
            i+=1
        return result

strs = ["flower","flow","flight"]
obj=Solution()
print(obj.longestCommonPrefix(strs))
