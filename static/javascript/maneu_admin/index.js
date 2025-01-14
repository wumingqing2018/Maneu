$(document).ready(function () {
    detail_admin()
    $('#update').click(function () {
        $.ajax({
            url: admin_update,
            method: 'GET',
            data: {
                id : admin_id,
                phone: $('#phone').val(),
                nickname: $('#nickname').val(),
                location: $('#location').val(),
                content: $('#content').val()
            },
            success:function (res) {
                alert('修改成功')
            }
        })
    })
    function detail_admin() {
        $.ajax({
            url: admin_detail,
            method: 'GET',
            data: {
                id : admin_id,
            },
            success:function (res) {
                console.log(res)
                $('#time').val(res.data.time)
                $('#phone').val(res.data.phone)
                $('#nickname').val(res.data.nickname)
                $('#location').val(res.data.location)
                $('#content').val(res.data.content)
            }
        })
    }
    function update_admin(){
        $.ajax({
            url: admin_update,
            method: 'GET',
            data: {
                id : admin_id,
                phone: $('#phone').val(),
                nickname: $('#nickname').val(),
                location: $('#location').val(),
                content: $('#content').val()
            },
            success:function (res) {
                console.log(res)
            }
        })
    }
})
