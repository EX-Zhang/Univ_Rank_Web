function setupChart(chart_data) {


    var myChart = echarts.init(document.getElementById('main'));

    myChart.setOption(chart_data);

}

function GET_Univ_Data() {

    var start = document.getElementById("Data_Start").value;

    var end = document.getElementById("Data_End").value;

    var data_type = $('#data_type').val();

    var lang = $('input:radio[name=Lang]:checked').val();

    if (!Valid_Input(start, end)) {
        return;
    }

    var url = "/requestData";

    $.get(url, { start: start, end: end, data_type: data_type, lang: lang }, function (data) {

        if (data.statue == "Valid" && data_type == "pie_chart") {

            setupChart($.parseJSON(data.data));

        }
        else if (data.statue == "Valid" && data_type == "table") {

            $('#main').html(generate_table(data.data));

            $('#UnivRankTable').slice(10).hide();

        }
        else {

            Setup_btn_tooltip("Input Number out of Range");

        }

    });

}

function Valid_Input(start, end) {

    var btn = $("#submit_range_btn");

    if (typeof (btn.attr('data-bs-original-title')) != 'undefined' && btn.attr('data-bs-original-title') != false) {

        btn.removeAttr('data-bs-original-title');

    }

    if (typeof (btn.attr('title')) != 'undefined' && btn.attr('title') != false) {

        btn.removeAttr('title');

    }

    if (typeof (btn.attr('aria-describedby')) != 'undefined' && btn.attr('aria-describedby') != false) {

        $("#" + btn.attr('aria-describedby')).remove();

        btn.removeAttr('aria-describedby');

    }

    btn.tooltip('dispose');

    if (start.length <= 0 || end.length <= 0) {

        Setup_btn_tooltip("Please Input a Range");

        return false;

    }

    if (isNaN(Number(start)) || isNaN(Number(end))) {

        Setup_btn_tooltip("Please Input Valid Number");

        return false;

    }

    return true;

}

function Setup_btn_tooltip(tip_msg) {

    var btn = $("#submit_range_btn");



    btn.tooltip({

        placement: 'bottom',

        trigger: 'focus',

        title: tip_msg

    });

    btn.tooltip('show');

}

function generate_table(table_data) {

    var attr = $('#main').attr('_echarts_instance_');

    if (typeof (attr) != 'undefined' && attr != false) {

        $('#main').removeAttr('_echarts_instance_');

    }


    var html = "<thead><tr style='text-align:center;'>";

    for (i in table_data.header) {

        html += "<th style='margin-left:15px; border:1px black solid;'>" + table_data.header[i] + "</th>";

    }

    html += "</tr></thead>";

    html += "<tbody id='UnivRankTbody'>";

    for (i in table_data.data) {

        cur = table_data.data[i]

        html += "<tr style='text-align:center;'>";

        for (j in cur) {

            html += "<td style='border:1px black solid;'>" + cur[j] + "</td>";

        }

        html += "</tr>";

    }

    html += "</tbody>";

    return "<table id='UnivRankTable' style='border-collapse: collapse;margin:auto;' border='1' cellspacing='0'>" + html + "</table>";
}

