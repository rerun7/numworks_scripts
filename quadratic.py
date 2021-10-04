import math 

def intQuestion(question):
    while True:
        try:
            rep = float(input(question))
        except:
            print("Input must be numerical.")
        else:
            return rep
  
def equationroots( a, b, c): 
    dis = b * b - 4 * a * c 
    sqrt_val = math.sqrt(abs(dis)) 
      
    if dis > 0: 
        print("Real and different roots.") 
        print((-b + sqrt_val)/(2 * a)) 
        print((-b - sqrt_val)/(2 * a)) 
      
    elif dis == 0: 
        print("Real and same roots.") 
        print(-b / (2 * a)) 
      
    else:
        print("Complex Roots") 
        print(- b / (2 * a), " + i", sqrt_val) 
        print(- b / (2 * a), " - i", sqrt_val) 
  
a = intQuestion("A: ")
b = intQuestion("B: ")
c = intQuestion("C: ")
print()
  
if a == 0: 
    print("Input correct quadratic equation") 
  
else:
    equationroots(a, b, c)