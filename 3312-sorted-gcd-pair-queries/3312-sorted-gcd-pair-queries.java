class Solution {
    public int[] gcdValues(int[] nums, long[] queries) {
        int maxVal = 0;
        for (int num : nums) {
            maxVal = Math.max(maxVal, num);
        }
        
        long[] count = new long[maxVal + 1];
        for (int num : nums) {
            count[num]++;
        }
        
        long[] gcdCount = new long[maxVal + 1];
        for (int i = maxVal; i >= 1; i--) {
            long totalMultiples = 0;
            for (int j = i; j <= maxVal; j += i) {
                totalMultiples += count[j];
            }
            
            long pairsWithDivisor = totalMultiples * (totalMultiples - 1) / 2;
            for (int j = 2 * i; j <= maxVal; j += i) {
                pairsWithDivisor -= gcdCount[j];
            }
            
            gcdCount[i] = pairsWithDivisor;
        }
        
        long[] prefixSum = new long[maxVal + 1];
        for (int i = 1; i <= maxVal; i++) {
            prefixSum[i] = prefixSum[i - 1] + gcdCount[i];
        }
        
        int[] ans = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            long targetIndex = queries[i];
            
            int low = 1, high = maxVal, answerGcd = maxVal;
            while (low <= high) {
                int mid = low + (high - low) / 2;
                if (prefixSum[mid] > targetIndex) {
                    answerGcd = mid;
                    high = mid - 1;
                } else {
                    low = mid + 1;
                }
            }
            ans[i] = answerGcd;
        }
        
        return ans;
    }
}