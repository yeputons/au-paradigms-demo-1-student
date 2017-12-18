#!/usr/bin/env python3

def add(a, b):
    return a + b

def test_add():
    assert add(2, 2) == 4
    assert add(5, 10) == 15

def main():
    print("Hello World")

if __name__ == "__main__":
    main()
