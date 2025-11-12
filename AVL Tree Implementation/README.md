# AVL Tree Implementation in Python

## Overview

This is a **complete, production-ready implementation of an AVL tree** (Adelson-Velsky and Landis tree) in Python. AVL trees are **self-balancing binary search trees** that maintain a balanced height through automatic rotations, ensuring O(log n) time complexity for insertion, deletion, and search operations.

## What is an AVL Tree?

An AVL tree is a binary search tree with an additional balance property:
- **For every node**, the heights of its left and right subtrees differ by at most 1
- This property is maintained through **rotations** after insertions and deletions
- **Balance Factor** = height(left subtree) - height(right subtree)
- Valid balance factors: **{-1, 0, 1}**

## Why AVL Trees?

### Problem with Regular BST
Regular Binary Search Trees can degenerate into a linked list when inserting sorted data:
```
Inserting 1, 2, 3, 4, 5 in a regular BST:
    1
     \
      2
       \
        3
         \
          4
           \
            5
Height: O(n) - WORST CASE!
```

### AVL Solution
AVL trees automatically rebalance through rotations:
```
Inserting 1, 2, 3, 4, 5 in an AVL tree:
      2
     / \
    1   4
       / \
      3   5
Height: O(log n) - GUARANTEED!
```

## Features

### Core Operations
✅ **Insertion** - O(log n) time with automatic balancing
✅ **Deletion** - O(log n) time with rebalancing  
✅ **Search** - O(log n) time guaranteed
✅ **Rotations** - Automatic balance maintenance through 4 rotation types

### Rotation Types
1. **Left-Left (LL)** - Single right rotation
2. **Right-Right (RR)** - Single left rotation
3. **Left-Right (LR)** - Double rotation (left then right)
4. **Right-Left (RL)** - Double rotation (right then left)

### Additional Features
- In-order, pre-order, post-order, level-order traversals
- Find minimum and maximum values
- Successor and predecessor operations
- Tree statistics and metrics tracking
- Visual tree structure printing
- Comprehensive verification of AVL properties
- Detailed verbose mode for learning

## Files

| File | Description |
|------|-------------|
| `avl_tree.py` | Main AVL tree implementation with all operations |
| `test_avl.py` | Comprehensive test suite (80+ tests) |
| `avl_demo.py` | Interactive demonstration of all features |
| `README.md` | This file - complete documentation |

## Installation & Requirements

### Requirements
- Python 3.7 or higher
- No external dependencies (uses only Python standard library)

### Installation
```bash
# Clone or download the files to your directory
cd "AVL Tree Implementation"

# No installation needed - pure Python!
```

## Usage

### Quick Start

```python
from avl_tree import AVLTree

# Create an AVL tree
avl = AVLTree()

# Insert values
avl.insert(50)
avl.insert(30)
avl.insert(70)
avl.insert(20)
avl.insert(40)

# Search for a value
node = avl.search(30)
print(f"Found: {node.key}" if node else "Not found")

# Delete a value
avl.delete(30)

# Get sorted values (in-order traversal)
print(f"Sorted: {avl.inorder_traversal()}")

# Print tree structure
avl.print_tree()
```

### Verbose Mode (Learning)

```python
# Enable verbose output to see rotation details
avl = AVLTree(verbose=True)

# Watch the magic happen!
avl.insert(10)
avl.insert(20)
avl.insert(30)  # Triggers RR rotation - you'll see the details!
```

### Running Tests

```bash
# Run comprehensive test suite
python test_avl.py

# Expected output:
# ✅ 80+ tests passed
# ✅ All balance properties verified
# ✅ Ready for production use
```

### Running Demo

```bash
# Interactive demonstration
python avl_demo.py

# Shows:
# - Sequential insertions
# - All rotation cases
# - Deletion with rebalancing
# - Search operations
# - Traversals
# - AVL vs BST comparison
```

## API Reference

### Class: AVLTree

#### Constructor
```python
AVLTree(verbose: bool = False)
```
- `verbose`: Enable detailed operation logging

#### Insertion
```python
insert(key: int) -> None
```
Insert a key into the tree. Automatically maintains balance through rotations.

#### Deletion
```python
delete(key: int) -> None
```
Delete a key from the tree. Rebalances if necessary.

#### Search
```python
search(key: int) -> Optional[AVLNode]
```
Search for a key. Returns the node if found, None otherwise.

#### Utility Methods
```python
min_value() -> Optional[int]                    # Get minimum value
max_value() -> Optional[int]                    # Get maximum value
count_nodes() -> int                            # Count total nodes
successor(key: int) -> Optional[int]            # Find successor
predecessor(key: int) -> Optional[int]          # Find predecessor
```

#### Traversals
```python
inorder_traversal() -> List[int]                # Left-Root-Right (sorted)
preorder_traversal() -> List[int]               # Root-Left-Right
postorder_traversal() -> List[int]              # Left-Right-Root
level_order_traversal() -> List[int]            # Breadth-first
```

#### Visualization
```python
print_tree() -> None                            # Print tree structure
print_node_info(key: int) -> None              # Print node details
print_statistics() -> None                      # Print tree statistics
```

#### Verification
```python
verify_avl() -> bool                            # Verify AVL properties
is_balanced() -> bool                           # Check if balanced
height(node: Optional[AVLNode]) -> int         # Get node height
get_balance(node: Optional[AVLNode]) -> int    # Get balance factor
```

## Understanding Rotations

### Left-Left (LL) Case
**When:** Left subtree is too tall, and imbalance is in left child's left subtree  
**Solution:** Single right rotation

```
    y                    x
   / \                  / \
  x   T3    ===>       T1  y
 / \                      / \
T1  T2                   T2  T3
```

### Right-Right (RR) Case
**When:** Right subtree is too tall, and imbalance is in right child's right subtree  
**Solution:** Single left rotation

```
  x                        y
 / \                      / \
T1  y        ===>        x   T3
   / \                  / \
  T2  T3               T1  T2
```

### Left-Right (LR) Case
**When:** Left subtree is too tall, but imbalance is in left child's right subtree  
**Solution:** Double rotation (left on child, then right on parent)

```
    z           z                y
   / \         / \              / \
  x   T4  =>  y   T4    =>     x   z
 / \         / \              /|   |\
T1  y       x   T3           T1 T2 T3 T4
   / \     / \
  T2  T3  T1  T2
```

### Right-Left (RL) Case
**When:** Right subtree is too tall, but imbalance is in right child's left subtree  
**Solution:** Double rotation (right on child, then left on parent)

```
  x             x                y
 / \           / \              / \
T1  z    =>   T1  y     =>     x   z
   / \           / \          /|   |\
  y   T4        T2  z        T1 T2 T3 T4
 / \               / \
T2  T3            T3  T4
```

## Performance Characteristics

| Operation | Average Case | Worst Case | Explanation |
|-----------|-------------|------------|-------------|
| Insert | O(log n) | O(log n) | Guaranteed by balance property |
| Delete | O(log n) | O(log n) | Guaranteed by balance property |
| Search | O(log n) | O(log n) | Guaranteed by balance property |
| Min/Max | O(log n) | O(log n) | Height-dependent traversal |
| Traversal | O(n) | O(n) | Must visit all nodes |

**Space Complexity:** O(n) for storing n nodes

### Comparison with Regular BST

| Scenario | Regular BST | AVL Tree |
|----------|------------|----------|
| Random insertions | ~O(log n) | O(log n) guaranteed |
| Sorted insertions | O(n) - degenerates! | O(log n) - stays balanced! |
| Worst-case height | n | 1.44 * log₂(n) |
| Rotations overhead | None | ~0.5 per insert average |

## Test Coverage

The test suite (`test_avl.py`) includes 80+ tests covering:

✅ Node creation and basic operations  
✅ All four rotation cases (LL, RR, LR, RL)  
✅ Multiple insertions with automatic balancing  
✅ Search operations (existing and non-existing keys)  
✅ Deletion of leaf nodes  
✅ Deletion of nodes with one child  
✅ Deletion of nodes with two children  
✅ Deletion triggering rebalancing  
✅ Min/Max operations  
✅ Successor/Predecessor operations  
✅ All traversal methods  
✅ Sequential insertions (BST worst case)  
✅ Duplicate key handling  
✅ Empty tree operations  
✅ Stress test with 1000+ nodes  
✅ AVL property verification  

## Educational Value

This implementation is designed for **learning and teaching**:

1. **Detailed Comments** - Every operation is thoroughly documented
2. **Verbose Mode** - See exactly what happens during rotations
3. **Visual Output** - Tree structure printing for understanding
4. **Step-by-Step Demos** - Interactive demonstrations with explanations
5. **Comprehensive Tests** - Learn by seeing all edge cases
6. **Clean Code** - Pythonic, readable, maintainable

## Real-World Applications

AVL trees are used in scenarios requiring **guaranteed fast lookups**:

- **Database indexing** - Ensure O(log n) queries
- **Memory management** - Virtual memory page tables
- **File systems** - Directory structures
- **Network routing** - IP routing tables
- **Compiler symbol tables** - Fast identifier lookup
- **In-memory databases** - Redis, SQLite use similar structures

## Project Context

**Assignment Requirement:**
> "Implement either an AVL tree or a Red-Black tree in your preferred programming language. This involves implementing insertion, deletion, searching, and rotation operations. Emphasize the importance of maintaining balance throughout these operations."

**What This Implementation Provides:**
- ✅ Complete AVL tree implementation
- ✅ All required operations (insert, delete, search, rotations)
- ✅ Emphasis on balance maintenance through verbose logging
- ✅ Comprehensive testing proving correctness
- ✅ Educational demonstrations
- ✅ Production-ready code quality
- ✅ Proper documentation

## Author

**Vincent**  
Data Structures Programming Project  
November 12, 2025

## License

This implementation is for educational purposes.

## References

1. Adelson-Velsky, G.; Landis, E. M. (1962). "An algorithm for the organization of information"
2. Knuth, Donald (1998). "The Art of Computer Programming, Volume 3: Sorting and Searching"
3. Cormen, Thomas H., et al. (2009). "Introduction to Algorithms, Third Edition"

---

**Key Learning Points:**

1. **AVL trees guarantee O(log n) height** through rotations
2. **Four rotation types** handle all imbalance cases
3. **Balance factor** (-1, 0, 1) determines when rotations are needed
4. **Small rotation overhead** is worth the guaranteed performance
5. **Critical for worst-case scenarios** where regular BST fails

---

*For questions or issues, please review the code comments and test cases. Every line is documented to aid understanding.*
