#ifndef DATASET_H
#define DATASET_H

void generateRandomData(int arr[], int n);
void generateSortedData(int arr[], int n);
void generateReverseSortedData(int arr[], int n);
void generateNearlySortedData(int arr[], int n, float sorted_percentage);
void shuffleArray(int arr[], int n);

#endif