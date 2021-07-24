from classic import Classic
from genetic import Genetic

if __name__ == "__main__":
  a = Classic(2, -5, 47, -3, 4, 0)
  a.run()  
  b = Genetic(2, -5, 47, -3, 4, a.f_max, a.f_min, 0) 
  b.run()
