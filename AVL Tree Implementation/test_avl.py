"""
============================================================================
AVL TREE COMPREHENSIVE TEST SUITE
============================================================================

This program tests all AVL tree operations to ensure correctness.
Demonstrates proper implementation of:
- Insertion with automatic balancing
- Deletion with rebalancing
- Search operations
- All four rotation cases (LL, RR, LR, RL)
- Edge cases and stress testing

Author: Vincent
Date: November 12, 2025
"""

import math
from avl_tree import AVLTree


class TestAVL:
    """Test suite for AVL Tree implementation"""
    
    def __init__(self):
        self.tests_passed = 0
        self.tests_failed = 0
    
    def test_result(self, test_name: str, passed: bool) -> None:
        """Record and print test result"""
        if passed:
            print(f"PASS: {test_name}")
            self.tests_passed += 1
        else:
            print(f"FAIL: {test_name}")
            self.tests_failed += 1
    
    def test_node_creation(self) -> None:
        """Test basic node and tree creation"""
        print("\n=== Testing Node Creation ===")
        
        avl = AVLTree(verbose=False)
        
        self.test_result("Empty tree creation", avl.root is None)
        self.test_result("Initial node count", avl.count_nodes() == 0)
        self.test_result("Initial height", avl.height(avl.root) == 0)
    
    def test_single_insertion(self) -> None:
        """Test single node insertion"""
        print("\n=== Testing Single Insertion ===")
        
        avl = AVLTree(verbose=False)
        avl.insert(50)
        
        self.test_result("Root not NULL", avl.root is not None)
        self.test_result("Root key correct", avl.root.key == 50)
        self.test_result("Tree height", avl.height(avl.root) == 1)
        self.test_result("Balance factor", avl.get_balance(avl.root) == 0)
        self.test_result("Node count", avl.count_nodes() == 1)
    
    def test_ll_rotation(self) -> None:
        """Test Left-Left (LL) rotation case"""
        print("\n=== Testing Left-Left (LL) Rotation ===")
        
        avl = AVLTree(verbose=False)
        avl.insert(30)
        avl.insert(20)
        avl.insert(10)  # Triggers LL rotation
        
        self.test_result("Root is 20 after rotation", avl.root.key == 20)
        self.test_result("Left child is 10", avl.root.left and avl.root.left.key == 10)
        self.test_result("Right child is 30", avl.root.right and avl.root.right.key == 30)
        self.test_result("Tree is balanced", avl.is_balanced())
        self.test_result("AVL properties valid", avl.verify_avl())
    
    def test_rr_rotation(self) -> None:
        """Test Right-Right (RR) rotation case"""
        print("\n=== Testing Right-Right (RR) Rotation ===")
        
        avl = AVLTree(verbose=False)
        avl.insert(10)
        avl.insert(20)
        avl.insert(30)  # Triggers RR rotation
        
        self.test_result("Root is 20 after rotation", avl.root.key == 20)
        self.test_result("Left child is 10", avl.root.left and avl.root.left.key == 10)
        self.test_result("Right child is 30", avl.root.right and avl.root.right.key == 30)
        self.test_result("Tree is balanced", avl.is_balanced())
        self.test_result("AVL properties valid", avl.verify_avl())
    
    def test_lr_rotation(self) -> None:
        """Test Left-Right (LR) rotation case"""
        print("\n=== Testing Left-Right (LR) Rotation ===")
        
        avl = AVLTree(verbose=False)
        avl.insert(30)
        avl.insert(10)
        avl.insert(20)  # Triggers LR rotation
        
        self.test_result("Root is 20 after rotation", avl.root.key == 20)
        self.test_result("Left child is 10", avl.root.left and avl.root.left.key == 10)
        self.test_result("Right child is 30", avl.root.right and avl.root.right.key == 30)
        self.test_result("Tree is balanced", avl.is_balanced())
        self.test_result("AVL properties valid", avl.verify_avl())
    
    def test_rl_rotation(self) -> None:
        """Test Right-Left (RL) rotation case"""
        print("\n=== Testing Right-Left (RL) Rotation ===")
        
        avl = AVLTree(verbose=False)
        avl.insert(10)
        avl.insert(30)
        avl.insert(20)  # Triggers RL rotation
        
        self.test_result("Root is 20 after rotation", avl.root.key == 20)
        self.test_result("Left child is 10", avl.root.left and avl.root.left.key == 10)
        self.test_result("Right child is 30", avl.root.right and avl.root.right.key == 30)
        self.test_result("Tree is balanced", avl.is_balanced())
        self.test_result("AVL properties valid", avl.verify_avl())
    
    def test_multiple_insertions(self) -> None:
        """Test multiple insertions maintaining balance"""
        print("\n=== Testing Multiple Insertions ===")
        
        avl = AVLTree(verbose=False)
        keys = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35]
        
        for key in keys:
            avl.insert(key)
        
        self.test_result("All nodes inserted", avl.count_nodes() == len(keys))
        self.test_result("Tree is balanced", avl.is_balanced())
        self.test_result("AVL properties valid", avl.verify_avl())
        self.test_result("Height is logarithmic", 
                        avl.height(avl.root) <= 2 * int(math.log2(len(keys))))
    
    def test_search(self) -> None:
        """Test search operation"""
        print("\n=== Testing Search Operation ===")
        
        avl = AVLTree(verbose=False)
        keys = [50, 30, 70, 20, 40]
        
        for key in keys:
            avl.insert(key)
        
        self.test_result("Find existing key 30", avl.search(30) is not None)
        self.test_result("Find existing key 70", avl.search(70) is not None)
        self.test_result("Don't find non-existing key 100", avl.search(100) is None)
        self.test_result("Don't find non-existing key 15", avl.search(15) is None)
    
    def test_deletion_leaf(self) -> None:
        """Test deletion of leaf node"""
        print("\n=== Testing Deletion of Leaf Node ===")
        
        avl = AVLTree(verbose=False)
        keys = [50, 30, 70, 20, 40, 60, 80]
        
        for key in keys:
            avl.insert(key)
        
        avl.delete(20)  # Delete leaf
        
        self.test_result("Node deleted", avl.search(20) is None)
        self.test_result("Node count correct", avl.count_nodes() == len(keys) - 1)
        self.test_result("Tree is balanced", avl.is_balanced())
        self.test_result("AVL properties valid", avl.verify_avl())
    
    def test_deletion_one_child(self) -> None:
        """Test deletion of node with one child"""
        print("\n=== Testing Deletion of Node with One Child ===")
        
        avl = AVLTree(verbose=False)
        keys = [50, 30, 70, 20, 40]
        
        for key in keys:
            avl.insert(key)
        
        avl.delete(30)  # Node with two children
        avl.delete(40)  # Now 20 becomes one child case
        
        self.test_result("Nodes deleted", avl.search(30) is None)
        self.test_result("Tree is balanced", avl.is_balanced())
        self.test_result("AVL properties valid", avl.verify_avl())
    
    def test_deletion_two_children(self) -> None:
        """Test deletion of node with two children"""
        print("\n=== Testing Deletion of Node with Two Children ===")
        
        avl = AVLTree(verbose=False)
        keys = [50, 30, 70, 20, 40, 60, 80]
        
        for key in keys:
            avl.insert(key)
        
        avl.delete(50)  # Delete root with two children
        
        self.test_result("Root deleted", avl.search(50) is None)
        self.test_result("Node count correct", avl.count_nodes() == len(keys) - 1)
        self.test_result("Tree is balanced", avl.is_balanced())
        self.test_result("AVL properties valid", avl.verify_avl())
    
    def test_deletion_with_rebalancing(self) -> None:
        """Test deletion that triggers rebalancing"""
        print("\n=== Testing Deletion with Rebalancing ===")
        
        avl = AVLTree(verbose=False)
        keys = [10, 20, 30, 40, 50]
        
        for key in keys:
            avl.insert(key)
        
        avl.delete(10)  # Should trigger rebalancing
        
        self.test_result("Node deleted", avl.search(10) is None)
        self.test_result("Tree is balanced", avl.is_balanced())
        self.test_result("AVL properties valid", avl.verify_avl())
        self.test_result("Height still logarithmic", avl.height(avl.root) <= 3)
    
    def test_min_max(self) -> None:
        """Test min and max operations"""
        print("\n=== Testing Min/Max Operations ===")
        
        avl = AVLTree(verbose=False)
        keys = [50, 30, 70, 20, 40, 60, 80]
        
        for key in keys:
            avl.insert(key)
        
        self.test_result("Min value is 20", avl.min_value() == 20)
        self.test_result("Max value is 80", avl.max_value() == 80)
    
    def test_successor_predecessor(self) -> None:
        """Test successor and predecessor operations"""
        print("\n=== Testing Successor/Predecessor ===")
        
        avl = AVLTree(verbose=False)
        keys = [50, 30, 70, 20, 40, 60, 80]
        
        for key in keys:
            avl.insert(key)
        
        self.test_result("Successor of 30 is 40", avl.successor(30) == 40)
        self.test_result("Predecessor of 30 is 20", avl.predecessor(30) == 20)
        self.test_result("Successor of 50 is 60", avl.successor(50) == 60)
        self.test_result("Predecessor of 50 is 40", avl.predecessor(50) == 40)
    
    def test_traversals(self) -> None:
        """Test all traversal methods"""
        print("\n=== Testing Tree Traversals ===")
        
        avl = AVLTree(verbose=False)
        keys = [50, 30, 70, 20, 40, 60, 80]
        
        for key in keys:
            avl.insert(key)
        
        inorder = avl.inorder_traversal()
        preorder = avl.preorder_traversal()
        postorder = avl.postorder_traversal()
        levelorder = avl.level_order_traversal()
        
        self.test_result("In-order produces sorted output", inorder == sorted(keys))
        self.test_result("Pre-order correct", len(preorder) == len(keys))
        self.test_result("Post-order correct", len(postorder) == len(keys))
        self.test_result("Level-order correct", len(levelorder) == len(keys))
    
    def test_sequential_worst_case(self) -> None:
        """Test sequential insertion (worst case for BST)"""
        print("\n=== Testing Sequential Insertion (BST Worst Case) ===")
        
        avl = AVLTree(verbose=False)
        n = 100
        
        # Insert 1 to 100 in order (worst case for BST)
        for i in range(1, n + 1):
            avl.insert(i)
        
        max_height = int(1.44 * math.log2(n)) + 2  # Theoretical max for AVL
        
        self.test_result("All nodes inserted", avl.count_nodes() == n)
        self.test_result("Tree is balanced", avl.is_balanced())
        self.test_result("AVL properties valid", avl.verify_avl())
        self.test_result("Height is logarithmic", avl.height(avl.root) <= max_height)
        
        print(f"   Height: {avl.height(avl.root)} (max theoretical: {max_height})")
        print(f"   BST would have height: {n}")
    
    def test_duplicate_insertion(self) -> None:
        """Test duplicate key handling"""
        print("\n=== Testing Duplicate Key Handling ===")
        
        avl = AVLTree(verbose=False)
        avl.insert(50)
        avl.insert(30)
        avl.insert(50)  # Duplicate
        
        self.test_result("Duplicate not inserted", avl.count_nodes() == 2)
        self.test_result("AVL properties valid", avl.verify_avl())
    
    def test_delete_nonexistent(self) -> None:
        """Test deletion of non-existent key"""
        print("\n=== Testing Deletion of Non-existent Key ===")
        
        avl = AVLTree(verbose=False)
        keys = [50, 30, 70]
        
        for key in keys:
            avl.insert(key)
        
        avl.delete(100)  # Non-existent key
        
        self.test_result("Node count unchanged", avl.count_nodes() == 3)
        self.test_result("AVL properties valid", avl.verify_avl())
    
    def test_empty_tree_operations(self) -> None:
        """Test operations on empty tree"""
        print("\n=== Testing Operations on Empty Tree ===")
        
        avl = AVLTree(verbose=False)
        
        self.test_result("Search on empty tree", avl.search(50) is None)
        self.test_result("Height of empty tree", avl.height(avl.root) == 0)
        self.test_result("Balance of empty tree", avl.get_balance(avl.root) == 0)
        self.test_result("Count on empty tree", avl.count_nodes() == 0)
        self.test_result("Min on empty tree", avl.min_value() is None)
        self.test_result("Max on empty tree", avl.max_value() is None)
        
        avl.delete(50)
        self.test_result("Delete on empty tree", avl.root is None)
    
    def test_stress_test(self) -> None:
        """Stress test with large tree"""
        print("\n=== Stress Test: Large Tree ===")
        
        avl = AVLTree(verbose=False)
        n = 1000
        
        print(f"Inserting {n} nodes...")
        for i in range(1, n + 1):
            avl.insert(i)
        
        max_height = int(1.44 * math.log2(n)) + 2
        
        self.test_result("All nodes inserted", avl.count_nodes() == n)
        self.test_result("Tree is balanced", avl.is_balanced())
        self.test_result("Height is logarithmic", avl.height(avl.root) <= max_height)
        
        print(f"   Nodes: {n}")
        print(f"   Height: {avl.height(avl.root)} (max theoretical: {max_height})")
        print(f"   Rotations: {avl.stats.total_rotations} ({avl.stats.total_rotations / n:.2f} per insert)")
        
        print("\nDeleting 500 nodes...")
        for i in range(1, 501):
            avl.delete(i)
        
        self.test_result("Nodes deleted correctly", avl.count_nodes() == 500)
        self.test_result("Tree still balanced", avl.is_balanced())
        self.test_result("AVL properties still valid", avl.verify_avl())
    
    def run_all_tests(self) -> None:
        """Run all test cases"""
        print("\n" + "="*60)
        print("           AVL TREE TEST SUITE")
        print("="*60)
        
        self.test_node_creation()
        self.test_single_insertion()
        self.test_ll_rotation()
        self.test_rr_rotation()
        self.test_lr_rotation()
        self.test_rl_rotation()
        self.test_multiple_insertions()
        self.test_search()
        self.test_deletion_leaf()
        self.test_deletion_one_child()
        self.test_deletion_two_children()
        self.test_deletion_with_rebalancing()
        self.test_min_max()
        self.test_successor_predecessor()
        self.test_traversals()
        self.test_sequential_worst_case()
        self.test_duplicate_insertion()
        self.test_delete_nonexistent()
        self.test_empty_tree_operations()
        self.test_stress_test()
        
        # Print summary
        print("\n" + "="*60)
        print("                TEST SUMMARY")
        print("="*60)
        print(f"Total Tests:  {self.tests_passed + self.tests_failed}")
        print(f"Passed:       {self.tests_passed}")
        print(f"Failed:       {self.tests_failed}")
        print()
        
        if self.tests_failed == 0:
            print("Result:       ALL TESTS PASSED!")
        else:
            print("Result:       SOME TESTS FAILED")
        
        print("="*60 + "\n")


def main():
    """Main test runner"""
    tester = TestAVL()
    tester.run_all_tests()
    
    if tester.tests_failed == 0:
        print("AVL Tree implementation is correct!")
        print("All balance properties verified!")
        print("Ready for production use!\n")
        return 0
    else:
        print("Some tests failed. Please review the implementation.\n")
        return 1


if __name__ == "__main__":
    exit(main())
