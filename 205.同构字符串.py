class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t={}
        t_to_s={}
        n=len(s)
        for i in range(n):
            s_char=s[i]
            t_char=t[i]
            if s_char in s_to_t and s_to_t[s_char]!=t_char:
                return False
            if t_char in t_to_s and t_to_s[t_char]!=s_char:
                return False
            s_to_t[s_char]=t_char
            t_to_s[t_char]=s_char
        return True
