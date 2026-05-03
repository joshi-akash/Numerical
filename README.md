# Numerical_and-_Statistical_Computing

This repository contains simple Python implementations of various numerical methods, designed for beginners and suitable for B.Tech practical exams. Each method is implemented in a separate Python file using only basic Python syntax, without any external libraries.

## Implemented Methods

1. **Bisection Method** (`bisection.py`)  
   Finds the root of the equation \(x^2 - 4 = 0\) in the interval [1, 3] with tolerance 0.001.

2. **Regula Falsi Method** (`regula_falsi.py`)  
   Finds the root of the equation \(x^2 - 4 = 0\) in the interval [1, 3] with tolerance 0.001.

3. **Newton-Raphson Method** (`newton_raphson.py`)  
   Finds the root of the equation \(x^2 - 4 = 0\) starting from initial guess x=3 with tolerance 0.001.

4. **Gauss Elimination Method** (`gauss_elimination.py`)  
   Solves the system of linear equations:  
   2x + y - z = 8  
   -3x - y + 2z = -11  
   -2x + y + 2z = -3

5. **Jacobi Iteration Method** (`jacobi.py`)  
   Solves the same system as above using Jacobi iteration with initial guess [0, 0, 0] and tolerance 0.001.

6. **Gauss-Seidel Iteration Method** (`gauss_seidel.py`)  
   Solves the same system as above using Gauss-Seidel iteration with initial guess [0, 0, 0] and tolerance 0.001.

7. **Newton Forward Interpolation** (`newton_forward.py`)  
   Interpolates the value at x=1.5 using data points: (0,1), (1,2), (2,4), (3,8).

8. **Newton Backward Interpolation** (`newton_backward.py`)  
   Interpolates the value at x=2.5 using the same data points.

## Requirements

- Python 3.x (no external libraries required)

## How to Run

1. Clone or download the repository.
2. Open a terminal in the project directory.
3. Run any program using: `python <filename>.py`

For example:
```
python bisection.py
```

Each program will display iteration details (where applicable) and the final result.

## Author

Bhavishya Badoni

## License

This project is for educational purposes.