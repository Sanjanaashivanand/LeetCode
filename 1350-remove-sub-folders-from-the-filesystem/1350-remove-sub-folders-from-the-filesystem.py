class Solution(object):
    def removeSubfolders(self, folders):
        """
        :type folders: List[str]
        :rtype: List[str]
        """
        folders.sort()  # Lexicographical sort: parents come before children
        result = []

        for folder in folders:
            if not result or not folder.startswith(result[-1] + '/'):
                result.append(folder)

        return result
