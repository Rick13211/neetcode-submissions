class Solution {
    public boolean isAnagram(String s, String t) {
        int[] sarr = new int[27];
        int[] tarr = new int[27];

        for(int i=0; i<s.length(); i++){
            sarr[s.charAt(i)-'a']++;
            
        }
        for(int i=0; i<t.length(); i++){
            tarr[t.charAt(i)-'a']++;
            
        }
        for(int i=0; i<27; i++){
            if(sarr[i]!=tarr[i])return false;
        }
        return true;
    }
}
