function serviceDelete(obj) {
    if (confirm("您确定要删除吗？")) {
        $.ajax({
            url: service_delete,
            type: 'POST',
            data: {
                "id": obj.previousElementSibling.value,
                "csrfmiddlewaretoken": $("[name='csrfmiddlewaretoken']").val()
            },
            success: function (res) {
                obj.parentElement.remove()
            }
        })
    } else {
        return false;
    }
}