#include <iostream>
#include <vector>
using namespace std;

class Matrix {
private:
    int ord[2]; // order array
public:
    int rows;
    int cols;
    vector<vector<int>> data;

    bool check(const vector<vector<int>>& D) {
        if (D.empty()) return false;

        int c = D[0].size();
        for (const vector<int>& v : D) {
            if (v.size() != c)
                return false;
        }

        rows = D.size();
        cols = c;

        ord[0] = rows;
        ord[1] = cols;

        return true;
    }

    Matrix() = default;

    Matrix(const vector<vector<int>>& v) {
        if (!check(v)) {
            throw runtime_error("Invalid vector");
        }
        data = v;
    }

    void display() const {
        for (const auto& row : data) {
            for (int x : row) {
                cout << x << " ";
            }
            cout << "\n";
        }
        cout << endl;
    }

    pair<int, int> getOrd();
    bool operator==(const Matrix& other);
    Matrix operator+(const Matrix& other);
    Matrix operator-(const Matrix& other);
    // Matrix operator*(const Matrix& other);
};

pair<int,int> Matrix::getOrd() {
    return {rows, cols};
}

bool Matrix::operator==(const Matrix& other){
    return data == other.data;
}

// Addition
Matrix Matrix::operator+(const Matrix& other) {
    if (rows != other.rows || cols != other.cols)
        throw runtime_error("Matrix order mismatch");

    vector<vector<int>> result(rows, vector<int>(cols));

    for (int i = 0; i < rows; i++)
        for (int j = 0; j < cols; j++)
            result[i][j] = data[i][j] + other.data[i][j];

    return Matrix(result);
}

// Subtraction
Matrix Matrix::operator-(const Matrix& other) {
    if (rows != other.rows || cols != other.cols)
        throw runtime_error("Matrix order mismatch");

    vector<vector<int>> result(rows, vector<int>(cols));

    for (int i = 0; i < rows; i++)
        for (int j = 0; j < cols; j++)
            result[i][j] = data[i][j] - other.data[i][j];

    return Matrix(result);
}

// Multiplication
// Matrix Matrix::operator*(const Matrix& other) {
//     if (cols != other.rows) {
//         vector<vector<int>> result(rows, vector<int>(other.cols));
        
//     }
// }

int main() {
    cout << "Code Started\n";

    vector<vector<int>> v = {
        {1,2,3},
        {4,5,6},
        {7,8,9}
    };

    Matrix m(v);
    m.display();

    vector<vector<int>> b = {
        {7,8,9},
        {4,5,6},
        {1,2,3}
    };

    Matrix a(b);
    a.display();

    auto o = m.getOrd();
    cout << "Matrix Order M: " << o.first << " x " << o.second << endl;

    auto c = a.getOrd();
    cout << "Matrix Order A: " << c.first << " x " << c.second << endl;

    Matrix d;
    cout << "Sum" << endl;
    d=a+m;
    d.display();
    cout << "Difference" << endl;
    d=a-m;
    d.display();

    return 0;
}
