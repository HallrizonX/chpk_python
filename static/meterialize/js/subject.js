$(document).ready(function () {
    startTime();
    // Left menu tooltips
    $('.tooltipped').tooltip({
        'inDuration': 100,
        'outDuration': 100,
    });

    // search
    $('body').on('input', '#input-search', function () {
        var val = $(this).val();
        console.log(val);
        $.ajax({
            type: 'GET',
            url: '/api/find.subject/',
            data: {"text": val},
            success: function (data) {
                $(".subject-table-body").html("");
            }
        }).then(function (data) {
            $(".subject-table-body").append(data);
        })
    })
});

// head time
function startTime() {
    var today = new Date();
    var h = today.getHours();
    var m = today.getMinutes();
    var s = today.getSeconds();
    m = checkTime(m);
    s = checkTime(s);
    document.getElementById('time-head').innerHTML =
        h + ":" + m + ":" + s;
    var t = setTimeout(startTime, 500);
}

function checkTime(i) {
    if (i < 10) {
        i = "0" + i
    }
    // add zero in front of numbers < 10
    return i;
}