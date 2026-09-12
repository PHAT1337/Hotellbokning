class Room:
    def __init__(self, number, room_type, price):
        self.number = number
        self.room_type = room_type
        self.price = price
        self.booked = False
        self.guest = None
        
room1 = Room(101, "Enkelrum", 800)
room2 = Room(102, "Enkelrum", 800)
room3 = Room(103, "Enkelrum", 800)
room4 = Room(104, "Dubbelrum", 1200)
room5 = Room(105, "Dubbelrum", 1200)
room6 = Room(201, "Enkelrum", 800)
room7 = Room(202, "Enkelrum", 800)
room8 = Room(203, "Dubbelrum", 1200)
room9 = Room(204, "Dubbelrum", 1200)
room10 = Room(205, "Svit", 2500)

rooms = [room1, room2, room3, room4, room5, room6, room7, room8, room9, room10]

def show_rooms():
    for room in rooms:
        if room.booked:
            print(f"Rum {room.number} - {room.room_type} - {room.price} kr bokad av {room.guest}")
        else:
            print(f"Rum {room.number} - {room.room_type} - {room.price} kr - Ledigt")

def show_free_rooms():
   for room in rooms:
      if not room.booked:
           print(f"Ledigt rum {room.number} - {room.room_type} - {room.price} kr")

def search_room():
    
    try:
        rum = int(input("Välj rum nummer: "))
        
        rum_finns = False
        
        for room in rooms:
            if room.number == rum:
                rum_finns = True


                if room.booked:
                    print(f"Rum {room.number} - {room.room_type} - {room.price} kr bokad av {room.guest}")
                else:
                    print(f"Rum {room.number} - {room.room_type} - {room.price} kr - Ledigt")

        if not rum_finns:
            print("Du har valt ett felaktigt rum nummer!")
                
    except ValueError:
        print("Du måste ange ett rumsnummer med siffror.")

def check_in():
    namn = input("Ange ditt Efternamn: ")
    
    try:
        rum = int(input("Välj ett rum: "))
        
        rum_finns = False
        
        for room in rooms: 
            if room.number == rum:
                rum_finns = True
                
                if not room.booked:
                    room.booked = True
                    room.guest = namn
                    print(f"{namn} har valt rum {room.number}")
                
                else:
                    print("Rummet är redan bokat.")
        
        if not rum_finns:
            print("Du har valt ett felaktigt rum nummer!")
    
    except ValueError:
        print("Du måste ange ett rumsnummer med siffror.")            

def check_out():
    namn = input("Ange namnet du har bokat under: ")
    
    try:
        rum = int(input("Vilket rum vill du checka ut? "))
        
        rum_finns = False
        
        for room in rooms:
            if room.number == rum:
                rum_finns = True
                    
                if not room.booked:
                    print("Rummet är inte bookat.")
                        
                elif room.guest != namn:
                    print("Ditt namn stämmer inte med bokningen.")
                        
                else:
                    print(f"{room.guest} ha nu checkat ut ur rum {room.number}")
                    room.booked = False
                    room.guest = None
                    
                        
        if not rum_finns:        
            print("Du har valt ett felaktigt rum nummer!")
    
    except ValueError:
        print("Du måste ange ett rumsnummer med siffror.") # try/except för att kolla om input för rum är int

while True:
    
    print("""--- Meny ---
          
1. Visa alla rum
2. Visa lediga rum
3. Sök rum
4. Checka in
5. Checka ut
6. Avsluta
          """)
    
    meny = input("Välj ett alternativ")
    
    if meny == "1":
        show_rooms()
      
    elif meny == "2":
        show_free_rooms()

    elif meny == "3":
        search_room()
        
    elif meny == "4":
        check_in()
        
    elif meny == "5":
        check_out()
        
    elif meny == "6":
        print(" Välkommen åter!")
        break
    
    else:
        print("Ogiltigt val, välj 1-6.")
