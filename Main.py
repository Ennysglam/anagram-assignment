ana1 = "Heart"
ana2 ="Earth"
ana1= ana1.lower()
ana2 = ana2.lower()
ana1_sorted = sorted(ana1)
ana2_sorted = sorted (ana2)
print(sorted(ana1) == sorted(ana2))
def find_anagrams(ana1, ana2):
    if ana1_sorted == ana2_sorted:
        return True
    else:
        return False

