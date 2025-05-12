# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """

    def getList(self) -> list["NestedInteger"]:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """


class NestedIterator:
    def __init__(self, nestedList: list["NestedInteger"]):
        """
        Time:  O(n)
        Space: O(n)
        """
        self.stack = []

        for i in range(len(nestedList) - 1, -1, -1):
            self.stack.append(nestedList[i])

    def next(self) -> int:
        """
        Time:  O(1)
        Space: O(1)
        """
        return self.stack.pop().getInteger()

    def hasNext(self) -> bool:
        """
        Time:  O(n)
        Space: O(n)
        """
        while self.stack:
            elem = self.stack[-1]
            if elem.isInteger():  # head of stack is ready to be returned as int
                return True

            # flatten nested until head of stack is integer
            self.stack.pop()
            nested = elem.getList()
            for i in range(len(nested) - 1, -1, -1):
                self.stack.append(nested[i])

        return False


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
