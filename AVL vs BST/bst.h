#ifndef BST_H
#define BST_H

#include <time.h>

typedef struct BSTNode { // BST Node Structure
    int data;
    struct BSTNode *left;
    struct BSTNode *right;
} BSTNode;


typedef struct { // performance metrics structure
    long comparisons;
    double time_taken;
    int final_height;
} Metrics;

BSTNode* createBSTNode(int data); // function prototypes
BSTNode* bst_insert(BSTNode* root, int data, Metrics* metrics);
BSTNode* bst_search(BSTNode* root, int data, Metrics* metrics);
BSTNode* bst_delete(BSTNode* root, int data, Metrics* metrics);
int bst_height(BSTNode* root);
void bst_inorder(BSTNode* root);
void freeBST(BSTNode* root);

#endif