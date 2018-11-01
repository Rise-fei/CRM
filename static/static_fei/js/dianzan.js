$(function () {
    $(".like-img").click(function () {
        var user = $('#a_user').text();
        var article = $(this).parent().next().text();
        var up = $(this).parent().parent().prev().children(".up-count");
        var down = $(this).parent().parent().parent().next().children(":first-child").children(":first-child");
        var islike = $(this).parent().parent().parent().next().next().children(":last-child").children(":last-child");
        // {#alert($("[name='csrfmiddlewaretoken']").val())#}
        // {#alert(down.text())#}
        // 2. 用AJAX发送到服务端
        $.ajax({
            url: "/up_count/",
            type: "post",
            data: {
                "user": user,
                "article": article,
                "csrfmiddlewaretoken":$("[name='csrfmiddlewaretoken']").val()
            },
            success: function (data) {
                // alert("nohao");
                // console.log('dsafds');
                if (!data.error) {
                    alert("请先登录再操作");
                }
                else {
                    down.text(data['count-down']);
                    up.text(data['count-up']);
                    // {#alert(data['is_up'])#}
                    if (data["is_up"]) {

                        alert('已经点过赞，不能再点了');
                        islike.text("已点赞");
                        islike.css({"color": "red"})
                    } else {
                        alert('点赞成功');
                        islike.text("已点赞");
                        islike.css({"color": "red"})

                    }
                    setTimeout(function () {
                        islike.text(" ")
                    }, 2000)
                }

            }

        })
    });
    $(".dislike-img").click(function () {
        var user = $('#a_user').text();
        var article = $(this).parent().next().text();
        var down = $(this).parent().parent().prev().children(".down-count");
        var up = $(this).parent().parent().parent().prev().children(":first-child").children(":first-child");
        var islike = $(this).parent().parent().parent().next().children(":last-child").children(":last-child");
        // 2. 用AJAX发送到服务端
        $.ajax({
            url: "/down_count/",
            type: "post",
            data: {
                "user": user,
                "article": article,
                // {#"csrfmiddlewaretoken": $("[name='csrfmiddlewaretoken']").val()#}
            },
            success: function (data) {
                 if (!data.error) {
                    alert("请先登录再操作");
                }
                else{
                      up.text(data['count-up']);
                down.text(data['count-down']);
                if (data["is_up"]) {
                    islike.text("已踩");
                    alert('已经踩过，不能再踩了');
                    islike.css({"color": "red"});
                } else {
                    alert('踩成功');
                    islike.text("已踩");
                    islike.css({"color": "red"})
                }
                setTimeout(function () {
                    islike.text(" ")
                }, 2000)
                 }

            }


        })
    });

})