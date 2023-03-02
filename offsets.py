orgInAttack = "0x076782c8"

orgRegion = "0x140000000"
orgLevel = "0x1462450"

orgLocalPlayer = "0x01ee8cb0" # Needs PlayerExtra
PlayerExtra = "0x8"
orgEntityList = "0x1b37a78"
orgCurrentShield = "0x0170"

orgLocalOrigin = "0x0158"

orgGlowEnable = "0x03c0" # Needs PlayerExtra
orgGlowThroughWall = "0x03c0" # + 0x10
orgGlowColor = "0x1d0"

orgTeam = "0x044c"
orgName = "0x0589"
orgLifeState = "0x0798"
orgBleedoutState = "0x2740"
orgZooming = "0x1c51"
orgLastVisibleTime = "0x1A78"


inAttack = int(orgInAttack, 16)
    
region = int(orgRegion, 16)
level = int(orgLevel, 16)

localPlayer = int(orgLocalPlayer, 16) + int(PlayerExtra, 16)
entityList = int(orgEntityList, 16)
currentShield = int(orgCurrentShield, 16)

localOrigin = int(orgLocalOrigin, 16)

glowEnable = int(orgGlowEnable, 16) + int(PlayerExtra, 16)
glowThroughWall = int(orgGlowThroughWall, 16) + int("0x10", 16)
glowColor = int(orgGlowColor, 16)

team = int(orgTeam, 16)
name = int(orgName, 16)
lifeState = int(orgLifeState, 16)
bleedoutState = int(orgBleedoutState, 16)
zooming = int(orgZooming, 16)
lastVisibleTime = int(orgLastVisibleTime, 16)