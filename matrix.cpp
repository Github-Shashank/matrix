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

        rows = D.size();
        cols = D[0].size();
        for (const vector<int>& v : D) {
            if (v.size() != cols){
                return false;
            }
        }

        ord[0] = rows;
        ord[1] = cols;

        return true;
    }
    void setOrder(int& r,int& c) const;
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
    Matrix operator*(const Matrix& other);
    Matrix operator*(const int& num)const;
    friend Matrix operator*(int num, const Matrix& m) {
        return m * num;
    }
};

pair<int,int> Matrix::getOrd() {
    return {rows, cols};
}

bool Matrix::operator==(const Matrix& other){
    return data == other.data;
}

void Matrix::setOrder(int &r, int &c) const{ 
    r = rows;
    c = cols;
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
Matrix Matrix::operator*(const Matrix& other) {
    int x,y,i,j;
    this->setOrder(x,y);
    other.setOrder(i,j);
    if (cols != other.rows) {
        throw runtime_error("Matrix dimensions do not match for multiplication");
    }
    vector<vector<int>> result(x,vector<int>(j));

    for (int self = 0; self < x; self++) {
        for (int othr = 0; othr < j; othr++) {
            for (int dot = 0; dot < y; dot++) {
                result[self][othr] += data[self][dot]*other.data[dot][othr];
            }
        }
    }
    return Matrix(result);
}

Matrix Matrix::operator*(const int& num) const {
    int x,y;
    this->setOrder(x,y);
    vector<vector<int>> result(x,vector<int>(y));
    for (int r = 0; r < x; r++) {
        for (int c = 0; c < y; c++) {
            result[r][c] = data[r][c]*num;
        }
    }
    return Matrix(result);
}

int main() {
    cout << "Code Started\n";

    vector<vector<int>> v = {
        {1,2,3},
        {4,5,6}//,
        // {7,8,9}
    };

    Matrix m(v);
    m.display();

    vector<vector<int>> b = {
        {7,8},
        {4,5},
        {1,2}
    };

    Matrix a(b);
    a.display();

    auto o = m.getOrd();
    cout << "Matrix Order M: " << o.first << " x " << o.second << endl;

    auto c = a.getOrd();
    cout << "Matrix Order A: " << c.first << " x " << c.second << endl;

    Matrix d;
    // cout << "Sum" << endl;
    // d=a+m;
    // d.display();
    // cout << "Difference" << endl;
    // d=a-m;
    // d.display();
    cout << endl << "a" << endl;
    a.display();
    cout << "m" << endl;
    m.display();
    cout << "Multiply" << endl;
    d = a*m;
    d.display();
    
    cout << "a" << endl;
    a.display();
    d  = a*5;
    d.display();
    d = 5 * a;
    d.display();

    return 0;
}
