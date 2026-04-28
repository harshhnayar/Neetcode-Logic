class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()){
            return false;
        }

        char[] sS = s.toCharArray();
        char[] tS = t.toCharArray();
        Arrays.sort(sS);
        Arrays.sort(tS);
        return Arrays.equals(sS, tS);
    }
}
