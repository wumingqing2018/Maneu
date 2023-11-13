function serviceUpdate(obj) {
    $.ajax({
        url: service_update,
        type: 'POST',
        data: {
            "id": obj.nextElementSibling.value,
            "content": obj.previousElementSibling.value,
            "csrfmiddlewaretoken": $("[name='csrfmiddlewaretoken']").val()
        },
        success:function (res) {
            alert('更新成功')
        }
    })
}