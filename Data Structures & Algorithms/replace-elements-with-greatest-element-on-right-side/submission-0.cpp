class Solution {
public:
    vector<int> replaceElements(vector<int>& arr) {
        int n = arr.size(); // get the len of arr
        vector<int> ans(n);

        for (int i = 0; i < n; i++) {
            int rightMax = -1; // because we need to autopilot if not bigger
            for (int j = i + 1; j < n; j++) {
                rightMax = max(rightMax, arr[j]);
            }
            ans[i] = rightMax;
        }
        return ans;
    }
};