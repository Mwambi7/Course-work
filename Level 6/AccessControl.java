import java.util.Scanner; 

class AccessControl {

    static void checkAccess(String role) throws Exception {
        if (!role.equalsIgnoreCase("doctor")) {
            throw new Exception("Access Denied: Only doctors can view patient personal information.");
        }
    }

    public static void main(String[] args) {
        // Create a Scanner object to read input
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter your role: ");
        String role = scanner.nextLine(); 

        try {
            checkAccess(role); 
            System.out.println("Access Granted: Viewing patient personal information...");
        } catch (Exception e) {
            System.out.println(e.getMessage());
        } finally {
            scanner.close(); 
        }
    }
}