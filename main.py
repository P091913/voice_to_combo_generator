import sys
from Modules.record_voice import *
import time

def main():
    option = grab_action()
    if option:
        voice()
    else:
        sys.exit()



def grab_action():
    key_input = input("Press 'r' to record, or 'x' to quit.")
    while True:
        try:
            key = key_input.replace(" ", "").lower()
            if key == 'r':
                print("Space pressed - Start recording.")
                return True
            elif key == 'x':
                print("Exiting...")
                return False
        except Exception as e:
            print(f"Error: {e}")
            return False


if __name__ == '__main__':
    main()