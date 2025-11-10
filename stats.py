def word_count(text):
    words = text.split()
    return len(words)

def characters_count(text):
    counts = {}
    for ch in text.lower():
        if ch not in counts:
            counts[ch] = 0
        counts[ch] += 1
    return counts

def sorted_list(counts):
    items = []
    for ch,n in counts.items():
        if ch.isalpha():
            items.append({"char": ch, "num": n})

    def sort_on(d):
        return d["num"]

    items.sort(key=sort_on, reverse=True)
    
    return items
