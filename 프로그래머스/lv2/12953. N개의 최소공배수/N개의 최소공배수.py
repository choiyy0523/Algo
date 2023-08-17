def gcd(a, b):
    r = a % b   
    if r > 0:
        while r > 0:
            a = b
            b = r
            r = a % b
        return(b)
    elif r == 0:
        return(b)
    
def lcm(a, b):
    g = gcd(a, b)
    return (g * (a//g) * (b//g))
        

def solution(arr):
    while len(arr) > 1:
        arr[0:2] = [lcm(arr[0], arr[1])]
        l = arr[0]
    
    answer = arr[0]
        
    return answer