class Solution:
    def printAllDups(self, root):
            # dictionary to store the subtree patterns and their counts
            subtree_patterns = {}
            # list to store the duplicate subtrees
            duplicate_subtrees = []

            def traverse(node):
                if node is None:
                    return "#"

                # serialize the subtree
                subtree = str(node.val) + "," + traverse(node.left) + "," + traverse(node.right)

                # count the occurrence of the subtree pattern
                subtree_patterns[subtree] = subtree_patterns.get(subtree, 0) + 1

                # if the subtree pattern occurs more than once, add it to the duplicate subtrees list
                if subtree_patterns[subtree] == 2:
                    duplicate_subtrees.append(node)

                return subtree

            traverse(root)

            return duplicate_subtrees