class DengeBenXi:
    def __init__(self, account, term, rate, jiaxi=0, youhuiquan=0):
        self.account = account
        self.term = term
        self.rate = rate
        self.jiaxi = jiaxi
        self.youhuiquan = youhuiquan

    def changgui_biao(self):
        # 每月应付金额 = 贷款本金×[年化利率/12×(1+年化利率/12) ^ 还款月数]÷ {[(1+年化利率/12) ^ 还款月数]-1}
        #a = self.account * (self.rate / 12) * [(1 + self.rate / 12) ** self.term] / [(1 + self.rate / 12) ** self.term - 1]
        a=(1+self.rate/12)**self.term*(self.rate/12)
        b=(1+self.rate/12)**self.term-1
        c=self.account*a/b
        return c


mini = DengeBenXi(39000, 12, 0.105)
print(mini.changgui_biao())
