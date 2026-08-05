class Solution {
public:
    vector<int> sortArray(vector<int>& nums) {
        if (nums.empty()) {
            return nums;
        }

        mergeSort(nums, 0, static_cast<int>(nums.size()) - 1);
        return nums;
    }

private:
    void mergeSort(vector<int>& arr, int l, int r) {
        if (l >= r) {
            return;
        }

        int m = l + (r - l) / 2;

        mergeSort(arr, l, m);
        mergeSort(arr, m + 1, r);
        merge(arr, l, m, r);
    }

    void merge(vector<int>& arr, int l, int m, int r) {
        vector<int> temp;
        temp.reserve(r - l + 1);

        int i = l;
        int j = m + 1;

        while (i <= m && j <= r) {
            if (arr[i] <= arr[j]) {
                temp.push_back(arr[i]);
                i++;
            } else {
                temp.push_back(arr[j]);
                j++;
            }
        }

        while (i <= m) {
            temp.push_back(arr[i]);
            i++;
        }

        while (j <= r) {
            temp.push_back(arr[j]);
            j++;
        }

        for (int k = l; k <= r; k++) {
            arr[k] = temp[k - l];
        }
    }
};