from re import I

from cv2 import exp
from import_module import *

def buycoin_market(target_item, buy_amout):
        try:
                query = {
                        'market': target_item,
                        'side': 'bid',
                        'ord_type': 'price',
                        'price': buy_amout,
                }

                query_string = urlencode(query).encode()

                m = hashlib.sha512()
                m.update(query_string)
                query_hash = m.hexdigest()

                payload = {
                        'access_key': access_key,
                        'nonce': str(uuid.uuid4()),
                        'query_hash': query_hash,
                        'query_hash_alg': 'SHA512',
                }

                jwt_token = str(jwt.encode(payload, secret_key))
                authorization_token = 'Bearer {}'.format(jwt_token)
                headers = {"Authorization": authorization_token}

                res = requests.post(server_url + "/v1/orders", params=query, headers=headers)
                logging.info("")
                logging.info("----------------------------------------------")
                logging.info("시장가 매수 완료!")
                logging.info(res)
                logging.info("----------------------------------------------")

                return res
        except Exception:
                raise
def get_balance(target_item):
        try:
                ret_balance = 0
                max_count = 0

                payload = {
                        'access_key': access_key,
                        'nonce': str(uuid.uuid4()),
                }

                jwt_token = str(jwt.encode(payload, secret_key))
                authorization_token = 'Bearer {}'.format(jwt_token)
                headers = {"Authorization": authorization_token}

                while True:
                        max_count = max_count + 1
                        res = requests.get(server_url + "/v1/accounts", headers=headers)
                        my_asset = res.json()

                        for myasset in my_asset:
                                if myasset['currency'] == target_item.split('-')[1]:
                                        ret_balance = myasset['balance']

                        if Decimal(str(ret_balance)) > Decimal(str(0)):
                                break

                        if max_count > 100:
                                break

                        logging.info("[주문가능 잔고 리턴용] 요청 재처리중...")
                
                return ret_balance

        except Exception:
                raise

def sellcoin_market(target_item):
        try:
                current_balance = get_balance(target_item)
                query = {
                        'market': target_item,
                        'side': 'ask',
                        'ord_type': 'market',
                        'volume': current_balance,
                }

                query_string = urlencode(query).encode()

                m = hashlib.sha512()
                m.update(query_string)
                query_hash = m.hexdigest()

                payload = {
                        'access_key': access_key,
                        'nonce': str(uuid.uuid4()),
                        'query_hash': query_hash,
                        'query_hash_alg': 'SHA512',
                }

                jwt_token = str(jwt.encode(payload, secret_key))
                authorization_token = 'Bearer {}'.format(jwt_token)
                headers = {"Authorization": authorization_token}
                res = requests.post(server_url + "/v1/orders", params=query, headers=headers)
                logging.info("시장가 매도 완료")
                logging.info(res)

                return res
        except Exception:
                raise
