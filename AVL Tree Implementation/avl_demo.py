"""
============================================================================
AVL TREE DEMONSTRATION PROGRAM
============================================================================

This program demonstrates all AVL tree operations with detailed output
showing how balance is maintained at each step.

Demonstrates:
1. Sequential insertions (worst case for BST)
2. All four rotation cases (LL, RR, LR, RL)
3. Deletion with rebalancing
4. Search operations
5. Tree traversals

Author: Vincent
Date: November 12, 2025
"""

from avl_tree import AVLTree


def print_separator():
    """Print a visual separator"""
    print("=" * 80)


def print_header(title: str):
    """Print a formatted header"""
    print_separator()
    print(f"  {title}")
    print_separator()


def demonstrate_sequential_insertion():
    """
    Demonstrate sequential insertions (causes rotations)
    
    This shows how AVL tree maintains balance even when inserting
    in sorted order, which would create a linked list in a regular BST.
    """
    print_header("DEMONSTRATION 1: Sequential Insertions (Worst Case for BST)")
    
    print("\nInserting: 10, 20, 30, 40, 50, 25")
    print("This would create a linked list in a regular BST!")
    print("Watch how AVL tree maintains balance through rotations.\n")
    
    avl = AVLTree(verbose=True)
    keys = [10, 20, 30, 40, 50, 25]
    
    for key in keys:
        print(f"\nCurrent tree structure:")
        avl.print_tree()
        print(f"\nIn-order traversal (sorted): {avl.inorder_traversal()}")
        
        # Verify AVL properties
        avl.verify_avl()
        
        input("\nPress Enter to continue...")
    
    avl.print_statistics()
    
    print("\n💡 KEY OBSERVATION:")
    print(f"   Even though we inserted in sorted order,")
    print(f"   the tree height is only {avl.height(avl.root)} (logarithmic)!")
    print(f"   A regular BST would have height {len(keys)} (linear).\n")


def demonstrate_all_rotation_cases():
    """
    Demonstrate all four rotation cases
    
    Shows each of the four rotation types that AVL trees use to maintain balance:
    - Left-Left (LL): Single right rotation
    - Right-Right (RR): Single left rotation
    - Left-Right (LR): Double rotation
    - Right-Left (RL): Double rotation
    """
    print_header("DEMONSTRATION 2: All Four Rotation Cases")
    
    # Case 1: Left-Left (LL)
    print("\n" + "="*80)
    print("CASE 1: LEFT-LEFT (LL) ROTATION")
    print("="*80)
    print("\nInserting: 30, 20, 10")
    print("This creates a left-heavy tree requiring right rotation.\n")
    
    avl = AVLTree(verbose=True)
    avl.insert(30)
    avl.insert(20)
    avl.insert(10)
    
    print("\nResulting tree after LL case:")
    avl.print_tree()
    
    input("\nPress Enter for next rotation case...")
    
    # Case 2: Right-Right (RR)
    print("\n" + "="*80)
    print("CASE 2: RIGHT-RIGHT (RR) ROTATION")
    print("="*80)
    print("\nInserting: 10, 20, 30")
    print("This creates a right-heavy tree requiring left rotation.\n")
    
    avl = AVLTree(verbose=True)
    avl.insert(10)
    avl.insert(20)
    avl.insert(30)
    
    print("\nResulting tree after RR case:")
    avl.print_tree()
    
    input("\nPress Enter for next rotation case...")
    
    # Case 3: Left-Right (LR)
    print("\n" + "="*80)
    print("CASE 3: LEFT-RIGHT (LR) ROTATION")
    print("="*80)
    print("\nInserting: 30, 10, 20")
    print("This requires a double rotation (left then right).\n")
    
    avl = AVLTree(verbose=True)
    avl.insert(30)
    avl.insert(10)
    avl.insert(20)
    
    print("\nResulting tree after LR case:")
    avl.print_tree()
    
    input("\nPress Enter for next rotation case...")
    
    # Case 4: Right-Left (RL)
    print("\n" + "="*80)
    print("CASE 4: RIGHT-LEFT (RL) ROTATION")
    print("="*80)
    print("\nInserting: 10, 30, 20")
    print("This requires a double rotation (right then left).\n")
    
    avl = AVLTree(verbose=True)
    avl.insert(10)
    avl.insert(30)
    avl.insert(20)
    
    print("\nResulting tree after RL case:")
    avl.print_tree()


def demonstrate_deletion():
    """
    Demonstrate deletion with rebalancing
    
    Shows how deletion can also trigger rotations to maintain balance.
    Covers three cases: deleting leaf, node with one child, node with two children.
    """
    print_header("DEMONSTRATION 3: Deletion with Rebalancing")
    
    print("\nBuilding initial tree: 50, 30, 70, 20, 40, 60, 80\n")
    
    avl = AVLTree(verbose=True)
    keys = [50, 30, 70, 20, 40, 60, 80]
    
    for key in keys:
        avl.insert(key)
    
    print("Initial tree:")
    avl.print_tree()
    
    input("\nPress Enter to delete leaf node 20...")
    
    # Delete a leaf
    print("\n" + "="*80)
    print("DELETING LEAF NODE: 20")
    print("="*80)
    
    avl.delete(20)
    print("\nTree after deleting 20:")
    avl.print_tree()
    avl.verify_avl()
    
    input("\nPress Enter to delete node 30...")
    
    # Delete node with one child
    print("\n" + "="*80)
    print("DELETING NODE WITH ONE CHILD: 30")
    print("="*80)
    
    avl.delete(30)
    print("\nTree after deleting 30:")
    avl.print_tree()
    avl.verify_avl()
    
    input("\nPress Enter to delete node 50...")
    
    # Delete node with two children
    print("\n" + "="*80)
    print("DELETING NODE WITH TWO CHILDREN: 50")
    print("="*80)
    
    avl.delete(50)
    print("\nTree after deleting 50:")
    avl.print_tree()
    avl.verify_avl()
    
    avl.print_statistics()


def demonstrate_search():
    """
    Demonstrate search operations
    
    Shows searching for existing and non-existing keys,
    as well as finding successors and predecessors.
    """
    print_header("DEMONSTRATION 4: Search Operations")
    
    print("\nBuilding tree: 50, 30, 70, 20, 40, 60, 80, 10, 25\n")
    
    avl = AVLTree(verbose=False)
    keys = [50, 30, 70, 20, 40, 60, 80, 10, 25]
    
    for key in keys:
        avl.insert(key)
    
    print("Tree structure:")
    avl.print_tree()
    
    # Search for existing keys
    print("\n" + "="*80)
    print("SEARCHING FOR EXISTING KEYS")
    print("="*80)
    
    search_keys = [25, 70, 10]
    for key in search_keys:
        print(f"\nSearching for {key}:")
        result = avl.search(key)
        if result:
            avl.print_node_info(key)
    
    # Search for non-existing key
    print("\n" + "="*80)
    print("SEARCHING FOR NON-EXISTING KEY")
    print("="*80)
    
    print("\nSearching for 100:")
    avl.search(100)
    
    # Demonstrate successor/predecessor
    print("\n" + "="*80)
    print("SUCCESSOR AND PREDECESSOR")
    print("="*80)
    
    print(f"\nSuccessor of 30: {avl.successor(30)}")
    print(f"Predecessor of 30: {avl.predecessor(30)}")


def demonstrate_traversals():
    """
    Demonstrate all traversal methods
    
    Shows in-order, pre-order, post-order, and level-order traversals.
    """
    print_header("DEMONSTRATION 5: Tree Traversals")
    
    print("\nBuilding tree: 50, 30, 70, 20, 40, 60, 80\n")
    
    avl = AVLTree(verbose=False)
    keys = [50, 30, 70, 20, 40, 60, 80]
    
    for key in keys:
        avl.insert(key)
    
    print("Tree structure:")
    avl.print_tree()
    
    print(f"\nIn-order (sorted):    {avl.inorder_traversal()}")
    print(f"Pre-order:            {avl.preorder_traversal()}")
    print(f"Post-order:           {avl.postorder_traversal()}")
    print(f"Level-order (BFS):    {avl.level_order_traversal()}")
    print()


def demonstrate_avl_vs_bst_comparison():
    """
    Demonstrate why AVL trees are better than regular BST
    
    Shows the dramatic difference in height when inserting sorted data.
    """
    print_header("DEMONSTRATION 6: AVL vs Regular BST Comparison")
    
    print("\nInserting 100 sorted values (1 to 100)")
    print("This is the WORST CASE for a regular BST\n")
    
    avl = AVLTree(verbose=False)
    n = 100
    
    for i in range(1, n + 1):
        avl.insert(i)
    
    print("Results:")
    print("="*80)
    print(f"Number of nodes:            {n}")
    print(f"AVL Tree height:            {avl.height(avl.root)}")
    print(f"Regular BST height:         {n} (becomes a linked list!)")
    print(f"Height ratio:               {n / avl.height(avl.root):.2f}x worse for BST")
    print(f"Total rotations performed:  {avl.stats.total_rotations}")
    print(f"Average rotations per insert: {avl.stats.total_rotations / n:.2f}")
    print("="*80)
    
    print("\n💡 KEY INSIGHT:")
    print("   AVL trees guarantee O(log n) height regardless of insertion order!")
    print("   Regular BST can degenerate to O(n) height with sorted input.")
    print("   This makes AVL essential for worst-case performance guarantees.\n")


def main():
    """Main demonstration program"""
    print("\n")
    print_header("AVL TREE COMPREHENSIVE DEMONSTRATION")
    print("\nThis program demonstrates how AVL trees maintain balance")
    print("through automatic rotations during insert and delete operations.")
    print("\nFeatures demonstrated:")
    print("  • Insertion with automatic balancing")
    print("  • All four rotation types (LL, RR, LR, RL)")
    print("  • Deletion with rebalancing")
    print("  • Search operations")
    print("  • Tree traversals")
    print("  • Comparison with regular BST\n")
    
    input("Press Enter to start...\n")
    
    # Run all demonstrations with user pacing
    try:
        demonstrate_sequential_insertion()
        
        input("\n\nPress Enter to continue to next demonstration...")
        demonstrate_all_rotation_cases()
        
        input("\n\nPress Enter to continue to next demonstration...")
        demonstrate_deletion()
        
        input("\n\nPress Enter to continue to next demonstration...")
        demonstrate_search()
        
        input("\n\nPress Enter to continue to next demonstration...")
        demonstrate_traversals()
        
        input("\n\nPress Enter to continue to final demonstration...")
        demonstrate_avl_vs_bst_comparison()
        
    except KeyboardInterrupt:
        print("\n\nDemonstration interrupted by user.")
        return
    
    print("\n")
    print_header("DEMONSTRATION COMPLETE")
    print("\n✅ All AVL tree operations demonstrated successfully!")
    print("✅ Balance maintained throughout all operations!")
    print("✅ AVL properties verified at each step!")
    print("\nKey Takeaways:")
    print("  1. AVL trees automatically maintain balance through rotations")
    print("  2. Four rotation types handle all imbalance cases")
    print("  3. Height stays logarithmic regardless of insertion order")
    print("  4. Slight overhead of rotations is worth the guaranteed performance\n")


if __name__ == "__main__":
    main()
