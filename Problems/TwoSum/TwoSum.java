package Problems.TwoSum;
import java.util.Arrays;

/**
 * TwoSum
 */
public class TwoSum {
    /*
    public int[] twoSum(int[] nums, int target) {
        // Approach: Brute Force
        // Runtime = O(n^2)
        // Space = O(n)
        
        int size = nums.length;
        int[] ans = new int[2];
        
        for(int i = 0; i < size; i++){
            for(int j = i+1; j < size; j++){
                if(nums[i] + nums[j] == target){
                    ans[0] = i;
                    ans[1] = j;
                    return ans;
                }
            }
        }
        return ans;
    }
    */
    public int[] twoSum(int[] nums, int target){
        // Approach: Two Pointers
        // Runtime: O(nlogn)
        // Space Complexity: O(n)
        
        int front = 0, end = nums.length - 1;
        int[] ans = new int[2];
        int[] sorted = Arrays.copyOf(nums,nums.length);
        
        Arrays.sort(sorted);
        
        while(front < end){
            int sum = sorted[front] + sorted[end];
            
            if(sum == target){
                break;
            } else if(sum < target){
                front++;
            } else{
                end--;
            }
        }
        
        for(int i = 0; i < nums.length; i++){
            if (sorted[front] == nums[i]) {
                ans[0] = i;
            }
        }
        
        //Looping through array backwards
        for(int i = nums.length-1; i >= 0; i--){
            if(sorted[end] == nums[i]){
                ans[1] = i;
            }
        }
        
        return ans;
    }
    
}