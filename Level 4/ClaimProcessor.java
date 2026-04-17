public class ClaimProcessor {
    private static final double CO_PAY_PERCENT = 0.10;

    public double calculateClaim(double totalAmount) {
        return totalAmount * (1 - CO_PAY_PERCENT);
    }
}
/*This class handles the Abstraction of the business rules. 
The main program doesn't need to know how the math works, just that it can call this method. */