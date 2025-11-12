#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "dataset.h"

void generateRandomData(int arr[], int n) { // gen random dataset
    for (int i = 0; i < n; i++) {
        arr[i] = rand() % 10000;
    }
}

void generateSortedData(int arr[], int n) { // generate sorted data set
    for (int i = 0; i < n; i++) {
        arr[i] = i + 1;
    }
}

void generateReverseSortedData(int arr[], int n) { // generate reverse sorted dataset
    for (int i = 0; i < n; i++) {
        arr[i] = n - i;
    }
}

// generate nearly sorted dataset
void generateNearlySortedData(int arr[], int n, float sorted_percentage) {
    generateSortedData(arr, n);
    
    // shuffle a portion
    int elementsToShuffle = (int)(n * (1.0 - sorted_percentage));
    
    for (int i = 0; i < elementsToShuffle; i++) {
        int idx1 = rand() % n;
        int idx2 = rand() % n;
        
        int temp = arr[idx1];
        arr[idx1] = arr[idx2];
        arr[idx2] = temp;
    }
}

// shuffle array 
void shuffleArray(int arr[], int n) {
    for (int i = n - 1; i > 0; i--) {
        int j = rand() % (i + 1);
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
}