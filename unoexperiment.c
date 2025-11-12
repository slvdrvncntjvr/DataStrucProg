#include <stdio.h>

typedef struct BSTNode {
    int data;
    struct BSTNode *left;
    struct BSTNode *right;
} BSTNode;

typedef struct AVLNode {
    int data;
    int height;
    struct AVLNode *left;
    struct AVLNode *right;
} AVLNode;

typedef struct {
    long comparisons;
    long rotations;
    double time_taken;
    int final_height;
} PerformanceMetrics;

// Generate different datasets
void generateRandomData(int arr[], int n);
void generateSortedData(int arr[], int n);
void generateReverseSortedData(int arr[], int n);
void generateNearlySortedData(int arr[], int n, float sorted_percentage);

void runExperiment(int dataset[], int size, char* dataset_type) {
    PerformanceMetrics bst_metrics, avl_metrics;
    
    // Test BST
    clock_t start = clock();
    BSTNode* bst_root = NULL;
    for(int i = 0; i < size; i++) {
        bst_root = bst_insert(bst_root, dataset[i], &bst_metrics);
    }
    bst_metrics.time_taken = (double)(clock() - start) // CLOCKS_PER_SEC;
    bst_metrics.final_height = getHeight(bst_root);
    
    // Test AVL
    start = clock();
    AVLNode* avl_root = NULL;
    for(int i = 0; i < size; i++) {
        avl_root = avl_insert(avl_root, dataset[i], &avl_metrics);
    }
    avl_metrics.time_taken = (double)(clock() - start) / CLOCKS_PER_SEC;
    avl_metrics.final_height = getAVLHeight(avl_root);
    
    // Display comparison
    printComparison(dataset_type, &bst_metrics, &avl_metrics, size);
}