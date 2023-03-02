import pyupbit

#기본 정보 셋팅
print('API를 입력해주세요')
print('')
access = input('access(api)_key : ')       # 본인 값으로 변경
secret = input('secret_key : ')         # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)
print('')

#---코인종목 진입비율 설정
symbol0 =input('종목 입력 (EX:KRW-BTC): ') # symbol0=코인
input_rate= int(input('진입비율 입력: '))
print('')

#현재가 
coin_last=float(pyupbit.get_current_price(symbol0))
print('현재가: {}'.format(coin_last))

#지갑 잔고 불러오기
balance_wallet = upbit.get_balance("KRW")
print('')
print('현재 잔고를 알려드립니다.:', end=' ')
print(balance_wallet)
print('')

# 주문량 (수수료 0.05%이므로 0.1로 계산해서 차감)
amount0=float(((balance_wallet)*float(input_rate-0.1))/(100*coin_last))
#전체 주문 금액
order_price= (amount0*coin_last)

#매수
B=0
while True:
    if B==1:
        print('현재 지갑 잔고')
        print(balance_wallet)
        print('현재가: {}'.format(coin_last))
        print('')
        print('1:매수, 2:매도')
        A=int(input('매수주문을 체결할게요 1을 눌러주세요: '))
    if A ==1 :
        print('매수완료')
        print('')
        print('매수가: {}'.format(coin_last))
        print('')
        order = upbit.buy_market_order(symbol0, order_price)
        A=int(input('매도주문을 체결할게요 2을 눌러주세요: '))
        print('')
#매도
        if A == 2:
            print('매도가: {}'.format(coin_last))
            print('')
            order = upbit.sell_market_order(symbol0, amount0)
            print('매도 완료')
            print('')
            A=int(input('거래를 멈추겠습니까?(비동의 1 입력): '))
            print('')
            if A == 1:
                B = 1
                continue
            else:
                break
    else:
        print('1 입력해')
        print('다시 물어볼게')
        print('')
        continue