# class Human():

#     def __init__(self, city, region, people, city, kod):
#         self.city = city
#         self.region = region
#         self.people = people
#         self.city = city
#         self.country = country
#         self.address = address

#     def setcity(self):
#         self.city = input("enter city = ")
        
#     def setregion(self):
#         self.region = input("enter region = ")
        
#     def setpeople(self):
#         self.people = input("enter people = ")
        
#     def setCity(self):
#         self.city = input("enter city = ")
        
#     def setCountry(self):
#         self.country = input("enter country = ")

#     def setAddress(self):
#         self.address = input("enter address = ") 

#     def setAll(self):
#         self.city = input("enter city") 
#         self.region = input("enter region") 
#         self.people = input("enter people") 
#         self.city = input("enter city") 
#         self.country = input("enter country") 
#         self.address = input("enter address") 

#     def getcity(self):
#         print(self.city)
    
#     def getregion(self):
#         print(self.region)
    
#     def getpeople(self):
#         print(self.people)

#     def getCity(self):
#         print(self.city)

#     def getCountry(self):
#         print(self.country)

#     def getAddress(self):
#         print(self.address)

#     def out(self):
#         print("city ", self.city)
#         print("region ", self.region)
#         print("people ", self.people)
#         print("city ", self.city)
#         print("country ", self.country)
#         print("address ", self.address)

# alik = Human("Alik", "8 apr", "89891601616", "Sochi", "russia", "st.br17")


class City():

    def __init__(self, city, region, people, index, kod):
        self.city = city
        self.region = region
        self.people = people
        self.index = index
        self.kod = kod

    def setCity(self):
        self.city = input("enter city = ")
        
    def setRegion(self):
        self.region = input("enter region = ")
        
    def setPeople(self):
        self.people = input("enter people = ")
        
    def setindex(self):
        self.index = input("enter index = ")
        
    def setKod(self):
        self.kod = input("enter kod = ")

    def setAll(self):
        self.city = input("enter city") 
        self.region = input("enter region") 
        self.people = input("enter people") 
        self.index = input("enter index") 
        self.kod = input("enter kod")

    def getcity(self):
        print(self.city)
    
    def getregion(self):
        print(self.region)
    
    def getpeople(self):
        print(self.people)

    def getKod(self):
        print(self.kod)

    def getKod(self):
        print(self.kod)


    def out(self):
        print("city ", self.city)
        print("region ", self.region)                                                                   
        print("people ", self.people)
        print("index ", self.index)
        print("kod ", self.kod)

alik = City("sochi", "kranodarski kray", "100000", "257925", "1234")

alik.out()



        