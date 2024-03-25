class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
        vector<int> res;
        for(int num : nums)
        {
            int index = abs(num) - 1;
            if(nums[index] < 0)
            {
                res.push_back(abs(num));
            }
            else
            {
                nums[index] = -1 * nums[index];
            }
        }
        return res;
    }
};
