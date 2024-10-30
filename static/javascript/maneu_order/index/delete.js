function deleteBtn(obj) {
    if (confirm("您确定要删除吗？")) {
        $.ajax({
            url: api_delete,
            type: 'GET',
            data: {
                order_id: obj.alt,
            },
            success: function (res) {
                if (res.status === true){
                    obj.parentElement.parentElement.parentElement.parentElement.remove()
                }else {
                    alert(res.message)
                }
            },
        })
    } else {
        return false;
    }
}
