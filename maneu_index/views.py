import json

from django.shortcuts import render
from maneu.models import *


def index1(request):
    ManeuReport.objects.filter().all().delete()
    tableList = [ManeuRefraction.objects.filter().all(),
                 ManeuSubjectiveRefraction.objects.filter().all(),
                 ManeuVision.objects.filter().all(),
                 ManeuVisionSolutions.objects.filter().all()]
    for data in tableList:
        for i in data:
            if i.guess_id:
                guest = ManeuGuess.objects.filter(id=i.guess_id).first()
                if guest and i.content:
                    content = json.loads(i.content)
                    data = {"OD": {}, "OS": {}, "PD":"", "Function": ""}
                    try:
                        remark = content["remark"]
                    except:
                        remark = ""
                    try:
                        data["PD"] = content["pd"]
                    except:
                        data["PD"] = ""
                    try:
                        data["Function"] = content["function"]
                    except:
                        data["Function"] = ""
                    try:
                        data["OD"]["VA"] = content["OD_VA"]
                    except:
                        data["OD"]["VA"] = "0"
                    try:
                        data["OD"]["SPH"] = content["OD_SPH"]
                    except:
                        data["OD"]["SPH"] = "0"
                    try:
                        data["OD"]["CYL"] = content["OD_CYL"]
                    except:
                        data["OD"]["CYL"] = "0"
                    try:
                        data["OD"]["AX"] = content["OD_AX"]
                    except:
                        data["OD"]["AX"] = "0"
                    try:
                        data["OD"]["BCVA"] = content["OD_BCVA"]
                    except:
                        data["OD"]["BCVA"] = "0"
                    try:
                        data["OD"]["AL"] = content["OD_AL"]
                    except:
                        data["OD"]["AL"] = "0"
                    try:
                        data["OD"]["AK"] = content["OD_AK"]
                    except:
                        data["OD"]["AK"] = "0"
                    try:
                        data["OD"]["AD"] = content["OD_AD"]
                    except:
                        data["OD"]["AD"] = "0"
                    try:
                        data["OD"]["CCT"] = content["OD_CCT"]
                    except:
                        data["OD"]["CCT"] = "0"
                    try:
                        data["OD"]["LT"] = content["OD_LT"]
                    except:
                        data["OD"]["LT"] = "0"
                    try:
                        data["OD"]["VT"] = content["OD_VT"]
                    except:
                        data["OD"]["VT"] = "0"
                    try:
                        data["OD"]["PR"] = content["OD_PR"]
                    except:
                        data["OD"]["PR"] = "0"
                    try:
                        data["OD"]["FR"] = content["OD_FR"]
                    except:
                        data["OD"]["FR"] = "0"
                    try:
                        data["OD"]["ADD"] = content["OD_ADD"]
                    except:
                        data["OD"]["ADD"] = "0"

                    try:
                        data["OS"]["VA"] = content["OS_VA"]
                    except:
                        data["OS"]["VA"] = "0"
                    try:
                        data["OS"]["SPH"] = content["OS_SPH"]
                    except:
                        data["OS"]["SPH"] = "0"
                    try:
                        data["OS"]["CYL"] = content["OS_CYL"]
                    except:
                        data["OS"]["CYL"] = "0"
                    try:
                        data["OS"]["AX"] = content["OS_AX"]
                    except:
                        data["OS"]["AX"] = "0"
                    try:
                        data["OS"]["BCVA"] = content["OS_BCVA"]
                    except:
                        data["OS"]["BCVA"] = "0"
                    try:
                        data["OS"]["AL"] = content["OS_AL"]
                    except:
                        data["OS"]["AL"] = "0"
                    try:
                        data["OS"]["AK"] = content["OS_AK"]
                    except:
                        data["OS"]["AK"] = "0"
                    try:
                        data["OS"]["AD"] = content["OS_AD"]
                    except:
                        data["OS"]["AD"] = "0"
                    try:
                        data["OS"]["CCT"] = content["OS_CCT"]
                    except:
                        data["OS"]["CCT"] = "0"
                    try:
                        data["OS"]["LT"] = content["OS_LT"]
                    except:
                        data["OS"]["LT"] = "0"
                    try:
                        data["OS"]["VT"] = content["OS_VT"]
                    except:
                        data["OS"]["VT"] = "0"
                    try:
                        data["OS"]["PR"] = content["OS_PR"]
                    except:
                        data["OS"]["PR"] = "0"
                    try:
                        data["OS"]["FR"] = content["OS_FR"]
                    except:
                        data["OS"]["FR"] = "0"
                    try:
                        data["OS"]["ADD"] = content["OS_ADD"]
                    except:
                        data["OS"]["ADD"] = "0"
                    try:
                        ManeuReport.objects.create(id=i.id, guest_id=i.guess_id, admin_id=i.admin_id, time=i.time,
                                                   name=guest.name, phone=guest.phone, remark=remark,
                                                   content=json.dumps(data))

                    except:
                        report = ManeuReport.objects.filter(id=i.id).first()
                        report_data = json.loads(report.content)
                        report_data.update(data)
                        ManeuReport.objects.filter(id=i.id).update(content=json.dumps(report_data))

    return render(request, 'maneu/base.html')


def index2(request):
    ManeuGuest.objects.filter().all().delete()
    tableList = [ManeuGuess.objects.filter().all(),
                 ManeuGuessV2.objects.filter().all()]
    for data in tableList:
        for i in data:
            try:
                ManeuGuest.objects.create(id=i.id, admin_id=i.admin_id, time=i.time, name=i.name, phone=i.phone, remark=i.remark, age=i.age, dfh=i.dfh, sex=i.sex, ot=i.ot, em=i.em)
            except:
                ManeuGuest.objects.filter(id=i.id).update(admin_id=i.admin_id, time=i.time, name=i.name, phone=i.phone, remark=i.remark, age=i.age, dfh=i.dfh, sex=i.sex, ot=i.ot, em=i.em)

    return render(request, 'maneu/base.html')

def index3(request):

    ManeuAdmin.objects.filter(id='36483774080401481140071775853431').update(id='f8e85e26-36cf-11ee-954d-e0d55ebbde98')
    ManeuAdmin.objects.filter(id='23208668181988748078136965958996').update(id='086fd1ef-4aca-11ed-a8ac-00163e02ac92')

    ManeuGuest.objects.filter(admin_id='36483774080401481140071775853431').update(admin_id='f8e85e26-36cf-11ee-954d-e0d55ebbde98')
    ManeuGuest.objects.filter(admin_id='23208668181988748078136965958996').update(admin_id='086fd1ef-4aca-11ed-a8ac-00163e02ac92')
    ManeuReport.objects.filter(admin_id='36483774080401481140071775853431').update(admin_id='f8e85e26-36cf-11ee-954d-e0d55ebbde98')
    ManeuReport.objects.filter(admin_id='23208668181988748078136965958996').update(admin_id='086fd1ef-4aca-11ed-a8ac-00163e02ac92')
    ManeuStore.objects.filter(admin_id='36483774080401481140071775853431').update(admin_id='f8e85e26-36cf-11ee-954d-e0d55ebbde98')
    ManeuStore.objects.filter(admin_id='23208668181988748078136965958996').update(admin_id='086fd1ef-4aca-11ed-a8ac-00163e02ac92')
    ManeuService.objects.filter(admin_id='36483774080401481140071775853431').update(admin_id='f8e85e26-36cf-11ee-954d-e0d55ebbde98')
    ManeuService.objects.filter(admin_id='23208668181988748078136965958996').update(admin_id='086fd1ef-4aca-11ed-a8ac-00163e02ac92')
    ManeuOrder.objects.filter(admin_id='36483774080401481140071775853431').update(admin_id='f8e85e26-36cf-11ee-954d-e0d55ebbde98')
    ManeuOrder.objects.filter(admin_id='23208668181988748078136965958996').update(admin_id='086fd1ef-4aca-11ed-a8ac-00163e02ac92')
    ManeuUsers.objects.filter(id='36483774080401481140071775853431').update(id='f8e85e26-36cf-11ee-954d-e0d55ebbde98')
    ManeuUsers.objects.filter(id='23208668181988748078136965958996').update(id='086fd1ef-4aca-11ed-a8ac-00163e02ac92')
