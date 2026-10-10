

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
        distance = int(input("Masofa (km): "))
        remained = batteryCharge-spendingChargePerKm*distance
        if(remained>0):
            batteryCharge = remained
            distances.append(distance)
            print(f"Qoldiq zaryad: {remained}%")
            print("Qaror: Uching")
        else:
            print(f"Qaror: Uchmang, quvvat yetmaydi")
    else:
        print(f"Yetib borilgan nuqtalar: {len(distances)}")
    

main()