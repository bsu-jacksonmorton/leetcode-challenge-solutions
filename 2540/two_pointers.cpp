class Solution {
public:
    /*
    Two pointers approach.
    Runtime: O(n + m) where n is the size of list nums1 and m is the size of list nums2.
    Space: O(1)
    */
    int getCommon(vector<int>& nums1, vector<int>& nums2) {
        int i = 0;
        int j = 0;
        while(i < nums1.size() && j < nums2.size())
        {
            if(nums1[i] == nums2[j])
            {
                return nums1[i];
            }
            else if(nums1[i] < nums2[j])
            {
                i += 1;
            }
            else
            {
                j += 1;
            }
        }
        return -1;
    }
};