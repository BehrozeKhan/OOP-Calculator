class Calculator():
    def __init__(self,val1,val2):
        self.val1 = val1
        self.val2 = val2
    
    def add(self):
        val3 = self.val1 + self.val2
        return val3
    
    def subtract(self):
        val4 = self.val2 - self.val1
        return val4
    
    def multiply(self):
        val5 = self.val1 * self.val2
        return val5
    
    def divide(self):
        val6 = self.val2 / self.val1
        return val6

val1 = int(input("Enter the first value: "))
val2 = int(input("Enter the second value: "))
cal = Calculator(val1,val2)

print("The addition of two given values is: ", cal.add())
print("The subtraction of two given values is: ", cal.subtract())
print("The multiplication of two given values is: ", cal.multiply())
print("The division of two given values is: ", cal.divide())
