from l9.entity import Entity
from typing import Generic, TypeVar, Self, NoReturn


T = TypeVar('T', bound=Entity)


class BSTNode(Generic[T]):
    def __init__(self, object_: T) -> None:
        self.__object = object_

        self.left: Self | None = None
        self.right: Self | None = None

    @property
    def object(self) -> T:
        return self.__object

    @property
    def key(self) -> str:
        return self.__object.key

    def __repr__(self) -> str:
        return f"<BSTNode[{self.key}, {self.object}]>"


def insert(node: BSTNode[T] | None, object_: T) -> BSTNode[T] | NoReturn:
    if node is None:
        return BSTNode[T](object_)
    elif object_.key < node.key:
        node.left = insert(node.left, object_)
    elif object_.key > node.key:
        node.right = insert(node.right, object_)
    else:
        raise ValueError("Identical keys are not allowed")

    return node


def find(node: BSTNode[T] | None, key: str) -> BSTNode[T] | NoReturn:
    if node is None:
        raise KeyError(f"Key {key} not found.")

    if node.key == key:
        return node
    elif key < node.key:
        return find(node.left, key)
    else:
        return find(node.right, key)


def update(node: BSTNode[T] | None, object_: T) -> None | NoReturn:
    target: BSTNode[T] = find(node, object_.key)
    target.object.update(object_)
    return None


def display(node: BSTNode[T] | None, space: str = "\t", level: int = 0) -> None:
    if node is None:
        print(f"{space * level}∅")
        return None

    if not node.left and not node.right:
        print(f"{space * level}{node.key}")
        return None

    display(node.right, space, level + 1)
    print(f"{space * level}{node.key}")
    display(node.left, space, level + 1)


def tree_size(node: BSTNode[T] | None) -> int:
    if node is None:
        return 0

    # return 1 + tree_size(node.left) + tree_size(node.right)
    return tree_size(node.left) + 1 + tree_size(node.right)


def inorder_traversal(node: BSTNode[T] | None) -> list[T]:
    if node is None:
        return []

    return inorder_traversal(node.left) + [node.object] + inorder_traversal(node.right)


# ============================================================================================== #
# ======================================== LAB 9 =============================================== #
# ============================================================================================== #
def preorder_traversal(node: BSTNode[T] | None) -> list[T]:
    if node is None:
        return []

    return inorder_traversal(node.left) + [node.object] + inorder_traversal(node.right)


def postorder_traversal(node: BSTNode[T] | None) -> list[T]:
    if node is None:
        return []

    return inorder_traversal(node.left) + [node.object] + inorder_traversal(node.right)
# ============================================================================================== #
# ============================================================================================== #
# ============================================================================================== #


if __name__ == '__main__':
    entity_0 = Entity("e0", 10, 100.)
    entity_1 = Entity("e1", 11, 400.)
    entity_2 = Entity("e2", 12, 500.)
    entity_3 = Entity("e3", 13, 200.)

    root: BSTNode[Entity] = BSTNode(entity_2)

    insert(root, entity_0)
    insert(root, entity_1)
    insert(root, entity_3)

    display(root)

    entity = find(root, "e1")

    print(entity)

    entity_2_updated = Entity("e2", 113, 2100.)
    update(root, entity_2_updated)

    print(inorder_traversal(root))
    print(tree_size(root))

