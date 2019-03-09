# pytest linked_list.py     is for run tests
# python3.6 linked_list.py -l1 1 2 3 -l2 2 5 7  it runs mergeTwoLists method
# with custom linked lists 1->2->3 and 2->5->7
# Сложность - O(n)


import argparse


class ListNode:

    def __init__(self, value):

        self.value = value
        self.next = None


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:

    if not (l1 and l2):
        l3 = l1 if l1 else l2
    else:
        l3, l3.next = (l2, mergeTwoLists(l1, l2.next)) if l1.value >= l2.value else (l1, mergeTwoLists(l1.next, l2))

    return l3


def unpack_linked_list(node: ListNode) -> tuple:

    current_node = node
    result = list()
    result.append(current_node.value)
    while current_node.next:
        current_node = current_node.next
        result.append(current_node.value)

    return tuple(result)


def create_linked_list(values: tuple) -> ListNode:
    lst = ListNode(values[0])
    if len(values) > 1:
        lst.next = ListNode(values[1])
        current_node = lst.next
        for value in values[2:]:
            current_node.next = ListNode(value)
            current_node = current_node.next

    return lst


def test_create_linked_list() -> None:

    lst = create_linked_list((4, 7))
    assert (lst.value, lst.next.value, lst.next.next) == (4, 7, None)


def test_unpack_linked_list() -> None:

    lst = ListNode(4)
    lst.next = ListNode(7)
    lst.next.next = ListNode(9)
    result = unpack_linked_list(lst)
    assert result == (4, 7, 9)


def test_mergeTwoLists() -> None:

    # l1 = 3->7
    l1 = create_linked_list((3, 7))

    # l2 = 2->3->5
    l2 = create_linked_list((2, 3, 5))

    # l3 = 2->3->3->5->7
    l3 = mergeTwoLists(l1, l2)
    result = unpack_linked_list(l3)
    assert result == (2, 3, 3, 5, 7)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="two linked lists merging")
    parser.add_argument("-l1", default=(1, 2, 4), nargs="+", type=int, help='first list')
    parser.add_argument("-l2", default=(1, 3, 4), nargs="+", type=int, help='second list')
    args = parser.parse_args()

    # l1 = 1->2->4 by default
    l1 = create_linked_list(tuple(args.l1))

    # l2 = 1->3->4 by default
    l2 = create_linked_list(tuple(args.l2))

    l3 = mergeTwoLists(l1, l2)
    result = unpack_linked_list(l3)
    print(result)
