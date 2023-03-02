import PymemLinux
import offsets
import main

def getUnresolvedBasePointer():
    unresolvedBasePointer = offsets.region + offsets.localPlayer
    return unresolvedBasePointer

def getBasePointer(pml):
    m_basePointer = pml.read_longlong(getUnresolvedBasePointer())
    return m_basePointer

def getLocationX(pml):
    basePointer = getBasePointer(pml)
    longPtr = basePointer + offsets.localOrigin
    result = pml.read_float(longPtr)
    return result

def getLocationY(pml):
    basePointer = getBasePointer(pml)
    longPtr = basePointer + offsets.localOrigin + 4
    result = pml.read_float(longPtr)
    return result

def getLocationZ(pml):
    basePointer = getBasePointer(pml)
    longPtr = basePointer + offsets.localOrigin + (4 * 2)
    result = pml.read_int(longPtr)
    return result

def getTeamNumber(pml):
    basePointer = getBasePointer(pml)
    longPtr = basePointer + offsets.team
    result = pml.read_int(longPtr)
    return result

def isInAttack(pml):
    basePointer = getBasePointer(pml)
    longPtr = offsets.region + offsets.inAttack
    result = pml.read_int(longPtr)
    return result > 0

def getName(pml):
    basePointer = getBasePointer(pml)
    longPtr = basePointer + offsets.name
    result = pml.read_string(longPtr)
    return result

def isKnocked(pml):
    basePointer = getBasePointer(pml)
    longPtr = basePointer + offsets.bleedoutState
    result = pml.read_short(longPtr)
    return result > 0

def isDead(pml):
    basePointer = getBasePointer(pml)
    longPtr = basePointer + offsets.lifeState
    result = pml.read_short(longPtr)
    return result > 0

def isZooming(pml):
    basePointer = getBasePointer(pml)
    longPtr = basePointer + offsets.zooming
    result = pml.read_short(longPtr)
    return result > 0