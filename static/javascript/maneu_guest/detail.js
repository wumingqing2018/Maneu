$(document).ready(function () {
    $('.delete').click(function () {
        if (confirm("确定要删除吗？")) {
            guest_delete(guest_id);
        } else {
            return false;
        }
    })

    function guest_detail(guest_id) {
        $.ajax({
            url: api_detail,
            method: 'GET',
            data: {
                id: guest_id
            },
            success: function (res) {
                if (res.status === true) {
                    console.log(res)
                    $('#time').text(res.data.time)
                    $('#name').text(res.data.name)
                    $('#call').text(res.data.phone)
                    $('#age').text(res.data.age)
                    $('#DFH').text(res.data.dfh)
                    $('#sex').text(res.data.sex)
                    $('#OT').text(res.data.ot)
                    $('#EM').text(res.data.em)
                    $('#remark').text(res.data.remark)
                } else {
                    console.log(res.message)
                }
            }
        })
    }

    function guest_delete(guest_id) {
        $.ajax({
            url: api_delete,
            method: 'GET',
            data: {
                id: guest_id
            },
            success: function (res) {
                if (res.status === true) {
                    alert("删除成功，即将跳转到列表页。")
                    window.location.href = web_detail
                } else {
                    console.log(res.message)
                }
            }
        })
    }


    guest_detail(guest_id)
})