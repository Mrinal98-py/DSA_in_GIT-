def permute(s, l, r):
    if l == r:
        print("".join(s))
    else:
        for i in range(l, r + 1):
            s[l], s[i] = s[i], s[l]  # Swap
            permute(s, l + 1, r)
            s[l], s[i] = s[i], s[l]  # Backtrack

def generate_permutations(string):
    n = len(string)
    s = list(string)
    permute(s, 0, n - 1)

# git update
# Example usage
string = "ABC"
generate_permutations(string)
