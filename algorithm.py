
class Algorithm(object):
  def __init__(self, a, b, c, d, number_of_chromosomes, mutation = 0): 
    self.a = a 
    self.b = b 
    self.c = c 
    self.d = d 
    self.f_min_classic = 0 
    self.f_max_classic = 0 
    self.number_of_chromosomes = number_of_chromosomes
    self.mutation = mutation if mutation else number_of_chromosomes // 4
  
  def print_result(self, number, iteration, text):
      array_of_string = text.split()
      print(array_of_string[0], number, array_of_string[1], bin(number), array_of_string[2], iteration)
