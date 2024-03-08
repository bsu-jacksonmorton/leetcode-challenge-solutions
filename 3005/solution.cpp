class Solution {
public:
	/*
		Returns the number of total elements that have the maximum frequency in the list.
		My approach uses a simple array of integers to store the frequencies and I maintain a list of members that have the max frequency as I count.
		This allows for a quick and efficient single-pass through the array.
		O(n) - Runtime
		O(1) - Space
	*/
    int maxFrequencyElements(vector<int>& nums) {
        int maxVal = 0;
        int members = 0;
        int count[101] = {0};
        for(auto num : nums)
        {
            count[num] += 1;
            if(maxVal < count[num])
            {
                members = 1;
                maxVal = count[num];
            }
            else if(count[num] == maxVal)
            {
                members += 1;
            }
        }
        return members * maxVal;
    }
};