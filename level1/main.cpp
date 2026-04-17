/*This is login validation program.The username and password are hardcoded.
The user is required to input their username and password which are then validated against the predefined credentials.*/
#include <iostream>
#include <string>
using namespace std;
int main() {
	
	// Predefined credentials
	const string USERNAME = "adminKE";
	const string PASSWORD = "254Secure";
	string userName, inputPassword;
	const int maxAttempts = 3;
	int attempts = 0;
	bool loggedIn = false;

	while (attempts<maxAttempts) {
		// Prompt user for username and password
		cout << "Enter username: ";
		cin >> userName;
		cout << "Enter password: ";
		cin >> inputPassword;

		// Validate credentials
		if (userName == USERNAME && inputPassword == PASSWORD) {
			cout << "Login successful!" << endl;
			loggedIn = true;
			break; // Exit the loop if login is successful
		} else	{
			attempts++;
			cout << "Invalid Credentials! "<<(maxAttempts-attempts)<<" " << "Remaining attempts" << endl;
			
		}
	}// end of while loop
	
	if (!loggedIn) {
		cout << "Your account has been blocked!"<< endl;
	}
	return 0;

		
}