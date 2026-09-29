class Solution:

    def encode(self, strs):
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s):
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':      # acha o fim do número
                j += 1
            tam = int(s[i:j])
            res.append(s[j+1 : j+1+tam])
            i = j + 1 + tam         # pula para o próximo bloco
        return res
