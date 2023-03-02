import PymemLinux
import offsets

m_entityListIndex = 0
m_lastVisibleTime = 0.0

def getUnresolvedBasePointer():
    unresolvedBasePointer = offsets.region + offsets.entityList + ((m_entityListIndex + 1) << 5)
    return unresolvedBasePointer

def getBasePointer(pml):
    m_basePointer = pml.read_longlong(getUnresolvedBasePointer())
    return m_basePointer

def Player(entityListIndex):
    m_entityListIndex = entityListIndex

def isDead(pml):
    basePointer = getBasePointer(pml)
    longPtr = basePointer + offsets.lifeState
    result = pml.read_short(longPtr)
    return result > 0

def isKnocked(pml):
    basePointer = getBasePointer(pml)
    longPtr = basePointer + offsets.bleedoutState
    result = pml.read_short(longPtr)
    return result > 0

def getName(pml):
    basePointer = getBasePointer(pml)
    longPtr = basePointer + offsets.name
    result = pml.read_string(longPtr)
    return result

def isValid(pml):
    return getBasePointer(pml) > 0 and isDead(pml) == False

def getInvalidReason(pml):
    if (getBasePointer(pml) == 0):
        return "base pointer wrong"
    elif (isDead(pml)):
        return "player dead"
    elif (not getName(pml)):
        return "name empty"
    else:
        return "player valid"

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

def getShieldsValue():
    basePointer = getBasePointer(pml)
    longPtr = basePointer + offsets.currentShield
    result = pml.read_int(longPtr)
    return result

def getGlowEnable(pml):
    basePointer = getBasePointer(pml)
    longPtr = basePointer + offsets.glowEnable
    result = pml.read_int(longPtr)
    return result

def setGlowEnable(pml, isglowenable):
    basePointer = getBasePointer(pml)
    longPtr = basePointer + offsets.glowEnable
    pml.write_int(longPtr, isglowenable)

def getGlowThroughWall(pml):
    basePointer = getBasePointer(pml)
    longPtr = basePointer + offsets.glowThroughWall
    result = pml.read_int(longPtr)
    return result

def setGlowThroughWall(pml, isglowthroughwall):
    basePointer = getBasePointer(pml)
    longPtr = basePointer + offsets.glowThroughWall
    pml.write_int(longPtr, isglowthroughwall)

def getGlowColorRed(pml):
    basePointer = getBasePointer(pml)
    longPtr = basePointer + offsets.glowColor
    result = pml.read_int(longPtr)
    return result

def setGlowColorRed(pml, color):
    if (color > 100):
        color = 100
    if (color < 0):
        color = 0
    basePointer = getBasePointer(pml)
    longPtr = basePointer + offsets.glowColor
    pml.write_float(longPtr, color)

def setGlowColorGreen(pml, color):
    if (color > 100):
        color = 100
    if (color < 0):
        color = 0
    basePointer = getBasePointer(pml)
    longPtr = basePointer + offsets.glowColor + 4
    pml.write_float(longPtr, color)

def setGlowColorBlue(pml, color):
    if (color > 100):
        color = 100
    if (color < 0):
        color = 0
    basePointer = getBasePointer(pml)
    longPtr = basePointer + offsets.glowColor + (4 * 2)
    pml.write_float(longPtr, color)

def getLastVisibleTime(pml):
    basePointer = getBasePointer(pml)
    longPtr = basePointer + offsets.lastVisibleTime
    result = pml.read_float(longPtr)
    return result

def isVisible(pml):
    lastVisibleTime = getLastVisibleTime(pml)
    isVisible = lastVisibleTime > m_lastVisibleTime
    m_lastVisibleTime = lastVisibleTime
    return isVisible