#include <iostream>
#include <vector>

// Function to perform Cube Sort
void cubeSort(std::vector<int>& arr) {
    int n = arr.size();
    std::vector<int> temp(n);

    // Initialize the temporary array with zeros
    for (int i = 0; i < n; ++i)
        temp[i] = 0;

    // Count the occurrences of each element
    for (int i = 0; i < n; ++i)
        ++temp[arr[i]];

    // Update the array with sorted values
    int index = 0;
    for (int i = 0; i < n; ++i) {
        while (temp[i] > 0) {
            arr[index++] = i;
            --temp[i];
        }
    }
}

int main() {
    std::vector<int> arr = {5, 2, 9, 1, 5, 6};
    cubeSort(arr);

    std::cout << "Sorted array: ";
    for (int num : arr)
        std::cout << num << " ";
    std::cout << std::endl;

    return 0;
}
