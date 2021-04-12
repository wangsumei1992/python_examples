class Dengbendengxi():

    def __init__(self, amount, month, jiaxi = 0, youhuiquan = 0):
        self.amount = float(amount)
        self.month = int(month)
        self.jiaxi = float(jiaxi)
        self.youhuiquan = float(youhuiquan)
    def changguibiao(self):
        '''每月还款金额=（借款本金 / 期限）+ 借款本金 * 0.0048 '''
        return ((self.amount/self.month)  + self.amount * 0.0048)

    def jiaxi_biao(self):
        return ((self.jiaxi / 12) / 1.9 * self.amount)

    def jiangli(self):
        return self.youhuiquan / 12 / 1.9 * self.month * self.amount

    def yuqishouyi(self):
        return (self.changguibiao() * self.month - self.amount)

    def jiaxi_yuqishouyi(self):
        return (self.jiaxi_biao() * 12 + self.yuqishouyi())


s = Dengbendengxi(5000, 6, 0.1, 0)
print(s.changguibiao())
