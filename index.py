from flask import Flask , request , jsonify, redirect, url_for
import requests , json , random
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/',methods=["GET"])
def root():
    return redirect('https://pixiv.acerkaio.top/')

@app.route('/uid/<uid>',methods=["GET"])

def uid(uid):

    url = f'https://open.pximg.org/works.php?uid=' + uid
    

    header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                            'Chrome/112.0.0.0 Safari/537.36',
            'cookie': '__yjs_duid=1_b1ac9fc87dce4de5552d7cf0924fb4981686228951567; u=b0281776fd75d3eefeb3562b2a5e6534; '
                        '__bid_n=1889b14047a51b2b754207; '
                        'FPTOKEN=qU+ieOMqkW6y6DlsOZ+D/T'
                        '+SCY6yS3dYvGXKibFoGBijKuUuSbc3ACFDzjlcC18wuDjNLENrw4ktAFAqnl3Akg492Lr4fbvNrkdJ'
                        '/ZQrluIdklkNDAKYnPrpcbe2H9y7AtX+/b+FCTkSTNv5+qB3OtQQ3BXXsEen72oEoAfK+H6'
                        '/u6ltZPdyHttJBJiXEDDS3EiUVt+S2w+8ozXENWbNt/AHeCgNUMmdeDinAKCR+nQSGK/twOoTLOU/nxBeSAazg'
                        '+wu5K8ooRmW00Bk6XAqC4Cb829XR3UinZHRsJxt7q9biKzYQh'
                        '+Yu5s6EHypKwpA6RPtVAC1axxbxza0l5LJ5hX8IxJXDaQ6srFoEzQ92jM0rmDynp+gT'
                        '+3qNfEtB2PjkURvmRghGUn8wOcUUKPOqg==|mfg5DyAulnBuIm/fNO5JCrEm9g5yXrV1etiaV0jqQEw=|10'
                        '|dcfdbf664758c47995de31b90def5ca5; PHPSESSID=18397defd82b1b3ef009662dc77fe210; '
                        'Hm_lvt_de3f6fd28ec4ac19170f18e2a8777593=1686322028,1686360205; '
                        'history=cid%3A2455%2Ccid%3A2476%2Ccid%3A5474%2Ccid%3A5475%2Ccid%3A2814%2Cbid%3A3667; '
                        'Hm_lpvt_de3f6fd28ec4ac19170f18e2a8777593=1686360427'}

    response = requests.get(url, headers=header)
    
    json_object = json.loads(response.text)

    return json_object


@app.route('/rk/<pg>',methods=["GET"])

def rk(pg):

    url = f'https://open.pximg.org/rank.php?p=' + pg
    

    header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                            'Chrome/112.0.0.0 Safari/537.36',
            'cookie': '__yjs_duid=1_b1ac9fc87dce4de5552d7cf0924fb4981686228951567; u=b0281776fd75d3eefeb3562b2a5e6534; '
                        '__bid_n=1889b14047a51b2b754207; '
                        'FPTOKEN=qU+ieOMqkW6y6DlsOZ+D/T'
                        '+SCY6yS3dYvGXKibFoGBijKuUuSbc3ACFDzjlcC18wuDjNLENrw4ktAFAqnl3Akg492Lr4fbvNrkdJ'
                        '/ZQrluIdklkNDAKYnPrpcbe2H9y7AtX+/b+FCTkSTNv5+qB3OtQQ3BXXsEen72oEoAfK+H6'
                        '/u6ltZPdyHttJBJiXEDDS3EiUVt+S2w+8ozXENWbNt/AHeCgNUMmdeDinAKCR+nQSGK/twOoTLOU/nxBeSAazg'
                        '+wu5K8ooRmW00Bk6XAqC4Cb829XR3UinZHRsJxt7q9biKzYQh'
                        '+Yu5s6EHypKwpA6RPtVAC1axxbxza0l5LJ5hX8IxJXDaQ6srFoEzQ92jM0rmDynp+gT'
                        '+3qNfEtB2PjkURvmRghGUn8wOcUUKPOqg==|mfg5DyAulnBuIm/fNO5JCrEm9g5yXrV1etiaV0jqQEw=|10'
                        '|dcfdbf664758c47995de31b90def5ca5; PHPSESSID=18397defd82b1b3ef009662dc77fe210; '
                        'Hm_lvt_de3f6fd28ec4ac19170f18e2a8777593=1686322028,1686360205; '
                        'history=cid%3A2455%2Ccid%3A2476%2Ccid%3A5474%2Ccid%3A5475%2Ccid%3A2814%2Cbid%3A3667; '
                        'Hm_lpvt_de3f6fd28ec4ac19170f18e2a8777593=1686360427'}

    response = requests.get(url, headers=header)
    
    json_object = json.loads(response.text)

    return json_object

@app.route('/pid/<pid>',methods=["GET"])

def pid(pid):

    url = f'https://open.pximg.org/pid.php?pid=' + pid
    

    header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                            'Chrome/112.0.0.0 Safari/537.36',
            'cookie': '__yjs_duid=1_b1ac9fc87dce4de5552d7cf0924fb4981686228951567; u=b0281776fd75d3eefeb3562b2a5e6534; '
                        '__bid_n=1889b14047a51b2b754207; '
                        'FPTOKEN=qU+ieOMqkW6y6DlsOZ+D/T'
                        '+SCY6yS3dYvGXKibFoGBijKuUuSbc3ACFDzjlcC18wuDjNLENrw4ktAFAqnl3Akg492Lr4fbvNrkdJ'
                        '/ZQrluIdklkNDAKYnPrpcbe2H9y7AtX+/b+FCTkSTNv5+qB3OtQQ3BXXsEen72oEoAfK+H6'
                        '/u6ltZPdyHttJBJiXEDDS3EiUVt+S2w+8ozXENWbNt/AHeCgNUMmdeDinAKCR+nQSGK/twOoTLOU/nxBeSAazg'
                        '+wu5K8ooRmW00Bk6XAqC4Cb829XR3UinZHRsJxt7q9biKzYQh'
                        '+Yu5s6EHypKwpA6RPtVAC1axxbxza0l5LJ5hX8IxJXDaQ6srFoEzQ92jM0rmDynp+gT'
                        '+3qNfEtB2PjkURvmRghGUn8wOcUUKPOqg==|mfg5DyAulnBuIm/fNO5JCrEm9g5yXrV1etiaV0jqQEw=|10'
                        '|dcfdbf664758c47995de31b90def5ca5; PHPSESSID=18397defd82b1b3ef009662dc77fe210; '
                        'Hm_lvt_de3f6fd28ec4ac19170f18e2a8777593=1686322028,1686360205; '
                        'history=cid%3A2455%2Ccid%3A2476%2Ccid%3A5474%2Ccid%3A5475%2Ccid%3A2814%2Cbid%3A3667; '
                        'Hm_lpvt_de3f6fd28ec4ac19170f18e2a8777593=1686360427'}

    response = requests.get(url, headers=header)
    
    json_object = json.loads(response.text.replace("https:\/\/i.pximg.net", "https:\/\/i.pixiv.re"))

    
    return json_object

@app.route('/rd',methods=["GET"])

def pid(pid):

    url = f'https://data.acerkaio.top/elaina.json'
    

    header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                            'Chrome/112.0.0.0 Safari/537.36',
            'cookie': '__yjs_duid=1_b1ac9fc87dce4de5552d7cf0924fb4981686228951567; u=b0281776fd75d3eefeb3562b2a5e6534; '
                        '__bid_n=1889b14047a51b2b754207; '
                        'FPTOKEN=qU+ieOMqkW6y6DlsOZ+D/T'
                        '+SCY6yS3dYvGXKibFoGBijKuUuSbc3ACFDzjlcC18wuDjNLENrw4ktAFAqnl3Akg492Lr4fbvNrkdJ'
                        '/ZQrluIdklkNDAKYnPrpcbe2H9y7AtX+/b+FCTkSTNv5+qB3OtQQ3BXXsEen72oEoAfK+H6'
                        '/u6ltZPdyHttJBJiXEDDS3EiUVt+S2w+8ozXENWbNt/AHeCgNUMmdeDinAKCR+nQSGK/twOoTLOU/nxBeSAazg'
                        '+wu5K8ooRmW00Bk6XAqC4Cb829XR3UinZHRsJxt7q9biKzYQh'
                        '+Yu5s6EHypKwpA6RPtVAC1axxbxza0l5LJ5hX8IxJXDaQ6srFoEzQ92jM0rmDynp+gT'
                        '+3qNfEtB2PjkURvmRghGUn8wOcUUKPOqg==|mfg5DyAulnBuIm/fNO5JCrEm9g5yXrV1etiaV0jqQEw=|10'
                        '|dcfdbf664758c47995de31b90def5ca5; PHPSESSID=18397defd82b1b3ef009662dc77fe210; '
                        'Hm_lvt_de3f6fd28ec4ac19170f18e2a8777593=1686322028,1686360205; '
                        'history=cid%3A2455%2Ccid%3A2476%2Ccid%3A5474%2Ccid%3A5475%2Ccid%3A2814%2Cbid%3A3667; '
                        'Hm_lpvt_de3f6fd28ec4ac19170f18e2a8777593=1686360427'}

    response = requests.get(url, headers=header)
    text = response.text
    res = json.loads(text)
    number = random.randint(0,(len(res) - 1))
    result = res[number]
    fina_res = json.dumps(result,ensure_ascii=False)

    return fina_res
