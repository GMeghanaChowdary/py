class Card:
   def __init__(self, currId, currImageUrl, currDeviceType, currPrice, curRating):
       self.id = currId
       self.imageUrl = currImageUrl
       self.deviceType = currDeviceType
       self.price = currPrice
       self.rating = curRating
      
   def printDetails(self):
       print("Product -", self.id, ":")
       print("imageUrl:", self.imageUrl)
       print("deviceType:", self.deviceType)
       print("price:", self.price)
       print("rating:", self.rating)
      
      
mobile = Card(1, "Dummy-url 1", "Mobile", 56000, 4.5)
laptop = Card(2, "Dummy-url 2", "Laptop", 94000, 4.8)
watch = Card(3, "Dummy-url 3", "Smart-watch", 18000, 3.5)


mobile.printDetails()
print()
laptop.printDetails()
print()
watch.printDetails()
