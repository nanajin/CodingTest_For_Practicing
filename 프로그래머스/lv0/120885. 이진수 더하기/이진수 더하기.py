def solution(bin1, bin2):
    seung = 0
    num = 0
    list1, list2 = list(bin1), list(bin2)
    
    for i in range(len(bin1)):
        num += int(list1.pop()) * (2**seung)
        seung += 1
    seung = 0
    for i in range(len(bin2)):
        num += int(list2.pop()) * (2**seung)
        seung += 1
    
    print(num)
    return bin(num)[2:]