import backtrader as bt
from datetime import datetime

class SmaCross(bt.Strategy):
    params = (('pfast',10),('pslow',30),('stop_loss',0.10),('take_profit',0.15),)

    def log(self, txt, dt=None):
        ''' Logging function for this strategy'''
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))

    def __init__(self):
        self.dataclose = self.datas[0].close
        self.order = None
        self.buyprice = None
        self.buycomm = None

        self.sma1 = bt.indicators.SimpleMovingAverage(self.datas[0], period=self.params.pfast)
        self.sma2 = bt.indicators.SimpleMovingAverage(self.datas[0], period=self.params.pslow)
        self.crossover = bt.indicators.CrossOver(self.sma1, self.sma2)

    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            return
        if order.status in [order.Completed]:
            if order.isbuy():
                self.log('BUY EXECUTED, Price: %.2f, Cost: %.2f, Comm %.2f' %
                         (order.executed.price,
                          order.executed.value,
                          order.executed.comm))

                self.buyprice = order.executed.price
                self.buycomm = order.executed.comm
            else:  # Sell
                self.log('SELL EXECUTED, Price: %.2f, Cost: %.2f, Comm %.2f' %
                         (order.executed.price,
                          order.executed.value,
                          order.executed.comm))
        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            self.log('Order Canceled/Margin/Rejected')

        self.order = None

    def next(self):
        if self.order:
            return

        if not self.position:
            if self.crossover > 0:
                self.log('BUY CREATE, %.2f' % self.dataclose[0])
                self.order = self.buy()
        else:
            if self.crossover < 0:
                self.log('SELL CREATE, %.2f' % self.dataclose[0])
                self.order = self.sell()

            elif self.dataclose[0] >= self.buyprice * (1.0 + self.params.take_profit):
                self.log('TAKE PROFIT, %.2f' % self.dataclose[0])
                self.order = self.sell()

            elif self.dataclose[0] <= self.buyprice * (1.0 - self.params.stop_loss):
                self.log('STOP LOSS HIT, %.2f' % self.dataclose[0])
                self.order = self.sell()

cerebro = bt.Cerebro()

data = bt.feeds.YahooFinanceCSVData(
    dataname='BTC-USD.csv',
    fromdate=datetime(2020, 1, 1),
    todate=datetime(2022, 12, 31),
)
cerebro.adddata(data)

cerebro.addstrategy(SmaCross)

cerebro.broker.setcash(100000.0)
cerebro.addsizer(bt.sizers.FixedSize, stake=10)

cerebro.addanalyzer(bt.analyzers.SharpeRatio, _name='mysharpe')
cerebro.addanalyzer(bt.analyzers.DrawDown, _name='mydrawdown')
cerebro.addanalyzer(bt.analyzers.TradeAnalyzer, _name='mytrades')

# Run the strategy
results = cerebro.run()

# Get the first (and only) strategy
strategy = results[0]

# Print the analyzers
print('Sharpe Ratio:', strategy.analyzers.mysharpe.get_analysis())
print('Drawdown:', strategy.analyzers.mydrawdown.get_analysis())
print('Trade Analyzer:', strategy.analyzers.mytrades.get_analysis())

# Plot the result
cerebro.plot(style='bar')

