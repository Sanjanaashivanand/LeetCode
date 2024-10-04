class Solution {
    public long dividePlayers(int[] skill) {
        Arrays.sort(skill);

        int sum = skill[0] + skill[skill.length-1];
        long chem = 0;
        for(int i=0; i<Math.floor(skill.length/2);i++){
            if(skill[i] + skill[skill.length - 1 - i] == sum){
                chem = chem + skill[i]  * skill[skill.length - 1 - i];
            }
            else{
                return -1;
            }
        }

        return chem;
    }
}