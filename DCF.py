import yfinance as yf

# Apple calculation
aapl = yf.Ticker("AAPL")

shrs_out = aapl.info['sharesOutstanding']

# rates
reqRate = 0.07
perpRate = 0.02
cashFlowGrowthRate = 0.03

years = [1, 2, 3, 4]

# in 1000s (2019, 2020, 2021, 2022)
FreeCashFlow = [58896000, 73365000,92953000, 111443000]

FutureFreeCashFlow = []

discountFactor = []

# discounted future FCF
discountedFutureFreeCashFlow= []

# terminal value
terminalValue = FreeCashFlow[-1] * (1 + perpRate) / (reqRate - perpRate)

# print(tv)

for year in years:
    cash_flow = FreeCashFlow[-1] * (1+cashFlowGrowthRate)**year
    FutureFreeCashFlow.append(cash_flow)
    discountFactor.append((1+reqRate)**year)

print(discountFactor)
print(FutureFreeCashFlow)

for i in range(0, len(years)):
    discountedFutureFreeCashFlow.append(FutureFreeCashFlow[i]/discountFactor[i])

print(discountedFutureFreeCashFlow)

discountedTerminalvalue = terminalValue/(1 + reqRate)**4
discountedFutureFreeCashFlow.append(discountedTerminalvalue)

todaysValue = sum(discountedFutureFreeCashFlow)

fairValue = (todaysValue/shrs_out) * 1000

print(fairValue)