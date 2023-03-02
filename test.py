'''
import PymemLinux
import time

inattack = 124224200
localplayer = 32410800 + 8
name = 1417
team = 1100
region = 5368709120
localorigin = 344
entitylist = 28539512

def main():
    pml = PymemLinux.PymemLinux(process_name="R5Apex.exe")
    print(f"Process id: {pml.process_id}")
    entitylistindex = 0
    while True:
        time.sleep(0.2)
        unresolvedBasePointer = region + entitylist
        basePointer = pml.read_longlong(address=unresolvedBasePointer)
        ptrLong = basePointer + localorigin
        result = pml.read_float(ptrLong)
        print(result)
    
    
if __name__ == "__main__":
    main()
'''