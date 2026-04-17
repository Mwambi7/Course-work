#include <iostream>
using namespace std;

// Procedural logic: Direct calculation
float calculateFare(float distance) {
    float baseFare = 200.0;
    float costPerKm = 50.0;
    return baseFare + (distance * costPerKm);
}

int main() {
    float dist;
    cout << "Enter distance in KM: ";
    cin >> dist;

    float total = calculateFare(dist);
    cout << "Total Fare: KES " << total << endl;

    return 0;
}