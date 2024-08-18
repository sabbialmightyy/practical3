from functions import *
def main():
    myqueue = DSAqueue()
    myqueue.push(10)
    print(f"You have popped {myqueue.pop()}")

if __name__ == "__main__":
    main()