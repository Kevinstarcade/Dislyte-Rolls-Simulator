from random import randrange
x = 1

rares = 0
epics = 0
legies = 0

lastEpic = 0
lastLegy = 0

epicPity = 0
legyPity = 0

rolls = []

for i in range(x):

    # 10-draw separator
    if i > 0 and i % 10 == 0:
        rolls.append("|")

    # rolling
    roll = randrange(100)

    # deciding rarity
    if roll == 0:
        result = "LEGENDARY"
        legies += 1
        lastLegy = 0

    elif 0 < roll < 21:
        result = "epic"
        epics += 1
        lastEpic = 0

    else:
        result = "r"
        rares += 1

    # pity counter
    if result != "LEGENDARY":
        lastLegy += 1
    if result != "epic":
        lastEpic += 1

    # pity
    if lastLegy >= 100:
        result = "LEGENDARY"
        lastLegy = 0
        legies += 1
        legyPity += 1

    elif lastEpic >= 20:
        result = "epic"
        lastEpic = 0
        epics += 1
        epicPity += 1

    rolls.append(result)

print(f"Rolls: {x}, Rares: {rares}, Epics: {epics}, Legendaries: {legies}")
print(f"Epic Pities Hit: {epicPity}, Legendary Pities Hit: {legyPity}")
print(f"True Epic Rate: {round(epics/x * 100, 2)}%, True Legendary rate: {round(legies/x * 100, 2)}%")