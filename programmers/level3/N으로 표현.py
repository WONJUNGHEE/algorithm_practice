def solution(N, number):
    array=[{N}]
    for i in range(2,9):
        case={int(str(N)*i)}
        for index in range(int(i/2)):
            for x in array[index]:
                for y in array[i-index -2]:
                    case.add(x+y)
                    case.add(x-y)
                    case.add(y-x)
                    case.add(x*y)
                    if x!=0: case.add(y//x)
                    if y!=0: case.add(x//y)
        if number in case:
            return i
        
        array.append(case)

    
    return -1
