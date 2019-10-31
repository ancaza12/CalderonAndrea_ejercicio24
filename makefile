metro.png : metro.py walk.dat
	python metro.py

metro.dat : metro.x
	./walk.x > walk.dat

metro.x : metro.cpp
	c++ metro.cpp -o metro.x