public class Main {
    public static void main(String[] args) {
        // Create objects from your other two files
        Patient patient = new Patient("LINET MWAMBI", "NHIF12345");
        ClaimProcessor processor = new ClaimProcessor();

        double bill = 10000.0;
        double nhifAmount = processor.calculateClaim(bill);

        System.out.println("Processing claim for: " + patient.getName());
        System.out.println("NHIF Payout: Ksh " + nhifAmount);
    }
}