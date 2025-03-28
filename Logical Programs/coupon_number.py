import random


class Coupon_Collector:
    @staticmethod
    def generate_random(max_value):
        """
        
        Arguments:
        Takes the max limit of the random value
        
        Outputs:
        Returns a random number using random library
        """

        return random.randint(0, max_value)
    
    @staticmethod
    def trals_count_distint_coupons(n):
        
        unique_Coupons=set()
        trials_count=0
        
        if n<0:
            print("The number is not zero")
        
        while len(unique_Coupons)<n:
            result=Coupon_Collector.generate_random(10)
            unique_Coupons.add(result)
            trials_count+=1
            
        return trials_count
    
max_coupon_count=int(input("Enter the number of coupons you need: "))    
result=Coupon_Collector.trals_count_distint_coupons(max_coupon_count)
print(result)
