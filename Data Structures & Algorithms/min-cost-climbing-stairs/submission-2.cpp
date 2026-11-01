class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        /* cost[i] = cost of taking a step.
        after paying you can do i+1th or i+2 floor.
        You can choose to start form index 0 or index 1
        return min cost to reach top stair case just past the last index in cost.
        */
        for (int i = cost.size() - 3; i >= 0; --i) {
            cost[i] += min(cost[i+1], cost[i+2]);
        }

        return min(cost[0], cost[1]);

    }
};
