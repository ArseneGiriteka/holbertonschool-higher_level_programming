#!/usr/bin/python3
import hidden_4


def main():
    names = dir(hidden_4)
    unsorted_names = []
    sorted_names = []
    for name in names:
        if not name.startswith("__"):
            unsorted_names.append(name)

    sorted_names = sorted(unsorted_names)
    for item in sorted_names:
        print(item)


if __name__ == "__main__":
    main()
