#include <iostream>
#include <unordered_map>
#include <string>

class Solution {
public:
    /*
    Frequency counter approach
    Runtime: O(n);
    Space: O(1) (we can use a constant buffer of size 26 since its all lower case letters.);
    */
    std::string customSortString(std::string order, std::string s) {
        std::string retVal;
        char buffer[26] = {0};
        for(auto c : s)
        {
            buffer[c-'a'] += 1;
        }
        for(auto c : order)
        {
            for(int i = 0; i < buffer[c-'a']; i++)
            {
                retVal.push_back(c);
            }
            buffer[c-'a'] = 0;
        }
        for(auto c : s)
        {
            for(int i = 0; i < buffer[c-'a']; i++)
            {
                retVal.push_back(c);
            }
            buffer[c-'a'] = 0;
        }
        return retVal;
    }
};