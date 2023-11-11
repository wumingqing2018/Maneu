function serviceDelete(obj){
    console.log(obj.alt)
    $.ajax({
        url: service_delete,
        type: 'POST',
        data: {
            "id": obj.alt,
            "csrfmiddlewaretoken": $("[name='csrfmiddlewaretoken']").val()
        },
        success: function (res) {
            obj.parentElement.parentElement.parentElement.parentElement.remove()
        }
    })
}