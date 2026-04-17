import java.util.Scanner;

// The Base
class PricingEngine {
    double baseFare = 200.0, costPerKm = 50.0;
    
    public double calculate(double dist) {
        return baseFare + (dist * costPerKm);
    }
}

// The Extension (Simple Inheritance)
class SurgePricing extends PricingEngine {
    public double calculate(double dist) {
        return super.calculate(dist) * 1.5; // Just adds 50% to the base logic
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter KM: ");
        double km = input.nextDouble();

        PricingEngine normal = new PricingEngine();
        PricingEngine surge = new SurgePricing();

        System.out.println("Normal: " + normal.calculate(km));
        System.out.println("Surge: " + surge.calculate(km));
    }
}