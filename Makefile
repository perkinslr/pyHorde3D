all: _matrix.so

_matrix.so: matrix.h matrix.cpp
	g++ matrix.cpp -o _matrix.so -O3 -fPIC --shared
