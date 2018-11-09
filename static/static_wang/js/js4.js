$("#checkbox_on").click(function () {
    // 判断是否已全部选中
    if ($("input[type='checkbox']").is(':checked')) {
        // 如果没有全部选中或已全选，点击则取消已选择的checkbox
        $("input[name='onclick_checkbox']:checkbox").each(function () {
            $(this).prop("checked", false);
        });
    } else {
        // 如果都没有选中的话，点击则全部选上
        $("input[name='onclick_checkbox']:checkbox").each(function () {
            $(this).prop("checked", true);
        });
    }
});
$("#many_del").click(function () {
    var check_obj = document.getElementsByName("onclick_checkbox");
    var check_val = [];
    for (k in check_obj) {
        if (check_obj[k].checked)
            check_val.push(check_obj[k].value);
    }
    if ($("input[type='checkbox']").is(':checked')) {
        $.ajax({
            url: "/wang/del_all4/",
            data: {'check_val': check_val},
            type: "post",
            dateType:"json",
            traditional:true,
            success: function (data) {
                location.href="/wang/task/";
                alert("删除成功")
            }
        })
    }
    else {
        alert("没有被选中")
    }
});

