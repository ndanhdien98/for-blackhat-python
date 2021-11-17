def anagrams(word, words):
    result = []
    for x in range(len(words)):
        if sorted(word) == sorted(words[x]):
            result.append(words[x])
    return result
anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada'])