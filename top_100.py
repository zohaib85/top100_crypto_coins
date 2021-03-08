from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, csv

'''Scripts scrapes coinpaprike site to get top 100 crypto metrics and save it to CSV'''

# Add driver to the PATH or point to exe
driver = webdriver.Chrome("C:\\chromedriver_win32\\chromedriver.exe")

# CSV data fields
fields = ["Rank", "Name", "Price", "MTD%", "YTD%", "ATH", "ATH Date", "MarketCap", "Min in Year", "CirculationSupply", "Max"]

# Get latest top 100 crypto endpoints from get_url() function

urls = ['https://coinpaprika.com/coin/btc-bitcoin/', 'https://coinpaprika.com/coin/eth-ethereum/', 
'https://coinpaprika.com/coin/usdt-tether/', 'https://coinpaprika.com/coin/ada-cardano/',
'https://coinpaprika.com/coin/bnb-binance-coin/', 'https://coinpaprika.com/coin/dot-polkadot/',
'https://coinpaprika.com/coin/xrp-xrp/', 'https://coinpaprika.com/coin/ltc-litecoin/', 
'https://coinpaprika.com/coin/link-chainlink/', 'https://coinpaprika.com/coin/bch-bitcoin-cash/',
'https://coinpaprika.com/coin/xlm-stellar/', 'https://coinpaprika.com/coin/uni-uniswap/', 
'https://coinpaprika.com/coin/doge-dogecoin/', 'https://coinpaprika.com/coin/xem-nem/', 
'https://coinpaprika.com/coin/wbtc-wrapped-bitcoin/', 'https://coinpaprika.com/coin/atom-cosmos/', 
'https://coinpaprika.com/coin/okb-okb/', 'https://coinpaprika.com/coin/aave-new/', 
'https://coinpaprika.com/coin/theta-theta-token/', 'https://coinpaprika.com/coin/xmr-monero/',
'https://coinpaprika.com/coin/vet-vechain/', 'https://coinpaprika.com/coin/trx-tron/', 
'https://coinpaprika.com/coin/eos-eos/', 'https://coinpaprika.com/coin/miota-iota/', 
'https://coinpaprika.com/coin/ht-huobi-token/', 'https://coinpaprika.com/coin/bsv-bitcoin-sv/',
'https://coinpaprika.com/coin/luna-terra/', 'https://coinpaprika.com/coin/xtz-tezos/', 
'https://coinpaprika.com/coin/ftt-ftx-token/', 'https://coinpaprika.com/coin/usdc-usd-coin/',
'https://coinpaprika.com/coin/neo-neo/', 'https://coinpaprika.com/coin/cro-cryptocom-chain/', 
'https://coinpaprika.com/coin/dai-dai/', 'https://coinpaprika.com/coin/hex-hex/', 
'https://coinpaprika.com/coin/snx-synthetix-network-token/', 'https://coinpaprika.com/coin/mkr-maker/',
'https://coinpaprika.com/coin/cel-celsius/', 'https://coinpaprika.com/coin/dash-dash/', 
'https://coinpaprika.com/coin/ksm-kusama/', 'https://coinpaprika.com/coin/egld-elrond/',
'https://coinpaprika.com/coin/leo-leo-token/', 'https://coinpaprika.com/coin/dcr-decred/',
'https://coinpaprika.com/coin/comp-compoundd/', 'https://coinpaprika.com/coin/lend-ethlend/',
'https://coinpaprika.com/coin/zec-zcash/', 'https://coinpaprika.com/coin/ethos-ethos/', 
'https://coinpaprika.com/coin/etc-ethereum-classic/', 'https://coinpaprika.com/coin/zil-zilliqa/', 
'https://coinpaprika.com/coin/btt-bittorrent/', 'https://coinpaprika.com/coin/uma-uma/',
'https://coinpaprika.com/coin/dfi-defi-chain/', 'https://coinpaprika.com/coin/algo-algorand/', 
'https://coinpaprika.com/coin/nexo-nexo/', 'https://coinpaprika.com/coin/rvn-ravencoin/', 
'https://coinpaprika.com/coin/enj-enjin-coin/', 'https://coinpaprika.com/coin/yfi-yearnfinance/',
'https://coinpaprika.com/coin/chsb-swissborg/', 'https://coinpaprika.com/coin/waves-waves/', 
'https://coinpaprika.com/coin/zrx-0x/', 'https://coinpaprika.com/coin/bat-basic-attention-token/', 
'https://coinpaprika.com/coin/ren-republic-protocol/', 'https://coinpaprika.com/coin/ftm-fantom/', 
'https://coinpaprika.com/coin/icx-icon/', 'https://coinpaprika.com/coin/fil-filecoin/', 
'https://coinpaprika.com/coin/rune-thorchain/', 'https://coinpaprika.com/coin/hbar-hedera-hashgraph/', 
'https://coinpaprika.com/coin/thr-thorecoin/', 'https://coinpaprika.com/coin/matic-matic-network/', 
'https://coinpaprika.com/coin/ont-ontology/', 'https://coinpaprika.com/coin/stx-blockstack/', 
'https://coinpaprika.com/coin/near-near-protocol/', 'https://coinpaprika.com/coin/dgb-digibyte/', 
'https://coinpaprika.com/coin/busd-binance-usd/', 'https://coinpaprika.com/coin/tfuel-theta-fuel/', 
'https://coinpaprika.com/coin/btcv-bitcoin-vault/', 'https://coinpaprika.com/coin/omg-omg-network/',
'https://coinpaprika.com/coin/nano-nano/', 'https://coinpaprika.com/coin/iost-iost/', 
'https://coinpaprika.com/coin/lrc-loopring/', 'https://coinpaprika.com/coin/avax-avalanche/',
'https://coinpaprika.com/coin/rsr-reserve-rights/', 'https://coinpaprika.com/coin/sol-solana/',
'https://coinpaprika.com/coin/chz-chiliz/', 'https://coinpaprika.com/coin/ttt-the-transfer-token/', 
'https://coinpaprika.com/coin/inb-insight-chain/', 'https://coinpaprika.com/coin/qtum-qtum/', 
'https://coinpaprika.com/coin/ocean-ocean-protocol/', 'https://coinpaprika.com/coin/mana-decentraland/',
'https://coinpaprika.com/coin/bnt-bancor/', 'https://coinpaprika.com/coin/btg-bitcoin-gold/', 
'https://coinpaprika.com/coin/hot-holo/', 'https://coinpaprika.com/coin/btmx-bitmax-token/', 
'https://coinpaprika.com/coin/zen-horizen/', 'https://coinpaprika.com/coin/sc-siacoin/',
'https://coinpaprika.com/coin/npxs-pundi-x/', 'https://coinpaprika.com/coin/ewt-energy-web-token/', 
'https://coinpaprika.com/coin/xdce-xinfin-network/', 'https://coinpaprika.com/coin/ar-arweave/',
'https://coinpaprika.com/coin/best-bitpanda-ecosystem-token/', 'https://coinpaprika.com/coin/qnt-quant/']

def get_urls():
    urls = []
    url = "https://coinpaprika.com/"

    driver.get(url)

    # find pop banner if there
    try:
        pop_up = driver.find_element_by_xpath("//span[@class='icon-cp-plus help-popup__close help-popup__close--photoBanner']").click()
    except Exception as e:
        print(e)

    for i in range(100):
        try:
            element = driver.find_element_by_link_text(str(i+1)).get_attribute("href")
            driver.execute_script("window.scrollTo(0, window.scrollY + 40)")
            time.sleep(3)
            print(element)
            urls.append(str(element))
        except Exception as e:
            print(e)
            continue
    print(urls)
    return urls



def get_data(url):
    data = []

    driver.get(url)
    try:
        pop_up = driver.find_element_by_xpath("//span[@class='icon-cp-plus help-popup__close help-popup__close--photoBanner']").click()
    except Exception as e:
        print(e)

    # coin name
    coin_name = driver.find_element_by_id("redditCoinName")
    print(coin_name.text.strip().split("\n")[0])
    data.append(coin_name.text.strip().split("\n")[-1])
    data.append(coin_name.text.strip().split("\n")[0])

    # coin price
    coin_price = driver.find_element_by_id("coinPrice")
    print(coin_price.text.replace(' ',''))
    data.append(coin_price.text.replace(' ',''))

    # get year % age
    year_percent = driver.find_elements_by_xpath("//div[@class='cp-coin__single-column']")
    for per in year_percent:
        if(per.text.startswith("Year")):
            print(per.text.split('\n')[1])
            data.append(per.text.split('\n')[1])
        if(per.text.startswith("Month")):
            print(per.text.split('\n')[1])
            data.append(per.text.split('\n')[1])

    # all time high
    ath = driver.find_element_by_xpath("//div[@class='cp-coin__bottom-small cp-coin__bottom-small--ath']")
    print(ath.text.split('\n')[0].replace(' ', ''))
    data.append(ath.text.split('\n')[0].replace(' ', ''))
    
    #ath date
    data.append(ath.text.split('\n')[1])

    # market cap
    mc = driver.find_element_by_xpath("//div[@class='cp-coin__bottom-small cp-coin__bottom-small--market-cap']")
    print(mc.text.replace(' ', ''))
    data.append(mc.text.replace(' ', ''))

    # extreme minimum
    ex_minimum = driver.find_element_by_id("currencyChartExtremeMin")
    print(ex_minimum.text.replace(' ', ''))
    data.append(ex_minimum.text.replace(' ', ''))

    # circulating supply
    cs = driver.find_element_by_xpath("//div[@class='cp-coin__bottom-small']")
    print(cs.text.split('\n')[0].replace(' ', ''))
    data.append(cs.text.split('\n')[0].replace(' ', ''))

    # max supply
    print(cs.text.split('\n')[-1].split(':')[-1].replace(' ', ''))
    data.append(cs.text.split('\n')[-1].split(':')[-1].replace(' ', ''))

    return data

#urls = get_urls()

coin_data = []

for url in urls:
    try:
        coin_data.append(get_data(url))
    except Exception as e:
        print(e)
        continue

# write to csv
with open('top100.csv', 'w', newline='') as f: 
    # using csv.writer method from CSV package 
    write = csv.writer(f) 
      
    write.writerow(fields)
    write.writerows(coin_data) 

print(coin_data)
driver.close()