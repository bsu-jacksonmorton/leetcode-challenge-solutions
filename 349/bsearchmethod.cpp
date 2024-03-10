class Solution {
public:
    int binary_search(int t, vector<int>& nums)
    {
        int l = 0;
        int r = nums.size() - 1;
        int m;
        while(l <= r)
        {
            m = l + (r - l) / 2;
            if(nums[m] == t)
            {
                return t;
            }
            else if(nums[m] < t)
            {
                l = m + 1;
            }
            else
            {
                r = m - 1;
            }
        }
        return -1;
    }
	/*
		Sort + Binary Search Method.
		Runtime: O(n log n) where n is the maximum size between the two lists
		Space: O(1) excluding the res vector.
	*/
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        if(nums2.size() < nums1.size())
        {
            return intersection(nums2, nums1);
        }
        sort(nums1.begin(), nums1.end());
        sort(nums2.begin(), nums2.end());
        vector<int> res;
        int i = 0;
        int num;
        while(i < nums1.size())
        {
            num = nums1[i];
            if(binary_search(num, nums2) != -1)
            {
              res.push_back(num);
            }
            while(i < nums1.size() && nums1[i] == num)
            {
                i += 1;
            }
        }
        return res;
    }
};