class Solution(object):
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        
        total = 0
        def dfs(value,depth):
            nonlocal total
            if value.isInteger():
                total += value.getInteger()*depth
            else:
                for list_val in value.getList():
                    dfs(list_val,depth+1)
        for i in nestedList:
            dfs(i,1)
        return total