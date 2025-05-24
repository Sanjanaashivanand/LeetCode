class UndergroundSystem {
    class Ticket{
        String stationName;
        int t;

        Ticket(String stationName, int t){
            this.stationName = stationName;
            this.t = t;
        }
    }

    HashMap<Integer, Ticket> customers;
    HashMap<String, ArrayList<Integer>> times;

    public UndergroundSystem() {
        customers = new HashMap<>();
        times = new HashMap<>();
    }
    
    public void checkIn(int id, String stationName, int t) {
        customers.put(id, new Ticket(stationName, t));
    }
    
    public void checkOut(int id, String stationName, int t) {
        Ticket checkIn = customers.get(id);
        String route = checkIn.stationName + " to " + stationName; 
        int time = t - checkIn.t;
        if(!times.containsKey(route)){
            times.put(route, new ArrayList<>());
        }
        times.get(route).add(time);
        customers.remove(id);
    }
    
    public double getAverageTime(String startStation, String endStation) {
        String route = startStation + " to " + endStation;
        ArrayList<Integer> hist = times.get(route);
        int sum = 0;
        for(int i : hist){
            sum+=i;
        }
        return (double) sum / hist.size();
    }
}

/**
 * Your UndergroundSystem object will be instantiated and called as such:
 * UndergroundSystem obj = new UndergroundSystem();
 * obj.checkIn(id,stationName,t);
 * obj.checkOut(id,stationName,t);
 * double param_3 = obj.getAverageTime(startStation,endStation);
 */