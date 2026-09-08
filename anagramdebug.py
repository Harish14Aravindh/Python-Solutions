from collections import defaultdict

def group_anagrams_sorting(strs: list[str]) -> list[list[str]]:
    anagram_map = defaultdict(list)
    
    for word in strs:
        sorted_key = "".join(sorted(word))
        print(f"Word: {word}, Sorted key: {sorted_key}")
        
        anagram_map[sorted_key].append(word)
        print(f"Current groups: {anagram_map}\n")
        
    return list(anagram_map.values())

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams_sorting(words))
