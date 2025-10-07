class Simple_Calculator:
    def add(self, a ,b):
        return a+b
    def subtract(self,a,b):
        return a-b
    def multiplication(self,a,b):
        return a*b
    def division(self,a,b):
        if b==0:
            raise ValueError("you can not divide using zero(0)")
        return a/b
    