def solution(s):
    if len(s) ==4 or len(s)==6:
        for i in s:
            if int(i,base=36) >=10:
                return False
    else:
        return False
    return True