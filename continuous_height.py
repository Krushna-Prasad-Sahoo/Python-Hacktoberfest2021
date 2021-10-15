import doctest


class Node(object):
    def __init__(self, element: int) -> None:
        self.data = element
        self.left = None
        self.right = None


class BST:
    def __init__(self) -> None:
        self.root = None

    def create(self, insert_element: int) -> None:
        if self.root == None:
            self.root = Node(insert_element)
        else:
            current = self.root
            while True:
                if current.data > insert_element:
                    if current.left != None:
                        current = current.left
                    else:
                        current.left = Node(insert_element)
                        break
                elif current.data < insert_element:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(insert_element)
                        break
                else:
                    break


def height_of_tree(root: Node) -> int:
    if not root:
        return -1
    return 1 + max(height_of_tree(root.right), height_of_tree(root.left))


def bst_height() -> None:
    t = int(input())
    for i in range(t):
        n = int(input())
        ar = list(map(int, input().split()))
        tree = BST()
        for i in range(n):
            tree.create(ar[i])
            print(height_of_tree(tree.root), end=" ")
        print()


if __name__ == "__main__":
    doctest.testmod()
    bst_height()
