


def parvoz_mumkinmi(windSpeed):
    return windSpeed>=0 and windSpeed<=10


def sarf_hisobla(distance,windSpeed,yuk=0):
    spendingChargePerKm = 2
    if(windSpeed>5 and windSpeed<=10):
        spendingChargePerKm = 3+yuk
    elif(windSpeed>=0 and windSpeed<=5):
        spendingChargePerKm = 2+yuk
    return distance*spendingChargePerKm

def hisobot_qatorlari(weightWithRegions:dict,routesKm):
    if(not weightWithRegions):
        return "Hisobot: bajarilgan nuqta yo'q."
    
    maxDistance = 0
    minDistance = float("inf")
    sumDistance = 0
    averageDistance = 0
    # min max sum average yo'lni aniqlash loop i
    for i in routesKm:
        if(i<minDistance):
            minDistance = i
        if(i>maxDistance):
            maxDistance = i
        sumDistance+=i

    averageDistance = sumDistance/len(routesKm)
    regions = list(weightWithRegions.keys())
    regions.sort;
    return f'''
Bajarilgan nuqtalar: {len(routesKm)}
Masofalar: {routesKm}
Max: {maxDistance}
Min: {minDistance} 
Sum: {sumDistance} 
Average: {averageDistance:.1f}
Tumanlar: {regions}'''

def main():

    BAZA = (41.31, 69.24)
    MARSHRUT = [
        {"tuman": "Chilonzor", "masofa": 5, "yuk": 2},
        {"tuman": "Yunusobod", "masofa": 8, "yuk": 1},
        {"tuman": "Chilonzor", "masofa": 6, "yuk": 3},
        {"tuman": "Sergeli", "masofa": 5, "yuk": 1},
    ]

    #completeRegionsNames = set()
    weightWithRegions = {}
    routesKm = []

    batteryCharge=100

    windSpeed = int(input("Shamol tezligi (ms): "))

    if(not parvoz_mumkinmi(windSpeed=windSpeed)):
        print("Taqiqlangan shamol sabab uchilmaydi")
        return

    for index in range(0,len(MARSHRUT)): 
        distance = MARSHRUT[index]['masofa']
        weight = MARSHRUT[index]['yuk']
        region = MARSHRUT[index]['tuman']

        batteryCharge =  batteryCharge - sarf_hisobla(distance=distance,windSpeed=windSpeed,yuk=weight)
        #completeRegionsNames.add(region)   
        weightWithRegions[region] = weightWithRegions.get(region,0)+weight
        routesKm.append(distance)
        if(batteryCharge<20):
            break
            
    print(f"Qoldiq zaryad: {batteryCharge}%")
    print(hisobot_qatorlari(weightWithRegions=weightWithRegions,routesKm=routesKm))
    print("Tumanlar bo'yicha yuk:")
    for k in weightWithRegions:
        print(f"\t{k} {weightWithRegions[k]} kg")

main()