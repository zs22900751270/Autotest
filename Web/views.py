from django.shortcuts import render
from django.http import HttpResponse
from Web import models
import json
from AppTest.TestRunner import *

# Create your views here.


def index(request):
    """index.html"""
    all_case_number = get_test_case_number(request)
    return render(request, "index.html", {"all_case_number": all_case_number})


def start(request):
    """start 'testRunner.py'"""
    try:
        name_list_str = request.POST.get("test_number")
        res = write_case(request, name_list_str)
        print(res)
        start_py_path = project_path + "/TestRunner.py"
        os.system("python %s" % start_py_path)
        res_json = json.dumps({"run_res": "运行成功", "write_res": res})
        return HttpResponse(res_json)
    except:
        res_json = json.dumps({"run_res": "运行失败", "write_res": res})
        return HttpResponse(res_json)


def get_test_case_number(request):
    """get all test case number"""
    all_case_number = []
    test_case_path = project_path + "/testCase"
    sprint_list = os.listdir(test_case_path)
    for sprint_name in sprint_list:
        if "Sprint" in sprint_name:
            case_number_path = test_case_path + "/" + sprint_name
            case_list = os.listdir(case_number_path)
            for case_name in case_list:
                if "case_Sprint" in case_name:
                    all_case_number.append(case_name)
    return all_case_number


def write_case(request, name_list_str):
    """add case number in caselist"""
    try:
        case_list_path = project_path + "/caselist.txt"
        print(case_list_path)
        case_list = name_list_str[2:-2].split('","')
        with open(case_list_path, "w") as f:
            for case_name in case_list:
                f.write(case_name + "\n")
        return "用例编号写入成功"
    except:
        return "用例编号写入失败"


def open_result(request):
    """display test result"""
    config = configparser.ConfigParser()
    config.read("config.ini")
    srceen_shot_path = config.get("report", "report_path")
    return HttpResponse(srceen_shot_path)


def search(request):
    """"""
    key = request.GET.get("searchNumberInput")
    # print(key)
    if key == "":
        all_case_number = get_test_case_number(request)
        return render(request, "index.html", {"all_case_number": all_case_number})
    elif ";" not in key:
        case_list = []
        all_case_number = get_test_case_number(request)
        for i in all_case_number:
            if key in i:
                case_list.append(i)
        return render(request, "index.html", {"all_case_number": case_list})
    else:
        case_list = key.split(";")
        return render(request, "index.html", {"all_case_number": case_list})







