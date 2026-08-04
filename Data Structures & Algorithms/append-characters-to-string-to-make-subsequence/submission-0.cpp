class Solution {
public:
    int appendCharacters(string s, string t) {
       /*
         i need to keep the order as well
         so maybe a two pointer would be better
         and then once they don't line up that means you 
         just append the rest to the end of str to end of s.
       */

       int i = 0, j = 0;

       while (i < s.length() && j < t.length()) {
        if (s[i] == t[j]) {
            ++i;
            ++j;
        } else {
            ++i;
        }
       }
       return t.length() - j;
    }
};