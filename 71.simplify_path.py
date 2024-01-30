class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        paths = path.split("/")
        simple_path = []
        for i in paths:
            if i != "":
                if i == ".":
                    continue
                elif i == "..":
                    if len(simple_path) > 0:
                        simple_path.pop()
                else:
                    simple_path.append(i)
        return "/" + "/".join(simple_path)


# we split the path with / and igonre empty and .
# we keep apending to stack
# if .. appear we want to go to parent so we pop an element from list
# at the end join the stack with / and add / at start
