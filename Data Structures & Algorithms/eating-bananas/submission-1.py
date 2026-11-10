class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        kmax = max(piles)
        kmin = 1
        while kmax>=kmin:
            time=0
            kav = (kmax+kmin)//2
            for i in piles:
                time+=math.ceil(i/kav)
            if time>h:
                kmin = kav + 1
            else:
                kmax = kav-1
        return kmin