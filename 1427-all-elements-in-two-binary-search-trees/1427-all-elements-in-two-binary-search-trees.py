class Solution(object):
    def getAllElements(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: List[int]
        """
        def inorder(root, arr):
            if not root:
                return
            inorder(root.left, arr)
            arr.append(root.val)
            inorder(root.right, arr)

        list1 = []
        list2 = []
        inorder(root1, list1)
        inorder(root2, list2)

        # Merge the two sorted lists
        res = []
        i = j = 0
        while i < len(list1) and j < len(list2):
            if list1[i] < list2[j]:
                res.append(list1[i])
                i += 1
            else:
                res.append(list2[j])
                j += 1

        while i < len(list1):
            res.append(list1[i])
            i += 1
        while j < len(list2):
            res.append(list2[j])
            j += 1

        return res
