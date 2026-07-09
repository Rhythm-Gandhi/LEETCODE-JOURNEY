class Solution {
    public int maxProfit(int[] prices) {
        int maxP = 0;
        int min = Integer.MAX_VALUE;

        for(int price : prices){
            if(price<min){
                min = price;
            }
            else{

                maxP = Math.max(maxP,price-min);
            }
        }
        return maxP;
    }
}