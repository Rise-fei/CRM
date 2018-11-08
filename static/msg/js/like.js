$(".like-img").click(function () {
    addZanStyle(this);
    $(".like-img").css({"display": "none"});
})
$(".dislike-img").click(function () {
    addZanStyle(this);
})

function addZanStyle(self) {
    var sp = document.createElement('span');
    var top = 0;
    var left = 0;
    var fontSize = 15;
    var opacity = 1;
    $(sp).text('+1');
    $(sp).css('top', top + 'px');
    $(sp).css('left', left + 'px');
    $(sp).css('fontSize', fontSize + 'px');
    $(sp).css('opacity', opacity);
    $(sp).css('color', 'green');
    $(sp).css('position', 'absolute');
    $(self).append(sp);
    var inte = setInterval(function () {
        top = top - 13;
        left = left + 10;
        opacity = opacity - 0.2;
        fontSize = fontSize + 5;
        $(sp).css('top', top + 'px');
        $(sp).css('left', left + 'px');
        $(sp).css('fontSize', fontSize + 'px');
        $(sp).css('opacity', opacity);
        if (opacity < 0) {
            clearInterval(inte);
            $(sp).remove();
        }
    }, 100);

}
