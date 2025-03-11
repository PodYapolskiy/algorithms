#include <vector>
#include <cmath>
#include <iostream>

using namespace std;


class Solution {
    public:
        vector<int> findClosestElements(vector<int>& arr, int k, int x) {
            /*
            Time:  O(n)
            Space: O(k)
            */
            int start = 0, end = arr.size() - 1;
            while (end - start >= k) {
                if (abs(arr[start] - x) <= abs(arr[end] - x)) end--;
                else start++;
            }
            vector<int> result;
            for (int i = start; i <= end; i++) result.push_back(arr[i]);
            return result;
        }
    };


int main() {
    vector<int> arr = {1, 2, 3, 4, 5};
    Solution solution;
    vector<int> result = solution.findClosestElements(arr, 4, 3);
    
    for (int num : result) {
        cout << num << " ";
    }

    return 0;
}