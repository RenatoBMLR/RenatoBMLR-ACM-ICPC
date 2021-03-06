#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 14:08:07 2018

@author: renatobottermaiolopesrodrigues
"""



class Solution:
    # @param A : integer
    # @return a list of integers
    def primesum(self, A):
        
        prime_lst = self.SieveOfEratosthenes(A)

        for i in range(0, len(prime_lst)):
            for j in range(len(prime_lst)-1, -1, -1):
                if prime_lst[i] + prime_lst[j]== A:
                    return prime_lst[i], prime_lst[j]
        
        
    def SieveOfEratosthenes(self, n): 
          
        # Create a boolean array "prime[0..n]" and initialize 
        #  all entries it as true. A value in prime[i] will 
        # finally be false if i is Not a prime, else true. 
        prime = [True for i in range(n+1)] 
        p = 2
    
        while (p * p <= n): 
              
            # If prime[p] is not changed, then it is a prime 
            if (prime[p] == True): 
    
                # Update all multiples of p 
                for i in range(p * 2, n+1, p): 
                    prime[i] = False
            p += 1
                    
        prime_numbers = []
        # Print all prime numbers 
        for p in range(2, n): 
            if prime[p]: 
                prime_numbers.append(p)
        return prime_numbers




    


