import argparse

def main(arg1, arg2):
    print(arg1, arg2)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('arg1')
    parser.add_argument('arg2')

    args = parser.parse_args()
    main(**vars(args))
