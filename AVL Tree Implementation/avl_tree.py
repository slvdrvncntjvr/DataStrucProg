"""
============================================================================
AVL TREE IMPLEMENTATION IN PYTHON
============================================================================

A complete implementation of AVL tree with detailed explanations of how
balance is maintained through rotations during insertions and deletions.

Author: Vincent
Date: November 12, 2025
"""

from typing import Optional, Tuple, List
from dataclasses import dataclass


# ============================================================================
# DATA STRUCTURES
# ============================================================================

class AVLNode:
    """
    AVL Tree Node
    
    Attributes:
        key: The value stored in the node
        height: Height of the subtree rooted at this node
        left: Pointer to left child
        right: Pointer to right child
    """
    def __init__(self, key: int):
        self.key = key
        self.height = 1  # New node is initially at height 1
        self.left: Optional['AVLNode'] = None
        self.right: Optional['AVLNode'] = None
    
    def __repr__(self) -> str:
        return f"AVLNode(key={self.key}, height={self.height})"


@dataclass
class TreeStats:
    """
    Tree Statistics
    
    Tracks metrics about tree operations
    """
    total_nodes: int = 0
    total_rotations: int = 0
    max_height: int = 0
    ll_rotations: int = 0  # Left-Left rotations
    rr_rotations: int = 0  # Right-Right rotations
    lr_rotations: int = 0  # Left-Right rotations
    rl_rotations: int = 0  # Right-Left rotations


# ============================================================================
# AVL TREE CLASS
# ============================================================================

class AVLTree:
    """
    AVL Tree Implementation
    
    A self-balancing binary search tree where the heights of the two child
    subtrees of any node differ by at most one. If at any time they differ
    by more than one, rebalancing is done through rotations to restore this property.
    """
    
    def __init__(self, verbose: bool = False):
        """
        Initialize an empty AVL tree
        
        Args:
            verbose: If True, print detailed operation information
        """
        self.root: Optional[AVLNode] = None
        self.stats = TreeStats()
        self.verbose = verbose
    
    # ========================================================================
    # HEIGHT AND BALANCE OPERATIONS
    # ========================================================================
    
    def height(self, node: Optional[AVLNode]) -> int:
        """
        Get height of a node
        
        Height of NULL node is 0
        Height of leaf node is 1
        
        Args:
            node: The node to get height from
            
        Returns:
            Height of the node
        """
        if node is None:
            return 0
        return node.height
    
    def get_balance(self, node: Optional[AVLNode]) -> int:
        """
        Calculate balance factor of a node
        
        Balance Factor (BF) = height(left subtree) - height(right subtree)
        
        BF > 0: Left subtree is taller (left-heavy)
        BF < 0: Right subtree is taller (right-heavy)
        BF = 0: Perfectly balanced
        
        For AVL tree: BF must be in {-1, 0, 1}
        
        Args:
            node: The node to calculate balance factor for
            
        Returns:
            Balance factor
        """
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)
    
    def update_height(self, node: AVLNode) -> None:
        """
        Update height of a node based on its children
        
        Height = 1 + maximum(height of left child, height of right child)
        
        Args:
            node: The node to update height for
        """
        if node is not None:
            node.height = 1 + max(self.height(node.left), self.height(node.right))
    
    def is_balanced(self, node: Optional[AVLNode] = None) -> bool:
        """
        Check if a subtree is balanced
        
        Args:
            node: Root of subtree to check (defaults to tree root)
            
        Returns:
            True if balanced, False otherwise
        """
        if node is None:
            node = self.root
        
        if node is None:
            return True
        
        bf = self.get_balance(node)
        return -1 <= bf <= 1
    
    # ========================================================================
    # ROTATION OPERATIONS
    # ========================================================================
    
    def rotate_right(self, y: AVLNode) -> AVLNode:
        r"""
        Perform RIGHT rotation (for Left-Left case)
        
        This rotation is performed when:
        - Node is left-heavy (BF > 1)
        - Left child is also left-heavy or balanced (BF >= 0)
        
        BEFORE:          AFTER:
              y            x
             / \          / \
            x   T3  ==>  T1  y
           / \              / \
          T1  T2           T2  T3
        
        Args:
            y: The node to rotate
            
        Returns:
            New root of the subtree (x)
        """
        if self.verbose:
            print(f"  🔄 Performing RIGHT ROTATION on node {y.key}")
            print(f"     Pivot: {y.key}, Moving up: {y.left.key}")
        
        # Save pointers
        x = y.left
        T2 = x.right
        
        # Perform rotation
        x.right = y
        y.left = T2
        
        # Update heights (bottom-up)
        self.update_height(y)
        self.update_height(x)
        
        # Update statistics
        self.stats.total_rotations += 1
        self.stats.ll_rotations += 1
        
        if self.verbose:
            print(f"     ✅ Rotation complete. New local root: {x.key}")
        
        return x
    
    def rotate_left(self, x: AVLNode) -> AVLNode:
        r"""
        Perform LEFT rotation (for Right-Right case)
        
        This rotation is performed when:
        - Node is right-heavy (BF < -1)
        - Right child is also right-heavy or balanced (BF <= 0)
        
        BEFORE:          AFTER:
            x              y
           / \            / \
          T1  y    ==>   x   T3
             / \        / \
            T2  T3     T1  T2
        
        Args:
            x: The node to rotate
            
        Returns:
            New root of the subtree (y)
        """
        if self.verbose:
            print(f"  🔄 Performing LEFT ROTATION on node {x.key}")
            print(f"     Pivot: {x.key}, Moving up: {x.right.key}")
        
        # Save pointers
        y = x.right
        T2 = y.left
        
        # Perform rotation
        y.left = x
        x.right = T2
        
        # Update heights (bottom-up)
        self.update_height(x)
        self.update_height(y)
        
        # Update statistics
        self.stats.total_rotations += 1
        self.stats.rr_rotations += 1
        
        if self.verbose:
            print(f"     ✅ Rotation complete. New local root: {y.key}")
        
        return y
    
    def rotate_left_right(self, node: AVLNode) -> AVLNode:
        """
        Perform LEFT-RIGHT rotation (for Left-Right case)
        
        This rotation is performed when:
        - Node is left-heavy (BF > 1)
        - Left child is right-heavy (BF < 0)
        
        This is a DOUBLE ROTATION:
        1. First: LEFT rotation on left child
        2. Second: RIGHT rotation on node
        
        Args:
            node: The node to rotate
            
        Returns:
            New root of the subtree
        """
        if self.verbose:
            print(f"  🔄 Performing LEFT-RIGHT (DOUBLE) ROTATION on node {node.key}")
            print(f"     Step 1: Left rotation on left child {node.left.key}")
        
        # Step 1: Left rotation on left child
        node.left = self.rotate_left(node.left)
        self.stats.lr_rotations += 1
        self.stats.total_rotations -= 1  # Adjust for double counting
        
        if self.verbose:
            print(f"     Step 2: Right rotation on node {node.key}")
        
        # Step 2: Right rotation on node
        return self.rotate_right(node)
    
    def rotate_right_left(self, node: AVLNode) -> AVLNode:
        """
        Perform RIGHT-LEFT rotation (for Right-Left case)
        
        This rotation is performed when:
        - Node is right-heavy (BF < -1)
        - Right child is left-heavy (BF > 0)
        
        This is a DOUBLE ROTATION:
        1. First: RIGHT rotation on right child
        2. Second: LEFT rotation on node
        
        Args:
            node: The node to rotate
            
        Returns:
            New root of the subtree
        """
        if self.verbose:
            print(f"  🔄 Performing RIGHT-LEFT (DOUBLE) ROTATION on node {node.key}")
            print(f"     Step 1: Right rotation on right child {node.right.key}")
        
        # Step 1: Right rotation on right child
        node.right = self.rotate_right(node.right)
        self.stats.rl_rotations += 1
        self.stats.total_rotations -= 1  # Adjust for double counting
        
        if self.verbose:
            print(f"     Step 2: Left rotation on node {node.key}")
        
        # Step 2: Left rotation on node
        return self.rotate_left(node)
    
    # ========================================================================
    # INSERTION OPERATION
    # ========================================================================
    
    def insert(self, key: int) -> None:
        """
        Insert a key into the AVL tree
        
        Public method that wraps the recursive insert operation
        
        Args:
            key: The value to insert
        """
        if self.verbose:
            print(f"\n{'='*60}")
            print(f"INSERTING KEY: {key}")
            print('='*60)
        
        self.root = self._insert_recursive(self.root, key)
        self.stats.max_height = self.height(self.root)
    
    def _insert_recursive(self, node: Optional[AVLNode], key: int) -> AVLNode:
        """
        Insert a key into the AVL tree (recursive implementation)
        
        This is the most critical operation for understanding AVL trees.
        The insertion process has 4 main steps:
        
        STEP 1: Perform standard BST insertion (recursive)
        STEP 2: Update height of the ancestor node
        STEP 3: Calculate balance factor to check if node became unbalanced
        STEP 4: If unbalanced, perform appropriate rotation(s)
        
        There are 4 cases for rebalancing:
        - Left-Left (LL): Single right rotation
        - Right-Right (RR): Single left rotation
        - Left-Right (LR): Double rotation (left then right)
        - Right-Left (RL): Double rotation (right then left)
        
        Args:
            node: Current node in recursion
            key: The value to insert
            
        Returns:
            The new root of the subtree
        """
        # ====================================================================
        # STEP 1: PERFORM STANDARD BST INSERTION
        # ====================================================================
        
        # Base case: found the insertion point
        if node is None:
            if self.verbose:
                print(f"  ➕ Inserting {key} as new leaf node")
            self.stats.total_nodes += 1
            return AVLNode(key)
        
        # Recursive insertion
        if key < node.key:
            if self.verbose:
                print(f"  ⬅️  {key} < {node.key}, going left")
            node.left = self._insert_recursive(node.left, key)
        elif key > node.key:
            if self.verbose:
                print(f"  ➡️  {key} > {node.key}, going right")
            node.right = self._insert_recursive(node.right, key)
        else:
            # Duplicate key - not allowed in this implementation
            if self.verbose:
                print(f"  ⚠️  Duplicate key {key}, ignoring")
            return node
        
        # ====================================================================
        # STEP 2: UPDATE HEIGHT OF CURRENT NODE
        # ====================================================================
        
        self.update_height(node)
        if self.verbose:
            print(f"  📏 Updated height of node {node.key} to {node.height}")
        
        # ====================================================================
        # STEP 3: GET BALANCE FACTOR AND CHECK IF NODE BECAME UNBALANCED
        # ====================================================================
        
        balance = self.get_balance(node)
        if self.verbose:
            status = "BALANCED"
            if balance > 1:
                status = "LEFT-HEAVY"
            elif balance < -1:
                status = "RIGHT-HEAVY"
            print(f"  ⚖️  Balance factor of node {node.key}: {balance} ({status})")
        
        # ====================================================================
        # STEP 4: IF UNBALANCED, PERFORM APPROPRIATE ROTATION
        # ====================================================================
        
        # LEFT-LEFT CASE (LL)
        # Tree is left-heavy AND left child is left-heavy or balanced
        if balance > 1 and key < node.left.key:
            if self.verbose:
                print(f"  🔍 Detected LEFT-LEFT case at node {node.key}")
                print(f"     Cause: Inserted {key} in left subtree of left child {node.left.key}")
            return self.rotate_right(node)
        
        # RIGHT-RIGHT CASE (RR)
        # Tree is right-heavy AND right child is right-heavy or balanced
        if balance < -1 and key > node.right.key:
            if self.verbose:
                print(f"  🔍 Detected RIGHT-RIGHT case at node {node.key}")
                print(f"     Cause: Inserted {key} in right subtree of right child {node.right.key}")
            return self.rotate_left(node)
        
        # LEFT-RIGHT CASE (LR)
        # Tree is left-heavy BUT left child is right-heavy
        if balance > 1 and key > node.left.key:
            if self.verbose:
                print(f"  🔍 Detected LEFT-RIGHT case at node {node.key}")
                print(f"     Cause: Inserted {key} in right subtree of left child {node.left.key}")
            return self.rotate_left_right(node)
        
        # RIGHT-LEFT CASE (RL)
        # Tree is right-heavy BUT right child is left-heavy
        if balance < -1 and key < node.right.key:
            if self.verbose:
                print(f"  🔍 Detected RIGHT-LEFT case at node {node.key}")
                print(f"     Cause: Inserted {key} in left subtree of right child {node.right.key}")
            return self.rotate_right_left(node)
        
        # If we reach here, node is balanced
        if self.verbose:
            print(f"  ✅ Node {node.key} remains balanced, no rotation needed")
        
        return node
    
    # ========================================================================
    # DELETION OPERATION
    # ========================================================================
    
    def delete(self, key: int) -> None:
        """
        Delete a key from the AVL tree
        
        Public method that wraps the recursive delete operation
        
        Args:
            key: The value to delete
        """
        if self.verbose:
            print(f"\n{'='*60}")
            print(f"DELETING KEY: {key}")
            print('='*60)
        
        self.root = self._delete_recursive(self.root, key)
        if self.root:
            self.stats.max_height = self.height(self.root)
    
    def _min_value_node(self, node: AVLNode) -> AVLNode:
        """
        Find the node with minimum value in a subtree
        
        Used in deletion when replacing a node with two children
        
        Args:
            node: Root of the subtree
            
        Returns:
            Node with minimum value
        """
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    def _delete_recursive(self, node: Optional[AVLNode], key: int) -> Optional[AVLNode]:
        """
        Delete a key from the AVL tree (recursive implementation)
        
        Similar to insertion, deletion has 4 main steps:
        
        STEP 1: Perform standard BST deletion
        STEP 2: Update height of the current node
        STEP 3: Calculate balance factor
        STEP 4: If unbalanced, perform appropriate rotation(s)
        
        The main difference: we check balance of children to determine rotation type
        
        Args:
            node: Current node in recursion
            key: The value to delete
            
        Returns:
            The new root of the subtree
        """
        # ====================================================================
        # STEP 1: PERFORM STANDARD BST DELETION
        # ====================================================================
        
        # Base case: key not found
        if node is None:
            if self.verbose:
                print(f"  ⚠️  Key {key} not found in tree")
            return node
        
        # Recursive deletion
        if key < node.key:
            if self.verbose:
                print(f"  ⬅️  {key} < {node.key}, going left")
            node.left = self._delete_recursive(node.left, key)
        elif key > node.key:
            if self.verbose:
                print(f"  ➡️  {key} > {node.key}, going right")
            node.right = self._delete_recursive(node.right, key)
        else:
            # Found the node to delete
            if self.verbose:
                print(f"  🎯 Found node to delete: {key}")
            
            # Case 1: Node with only one child or no child
            if node.left is None or node.right is None:
                temp = node.left if node.left else node.right
                
                if temp is None:
                    # No child case
                    if self.verbose:
                        print("     Leaf node - simply removing")
                    self.stats.total_nodes -= 1
                    return None
                else:
                    # One child case
                    if self.verbose:
                        print(f"     One child - replacing with child {temp.key}")
                    self.stats.total_nodes -= 1
                    return temp
            else:
                # Case 2: Node with two children
                # Get the inorder successor (smallest in the right subtree)
                temp = self._min_value_node(node.right)
                
                if self.verbose:
                    print(f"     Two children - replacing with successor {temp.key}")
                
                # Copy the successor's content to this node
                node.key = temp.key
                
                # Delete the successor
                node.right = self._delete_recursive(node.right, temp.key)
        
        # If tree had only one node, return
        if node is None:
            return node
        
        # ====================================================================
        # STEP 2: UPDATE HEIGHT OF CURRENT NODE
        # ====================================================================
        
        self.update_height(node)
        if self.verbose:
            print(f"  📏 Updated height of node {node.key} to {node.height}")
        
        # ====================================================================
        # STEP 3: GET BALANCE FACTOR
        # ====================================================================
        
        balance = self.get_balance(node)
        if self.verbose:
            status = "BALANCED"
            if balance > 1:
                status = "LEFT-HEAVY"
            elif balance < -1:
                status = "RIGHT-HEAVY"
            print(f"  ⚖️  Balance factor of node {node.key}: {balance} ({status})")
        
        # ====================================================================
        # STEP 4: IF UNBALANCED, PERFORM APPROPRIATE ROTATION
        # ====================================================================
        
        # Note: Unlike insertion, we check the balance of CHILDREN
        # to determine which rotation to perform
        
        # LEFT-LEFT CASE
        if balance > 1 and self.get_balance(node.left) >= 0:
            if self.verbose:
                print(f"  🔍 Detected LEFT-LEFT case at node {node.key}")
            return self.rotate_right(node)
        
        # LEFT-RIGHT CASE
        if balance > 1 and self.get_balance(node.left) < 0:
            if self.verbose:
                print(f"  🔍 Detected LEFT-RIGHT case at node {node.key}")
            return self.rotate_left_right(node)
        
        # RIGHT-RIGHT CASE
        if balance < -1 and self.get_balance(node.right) <= 0:
            if self.verbose:
                print(f"  🔍 Detected RIGHT-RIGHT case at node {node.key}")
            return self.rotate_left(node)
        
        # RIGHT-LEFT CASE
        if balance < -1 and self.get_balance(node.right) > 0:
            if self.verbose:
                print(f"  🔍 Detected RIGHT-LEFT case at node {node.key}")
            return self.rotate_right_left(node)
        
        if self.verbose:
            print(f"  ✅ Node {node.key} remains balanced after deletion")
        
        return node
    
    # ========================================================================
    # SEARCH OPERATION
    # ========================================================================
    
    def search(self, key: int) -> Optional[AVLNode]:
        """
        Search for a key in the AVL tree
        
        Standard BST search - AVL property doesn't change search logic,
        but guarantees O(log n) performance
        
        Args:
            key: The value to search for
            
        Returns:
            The node containing the key, or None if not found
        """
        if self.verbose:
            print(f"\nSearching for key: {key}")
        
        return self._search_recursive(self.root, key)
    
    def _search_recursive(self, node: Optional[AVLNode], key: int) -> Optional[AVLNode]:
        """
        Search for a key (recursive implementation)
        
        Args:
            node: Current node in recursion
            key: The value to search for
            
        Returns:
            The node containing the key, or None if not found
        """
        # Base cases: root is null or key is at root
        if node is None:
            if self.verbose:
                print(f"  ❌ Key {key} not found")
            return None
        
        if node.key == key:
            if self.verbose:
                print(f"  ✅ Found key {key}")
            return node
        
        # Key is smaller than root's key
        if key < node.key:
            if self.verbose:
                print(f"  ⬅️  Searching left subtree of {node.key}")
            return self._search_recursive(node.left, key)
        
        # Key is greater than root's key
        if self.verbose:
            print(f"  ➡️  Searching right subtree of {node.key}")
        return self._search_recursive(node.right, key)
    
    # ========================================================================
    # UTILITY OPERATIONS
    # ========================================================================
    
    def min_value(self) -> Optional[int]:
        """Get the minimum value in the tree"""
        if self.root is None:
            return None
        node = self._min_value_node(self.root)
        return node.key
    
    def max_value(self) -> Optional[int]:
        """Get the maximum value in the tree"""
        if self.root is None:
            return None
        current = self.root
        while current.right is not None:
            current = current.right
        return current.key
    
    def count_nodes(self) -> int:
        """Count total number of nodes in the tree"""
        return self._count_nodes_recursive(self.root)
    
    def _count_nodes_recursive(self, node: Optional[AVLNode]) -> int:
        """Count nodes recursively"""
        if node is None:
            return 0
        return 1 + self._count_nodes_recursive(node.left) + self._count_nodes_recursive(node.right)
    
    def successor(self, key: int) -> Optional[int]:
        """Find the successor of a given key"""
        current = self.root
        succ = None
        
        while current is not None:
            if key < current.key:
                succ = current.key
                current = current.left
            elif key > current.key:
                current = current.right
            else:
                # Found the key
                if current.right is not None:
                    return self._min_value_node(current.right).key
                break
        
        return succ
    
    def predecessor(self, key: int) -> Optional[int]:
        """Find the predecessor of a given key"""
        current = self.root
        pred = None
        
        while current is not None:
            if key > current.key:
                pred = current.key
                current = current.right
            elif key < current.key:
                current = current.left
            else:
                # Found the key
                if current.left is not None:
                    node = current.left
                    while node.right is not None:
                        node = node.right
                    return node.key
                break
        
        return pred
    
    # ========================================================================
    # TRAVERSAL OPERATIONS
    # ========================================================================
    
    def inorder_traversal(self) -> List[int]:
        """
        In-order traversal (Left-Root-Right)
        Produces sorted output
        
        Returns:
            List of keys in sorted order
        """
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node: Optional[AVLNode], result: List[int]) -> None:
        """In-order traversal helper"""
        if node is not None:
            self._inorder_recursive(node.left, result)
            result.append(node.key)
            self._inorder_recursive(node.right, result)
    
    def preorder_traversal(self) -> List[int]:
        """
        Pre-order traversal (Root-Left-Right)
        
        Returns:
            List of keys in pre-order
        """
        result = []
        self._preorder_recursive(self.root, result)
        return result
    
    def _preorder_recursive(self, node: Optional[AVLNode], result: List[int]) -> None:
        """Pre-order traversal helper"""
        if node is not None:
            result.append(node.key)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)
    
    def postorder_traversal(self) -> List[int]:
        """
        Post-order traversal (Left-Right-Root)
        
        Returns:
            List of keys in post-order
        """
        result = []
        self._postorder_recursive(self.root, result)
        return result
    
    def _postorder_recursive(self, node: Optional[AVLNode], result: List[int]) -> None:
        """Post-order traversal helper"""
        if node is not None:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.key)
    
    def level_order_traversal(self) -> List[int]:
        """
        Level-order traversal (Breadth-First)
        
        Returns:
            List of keys in level-order
        """
        if self.root is None:
            return []
        
        result = []
        queue = [self.root]
        
        while queue:
            current = queue.pop(0)
            result.append(current.key)
            
            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)
        
        return result
    
    # ========================================================================
    # VISUALIZATION OPERATIONS
    # ========================================================================
    
    def print_tree(self, space: int = 0, increment: int = 5) -> None:
        """
        Print the tree structure visually
        
        Format shows: [key(h=height, bf=balance_factor)]
        
        Args:
            space: Initial spacing
            increment: Space increment per level
        """
        self._print_tree_recursive(self.root, space, increment)
    
    def _print_tree_recursive(self, node: Optional[AVLNode], space: int, increment: int) -> None:
        """Print tree recursively"""
        if node is None:
            return
        
        # Increase distance between levels
        space += increment
        
        # Process right child first
        self._print_tree_recursive(node.right, space, increment)
        
        # Print current node after spacing
        print()
        for _ in range(increment, space):
            print(" ", end="")
        bf = self.get_balance(node)
        print(f"[{node.key}(h={node.height},bf={bf})]")
        
        # Process left child
        self._print_tree_recursive(node.left, space, increment)
    
    def print_node_info(self, key: int) -> None:
        """
        Print detailed information about a specific node
        
        Args:
            key: The key to find and print info for
        """
        node = self.search(key)
        if node is None:
            print(f"Node with key {key} not found")
            return
        
        print("╔════════════════════════════════════╗")
        print("║       NODE INFORMATION             ║")
        print("╠════════════════════════════════════╣")
        print(f"║ Key:            {node.key:18} ║")
        print(f"║ Height:         {node.height:18} ║")
        print(f"║ Balance Factor: {self.get_balance(node):18} ║")
        print(f"║ Left Child:     {'Yes' if node.left else 'No':18} ║")
        if node.left:
            print(f"║   └─ Key:       {node.left.key:18} ║")
        print(f"║ Right Child:    {'Yes' if node.right else 'No':18} ║")
        if node.right:
            print(f"║   └─ Key:       {node.right.key:18} ║")
        print("╚════════════════════════════════════╝")
    
    def print_statistics(self) -> None:
        """Print tree statistics"""
        print("\n╔════════════════════════════════════════════╗")
        print("║         TREE STATISTICS                    ║")
        print("╠════════════════════════════════════════════╣")
        print(f"║ Total Nodes:        {self.stats.total_nodes:20} ║")
        print(f"║ Maximum Height:     {self.stats.max_height:20} ║")
        print(f"║ Total Rotations:    {self.stats.total_rotations:20} ║")
        print("║                                            ║")
        print("║ Rotation Breakdown:                        ║")
        print(f"║   Left-Left (LL):   {self.stats.ll_rotations:20} ║")
        print(f"║   Right-Right (RR): {self.stats.rr_rotations:20} ║")
        print(f"║   Left-Right (LR):  {self.stats.lr_rotations:20} ║")
        print(f"║   Right-Left (RL):  {self.stats.rl_rotations:20} ║")
        print("╚════════════════════════════════════════════╝\n")
    
    # ========================================================================
    # VERIFICATION OPERATIONS
    # ========================================================================
    
    def verify_avl(self) -> bool:
        """
        Verify the entire tree satisfies AVL properties
        
        Checks:
        1. BST property (left < root < right)
        2. Balance property (|BF| ≤ 1 for all nodes)
        3. Height property (heights are correctly maintained)
        
        Returns:
            True if valid AVL tree, False otherwise
        """
        print("\n🔍 VERIFYING AVL TREE PROPERTIES...")
        
        # Check BST property
        is_bst = self._is_bst_util(self.root, float('-inf'), float('inf'))
        print(f"   BST Property: {'✅ VALID' if is_bst else '❌ INVALID'}")
        
        # Check balance property
        is_balanced = self._is_balanced_util(self.root)
        print(f"   Balance Property: {'✅ VALID' if is_balanced else '❌ INVALID'}")
        
        # Check heights
        heights_valid = self._verify_heights(self.root)
        print(f"   Heights: {'✅ VALID' if heights_valid else '❌ INVALID'}")
        
        is_valid = is_bst and is_balanced and heights_valid
        print(f"   Overall: {'✅ VALID AVL TREE' if is_valid else '❌ INVALID AVL TREE'}\n")
        
        return is_valid
    
    def _is_bst_util(self, node: Optional[AVLNode], min_val: float, max_val: float) -> bool:
        """Helper to verify BST property"""
        if node is None:
            return True
        
        if node.key <= min_val or node.key >= max_val:
            return False
        
        return (self._is_bst_util(node.left, min_val, node.key) and
                self._is_bst_util(node.right, node.key, max_val))
    
    def _is_balanced_util(self, node: Optional[AVLNode]) -> bool:
        """Helper to verify balance property"""
        if node is None:
            return True
        
        bf = self.get_balance(node)
        
        if bf < -1 or bf > 1:
            return False
        
        return self._is_balanced_util(node.left) and self._is_balanced_util(node.right)
    
    def _verify_heights(self, node: Optional[AVLNode]) -> bool:
        """Helper to verify heights"""
        if node is None:
            return True
        
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        expected_height = 1 + max(left_height, right_height)
        
        if node.height != expected_height:
            return False
        
        return self._verify_heights(node.left) and self._verify_heights(node.right)


# ============================================================================
# MAIN DEMONSTRATION (if run directly)
# ============================================================================

if __name__ == "__main__":
    print("\n" + "="*60)
    print("AVL TREE IMPLEMENTATION - QUICK DEMO")
    print("="*60)
    
    # Create an AVL tree with verbose output
    avl = AVLTree(verbose=True)
    
    # Insert some values
    print("\nInserting values: 10, 20, 30, 40, 50, 25")
    for key in [10, 20, 30, 40, 50, 25]:
        avl.insert(key)
    
    # Print tree structure
    print("\nTree Structure:")
    avl.print_tree()
    
    # Print statistics
    avl.print_statistics()
    
    # Verify AVL properties
    avl.verify_avl()
    
    print("\n✅ AVL Tree implementation in Python complete!")
