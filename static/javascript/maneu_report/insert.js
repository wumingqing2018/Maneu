$(document).ready(function () {
    $('#insert').click(function () {
        $.ajax({
            url: api_insert,
            method: "GET",
            data:{

            }
        })
    })
})