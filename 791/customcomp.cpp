#include <iostream>
#include <unordered_map>
#include <string>

class Solution {
public:
    /*
    Custom comparator approach
    Runtime: O(nlogn);
    Space: O(n);
    */
    std::string customSortString(std::string order, std::string s) {
        std::unordered_map<char, int> m; // Change from std::string to char
        for(int i = 0; i < order.size(); i++)
        {
            m[order[i]] = i; 
        }
        auto comparator = [&](char a, char b)
        {
            int index_a = m.find(a) == m.end() ? order.size() : m[a];
            int index_b = m.find(b) == m.end() ? order.size() : m[b];
            return index_a < index_b;
        };
        sort(s.begin(), s.end(), comparator);
        return s;
    }
};