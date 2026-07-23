class Solution {
    public int uniqueXorTriplets(int[] nums) {
        //Set<Integer> un = new HashSet<>();
        int n = nums.length;
        if(n<3){
            return n;
        }
        int d  = Integer.toBinaryString(n).length();
        return (int)Math.pow(2,d);
        
    }
}