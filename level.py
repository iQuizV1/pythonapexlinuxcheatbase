import PymemLinux
import offsets

def getBasePointer():
    basePointer = offsets.region + offsets.level
    return basePointer

def getName(pml):
    basePointer = getBasePointer()
    result = pml.read_string(basePointer)
    return result

def isPlayable(pml):
    if (not getName(pml)):
        return False
    if (getName(pml) == "mp_lobby"):
        return False
    return True

def isTrainingArea(pml):
    if (getName(pml) == "mp_rr_canyonlands_staging"):
        return True
    return False