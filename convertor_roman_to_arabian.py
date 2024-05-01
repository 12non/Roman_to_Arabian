def solution(roman: str) -> int:
    dictionario = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    result = 0
    prima = 0
    for i in roman:
        b = dictionario[i]
        #print(b)
        if b > prima:
            result = result + b - prima * 2
        else:
            result += b
        
        prima = b
    print(prima)
    return result

#print(solution("MMMCMXCIX"))  insert this string in your code
