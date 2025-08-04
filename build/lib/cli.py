# dronecli.py
import argparse

def main():
    parser = argparse.ArgumentParser(description="Demo CLI")
    parser.add_argument('go')
   # parser.add_argument('--', type=int, default=10)
    args = parser.parse_args()
    print("away")
#    print(f"Executing {args.go} at speed {args.speed}")

if __name__ == "__main__":
    main()
