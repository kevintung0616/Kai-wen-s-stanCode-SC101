"""
File: add2.py
Name: Kai-wen Tung
------------------------
TODO:
Test:
py add2.py test1
py add2.py test2
py add2.py test3
"""

import sys


class ListNode:
    def __init__(self, data=0, pointer=None):
        self.val = data
        self.next = pointer


def add_2_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    """
    First convert the listNode 'l1' and 'l2' into list and then into digits. After that, add the two numbers and
    convert it into a string. Finally reverse the string of the sum and convert it into a listNode
    :param l1:
    :param l2:
    :return: ans_link_list
    """
    l1_list = []
    cur_1 = l1
    # Convert the listnode l1 into a list 'l1_list'
    while cur_1 is not None:
        l1_list.append(cur_1.val)
        cur_1 = cur_1.next  # 使cur往前移動

    l1 = 0
    count_l1 = 0
    # Loop over l1_list to convert the list into digits
    for i in range(len(l1_list)):
        l1 = l1 + l1_list[i] * (10 ** count_l1)
        count_l1 = count_l1 + 1

    l2_list = []
    cur_2 = l2
    # Convert the listnode l2 into a list 'l2_list'
    while cur_2 is not None:
        l2_list.append(cur_2.val)
        cur_2 = cur_2.next  # 使cur往前移動

    l2 = 0
    count_l2 = 0
    # Loop over l2_list to convert the list into digits
    for i in range(len(l2_list)):
        l2 = l2 + l2_list[i] * (10 ** count_l2)
        count_l2 = count_l2 + 1

    ans = str(l1 + l2)

    # Reverse the answer string
    reverse_ans = ''
    count_ans = 0
    while count_ans < len(ans):
        reverse_ans = ans[count_ans] + reverse_ans
        count_ans = count_ans + 1

    ans_link_list = None
    for ch in reverse_ans:
        if ans_link_list is None:  # First digit in the linked list
            ans_link_list = ListNode(ch, None)
            ans_cur = ans_link_list
        else:
            new_node = ListNode(ch, None)
            ans_cur.next = new_node  # 讓cur連向new_node
            ans_cur = ans_cur.next  # 使cur永遠在linked_list末端，省去讓cur從頭跑到尾的計算時間

    return ans_link_list

####### DO NOT EDIT CODE BELOW THIS LINE ########


def traversal(head):
    """
    :param head: ListNode, the first node to a linked list
    -------------------------------------------
    This function prints out the linked list starting with head
    """

    cur = head
    while cur.next is not None:
        print(cur.val, end='->')
        cur = cur.next
    print(cur.val)


def main():
    args = sys.argv[1:]
    if not args:
        print('Error: Please type"python3 add2.py test1"')
    else:
        if args[0] == 'test1':
            l1 = ListNode(2, None)
            l1.next = ListNode(4, None)
            l1.next.next = ListNode(3, None)
            l2 = ListNode(5, None)
            l2.next = ListNode(6, None)
            l2.next.next = ListNode(4, None)
            ans = add_2_numbers(l1, l2)
            print('---------test1---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test2':
            l1 = ListNode(9, None)
            l1.next = ListNode(9, None)
            l1.next.next = ListNode(9, None)
            l1.next.next.next = ListNode(9, None)
            l1.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next.next = ListNode(9, None)
            l2 = ListNode(9, None)
            l2.next = ListNode(9, None)
            l2.next.next = ListNode(9, None)
            l2.next.next.next = ListNode(9, None)
            ans = add_2_numbers(l1, l2)
            print('---------test2---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test3':
            l1 = ListNode(0, None)
            l2 = ListNode(0, None)
            ans = add_2_numbers(l1, l2)
            print('---------test3---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        else:
            print('Error: Please type"python3 add2.py test1"')


if __name__ == '__main__':
    main()
