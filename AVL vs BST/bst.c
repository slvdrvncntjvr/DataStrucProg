#include <stdio.h>
#include <stdlib.h>
#include "bst.h"


BSTNode* createBSTNode(int data) { // create a new BST node
    BSTNode* newNode = (BSTNode*)malloc(sizeof(BSTNode));
    if (newNode == NULL) {
        printf("Memory allocation failed!\n");
        exit(1);
    }
    newNode->data = data;
    newNode->left = NULL;
    newNode->right = NULL;
    return newNode;
}

BSTNode* bst_insert(BSTNode* root, int data, Metrics* metrics) { // insert into BST
    if (root == NULL) {
        return createBSTNode(data);
    }
    
    metrics->comparisons++;
    
    if (data < root->data) {
        root->left = bst_insert(root->left, data, metrics);
    } else if (data > root->data) {
        root->right = bst_insert(root->right, data, metrics);
    }
    
    return root;
}

BSTNode* bst_search(BSTNode* root, int data, Metrics* metrics) { // search
    if (root == NULL) {
        return NULL;
    }
    
    metrics->comparisons++;
    
    if (data == root->data) {
        return root;
    } else if (data < root->data) {
        return bst_search(root->left, data, metrics);
    } else {
        return bst_search(root->right, data, metrics);
    }
}

BSTNode* findMin(BSTNode* root) { // find minimum
    while (root->left != NULL) {
        root = root->left;
    }
    return root;
}

BSTNode* bst_delete(BSTNode* root, int data, Metrics* metrics) { // deletion
    if (root == NULL) {
        return NULL;
    }
    
    metrics->comparisons++;
    
    if (data < root->data) {
        root->left = bst_delete(root->left, data, metrics);
    } else if (data > root->data) {
        root->right = bst_delete(root->right, data, metrics);
    } else {
        // node found - delete it
        if (root->left == NULL) {
            BSTNode* temp = root->right;
            free(root);
            return temp;
        } else if (root->right == NULL) {
            BSTNode* temp = root->left;
            free(root);
            return temp;
        }
        
        // node with two children
        BSTNode* temp = findMin(root->right);
        root->data = temp->data;
        root->right = bst_delete(root->right, temp->data, metrics);
    }
    
    return root;
}

int bst_height(BSTNode* root) {
    if (root == NULL) {
        return 0;
    }
    
    int leftHeight = bst_height(root->left);
    int rightHeight = bst_height(root->right);
    
    return (leftHeight > rightHeight ? leftHeight : rightHeight) + 1;
}

void bst_inorder(BSTNode* root) { //inorder
    if (root != NULL) {
        bst_inorder(root->left);
        printf("%d ", root->data);
        bst_inorder(root->right);
    }
}

void freeBST(BSTNode* root) { //free memory
    if (root != NULL) {
        freeBST(root->left);
        freeBST(root->right);
        free(root);
    }
}