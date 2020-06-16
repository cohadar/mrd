def main():
    b = 8
    for m in range(4, 19):
        a = b * m
        c = (a - b) // 2
        assert 2 * c == (a - b)
        print(b, a, m)


if __name__ == '__main__':
    main()
