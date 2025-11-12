"""
AVL Tree Traversal Demonstration

This program demonstrates the three main tree traversal methods:
1. In-order Traversal (Left-Root-Right) - Produces sorted output
2. Pre-order Traversal (Root-Left-Right) - Useful for copying tree
3. Post-order Traversal (Left-Right-Root) - Useful for deleting tree

Also includes: Level-order Traversal (Breadth-First) - Visits nodes level by level
"""

from avl_tree import AVLTree


def print_separator(title: str) -> None:
    """Print a formatted separator with title"""
    print("\n" + "="*70)
    print(f"  {title}")
    print("="*70)


def visualize_tree_structure(avl: AVLTree) -> None:
    """Print the tree structure"""
    print("\nTree Structure (rotated 90 clockwise):")
    print("Format: [key(h=height, bf=balance_factor)]")
    print("-" * 70)
    avl.print_tree()
    print("-" * 70)


def demo_basic_traversals():
    """Demonstrate basic tree traversals on a simple balanced tree"""
    print_separator("BASIC TRAVERSAL DEMONSTRATION")
    
    print("\nCreating AVL Tree with values: [50, 30, 70, 20, 40, 60, 80]")
    avl = AVLTree(verbose=False)
    
    keys = [50, 30, 70, 20, 40, 60, 80]
    for key in keys:
        avl.insert(key)
    
    visualize_tree_structure(avl)
    
    # In-order traversal
    print("\n1  IN-ORDER TRAVERSAL (Left-Root-Right)")
    print("   Purpose: Visits nodes in sorted order")
    print("   Process: Visit left subtree  Visit root  Visit right subtree")
    inorder = avl.inorder_traversal()
    print(f"   Result:  {inorder}")
    print(f"    Notice: Values are in SORTED order!")
    
    # Pre-order traversal
    print("\n2  PRE-ORDER TRAVERSAL (Root-Left-Right)")
    print("   Purpose: Useful for copying/serializing tree structure")
    print("   Process: Visit root  Visit left subtree  Visit right subtree")
    preorder = avl.preorder_traversal()
    print(f"   Result:  {preorder}")
    print(f"    Notice: Root (50) comes FIRST!")
    
    # Post-order traversal
    print("\n3  POST-ORDER TRAVERSAL (Left-Right-Root)")
    print("   Purpose: Useful for deleting tree (delete children before parent)")
    print("   Process: Visit left subtree  Visit right subtree  Visit root")
    postorder = avl.postorder_traversal()
    print(f"   Result:  {postorder}")
    print(f"    Notice: Root (50) comes LAST!")
    
    # Level-order traversal (Bonus)
    print("\n  LEVEL-ORDER TRAVERSAL (Breadth-First)")
    print("   Purpose: Visit nodes level by level from top to bottom")
    print("   Process: Use queue to visit nodes at each level")
    levelorder = avl.level_order_traversal()
    print(f"   Result:  {levelorder}")
    print(f"    Notice: Nodes visited level by level!")


def demo_complex_tree():
    """Demonstrate traversals on a more complex tree"""
    print_separator("COMPLEX TREE TRAVERSAL DEMONSTRATION")
    
    print("\n Creating AVL Tree with values: [100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 90]")
    avl = AVLTree(verbose=False)
    
    keys = [100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 90]
    for key in keys:
        avl.insert(key)
    
    visualize_tree_structure(avl)
    
    print("\n All Traversal Results:")
    print("" * 70)
    
    inorder = avl.inorder_traversal()
    print(f"In-order:     {inorder}")
    
    preorder = avl.preorder_traversal()
    print(f"Pre-order:    {preorder}")
    
    postorder = avl.postorder_traversal()
    print(f"Post-order:   {postorder}")
    
    levelorder = avl.level_order_traversal()
    print(f"Level-order:  {levelorder}")


def demo_traversal_step_by_step():
    """Show step-by-step traversal process"""
    print_separator("STEP-BY-STEP TRAVERSAL VISUALIZATION")
    
    print("\n Creating a simple tree with values: [20, 10, 30]")
    avl = AVLTree(verbose=False)
    
    for key in [20, 10, 30]:
        avl.insert(key)
    
    print("""
Tree Structure:
        
        20
       /  \\
      10   30

Let's trace each traversal:
""")
    
    print("" * 70)
    print("IN-ORDER (Left-Root-Right):")
    print("  Step 1: Visit left subtree of 20  Go to 10")
    print("  Step 2: 10 has no left child, visit 10  Output: 10")
    print("  Step 3: 10 has no right child, back to 20")
    print("  Step 4: Visit root 20  Output: 20")
    print("  Step 5: Visit right subtree of 20  Go to 30")
    print("  Step 6: 30 has no left child, visit 30  Output: 30")
    print("  Step 7: 30 has no right child, done!")
    print(f"  Result: {avl.inorder_traversal()}")
    
    print("\n" * 70)
    print("PRE-ORDER (Root-Left-Right):")
    print("  Step 1: Visit root 20  Output: 20")
    print("  Step 2: Visit left subtree of 20  Go to 10")
    print("  Step 3: Visit 10  Output: 10")
    print("  Step 4: 10 has no children, back to 20")
    print("  Step 5: Visit right subtree of 20  Go to 30")
    print("  Step 6: Visit 30  Output: 30")
    print("  Step 7: 30 has no children, done!")
    print(f"  Result: {avl.preorder_traversal()}")
    
    print("\n" * 70)
    print("POST-ORDER (Left-Right-Root):")
    print("  Step 1: Visit left subtree of 20  Go to 10")
    print("  Step 2: 10 has no children, visit 10  Output: 10")
    print("  Step 3: Back to 20, now visit right subtree  Go to 30")
    print("  Step 4: 30 has no children, visit 30  Output: 30")
    print("  Step 5: Back to 20, now visit root 20  Output: 20")
    print("  Step 6: Done!")
    print(f"  Result: {avl.postorder_traversal()}")


def demo_traversal_applications():
    """Demonstrate practical applications of traversals"""
    print_separator("PRACTICAL APPLICATIONS OF TRAVERSALS")
    
    avl = AVLTree(verbose=False)
    keys = [50, 30, 70, 20, 40, 60, 80]
    for key in keys:
        avl.insert(key)
    
    print("\n APPLICATION 1: Getting Sorted Data")
    print("   Use Case: Export tree data in sorted order")
    print("   Method: In-order traversal")
    sorted_data = avl.inorder_traversal()
    print(f"   Sorted data: {sorted_data}")
    
    print("\n APPLICATION 2: Serializing Tree Structure")
    print("   Use Case: Save tree to file or transmit over network")
    print("   Method: Pre-order traversal (stores tree structure)")
    preorder_data = avl.preorder_traversal()
    print(f"   Serialized: {preorder_data}")
    print("    Tip: Can reconstruct tree from pre-order + in-order")
    
    print("\n APPLICATION 3: Safe Tree Deletion")
    print("   Use Case: Delete all nodes without memory leaks")
    print("   Method: Post-order traversal (delete children first)")
    postorder_data = avl.postorder_traversal()
    print(f"   Deletion order: {postorder_data}")
    print("    Tip: Deletes children before parent (no dangling pointers)")
    
    print("\n APPLICATION 4: Level-wise Processing")
    print("   Use Case: Print tree level by level, find shortest path")
    print("   Method: Level-order traversal (Breadth-First)")
    levelorder_data = avl.level_order_traversal()
    print(f"   Level-order: {levelorder_data}")
    print("    Tip: Useful for finding closest nodes or minimum depth")


def demo_comparison():
    """Compare all traversal methods side by side"""
    print_separator("TRAVERSAL METHOD COMPARISON")
    
    avl = AVLTree(verbose=False)
    keys = [40, 20, 60, 10, 30, 50, 70]
    for key in keys:
        avl.insert(key)
    
    visualize_tree_structure(avl)
    
    print("\n COMPARISON TABLE")
    print("" * 70)
    print(f"{'Method':<15} {'Order':<20} {'First Node':<12} {'Last Node':<12}")
    print("" * 70)
    
    inorder = avl.inorder_traversal()
    preorder = avl.preorder_traversal()
    postorder = avl.postorder_traversal()
    levelorder = avl.level_order_traversal()
    
    print(f"{'In-order':<15} {'Left-Root-Right':<20} {inorder[0]:<12} {inorder[-1]:<12}")
    print(f"{'Pre-order':<15} {'Root-Left-Right':<20} {preorder[0]:<12} {preorder[-1]:<12}")
    print(f"{'Post-order':<15} {'Left-Right-Root':<20} {postorder[0]:<12} {postorder[-1]:<12}")
    print(f"{'Level-order':<15} {'Level-by-level':<20} {levelorder[0]:<12} {levelorder[-1]:<12}")
    print("" * 70)
    
    print("\n KEY CHARACTERISTICS:")
    print("   In-order:    Always produces SORTED output")
    print("   Pre-order:   Root always comes FIRST")
    print("   Post-order:  Root always comes LAST")
    print("   Level-order: Visits by DEPTH (breadth-first)")


def demo_verification():
    """Verify traversal correctness"""
    print_separator("TRAVERSAL VERIFICATION")
    
    print("\n Creating tree and verifying traversal properties...")
    avl = AVLTree(verbose=False)
    
    import random
    keys = random.sample(range(1, 101), 15)
    print(f"\n Inserting 15 random values: {keys}")
    
    for key in keys:
        avl.insert(key)
    
    inorder = avl.inorder_traversal()
    preorder = avl.preorder_traversal()
    postorder = avl.postorder_traversal()
    levelorder = avl.level_order_traversal()
    
    print("\n VERIFICATION RESULTS:")
    print("" * 70)
    
    # Check 1: All traversals have same number of nodes
    all_same_length = len(inorder) == len(preorder) == len(postorder) == len(levelorder) == len(keys)
    print(f"   All traversals visit all nodes: {all_same_length}")
    
    # Check 2: In-order produces sorted output
    is_sorted = inorder == sorted(keys)
    print(f"   In-order produces sorted output: {is_sorted}")
    
    # Check 3: All traversals contain same elements
    same_elements = set(inorder) == set(preorder) == set(postorder) == set(levelorder)
    print(f"   All traversals contain same elements: {same_elements}")
    
    # Check 4: Root is first in pre-order
    root_first_preorder = preorder[0] == avl.root.key
    print(f"   Root is first in pre-order: {root_first_preorder}")
    
    # Check 5: Root is last in post-order
    root_last_postorder = postorder[-1] == avl.root.key
    print(f"   Root is last in post-order: {root_last_postorder}")
    
    print("\n Traversal Results:")
    print(f"  In-order:    {inorder}")
    print(f"  Pre-order:   {preorder}")
    print(f"  Post-order:  {postorder}")
    print(f"  Level-order: {levelorder}")


def main():
    """Main demonstration runner"""
    print("\n" + "" + "="*68 + "")
    print("" + " "*15 + "AVL TREE TRAVERSAL METHODS" + " "*27 + "")
    print("" + " "*68 + "")
    print("" + "  This demo showcases the three main tree traversal methods:" + " "*8 + "")
    print("" + "   In-order (Left-Root-Right) - Sorted output" + " "*23 + "")
    print("" + "   Pre-order (Root-Left-Right) - Structure preservation" + " "*13 + "")
    print("" + "   Post-order (Left-Right-Root) - Safe deletion" + " "*21 + "")
    print("" + "   Level-order (Bonus) - Breadth-first traversal" + " "*20 + "")
    print("" + "="*68 + "")
    
    # Run all demonstrations
    demo_basic_traversals()
    demo_complex_tree()
    demo_traversal_step_by_step()
    demo_traversal_applications()
    demo_comparison()
    demo_verification()
    
    print("\n" + "="*70)
    print("   ALL TRAVERSAL DEMONSTRATIONS COMPLETED!")
    print("="*70)
    print("\n Key Takeaways:")
    print("  1. In-order traversal gives sorted output (BST property)")
    print("  2. Pre-order is useful for copying/serializing trees")
    print("  3. Post-order is useful for safe tree deletion")
    print("  4. Level-order visits nodes level by level (BFS)")
    print("  5. All traversals visit every node exactly once")
    print("\n Your AVL tree has fully functional traversal methods!\n")


if __name__ == "__main__":
    main()
