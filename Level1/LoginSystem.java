import java.util.Scanner;

public class LoginSystem {
    public static void main(String[] args) {
        // Predefined credentials
        final String USERNAME = "AdminKE";
        final String PASSWORD = "254Secure";
        
        String inputUserName, inputPassword;
        int maxAttempts = 3;
        int attempts = 0;
        boolean loggedIn = false;

        Scanner scanner = new Scanner(System.in);

        while (attempts < maxAttempts) {
            // Prompt user for username and password
            System.out.print("Enter username: ");
            inputUserName = scanner.nextLine(); // when you use .next() a logical error is encountered.
            
            System.out.print("Enter password: ");
            inputPassword = scanner.nextLine();

            // Validate credentials using .equals() for string comparison
            if (inputUserName.equals(USERNAME) && inputPassword.equals(PASSWORD)) {
                System.out.println("Login successful!");
                loggedIn = true;
                break; // Exit the loop if login is successful
            } else {
                attempts++;
                int remaining = maxAttempts - attempts;
                System.out.println("Invalid Credentials! " + remaining + " Remaining attempts");
            }
        } // end of while loop

        if (!loggedIn) {
            System.out.println("Your account has been blocked!");
        }

        scanner.close(); 
    }
}