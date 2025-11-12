"""
============================================================================
AVL TREE - QUICK START GUIDE
============================================================================

This file provides quick examples of how to use the AVL tree implementation.
Perfect for getting started quickly!

Author: Vincent
Date: November 12, 2025
"""

from avl_tree import AVLTree


def example_1_basic_operations():
    """Example 1: Basic insert, search, delete"""
    print("="*60)
    print("EXAMPLE 1: Basic Operations")
    print("="*60)
    
    # Create an AVL tree
    avl = AVLTree()
    
    # Insert some values
    print("\n1. Inserting values: 50, 30, 70, 20, 40, 60, 80")
    for key in [50, 30, 70, 20, 40, 60, 80]:
        avl.insert(key)
    
    # Search for a value
    print("\n2. Searching for 40:")
    result = avl.search(40)
    print(f"   Found: {result.key if result else 'Not found'}")
    
    # Get sorted values
    print("\n3. In-order traversal (sorted):")
    print(f"   {avl.inorder_traversal()}")
    
    # Delete a value
    print("\n4. Deleting 30")
    avl.delete(30)
    print(f"   After deletion: {avl.inorder_traversal()}")
    
    # Tree info
    print(f"\n5. Tree info:")
    print(f"   Height: {avl.height(avl.root)}")
    print(f"   Node count: {avl.count_nodes()}")
    print(f"   Min value: {avl.min_value()}")
    print(f"   Max value: {avl.max_value()}")


def example_2_visualize_tree():
    """Example 2: Visualize tree structure"""
    print("\n\n" + "="*60)
    print("EXAMPLE 2: Visualize Tree Structure")
    print("="*60)
    
    avl = AVLTree()
    
    print("\nInserting: 50, 30, 70, 20, 40, 60, 80, 10, 25")
    for key in [50, 30, 70, 20, 40, 60, 80, 10, 25]:
        avl.insert(key)
    
    print("\nTree structure (h=height, bf=balance factor):")
    avl.print_tree()


def example_3_watch_rotations():
    """Example 3: Watch rotations in action"""
    print("\n\n" + "="*60)
    print("EXAMPLE 3: Watch Rotations (Verbose Mode)")
    print("="*60)
    
    # Enable verbose mode to see rotation details
    avl = AVLTree(verbose=True)
    
    print("\nInserting 10, 20, 30 (triggers RR rotation):")
    avl.insert(10)
    avl.insert(20)
    avl.insert(30)  # This will trigger a rotation!
    
    print("\nFinal tree:")
    avl.print_tree()


def example_4_avl_vs_bst():
    """Example 4: AVL vs regular BST comparison"""
    print("\n\n" + "="*60)
    print("EXAMPLE 4: Why AVL Trees Matter")
    print("="*60)
    
    avl = AVLTree()
    n = 50
    
    print(f"\nInserting {n} sorted values (1 to {n})")
    print("This is the WORST CASE for a regular BST!\n")
    
    for i in range(1, n + 1):
        avl.insert(i)
    
    print("Results:")
    print(f"  AVL Tree height:      {avl.height(avl.root)}")
    print(f"  Regular BST height:   {n} (becomes a linked list!)")
    print(f"  Height ratio:         {n / avl.height(avl.root):.1f}x worse for BST")
    print(f"\n  AVL rotations needed: {avl.stats.total_rotations}")
    print(f"  Average per insert:   {avl.stats.total_rotations / n:.2f}")
    
    print("\n💡 Key insight: Small rotation cost gives huge performance guarantee!")


def example_5_advanced_operations():
    """Example 5: Advanced operations"""
    print("\n\n" + "="*60)
    print("EXAMPLE 5: Advanced Operations")
    print("="*60)
    
    avl = AVLTree()
    
    print("\nBuilding tree with: 50, 30, 70, 20, 40, 60, 80")
    for key in [50, 30, 70, 20, 40, 60, 80]:
        avl.insert(key)
    
    # Successor and predecessor
    print("\n1. Successor and Predecessor:")
    print(f"   Successor of 30:   {avl.successor(30)}")
    print(f"   Predecessor of 70: {avl.predecessor(70)}")
    
    # Different traversals
    print("\n2. Different Traversals:")
    print(f"   In-order:    {avl.inorder_traversal()}")
    print(f"   Pre-order:   {avl.preorder_traversal()}")
    print(f"   Post-order:  {avl.postorder_traversal()}")
    print(f"   Level-order: {avl.level_order_traversal()}")
    
    # Verify AVL properties
    print("\n3. Verify AVL Properties:")
    is_valid = avl.verify_avl()
    
    # Statistics
    print("\n4. Tree Statistics:")
    avl.print_statistics()


def example_6_real_world_scenario():
    """Example 6: Real-world scenario - maintaining sorted data"""
    print("\n\n" + "="*60)
    print("EXAMPLE 6: Real-World Scenario")
    print("="*60)
    print("\nScenario: Student grade database with fast lookups\n")
    
    avl = AVLTree()
    
    # Simulate student IDs being inserted in random order
    student_ids = [1005, 1002, 1008, 1001, 1006, 1003, 1009, 1004, 1007]
    
    print("1. Adding students to database:")
    for student_id in student_ids:
        avl.insert(student_id)
        print(f"   Added student {student_id}")
    
    print(f"\n2. Database has {avl.count_nodes()} students")
    print(f"   Tree height: {avl.height(avl.root)} (guarantees fast O(log n) lookup)")
    
    print("\n3. Quick lookups:")
    search_id = 1006
    result = avl.search(search_id)
    print(f"   Looking up student {search_id}: {'Found!' if result else 'Not found'}")
    
    print("\n4. Getting all students in sorted order:")
    print(f"   {avl.inorder_traversal()}")
    
    print("\n5. Finding neighboring students:")
    print(f"   Student after 1005: {avl.successor(1005)}")
    print(f"   Student before 1005: {avl.predecessor(1005)}")
    
    print("\n6. Remove a student:")
    avl.delete(1005)
    print(f"   Removed student 1005")
    print(f"   Remaining: {avl.inorder_traversal()}")
    print(f"   Tree automatically rebalanced: {avl.is_balanced()}")


def main():
    """Run all examples"""
    print("\n")
    print("=" * 80)
    print(" " * 25 + "AVL TREE QUICK START")
    print("=" * 80)
    
    print("\nThis guide shows common AVL tree operations with practical examples.")
    print("Each example demonstrates different features of the implementation.\n")
    
    # Run all examples
    example_1_basic_operations()
    example_2_visualize_tree()
    example_3_watch_rotations()
    example_4_avl_vs_bst()
    example_5_advanced_operations()
    example_6_real_world_scenario()
    
    # Final summary
    print("\n\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    print("\n✅ You now know how to:")
    print("   • Create and use AVL trees")
    print("   • Insert, delete, and search for values")
    print("   • Visualize tree structure")
    print("   • Understand why rotations maintain balance")
    print("   • Use advanced operations (successor, predecessor)")
    print("   • Apply AVL trees to real-world problems")
    
    print("\n📚 Next steps:")
    print("   • Run 'python test_avl.py' to see comprehensive tests")
    print("   • Run 'python avl_demo.py' for interactive demonstrations")
    print("   • Read 'README.md' for complete documentation")
    print("   • Explore 'avl_tree.py' to understand the implementation")
    
    print("\n💡 Remember:")
    print("   AVL trees guarantee O(log n) performance for insert/delete/search")
    print("   even in worst-case scenarios where regular BST would degenerate!\n")


if __name__ == "__main__":
    main()
