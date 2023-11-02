class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word=s.split(" ")
        p_to_s={}
        s_to_p={}
        if len(pattern)!=len(word):
            return False
        n=len(word)
        for i in range(n):
            p_char=pattern[i]
            s_char=word[i]
            if p_char in p_to_s and p_to_s[p_char]!=s_char:
                return False
            if s_char in s_to_p and s_to_p[s_char]!=p_char:
                return False
            p_to_s[p_char]=s_char
            s_to_p[s_char]=p_char
        return True
