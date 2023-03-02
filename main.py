import PymemLinux
import offsets
import localplayer
import time
import level
import player

def main():
    pml = PymemLinux.PymemLinux(process_name="R5Apex.exe")
    print("--- Starting Python Chair ---")
    print(f"Process id: {pml.process_id}")

if __name__ == "__main__":
    main()