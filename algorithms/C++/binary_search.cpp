#include <iostream>
#include <stdio.h>

using namespace std; 

int binary_search(int arr[], int value, int hight , int low){

    if (low <= hight){
        
        int mid = low + (hight - low)/2;
        if (arr[mid] == value){
            return 1;
        }
        else if (arr[mid] > value)
        {
            /* code */
            return binary_search(arr, value, mid - 1, low);
        }
        else{
            return binary_search(arr, value, hight, mid + 1);
        }
    
        
    }
    else{
        return -1;
    }
}



int main(void){
    int arr[] = {0, 2, 3, 4, 5, 6};
    int x = 4;
    int n = sizeof(arr) / sizeof(arr[0]);
    int result;
    result = binary_search(arr, x,n-1, 0);
    if (result == 1){
        cout<< "value is found!" << endl;
    }else{
        cout << "value is not found!" << endl;
    }
}