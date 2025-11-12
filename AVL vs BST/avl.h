#ifndef AVL_H
#define AVL_H

#include <time.h>

typedef struct AVLNode { // avl node struc
    int data;
    int height;
    struct AVLNode *left;
    struct AVLNode *right;
} AVLNode;

typedef struct { // metrics
    long comparisons;
    long rotations;
    double time_taken;
    int final_height;
} AVLMetrics;

AVLNode* createAVLNode(int data);
AVLNode* avl_insert(AVLNode* root, int data, AVLMetrics* metrics);
AVLNode* avl_search(AVLNode* root, int data, AVLMetrics* metrics);
AVLNode* avl_delete(AVLNode* root, int data, AVLMetrics* metrics);
int avl_height(AVLNode* root);
void avl_inorder(AVLNode* root);
void freeAVL(AVLNode* root);

#endif