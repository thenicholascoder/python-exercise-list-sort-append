#variables
h = float(input("hours: "))
r = float(input("rate: "))

#creating a function that will take arguments from given input from user
def computepay(h,r):

	#conditional statement from problem, if the pay is less than or equal to 40 the rate is normal
    if h <= 40:
        result = h*r
        return result
    #conditional else if, if hours is greater than 40, rate is multiplied by 1.5
    elif h > 40:
    	#h2 is the excess hours from 40 which then will be multiplied by 1.5*rate
        h2 = h-40
        r2 = 1.5*r
        #stored inside result is 40*rate + the excess hours*1.5rate
        result = (40*r)+(h2*r2)
        return result

#store the returned value into p while invoking the function computepay
p = computepay(h,r)

#print the result
print("Pay", p)
