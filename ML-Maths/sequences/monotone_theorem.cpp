#include<iostream>
using namespace std;
int main() {
    /* Show a_1 = 1, a_n = a_n-1 * 1/2 converges using the monotone
    convergence theorem: */
    float lim = 1.0f;
    for (int i = 2; i < 20; i++)
    {
        lim = lim/2;
        cout << "limit val = " << lim;
    }
    return 0;
}