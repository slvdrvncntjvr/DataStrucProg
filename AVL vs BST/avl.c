#include <stdio.h>
#include <stdlib.h>
#include "avl.h"

AVLNode* createAVLNode(int data) {
    AVLNode* newNode = (AVLNode*)malloc(sizeof(AVLNode)); // new avl node
    if (newNode == NULL) {
        printf("Memory allocation failed!\n");
        exit(1);
    }
    newNode->data = data;
    newNode->height = 1;
    newNode->left = NULL;
    newNode->right = NULL;
    return newNode;
}

int height(AVLNode* node) { // get height of node
    if (node == NULL) {
        return 0;
    }
    return node->height;
}

int maxHeight(int a, int b) {
    return (a > b) ? a : b;
}

int getBalance(AVLNode* node) { // balance calculation
    if (node == NULL) {
        return 0;
    }
    return height(node->left) - height(node->right);
}


AVLNode* rightRotate(AVLNode* y, AVLMetrics* metrics) {
    AVLNode* x = y->left;
    AVLNode* T2 = x->right;
    
    x->right = y;
    y->left = T2;
    
    y->height = maxHeight(height(y->left), height(y->right)) + 1;
    x->height = maxHeight(height(x->left), height(x->right)) + 1;
    
    metrics->rotations++;
    
    return x;
}

AVLNode* leftRotate(AVLNode* x, AVLMetrics* metrics) {
    AVLNode* y = x->right;
    AVLNode* T2 = y->left;

    y->left = x;
    x->right = T2;

    x->height = maxHeight(height(x->left), height(x->right)) + 1;
    y->height = maxHeight(height(y->left), height(y->right)) + 1;
    
    metrics->rotations++;
    
    return y;
}

AVLNode* avl_insert(AVLNode* root, int data, AVLMetrics* metrics) { // insert into avl
    // BST insertion
    if (root == NULL) {
        return createAVLNode(data);
    }
    
    metrics->comparisons++;
    
    if (data < root->data) {
        root->left = avl_insert(root->left, data, metrics);
    } else if (data > root->data) {
        root->right = avl_insert(root->right, data, metrics);
    } else {
        return root; 
    }
    
    root->height = 1 + maxHeight(height(root->left), height(root->right));
    
    int balance = getBalance(root);
    
    if (balance > 1 && data < root->left->data) {
        return rightRotate(root, metrics);
    }

    if (balance < -1 && data > root->right->data) {
        return leftRotate(root, metrics);
    }
    
    if (balance > 1 && data > root->left->data) {
        root->left = leftRotate(root->left, metrics);
        return rightRotate(root, metrics);
    }

    if (balance < -1 && data < root->right->data) {
        root->right = rightRotate(root->right, metrics);
        return leftRotate(root, metrics);
    }
    
    return root;
}

AVLNode* avl_search(AVLNode* root, int data, AVLMetrics* metrics) {
    if (root == NULL) {
        return NULL;
    }
    
    metrics->comparisons++;
    
    if (data == root->data) {
        return root;
    } else if (data < root->data) {
        return avl_search(root->left, data, metrics);
    } else {
        return avl_search(root->right, data, metrics);
    }
}

AVLNode* minValueNode(AVLNode* root) { // get the minimum value
    AVLNode* current = root;
    while (current->left != NULL) {
        current = current->left;
    }
    return current;
}

AVLNode* avl_delete(AVLNode* root, int data, AVLMetrics* metrics) { // delete
    if (root == NULL) {
        return root;
    }
    
    metrics->comparisons++;
    
    if (data < root->data) { // peform bst standard deletion
        root->left = avl_delete(root->left, data, metrics);
    } else if (data > root->data) {
        root->right = avl_delete(root->right, data, metrics);
    } else {
        if ((root->left == NULL) || (root->right == NULL)) {
            AVLNode* temp = root->left ? root->left : root->right;
            
            if (temp == NULL) {
                temp = root;
                root = NULL;
            } else {
                *root = *temp;
            }
            free(temp);
        } else {
            AVLNode* temp = minValueNode(root->right);
            root->data = temp->data;
            root->right = avl_delete(root->right, temp->data, metrics);
        }
    }
    
    if (root == NULL) {
        return root;
    }
    
    root->height = 1 + maxHeight(height(root->left), height(root->right)); // update height
    
    int balance = getBalance(root); // get balance factor
    

    if (balance > 1 && getBalance(root->left) >= 0) { // different cases
        return rightRotate(root, metrics);
    }
    
    if (balance > 1 && getBalance(root->left) < 0) {
        root->left = leftRotate(root->left, metrics);
        return rightRotate(root, metrics);
    }
    
    if (balance < -1 && getBalance(root->right) <= 0) {
        return leftRotate(root, metrics);
    }

    if (balance < -1 && getBalance(root->right) > 0) {
        root->right = rightRotate(root->right, metrics);
        return leftRotate(root, metrics);
    }
    
    return root;
}

int avl_height(AVLNode* root) {
    return height(root);
}

void avl_inorder(AVLNode* root) { // inorder traversal
    if (root != NULL) {
        avl_inorder(root->left);
        printf("%d ", root->data);
        avl_inorder(root->right);
    }
}

void freeAVL(AVLNode* root) { // free memory
    if (root != NULL) {
        freeAVL(root->left);
        freeAVL(root->right);
        free(root);
    }
}