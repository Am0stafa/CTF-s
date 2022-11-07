
#! array of all letters small and capital
def all2lettersCombinations():
    return [chr(i) for i in range(97,123)] + [chr(i) for i in range(65,91)]

#! all possible word that contain 2 alphabets: number of possibilities = 52^2
def all2lettersWords():
    return [i+j for i in all2lettersCombinations() for j in all2lettersCombinations()]
    
#! all possible word that contain 4 alphabets: number of possibilities = 52^4
def all4lettersWords():
    return [i+j+k+l for i in all2lettersCombinations() for j in all2lettersCombinations() for k in all2lettersCombinations() for l in all2lettersCombinations()]
    
#! all possible word that contain 5 alphabets: number of possibilities = 52^5
def all5lettersWords():
    return [i+j+k+l+m for i in all2lettersCombinations() for j in all2lettersCombinations() for k in all2lettersCombinations() for l in all2lettersCombinations() for m in all2lettersCombinations()]
#* more than that will take a lot of time    

#! all possible numbers of length 8 so you can add 05 and get all Saudi numbers: number of possibilities 9^8
def all8numbers():
    return [str(i)+str(j)+str(k)+str(l)+str(m)+str(n)+str(o)+str(p) for i in range(10) for j in range(10) for k in range(10) for l in range(10) for m in range(10) for n in range(10) for o in range(10) for p in range(10)]
 
#! all possible numbers of length 9 so you can add 012/011/010 and get all Egyptian numbers: number of possibilities 9^9
def all9numbers():
    return [str(i)+str(j)+str(k)+str(l)+str(m)+str(n)+str(o)+str(p)+str(q) for i in range(10) for j in range(10) for k in range(10) for l in range(10) for m in range(10) for n in range(10) for o in range(10) for p in range(10) for q in range(10)]