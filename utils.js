var requestedData;

function requestAPI(baseCurrency, targetCurrency)
{
    var strReturn = "";

    jQuery.ajax({
        url: "http://185.61.138.154/currencies/gavapi.php?base=" + baseCurrency.toString() + "&target=" + targetCurrency.toString(),
        type: "GET",
        cache: false,
        success: function(html) {
            strReturn = html;
        },
        async: false
      });

      return strReturn;
}

function reloadChart(chart)
{
    var baseCurrency = $("#baseSelect").val().toString();
    var targetCurrency = $("#targetSelect").val().toString();
    var returnedData = requestAPI(baseCurrency, targetCurrency);
    removeAllData(chart);
    for (var i=0; i<returnedData["date"].length; i++)
    {
        addData(chart, returnedData["date"][i], returnedData[targetCurrency][i]);
    }
    
    chart.update();
}

function addData(chart, label, data)
{
    chart.data.labels.push(label);
    chart.data.datasets.forEach((dataset) => {
        dataset.data.push(data);
    });
    chart.update();
}

function removeAllData(chart)
{
    while(chart.data.labels.length > 0)
    {
        removeData(chart, false);
    }
    chart.update();
}

function removeData(chart, update=true)
{
    chart.data.labels.pop();
    chart.data.datasets.forEach((dataset) => {
        dataset.data.pop();
    });
    if (update)
    {
        chart.update();
    }
}