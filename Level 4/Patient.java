public class Patient {
    private String name;
    private String policyNumber;

    public Patient(String name, String policyNumber) {
        this.name = name;
        this.policyNumber = policyNumber;
    }

    public String getName() { return name; }
    public String getPolicyNumber() { return policyNumber; }
}
/*This file defines who the patient is
 By keeping this separate, you can reuse the Patient class in other 
 parts of a larger system (like an Appointment or Billing module) 
 without bringing the Claim logic along with it.*/