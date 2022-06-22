public class Cashier {

    //1357. Apply Discount Every n Orders
    
    int customer = 1;
    int n;
    int discount;
    int[] products;
    int[] prices;
    
    public Cashier(int n, int discount, int[] products, int[] prices) {
        this.n = n;
        this.discount = discount;
        this.products = products;
        this.prices = prices;
    }
    
    public double getBill(int[] product, int[] amount) {
        
        double bill = 0;

        for(int i = 0 ; i < product.length ; i++){
            int price = 0;
            for (int j = 0; j < this.products.length; j++) {
                if(product[i] == this.products[j]) price = this.prices[j];
            }

            //amount[j] * (price of the jth product)
            bill = bill + amount[i]*price;     
        }

        double discountDb = this.discount;
        
        //discount -> bill * ((100 - discount) / 100)
        if(customer % this.n == 0) {
            bill = bill * ((100 - discountDb) / 100);
        }
       
        customer++; 
        return bill;
    }
        

    public static void main(String[] args) {
        // Cashier obj = new Cashier(n, discount, products, prices);
        // double param_1 = obj.getBill(product,amount);
        // System.out.println(param_1);
    }
}
