#include <fstream>
#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

pair<double, double> rotatePoint(double x, double y, double beta) {
    double rad = beta * (3.1415) / 180.0;
    double newX = x * cos(rad) - y * sin(rad);
    double newY = x * sin(rad) + y * cos(rad);
    return make_pair(newX, newY);
}

int main() {
    double Xa, Ya, Xb, Yb, Xo, Yo, beta;

    ifstream inputFile("input.txt");
    inputFile >> Xa >> Ya >> Xb >> Yb >> Xo >> Yo >> beta;
    inputFile.close();

    // поворот точки A
    pair<double, double> rotatedA = rotatePoint(Xa - Xo, Ya - Yo, beta);
    double XaRotated = rotatedA.first + Xo;
    double YaRotated = rotatedA.second + Yo;

    // поворот точки B
    pair<double, double> rotatedB = rotatePoint(Xb - Xo, Yb - Yo, beta);
    double XbRotated = rotatedB.first + Xo;
    double YbRotated = rotatedB.second + Yo;

    ofstream outputFile("output.txt");
    outputFile << fixed << setprecision(3) << XaRotated << " " << YaRotated << endl;
    outputFile << fixed << setprecision(3) << XbRotated << " " << YbRotated << endl;
    outputFile.close();

    return 0;
}
