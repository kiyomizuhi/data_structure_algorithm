#include <iostream>
using namespace std;

void bin_sort(int arr[], int n){
    int hd1 = 0;
    int hd2 = n - 1;
    int temp;

    while (hd1 != hd2){
        if (arr[hd1] == 0){
            hd1 += 1;
        } else {
            temp = arr[hd2];
            arr[hd2] = arr[hd1];
            arr[hd1] = temp;
            hd2 -= 1;
        }
    }
}

void print_array(int arr[], int size){
    int i;
    for (i = 0; i < size; i++)
        printf("%d ", arr[i]);
    printf("\n");
}

int main(){
    int arr[] = {0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0};
    int n = sizeof(arr)/sizeof(arr[0]);

    bin_sort(arr, n);
    printf("sorted array: \n");
    print_array(arr, n);
    return 0;
}
