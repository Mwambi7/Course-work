
#include <iostream>
#include <string>

using namespace std;

struct Member {
    string name;
    string id;
    double totalSavings;
};

int main() {
    Member m;// object instantiation
    double currentInput;
    m.totalSavings = 0; // Initialize to zero

    // 1. Input Member Details
    cout << "Enter Member Name: ";
    getline(cin, m.name);
    
    cout << "Enter Member ID: ";
    cin >> m.id;

    // 2. Input Contributions for 6 Months
    cout << "\nEnter monthly contributions for the last 6 months:\n";
    for (int i = 1; i <= 6; i++) {
        cout << "Month " << i << ": ";
        cin >> currentInput;
        
        // Add current input to the running total
        m.totalSavings += currentInput;
    }

    // 3. Display Results
    cout << "\n--- Financial Summary ---" << endl;
    cout << "Member: " << m.name << " (" << m.id << ")" << endl;
    cout << "Total Savings: $" << m.totalSavings << endl;

    return 0;
}