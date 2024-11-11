$(document).ready(function () {
    $('.delete').click(function () {
        return confirm("确定要删除吗？");
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
                    $('#dfh').text(res.data.dfh)
                    $('#sex').text(res.data.sex)
                    $('#ot').text(res.data.ot)
                    $('#em').text(res.data.em)
                    $('#remark').text(res.data.remark)

                }
            }
        })
    }

    guest_detail(guest_id)
})