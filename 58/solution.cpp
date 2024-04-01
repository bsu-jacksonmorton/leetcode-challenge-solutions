class Solution {
public:
	/*
	Runtime: O(n)
	Space: O(1)
	*/
    int lengthOfLastWord(string s) {
        int ans = 0;
        int i = s.length() - 1;
        while(s[i] == ' ')
        {
            i -= 1;
        }
        while(i > -1 && s[i] != ' ')
        {
            ans += 1;
            i -= 1;
        }
        return ans;
    }
};