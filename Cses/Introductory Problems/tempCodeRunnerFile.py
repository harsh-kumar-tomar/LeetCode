  for i in range(1,n+1):
        if  half_sum >= i :
            half_sum -= i
            arr1.append(i)
        else:
            arr2.append(i)
