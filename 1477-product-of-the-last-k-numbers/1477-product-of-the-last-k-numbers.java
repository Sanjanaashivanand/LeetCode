class ProductOfNumbers {
    private ArrayList<Integer> prefix= new ArrayList<>();
    private int size = 0;

    public ProductOfNumbers() {
        this.prefix.add(1);
        this.size=0;
    }
    
    public void add(int num) {
        if(num==0){
            this.prefix= new ArrayList<Integer>();
            this.prefix.add(1);
            this.size = 0;
        }
        else{
            this.prefix.add(this.prefix.get(size) * num);
            this.size++;
        }
    }
    
    public int getProduct(int k) {
        if(k>this.size) return 0;

        return this.prefix.get(this.size) / this.prefix.get(this.size-k);
    }
}

/**
 * Your ProductOfNumbers object will be instantiated and called as such:
 * ProductOfNumbers obj = new ProductOfNumbers();
 * obj.add(num);
 * int param_2 = obj.getProduct(k);
 */