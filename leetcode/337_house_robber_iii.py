# 337. House Robber III
#
# The thief has found himself a new place for his thievery again. There
# is only one entrance to this area, called the "root." Besides the
# root, each house has one and only one parent house. After a tour, the
# smart thief realized that "all houses in this place forms a binary
# tree". It will automatically contact the police if two directly-linked
# houses were broken into on the same night.
#
# Determine the maximum amount of money the thief can rob tonight
# without alerting the police.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rob(root: TreeNode, parent_robbed=False, memo=None) -> int:
    if memo is None:
        memo = {}
    if not root:
        return 0

    if (root, parent_robbed) not in memo:
        # case that current node is not robbed
        memo[root, parent_robbed] \
            = (rob(root.left, parent_robbed=False, memo=memo)
               + rob(root.right, parent_robbed=False, memo=memo))
        if not parent_robbed:
            # consider also the case that current node is robbed
            memo[root, parent_robbed] \
                = max(memo[root, parent_robbed],
                      (root.val + rob(root.left, parent_robbed=True, memo=memo)
                       + rob(root.right, parent_robbed=True, memo=memo)))

    return memo[root, parent_robbed]


if __name__ == '__main__':
    print(rob(TreeNode(val=3,
                       left=TreeNode(val=2,
                                     right=TreeNode(val=3)),
                       right=TreeNode(val=3,
                                      right=TreeNode(val=1)))))  # 7
    print(rob(TreeNode(val=3,
                       left=TreeNode(val=4,
                                     left=TreeNode(val=1),
                                     right=TreeNode(val=3)),
                       right=TreeNode(val=5,
                                      right=TreeNode(val=1)))))  # 9
    print(rob(TreeNode(val=2,
                       left=TreeNode(val=1,
                                     right=TreeNode(val=4)),
                       right=TreeNode(val=3))))  # 7
