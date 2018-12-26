class DengeBenXi:

	def __init__(self,account, term, rate, jiaxi=0, youhuiquan=0):
		self.account = float(account)
		self.term = int(term)
		self.rate = float(rate)
		self.jiaxi = float(jiaxi)
		self.youhuiquan = float(youhuiquan)


	def changgui_biao(self):
		# 每月应付金额 = 贷款本金×[年化利率/12×(1+年化利率/12) ^ 还款月数]÷ {[(1+年化利率/12) ^ 还款月数]-1}
		return self.account * {(self.rate / 12) * [(1 + self.rate / 12) ** self.term]} / [(1 + self.rate / 12) ** self.term - 1]

mini = DengeBenXi(39000, 12, 0.105)
mini.changgui_biao()

