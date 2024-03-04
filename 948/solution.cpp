class Solution {
public:
    /*
        Simple greedy approach to this problem. Each token is worth 1 point to our score if we play it face-up.
        This means that we want to maximize the number of tokens played face-up. In order to do this we need to have enough
        power to play the token. Therefore, we want to play the tokens with the highest power face-down so that we can have
        maximum power to play the lower power tokens face up. 
    */
    int bagOfTokensScore(vector<int>& tokens, int power) {
        int score = 0;
        sort(tokens.begin(), tokens.end());
        int start = 0;
        int end = tokens.size() - 1;
        while(start <= end)
        {
            if(tokens[start] <= power)
            {
                power -= tokens[start];
                score += 1;
                start += 1;
            }
            else if(score > 0 && start != end)
            {
                power += tokens[end];
                score -= 1;
                end -= 1;
            }
            else{
                break;
            }
        }
        return score;
    }
};