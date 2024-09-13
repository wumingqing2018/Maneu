$(function () {
    var start = moment().subtract(29, 'days');
    var end = moment();
    var myChart = echarts.init(document.getElementById('main1'), 'maneu');

    function cb(start, end) {
        $('#reportrange span').html(start.format('MMMM D, YYYY') + ' - ' + end.format('MMMM D, YYYY'));
        $('#body').empty();
        $.ajax({
                url: api_index,
                type: 'GET',
                data: {
                    start_day: start.format('YYYY-MM-DD'),
                    end_day: end.format('YYYY-MM-DD'),
                    start: start.format('YYYY-MM-DD 00:00:00'),
                    end: end.format('YYYY-MM-DD 23:59:59'),
                },
                success: function (res) {
                    console.log(res)
                    // 使用刚指定的配置项和数据显示图表。
                    var option = {
                        title: {
                            show: true, //显示策略，默认值true,可选为：true（显示） | false（隐藏）
                            // text: '零售数据：'+ res.count +'单\n\n新增客户：'+ res.count1 +'位' , //主标题文本，'\n'指定换行
                            link: '', //主标题文本超链接,默认值true
                            target: null, //指定窗口打开主标题超链接，支持'self' | 'blank'，不指定等同为'blank'（新窗口）
                            x: 'left', //水平安放位置，默认为'left'，可选为：'center' | 'left' | 'right' | {number}（x坐标，单位px）
                            y: 'top', //垂直安放位置，默认为top，可选为：'top' | 'bottom' | 'center' | {number}（y坐标，单位px）
                            textAlign: null,//水平对齐方式，默认根据x设置自动调整，可选为： left' | 'right' | 'center
                            backgroundColor: 'rgba(0,0,0,0)', //标题背景颜色，默认'rgba(0,0,0,0)'透明
                            borderColor: '#ccc', //标题边框颜色,默认'#ccc'
                            borderWidth: 0, //标题边框线宽，单位px，默认为0（无边框）
                            padding: 0, //标题内边距，单位px，默认各方向内边距为5，接受数组分别设定上右下左边距
                            itemGap: 10, //主副标题纵向间隔，单位px，默认为10
                            textStyle: { //主标题文本样式{"fontSize": 18,"fontWeight": "bolder","color": "#333"}
                                fontSize: 20,
                                fontStyle: 'normal',
                                fontWeight: 'normal',
                            },
                        },
                        tooltip: {},
                        legend: {
                            data: ['零售数据', '客户数据']
                        },
                        xAxis: {
                            data: res.time_list
                        },
                        yAxis: {},
                        series: [{
                            name: '零售数据',
                            type: 'line',
                            data: res.time_newList,
                        }, {
                            name: '客户数据',
                            type: 'line',
                            data: res.time_newList1,
                        }]
                    };
                    myChart.setOption(option);
                }
            }
        );
    }

    $('#reportrange').daterangepicker({
        startDate: start,
        endDate: end,
        ranges: {
            // 'Today': [moment(), moment()],
            // 'Yesterday': [moment().subtract(1, 'days'), moment().subtract(1, 'days')],
            '今天': [moment(), moment()],
            '昨天': [moment().subtract(1, 'days'), moment().subtract(1, 'days')],
            '七天内': [moment().subtract(6, 'days'), moment()],
            '三十天内': [moment().subtract(29, 'days'), moment()],
            '本月': [moment().startOf('month'), moment().endOf('month')],
            '上月': [moment().subtract(1, 'month').startOf('month'), moment().subtract(1, 'month').endOf('month')]
        }
    }, cb);
    cb(start, end);
});
