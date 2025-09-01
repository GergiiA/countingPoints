var canvas=document.getElementById('chart');

const labels = xValues;
const data = {
  labels: labels,
  datasets: [
    {
      label: '',
      data: yValues,
      //borderColor: '#000000',
      backgroundColor: barColors,
      hoverBackgroundColor: barColors2,
      borderWidth: 2,
      borderColor: barColors2,
    }
  ]
};

const config = {
  type: 'bar',
  data: data,
  options: {
    onClick: handleClicks,
    events: ['click', 'mousemove'],
    responsive: true,
    plugins: {
      legend: {
        position: 'top',
        display: false
      },
      title: {
        display: false,
        text: 'Chart.js Bar Chart'
      },
    }
  },
};

chart = new Chart(canvas, config)


/*
function changeLogs(logs, selected){
    console.log('selected:', selected);
    output=[]
    outputString=''
    l=document.getElementById('logList')
    l.innerHTML='<table class="logBox">';
    l.innerHTML += '<tr> <th>Reason</th> <th>Time</th> <th>Score</th> </tr>';
    for(var i=logs.length;i>logs.length;i--){
        //console.log(logs[i][1], selected);

        if(logs[i][1]==selected){
            console.log(logs[i]);
            console.log(i)
            //l.innerHTML+='<li><span class="reason">'+logs[i][3]+'</span> <strong class="score">'+logs[i][2]+'</strong> </li>';
            //l.innerHTML+='<li> <h3 class="reason">'+logs[i][3]+'</h3> <h3 class="score">'+logs[i][2]+'</h3> </li>'
            outputString+='<tr> <td>'+logs[i][3]+'</td> <td> '+logs[i][4]+' </td> <td> '+logs[i][2]+' </td></tr>'
            output.push([logs[i][3]+logs[i][2]]);
        }
    }
    console.log(output);
    if (outputString==''){
        outputString='Nothing here yet'
    }
    l.innerHTML+=outputString
    l.innerHTML+='</table>';
}
*/
function changeLogs(logs, selected){
    console.log(selected);
    box=document.getElementById('logBox');
    //box.innerHTML='';
    box.innerHTML = '<tr> <th>Reason</th> <th>Time</th> <th>Score</th> </tr>';
    output=''
    for(let i=logs.length - 1; i>=0; i--){
        if(selected==logs[i][1]){
            console.log(logs[i]);
            output+='<tr> <td>'+logs[i][3]+'</td> <td> '+logs[i][4]+' </td> <td> '+logs[i][2]+' </td></tr>'
        }
    }
    box.innerHTML += output ;
}

function handleClicks(evt){
    var activeElement = chart.getElementsAtEventForMode(evt, 'nearest', { intersect: true }, true);
    var index = activeElement[0].index+1;
    changeLogs(logs, index);
    //console.log('element', activeElement);
    //console.log('index', index);
}

changeLogs(logs, null)