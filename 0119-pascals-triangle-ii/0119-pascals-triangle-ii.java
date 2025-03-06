class Solution {
    public List<Integer> getRow(int rowIndex) {
        List<Integer> res = new ArrayList<Integer>();
        res.add(1);

        for (int i = 0; i < rowIndex; i++) {
            List<Integer> newRow = new ArrayList<>();
            newRow.add(1);
            for (int j = 1; j < res.size(); j++) {
                newRow.add(res.get(j - 1) + res.get(j));
            }
            newRow.add(1);
            res = newRow;
        }


        return res;
    }
}