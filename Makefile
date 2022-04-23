all: build/2d.gif \
	build/colormap/3d-Cyclic-hsv.png \
	build/3d-own.png \
	build/3d.gif

build/2d.gif: 2d.py | build
	python $^

build/colormap/3d-Cyclic-hsv.png: 3d_colormap.py | mapcolor
	python $^

build/3d-own.png: 3d_own.py | build
	python $^

build/3d.gif: 3d.py | build
	python $^

build:
	mkdir -p build

mapcolor: | build
	mkdir -p build/colormap

clean:
	rm -rf build

.PHONY: all clean