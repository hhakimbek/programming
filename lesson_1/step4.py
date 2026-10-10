def main():

    distances = []
    batteryCharge = int(input("Battery (%): "))
    windSpeed = int(input("Shamol (ms):"))
    spendingChargePerKm = 2
    
    if(windSpeed>=0 and windSpeed<=5):
        spendingChargePerKm = 2
    elif(windSpeed>=5 and windSpeed<=10):
        spendingChargePerKm = 3
    else:
        print("Qaror: Uchmang, shamol kuchli")
        return

    while (batteryCharge>=20):
        print('\n')
        distance = input("Masofa (km): ")
        
        if(distance=="stop"):
            break;
        
        distance = int(distance)
        remained = batteryCharge-spendingChargePerKm*distance
        if(remained>0):
            batteryCharge = remained
            distances.append(distance)
            print(f"Qoldiq zaryad: {remained}%")
            print("Qaror: Uching")
        else:
            print(f"Qaror: Uchmang, quvvat yetmaydi")
    else:
        print(f"\nYetib borilgan nuqtalar: {len(distances)} ta")
        hisobot_qatorlari(distances=distances)
    
def hisobot_qatorlari(distances:list):
    maxD = 0
    minD = float("inf")
    averageD = 0
    sumD = 0

    for i in distances:
        if(maxD<i):
            maxD=i
        if(minD>i):
            minD=i
        sumD+=i

    averageD = sumD/len(distances)

    print(f'''Max: {maxD}
Min: {minD}
Average: {averageD:.1f}
Sum: {sumD}
''')

main()
