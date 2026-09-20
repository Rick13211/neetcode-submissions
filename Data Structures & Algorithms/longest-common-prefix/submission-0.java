class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs == null || strs.length == 0) return "";
        String ref = strs[0];
        for (int ind = 1; ind < strs.length; ind++) {
            String current = strs[ind];
            StringBuilder common = new StringBuilder();
            int i = 0, j = 0;
            while (i < ref.length() && j < current.length() && ref.charAt(i) == current.charAt(j)) {
                common.append(ref.charAt(i));
                i++;
                j++;
            }
            ref = common.toString();
            if (ref.isEmpty()) return "";
        }
        return ref;
    }
}