// $(".btn_inquiry").click(function () {
//     var search_key = $("#search_key").val();
//     var select = document.getElementById("select_text");
//     var options = select.options;
//     var index = select.selectedIndex;
//     var selectText = options[index].text;
//     alert("ok");
//     if (search_key) {
//         $.ajax({
//             url: "/wang/check_all/",
//             data: {
//                 "search_key": search_key,
//                 "selectText": selectText,
//             },
//             type: "post",
//             dataType: "json",
//             success: function (data) {
//                 alert("OK")
//             }
//             })
//     } else {
//         alert("NB");
//         parent.document.location.href = "/wang/journal/";
//     }
//
// });