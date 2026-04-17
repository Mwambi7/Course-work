#include <iostream>
#include <string>

using namespace std;

string getAdvisory(double rainfall, double temperature) {
    // Nested if-else for range-based logic
    if (rainfall < 200) {
        return "Advisory: Irrigation Required";
    } 
    else {
        // This block only runs if rainfall >= 200
        if (temperature > 30) {
            return "Advisory: Monitor Soil";
        } 
        else {
            return "Advisory: Normal Conditions";
        }
    }
}

int main() {
    double rain, temp;

    cout << "Machakos Weather System" << endl;
    cout << "-----------------------" << endl;
    cout << "Enter Rainfall (mm): ";
    cin >> rain;
    cout << "Enter Temperature (C): ";
    cin >> temp;

    cout << getAdvisory(rain, temp) << endl;

    return 0;
}