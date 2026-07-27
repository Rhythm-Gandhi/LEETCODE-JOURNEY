class Solution {
    public int maxProduct(int[] nums) {
        int maxi = Integer.MIN_VALUE;
        for(int i =0;i<nums.length;i++){
            for(int j = i+1;j<nums.length;j++){
                int x = (nums[i]-1)*(nums[j]-1);
                maxi = Math.max(maxi,x);
            }
        }
        return maxi;
    }
}