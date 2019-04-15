$(document).ready(function () {
    $("#start").click(function () {
        var case_list = new Array();
        $("[id=case_number]:checked").each(function () {
            case_list.push($(this).val())
            $("#caseLen").html(case_list.length)
        })
        $.post("/start/", {"test_number": JSON.stringify(case_list)},  function (ret) {
            ret = JSON.parse(ret)
            $("#result2").html(ret["run_res"])
            $("#report").html("可复制下方路径打开测试报告")
        })
    })
})
$(document).ready(function () {
    $("#report_path").click(function () {
        var res = $("#report").text()
        if(res=="运行中，莫慌"){
            alert("运行未完成")
        }else{
            $.get("/open_result/", function (path) {
            $("#report_path").html(path)
        })}
    })
})
$(document).ready(function(){
    $("#allSelect").click(function(){
        $("[id=case_number]").each(function () {
            $("input:checkbox").prop("checked", true);
        })
    })
})
$(document).ready(function(){
    $("#cancelAllSelect").click(function(){
        $("[id=case_number]").each(function () {
            $("input:checkbox").prop("checked", false);
        })
    })
})
$(document).ready(function() {
    $("#toEnd").click(function () {
        $('html,body').animate({scrollTop: $("#toTop").offset().top}, 1600);
    })
})
$(document).ready(function() {
    $("#toTop").click(function () {
        $('html,body').animate({scrollTop:$("#toEnd").offset().top}, 1600);
    })
})
