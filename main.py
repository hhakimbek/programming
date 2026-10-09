
def parvoz_mumkinmi(windSpeed):
    return windSpeed>=0 and windSpeed<=10


def sarf_hisobla(distance,windSpeed):
    spendingChargePerKm = 2
    if(windSpeed>5 and windSpeed<=10):
        spendingChargePerKm = 3
    elif(windSpeed>=0 and windSpeed<=5):
        spendingChargePerKm = 2
    return distance*spendingChargePerKm

    
def hisobot_qatorlari(routes):
    if(len(routes)==0):
        return "Hisobot: bajarilgan nuqta yo'q."
    
    maxDistance = 0
    minDistance = float("inf")
    sumDistance = 0
    averageDistance = 0
    # min max sum average yo'lni aniqlash loop i
    for i in routes:
        if(i<minDistance):
            minDistance = i
        if(i>maxDistance):
            maxDistance = i
        sumDistance+=i

    averageDistance = sumDistance/len(routes)
    
    return f'''
== Nuqtalar {len(routes)} ta ===
{routes}
Max: {maxDistance}
Min: {minDistance} 
Sum: {sumDistance} 
Average: {averageDistance:.1f}
'''


def main():

    routes = []

    batteryCharge = int(input("Quvvat (%): "))
    
    while batteryCharge >= 20:
    
        distance = input("Masofa (km): ")

        if(distance=="stop"):
            print("Masofa tugadi")
            break

        distance = int(distance)
        
        windSpeed = int(input("Shamol tezligi (ms): "))

        if(not parvoz_mumkinmi(windSpeed=windSpeed)):
            print("Taqiqlangan shamol sabab")
            continue

        remained =  batteryCharge - sarf_hisobla(distance=distance,windSpeed=windSpeed)
    
        if(remained>=0):
            if(remained<15):
                print("Xavf bilan uching")

            batteryCharge=remained
            routes.append(distance)
            
            print(f"Dron yetib bordi ({remained}%)\n")
            print(hisobot_qatorlari(routes=routes))
            
        else:
            print("Dron yetib borolmaydi\n")
    else: 
        print(f"Zaryad 20% dan kam => {batteryCharge}%")



main()