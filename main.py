def get_best_word(points, words):
    scores = []
    size_score = []
    index_s = []
    for word in words:
        score = 0
        for i in word:
            score += points[ord(i) - 65]
        scores.append(score)
        size_score.append((len(word), score))
    max_s = max(scores)
    for i in range(len(scores)):
        if scores[i] == max_s:
            index_s.append(i)
    if len(index_s) == 1:
        return index_s[0]
    else:
        minl = size_score[index_s[0]][0]
        result = index_s[0]
        for i in index_s[0:]:
            if size_score[i][0] < minl:
                minl = size_score[i][0]
                result = i
        return result
    
def get_best_word(points, words):
    return max(range(len(words)), key=lambda i: (sum(points[ord(c)-65] for c in words[i]), -len(words[i]), -i) )