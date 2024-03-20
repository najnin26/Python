import argparse

if __name__ == '__main__':
    parser=argparse.ArgumentParser(
        description="my watch script"
        )
    
    parser.add_argument('num1', help="Number 1")
    parser.add_argument('num2', help="Number 2")
    parser.add_argument('operation', help="provide operator")
    
    args=parser.parse_args()
    print(args)