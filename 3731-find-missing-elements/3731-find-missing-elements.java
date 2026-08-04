class Solution {
    public List<Integer> findMissingElements(int[] nums) {
        List<Integer> n = new ArrayList<>();
        for (int num : nums) {
            n.add(num);
        }
        
        Collections.sort(n);
        List<Integer> lst = new ArrayList<>();
        
        for (int i = n.get(0); i < n.get(n.size() - 1); i++) {
            if (!n.contains(i)) {
                lst.add(i);
            } else {
                continue;
            }
        }
        
        return lst;
    
    }
}