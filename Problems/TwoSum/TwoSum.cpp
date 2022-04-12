#include <vector>;
#include <iostream>;
#include <algorithm>;
using namespace std;

/*
Problem Name: Two Sum

Description: 
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

EXAMPLES:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Input: nums = [3,2,4], target = 6
Output: [1,2]
*/

class Solution {
public: 
    vector<int> twoSum(vector<int>& nums, int target) {
        // Approach: Brute Force
        // Run time: O(n^2)
        // Space complexity: O(n)
        
        int length = nums.size();
        for(int i = 0; i < length; i++) {
            for(int j = i+1; j < length; j++) {
                if(nums[i]+nums[j] == target){
                    return {i,j};
                }
            }
        }
        return {-1,-1};
    }
    
    vector<int> twoSum(vector<int>& nums, int target) {
        // Approach: Two Pointers
        // Runtime: O(nlogn)
        // Space Complexity: O(n)
        

        int front = 0;
        int end = nums.size() - 1;
        
        vector<int> sorted = nums;
        sort(sorted.begin(),sorted.end());
        vector<int> ans;
        
        while (front < end) {
            int sum = sorted[front] + sorted[end];
            if (sum == target) {
                break;
            } else if (sum < target) {
                front++;
            } else {
                end--;
            }
        }
        
        for(int i = 0; i < nums.size(); i++){
            if(sorted[front] == nums[i] || sorted[end] == nums[i]){
                ans.push_back(i);
            }
            if(ans.size() == 2){
                break;
            }
        }
        return ans;
    }
};