from check_connection import checkconnection
from get_symbols import getsymbols

def main():

    test1=checkconnection()
    getsbl=getsymbols()

 

    while test1.check_conn() != 200 or test1.check_conn() == 200:
            symbols=getsbl.get_symbols()
            for i in range (0,len(symbols['data'])):
                print('Basecurrency: '+ symbols['data'][i]['baseCurrency'])
                print('Status: '+ symbols['data'][i]['status'])
                print('Minimum Order Amount: ' + symbols['data'][i]['minOrderAmount'])
                print('Minimum Order Value: '+ symbols['data'][i]['minOrderValue'])
                print('\n')
            break
            

if __name__=='__main__':
    main()