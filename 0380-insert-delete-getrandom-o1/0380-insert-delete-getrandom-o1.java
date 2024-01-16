class RandomizedSet {
    public HashSet<Integer> set;

    public RandomizedSet() {
        set = new HashSet<>();
    }
    
    public boolean insert(int val) {
        return set.add(val);
    }
    
    public boolean remove(int val) {
        return set.remove(val);
        
    }
    
    public int getRandom() {
        int size = set.size();
        int item = new Random().nextInt(size); 
        int i = 0;
        int rand = 0;
        for(int obj : set)
        {
            if (i == item){
                System.out.println(obj);
                return obj;
            }
                
            else{
                i++;
            }
        }
        return 0;
        
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */