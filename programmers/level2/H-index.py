def solution(citations):
    citations.sort(reverse=True)
    count=0
    for i in citations:
        if i<=count:
            return count
        count+=1
    return count