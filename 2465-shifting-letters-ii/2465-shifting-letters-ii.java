class Solution {
    public String shiftingLetters(String s, int[][] shifts) {
        int[] linesweep = new int[s.length()];
        int n = s.length();

        for(int[] shift: shifts){
            if(shift[2]==1){
                linesweep[shift[0]]++;
                if(shift[1]+1<n){
                    linesweep[shift[1]+1]--;
                }
            }
            else{
                linesweep[shift[0]]--;
                if(shift[1]+1<n){
                    linesweep[shift[1]+1]++;
                }
            }
        }

        StringBuilder sb = new StringBuilder(s);
        int numberOfShifts = 0;

        for(int i=0; i<n; i++){
            numberOfShifts = (numberOfShifts+linesweep[i])%26;
            if (numberOfShifts < 0) numberOfShifts += 26;
            char shiftedChar = (char) ('a' + ((s.charAt(i) - 'a' + numberOfShifts) % 26));
            sb.setCharAt(i, shiftedChar);
        }

        return sb.toString();
    }
}