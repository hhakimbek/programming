def checkDistance():
    batteryHealth = int(input("Batareya (%): "))
    count=0
    while batteryHealth>0:
        print("\n")
        
        distance = input("Masofani kiriting (km): ")
        
        if distance=="stop":
            print("Masofa tugagan")
            break
        
        speed = int(input("Shamol tezligi (m/s): "))
        persentage = 2
        
    
        if (speed>=0 and speed<=5):
            persentage=2
        elif (speed>=5 and speed<=10):
            persentage=3
        else:
            print("Uchish taqiqlangan")
            continue
        
        distance = float(distance)
        remainder = batteryHealth-distance*persentage
            
        if(remainder < 0):
            print("Zaryad yetmaydi.")
        else:
            print("Yetadi:", remainder, "%", "qoldi.")
            count+=1
            batteryHealth = remainder

    print(f"Nuqtalar: {count} ta")

        


checkDistance()




