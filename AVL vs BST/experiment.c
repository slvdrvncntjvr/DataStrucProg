#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include "bst.h"
#include "avl.h"
#include "dataset.h"

void printSeparator() {
    printf("========================================\n");
}

void printHeader(char* title) {
    printSeparator();
    printf("%s\n", title);
    printSeparator();
}

void printMetricsComparison(char* datasetType, int size, 
                           Metrics bstMetrics, AVLMetrics avlMetrics) {
    printHeader("PERFORMANCE COMPARISON REPORT");
    printf("Dataset Type: %s\n", datasetType);
    printf("Dataset Size: %d elements\n\n", size);
    
    printf("--- Binary Search Tree (BST) ---\n");
    printf("Final Height:        %d\n", bstMetrics.final_height);
    printf("Total Comparisons:   %ld\n", bstMetrics.comparisons);
    printf("Insertion Time:      %.6f seconds\n\n", bstMetrics.time_taken);
    
    printf("--- AVL Tree (Balanced) ---\n");
    printf("Final Height:        %d\n", avlMetrics.final_height);
    printf("Total Comparisons:   %ld\n", avlMetrics.comparisons);
    printf("Total Rotations:     %ld\n", avlMetrics.rotations);
    printf("Insertion Time:      %.6f seconds\n\n", avlMetrics.time_taken);
    
    printf("--- Analysis ---\n");

    if (bstMetrics.final_height > avlMetrics.final_height) { // height compare
        double heightRatio = (double)bstMetrics.final_height / avlMetrics.final_height;
        printf("BST is %.2fx taller than AVL\n", heightRatio);
    }
    
    // comparison of time (with zero-check)
    if (bstMetrics.time_taken > 0.000001 && avlMetrics.time_taken > 0.000001) {
        if (bstMetrics.time_taken > avlMetrics.time_taken) {
            double speedup = bstMetrics.time_taken / avlMetrics.time_taken;
            printf("AVL is %.2fx faster for insertions\n", speedup);
        } else {
            double speedup = avlMetrics.time_taken / bstMetrics.time_taken;
            printf("BST is %.2fx faster for insertions\n", speedup);
        }
    } else {
        printf("Insertion times too small to measure accurately\n");
    }
    
    if (bstMetrics.comparisons > avlMetrics.comparisons) {
        double compRatio = (double)bstMetrics.comparisons / avlMetrics.comparisons;
        printf("BST made %.2fx more comparisons\n", compRatio);
    }
    
    printf("\n");
}

void runExperiment(int dataset[], int size, char* datasetType) {
    Metrics bstMetrics = {0, 0.0, 0};
    AVLMetrics avlMetrics = {0, 0, 0.0, 0};

    printf("Testing BST with %s data...\n", datasetType);
    BSTNode* bstRoot = NULL;
    clock_t start = clock();
    
    for (int i = 0; i < size; i++) {
        bstRoot = bst_insert(bstRoot, dataset[i], &bstMetrics);
    }
    
    clock_t end = clock();
    bstMetrics.time_taken = (double)(end - start) / CLOCKS_PER_SEC;
    bstMetrics.final_height = bst_height(bstRoot);
    
    printf("Testing AVL with %s data...\n", datasetType);
    AVLNode* avlRoot = NULL;
    start = clock();
    
    for (int i = 0; i < size; i++) {
        avlRoot = avl_insert(avlRoot, dataset[i], &avlMetrics);
    }
    
    end = clock();
    avlMetrics.time_taken = (double)(end - start) / CLOCKS_PER_SEC;
    avlMetrics.final_height = avl_height(avlRoot);
    
    // print the comparison
    printMetricsComparison(datasetType, size, bstMetrics, avlMetrics);
    
    // search test
    printf("--- Search Performance Test ---\n");
    int searchKey = dataset[size / 2]; 
    
    Metrics bstSearchMetrics = {0, 0.0, 0};
    AVLMetrics avlSearchMetrics = {0, 0, 0.0, 0};
    
    start = clock();
    BSTNode* bstResult = bst_search(bstRoot, searchKey, &bstSearchMetrics);
    end = clock();
    double bstSearchTime = (double)(end - start) / CLOCKS_PER_SEC;
    
    start = clock();
    AVLNode* avlResult = avl_search(avlRoot, searchKey, &avlSearchMetrics);
    end = clock();
    double avlSearchTime = (double)(end - start) / CLOCKS_PER_SEC;
    
    printf("Searching for key: %d\n", searchKey);
    printf("BST: %ld comparisons, %.6f seconds, %s\n", 
           bstSearchMetrics.comparisons, bstSearchTime,
           bstResult ? "FOUND" : "NOT FOUND");
    printf("AVL: %ld comparisons, %.6f seconds, %s\n", 
           avlSearchMetrics.comparisons, avlSearchTime,
           avlResult ? "FOUND" : "NOT FOUND");
    
    if (bstSearchMetrics.comparisons > avlSearchMetrics.comparisons) {
        double ratio = (double)bstSearchMetrics.comparisons / avlSearchMetrics.comparisons;
        printf("BST required %.2fx more comparisons for search\n", ratio);
    }
    
    printf("\n");
    printSeparator();
    printf("\n");
    
    freeBST(bstRoot); // free memories
    freeAVL(avlRoot);
}

int main() {
    srand(time(NULL));
    
    int sizes[] = {100, 1000, 5000};
    int numSizes = 3;
    
    printf("\n");
    printHeader("AVL vs BST PERFORMANCE EXPERIMENT");
    printf("This experiment compares the performance of\n");
    printf("balanced (AVL) and unbalanced (BST) trees\n");
    printf("across different dataset scenarios.\n\n");
    
    for (int s = 0; s < numSizes; s++) {
        int size = sizes[s];
        int* dataset = (int*)malloc(size * sizeof(int));
        
        if (dataset == NULL) {
            printf("Memory allocation failed!\n");
            return 1;
        }
        
        printf("\n");
        char sizeHeader[100];
        sprintf(sizeHeader, "DATASET SIZE: %d ELEMENTS", size);
        printHeader(sizeHeader);
        printf("\n");
        
        generateRandomData(dataset, size); // test random data
        runExperiment(dataset, size, "RANDOM");

        generateSortedData(dataset, size); // this time test sorted
        runExperiment(dataset, size, "SORTED (ASCENDING)");
  
        generateReverseSortedData(dataset, size); // this time test reverse
        runExperiment(dataset, size, "REVERSE SORTED (DESCENDING)");
        
        generateNearlySortedData(dataset, size, 0.9); // nearly sorted dataset
        runExperiment(dataset, size, "NEARLY SORTED (90%)");
        
        free(dataset);
    }
    
    printf("\n");
    printHeader("EXPERIMENT COMPLETE");
    
    return 0;
}