.DEFAULT_GOAL := RUN

foo.o: foo.c
	gcc -c -Wall -Werror -fpic foo.c

libfoo.so: foo.o
	gcc -shared -o libfoo.so foo.o

test: main.c libfoo.so
	gcc -L. -Wall -o test main.c -lfoo

.PHONY: RUN
RUN: test
	export LD_LIBRARY_PATH=pwd
	./test
	python -m doctest -v use.doctest

.PHONY: clean
clean:
	-rm libfoo.so test
