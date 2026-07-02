class Solution {
    public void nextPermutation(int[] nums) {
        int idx = -1;
        for(int i = nums.length-2;i>=0;i--){
            if(nums[i]<nums[i+1]){
                idx = i;
                break;
            }
        }
        if(idx == -1){
            reverse(nums,0,nums.length-1);
            return;
        }
        
        for(int i = nums.length-1; i> idx ; i--){
            if(nums[i]> nums[idx]){
                swap(nums,i,idx);
                break;
            }
        }
        reverse(nums,idx+1,nums.length-1);

    }

    private void reverse(int[] arr , int start, int end ){
        while(start<end){
            swap(arr,start, end);
            start++;
            end--;
        }

    }

    private void swap(int[] arr, int i , int j){
        int temp = arr[i];
        arr[i]= arr[j];
        arr[j] = temp;         
    }
}       