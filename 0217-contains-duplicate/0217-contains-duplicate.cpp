class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> hash_map;

        for(int n: nums){
            if(hash_map.find(n) != hash_map.end()){
                return true;
            }
            hash_map.insert(n);
        }
        return false;
    }
};