class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        elems = [elem for elem in path.split("/") if elem not in {"", "."}]
        for elem in elems:  # clear from "///" and
            if elem == "..":
                if stack:  # pop last dir if not root
                    stack.pop()
            else:  # valid folder or file
                stack.append(elem)
        return "/" + "/".join(stack)
