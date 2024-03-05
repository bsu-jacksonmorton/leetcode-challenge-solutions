class Solution {
public:
	/*
		Two-pointer approach using iteration.
		Runtime: O(n)
		Space: O(1)
	*/
    int minimumLength(string s) {
        int start = 0;
        int end = s.size() - 1;
        while(start < end && s[start] == s[end])
        {
            char c = s[start];
            while(s[start] == c && start <= end)
            {
                start += 1;
            }
            while(s[end] == c && start <= end)
            {
                end -= 1;
            }
        }
        return end - start + 1;
    }
};