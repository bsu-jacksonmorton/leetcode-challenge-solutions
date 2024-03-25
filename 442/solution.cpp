class Solution {
public:
    /*
        We can use the same linked list approach as the find duplicate problem.
        Due to the fact that each element can only appear twice, we can keep track
        of elements we have seen by negating elements the first time we visit them.
        Upon revisitation, we can check if the element has previously been negated and
        if it has we can add it to our ans list.
    Runtime: O(n)
Space: O(1)
    */
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
