In this challenge, you are given a list of words written in an alien language, where the words are sorted lexicographically by the rules of this language. Surprisingly, the aliens also use English lowercase letters, but possibly in a different order.
Given a list of words written in the alien language, you have to return a string of unique letters sorted in the lexicographical order of the alien language as derived from the list of words.
If there’s no solution, that is, no valid lexicographical ordering, you can return an empty string.

def alien_order(words):
    adj_list = defaultdict(set)
    counts = Counter({c: 0 for word in words for c in word})
    outer = 0
    for word1, word2 in zip(words, words[1:]):
        outer += 1
        inner = 0
        for c, d in zip(word1, word2):
            inner += 1
            if c != d:
                if d not in adj_list[c]:
                    adj_list[c].add(d)
                    counts[d] += 1
                break

        else:  
            if len(word2) < len(word1):
                return ""

    
    result = []
    sources_queue = deque([c for c in counts if counts[c] == 0])
    while sources_queue:
        c = sources_queue.popleft()
        result.append(c)

        for d in adj_list[c]:
            counts[d] -= 1
            if counts[d] == 0:
                sources_queue.append(d)

    if len(result) < len(counts):
        return ""
    return "".join(result)