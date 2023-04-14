def solution(sequence):
    DP1 = [0] * len(sequence)
    DP2 = [0] * len(sequence)
    for i in range(len(sequence)):
        boolean = i%2
        alpha = 1 if boolean else -1
        DP1[i] = max(DP1[i], DP1[i-1] + sequence[i]*alpha)
        DP2[i] = max(DP2[i], DP2[i-1] + sequence[i]*(-1*alpha))
    return max(max(DP1), max(DP2))