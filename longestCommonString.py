def longestCommonSubString(str1, str2):
    size_str1 = len(str1)
    size_str2 = len(str2)

    mat = [[0 for i in range(size_str2+1)] for j in range(2)]

    result = 0

    for i in range(1, size_str1 + 1):
        for j in range(i, size_str2 + 1):
            if str1[i-1] == str2[j-1]:
                mat[i % 2][j] = mat[i-1 % 2][j-1] + 1
                if(mat[i % 2][j] > result):
                    result = mat[i % 2][j]
            else:
                mat[i % 2][j] = 0
    return result


str1 = "abcdefgh"
str2 = "defgbnh"

print(longestCommonSubString(str1, str2))
