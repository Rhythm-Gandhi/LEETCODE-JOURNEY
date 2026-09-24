class Solution {
    public int smallestIndex(int[] nums) {
        for (int i = 0 ; i < nums.length;i++){
            int num = nums[i];
            int summ = 0 ;
            while(num>0){
                summ += num%10;
                num /= 10;
            }
            if (summ == i){
                return i;
            }
        }
        return -1;
    }
}