from .util import running
import argparse

def main():
    parser = argparse.ArgumentParser(description="UEST Transport Assignment system")
    parser.add_argument("-n", help="network file")
    parser.add_argument("-d", help="demand file")
    parser.add_argument("-e", help="elements in diagram")
    parser.add_argument("-o", help="output diagram file")
    args = parser.parse_args()
    print(args)
    running()

if __name__ == "__main__":
    main()