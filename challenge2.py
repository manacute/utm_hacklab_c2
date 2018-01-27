def duplicates(word):
	used = ''
    dubs = ''
    for letter in ''.join(sorted(word)):
        if letter.lower() in used and letter.lower() not in dubs:
            dubs += letter.lower()
        used += letter.lower()
    return dubs

def shuffle(w1, w2, w3):
    sub = w1 + w2
    for letter in w3:
        if letter in sub:
            sub = sub[:sub.find(letter)] + sub[sub.find(letter) + 1:]
        else:
            return False
    if sub == '':
        return True
    return False

def remove_vowels(word_list):
    n = 0
    for word in word_list:
        i = 0
        while i < len(word):
            if word[i].lower() in 'aeiou':
                word = word[:i] + word[i + 1:]
            else:
                i += 1
        word_list[n] = word
        n += 1

def new_word(a, b):
    n = 0
    while n < len(a) - 3:
        m = 0
        while m < len(b) - 3:
            if a[n:n + 3] == b[m:m + 3]:
                return(a[:n + 3] + b[m + 3:])
            m += 1
        n += 1
    return('')

def word_score(word_list):
    scores = {}
    for word in word_list:
        score = 0
        used = ''
        for letter in word:
            score += (ord(letter) - 64) % 32
            if letter in used and '0' not in used:
                score -= 10
                used += '0'
            used += letter
        scores[word] = score + 10
    return(sorted(scores, key = scores.get, reverse = True))
