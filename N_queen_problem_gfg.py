class Solution:
    def nQueen(self, n):
        # code here
        bd=[None]*n
        rw=set()
        up=set()
        dn=set()
        ret=[]
        def bt(x=0):
            nonlocal n,bd,rw,up,dn,ret
            if x==n:
                return True
            for y in range(n):
                if y in rw or y+x in up or y-x in dn:
                    continue
                bd[x]=y
                rw.add(y)
                up.add(y+x)
                dn.add(y-x)
                if bt(x+1):
                    ret.append([x+1 for x in bd])
                bd[x]=None
                rw.discard(y)
                up.discard(y+x)
                dn.discard(y-x)
        bt()
        return ret
