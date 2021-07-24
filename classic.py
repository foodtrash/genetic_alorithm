from algorithm import Algorithm

class Classic(Algorithm):
  def __init__(self, a, b, c, d, number_of_chromo, mutation = 0):
    super().__init__(a, b, c, d, number_of_chromo, mutation)

  def run(self):
    self.f_min = 0 
    self.f_max = 0 
    f_min_iter = 0 
    f_max_iter = 0 
    iteration = 1 
    for x in range(-10, 54):
      result = self.a + self.b * x + self.c * x**2 + self.d * x ** 3
      if(result < self.f_min):
        self.f_min = result
        f_min_iter = iteration
      if(result > self.f_max):
        self.f_max = result
        f_max_iter = iteration
      iteration += 1
    print("     classic algorithm\n")
    super().print_result(self.f_max, f_max_iter, "max: bin: iter:")
    super().print_result(self.f_min, f_min_iter, "min: bin: iter:")
    
