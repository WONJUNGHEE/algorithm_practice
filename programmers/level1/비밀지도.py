def solution(n, arr1, arr2):
    answer = []
    for decimal1, decimal2 in zip(arr1, arr2):
        binary12 = str(bin(decimal1 | decimal2))[2:]
        binary12 = '0' * (n - len(binary12)) + binary12
        binary12 = binary12.replace('1', '#')
        binary12 = binary12.replace('0', ' ')
        answer.append(binary12)
    return answer


못품
출처: https://geonlee.tistory.com/98 [빠리의 택시 운전사]
