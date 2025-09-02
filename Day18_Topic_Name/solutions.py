# Solution.py
# Day 18: Python Coding Interview Challenge - Linked List Problems

from typing import Optional, List

# --- Helper Classes and Functions ---

class ListNode:
    """
    Definition for a singly-linked list node.
    Used in most problems.
    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class NodeWithRandom:
    """
    Definition for a node with a random pointer.
    Used in Problem 10.
    """
    def __init__(self, x: int, next: 'NodeWithRandom' = None, random: 'NodeWithRandom' = None):
        self.val = int(x)
        self.next = next
        self.random = random

def create_linked_list(items: List) -> Optional[ListNode]:
    """Helper function to create a linked list from a Python list."""
    if not items:
        return None
    head = ListNode(items[0])
    current = head
    for item in items[1:]:
        current.next = ListNode(item)
        current = current.next
    return head

def print_linked_list(head: Optional[ListNode]):
    """Helper function to print a linked list."""
    if not head:
        print("None")
        return
    
    nodes = []
    current = head
    while current:
        nodes.append(str(current.val))
        current = current.next
    print(" -> ".join(nodes) + " -> None")

# --- Problem 1: Implement a Singly Linked List ---

class SinglyLinkedList:
    """
    A from-scratch implementation of a Singly Linked List.
    """
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        """Inserts a new node at the end of the list."""
        new_node = ListNode(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def delete_node(self, key):
        """Deletes the first occurrence of a node with the given key."""
        temp = self.head
        # If head node itself holds the key to be deleted
        if temp and temp.val == key:
            self.head = temp.next
            temp = None
            return
        
        prev = None
        while temp and temp.val != key:
            prev = temp
            temp = temp.next
        
        if not temp:
            return # Key not present
        
        prev.next = temp.next
        temp = None

    def search(self, key) -> bool:
        """Searches for a key in the linked list."""
        current = self.head
        while current:
            if current.val == key:
                return True
            current = current.next
        return False

    def traverse(self):
        """Prints the linked list."""
        print_linked_list(self.head)

# --- Solution Class for LeetCode-style Problems ---

class Solution:
    
    # --- Problem 2: Reverse a Linked List ---
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reverses a singly linked list.
        Time: O(n), Space: O(1)
        """
        prev = None
        current = head
        while current:
            next_node = current.next  # Store next node
            current.next = prev       # Reverse current node's pointer
            prev = current            # Move pointers one position ahead
            current = next_node
        return prev

    # --- Problem 3: Detect a Cycle in a Linked List ---
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Detects if a cycle exists using Floyd's Tortoise and Hare algorithm.
        Time: O(n), Space: O(1)
        """
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    # --- Problem 4: Merge Two Sorted Linked Lists ---
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Merges two sorted linked lists into one sorted list.
        Time: O(n + m), Space: O(1)
        """
        dummy = ListNode()
        tail = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
            
        # Append the remainder of the non-empty list
        tail.next = list1 or list2
        
        return dummy.next

    # --- Problem 5: Remove N-th Node From End of List ---
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Removes the n-th node from the end of the list.
        Time: O(L), Space: O(1)
        """
        dummy = ListNode(0, head)
        left = dummy
        right = head
        
        # Move right pointer n steps ahead
        for _ in range(n):
            right = right.next
            
        # Move both pointers until right reaches the end
        while right:
            left = left.next
            right = right.next
            
        # Delete the Nth node from the end
        left.next = left.next.next
        
        return dummy.next

    # --- Problem 6: Add Two Numbers ---
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Adds two numbers represented by linked lists.
        Time: O(max(n, m)), Space: O(max(n, m)) for the new list
        """
        dummy = ListNode()
        current = dummy
        carry = 0
        
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            total = v1 + v2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            
            # Move pointers
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return dummy.next

    # --- Problem 7: Palindrome Linked List ---
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        Checks if a linked list is a palindrome.
        Time: O(n), Space: O(1)
        """
        if not head or not head.next:
            return True

        # 1. Find the middle of the list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # 2. Reverse the second half
        prev = None
        current = slow
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        second_half_head = prev
        
        # 3. Compare the first and reversed second halves
        first_half_head = head
        is_palindrome = True
        while second_half_head:
            if first_half_head.val != second_half_head.val:
                is_palindrome = False
                break
            first_half_head = first_half_head.next
            second_half_head = second_half_head.next
            
        return is_palindrome

    # --- Problem 8: Intersection Node of Two Linked Lists ---
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """
        Finds the node at which two lists intersect.
        Time: O(n + m), Space: O(1)
        """
        p1, p2 = headA, headB
        while p1 != p2:
            p1 = p1.next if p1 else headB
            p2 = p2.next if p2 else headA
        return p1

    # --- Problem 9: Reverse Nodes in k-Group ---
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Reverses nodes of a linked list k at a time.
        Time: O(n), Space: O(1)
        """
        dummy = ListNode(0, head)
        group_prev = dummy
        
        while True:
            kth = self.get_kth_node(group_prev, k)
            if not kth:
                break
            
            group_next = kth.next
            
            # Reverse the group
            prev, current = group_next, group_prev.next
            while current != group_next:
                temp = current.next
                current.next = prev
                prev = current
                current = temp
                
            temp = group_prev.next
            group_prev.next = kth
            group_prev = temp

        return dummy.next
    
    def get_kth_node(self, current, k):
        """Helper for reverseKGroup to find the k-th node."""
        while current and k > 0:
            current = current.next
            k -= 1
        return current

    # --- Problem 10: Copy List with Random Pointer ---
    def copyRandomList(self, head: 'Optional[NodeWithRandom]') -> 'Optional[NodeWithRandom]':
        """
        Creates a deep copy of a list with random pointers.
        Time: O(n), Space: O(n) using a hash map.
        """
        if not head:
            return None
        
        # Hash map to store the mapping from old node to new node
        old_to_new = {None: None}
        
        # First pass: create all new nodes and map them
        current = head
        while current:
            old_to_new[current] = NodeWithRandom(current.val)
            current = current.next
        
        # Second pass: connect the next and random pointers
        current = head
        while current:
            new_node = old_to_new[current]
            new_node.next = old_to_new[current.next]
            new_node.random = old_to_new[current.random]
            current = current.next
            
        return old_to_new[head]


# --- Main execution block to test the solutions ---

if __name__ == "__main__":
    solver = Solution()

    print("--- 1. Implement a Singly Linked List ---")
    ll = SinglyLinkedList()
    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_end(30)
    print("Original list:"); ll.traverse()
    print(f"Is 20 in the list? {ll.search(20)}")
    ll.delete_node(20)
    print("List after deleting 20:"); ll.traverse()
    
    print("\n--- 2. Reverse a Linked List ---")
    l2 = create_linked_list([1, 2, 3, 4, 5])
    print("Original list:"); print_linked_list(l2)
    reversed_l2 = solver.reverseList(l2)
    print("Reversed list:"); print_linked_list(reversed_l2)
    
    print("\n--- 3. Detect a Cycle in a Linked List ---")
    l3_cycle = create_linked_list([3, 2, 0, -4])
    l3_cycle.next.next.next.next = l3_cycle.next # Create cycle: -4 points to 2
    l3_no_cycle = create_linked_list([1, 2])
    print(f"List [3, 2, 0, -4, cycle] has cycle: {solver.hasCycle(l3_cycle)}")
    print(f"List [1, 2] has cycle: {solver.hasCycle(l3_no_cycle)}")
    
    print("\n--- 4. Merge Two Sorted Linked Lists ---")
    l4a = create_linked_list([1, 2, 4])
    l4b = create_linked_list([1, 3, 4])
    print("List 1:"); print_linked_list(l4a)
    print("List 2:"); print_linked_list(l4b)
    merged_l4 = solver.mergeTwoLists(l4a, l4b)
    print("Merged list:"); print_linked_list(merged_l4)
    
    print("\n--- 5. Remove N-th Node From End of List ---")
    l5 = create_linked_list([1, 2, 3, 4, 5])
    print("Original list:"); print_linked_list(l5)
    l5_removed = solver.removeNthFromEnd(l5, 2)
    print("List after removing 2nd from end:"); print_linked_list(l5_removed)
    
    print("\n--- 6. Add Two Numbers ---")
    l6a = create_linked_list([2, 4, 3])
    l6b = create_linked_list([5, 6, 4])
    print("Number 1 (342):"); print_linked_list(l6a)
    print("Number 2 (465):"); print_linked_list(l6b)
    sum_l6 = solver.addTwoNumbers(l6a, l6b)
    print("Sum (807):"); print_linked_list(sum_l6)

    print("\n--- 7. Palindrome Linked List ---")
    l7_palindrome = create_linked_list([1, 2, 3, 2, 1])
    l7_not_palindrome = create_linked_list([1, 2, 3, 4, 5])
    print("List [1,2,3,2,1]:"); print_linked_list(l7_palindrome)
    print(f"Is palindrome? {solver.isPalindrome(l7_palindrome)}")
    print("List [1,2,3,4,5]:"); print_linked_list(l7_not_palindrome)
    print(f"Is palindrome? {solver.isPalindrome(l7_not_palindrome)}")
    
    print("\n--- 8. Intersection Node of Two Linked Lists ---")
    # Create intersecting lists: listA = 4->1->8->4->5, listB = 5->6->1->8->4->5
    common_part = create_linked_list([8, 4, 5])
    l8a = ListNode(4, ListNode(1, common_part))
    l8b = ListNode(5, ListNode(6, ListNode(1, common_part)))
    intersection_node = solver.getIntersectionNode(l8a, l8b)
    print("List A:"); print_linked_list(l8a)
    print("List B:"); print_linked_list(l8b)
    print(f"Intersection node value: {intersection_node.val if intersection_node else 'None'}")
    
    print("\n--- 9. Reverse Nodes in k-Group ---")
    l9 = create_linked_list([1, 2, 3, 4, 5])
    print("Original list:"); print_linked_list(l9)
    reversed_k_l9 = solver.reverseKGroup(l9, 2)
    print("List after reversing in groups of 2:"); print_linked_list(reversed_k_l9)
    
    print("\n--- 10. Copy List with Random Pointer ---")
    node1 = NodeWithRandom(7)
    node2 = NodeWithRandom(13)
    node3 = NodeWithRandom(11)
    node4 = NodeWithRandom(10)
    node5 = NodeWithRandom(1)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node1.random = None
    node2.random = node1
    node3.random = node5
    node4.random = node3
    node5.random = node1
    copied_head = solver.copyRandomList(node1)
    print("Copying list with random pointers... (verified if pointers are new objects)")
    # Verification: check if copied nodes are new objects
    print(f"Original head == Copied head? {node1 is copied_head}")
    print(f"Original head.next == Copied head.next? {node1.next is copied_head.next}")
    print(f"Original head.random == Copied head.random? {node1.random is copied_head.random}")
