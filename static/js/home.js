/*var canvas=document.getElementById('chart');

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
 */


function chooseGrade(grade=0, first){

    if(first==false){
    chart.destroy()
    console.log('chart destroy try')
    }


    xValues=origData[grade].map(item=>item[1])
    console.log(xValues)
    yValues=origData[grade].map(item=>item[2])
    console.log(yValues)


    var canvas=document.getElementById('canvasChart');

    a=canvas
    console.log('a', a)

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
    globalThis.chart = new Chart(canvas, config)
}

function changeLogs(logs, selected, grade=0){
    //console.log(selected);
    box=document.getElementById('logBox');
    //box.innerHTML='';
    box.innerHTML = '<tr> <th>Reason</th> <th>Time</th> <th>Score</th> </tr>';
    output=''
    console.log(logs[grade].length)
    for(let i=logs[grade].length - 1; i>=0; i--){
        if(selected==logs[grade][i][1]){
            console.log(logs[i]);
            output+='<tr> <td>'+logs[grade][i][3]+'</td> <td> '+logs[grade][i][4]+' </td> <td> '+logs[grade][i][2]+' </td></tr>'
        }
    }

    box.innerHTML += output ;
}

function handleGradeChange(first=false){
    seletBox=document.getElementById('selectBox');
    selectedGradeId=seletBox.value
    chooseGrade(seletBox.value, first)
    changeLogs(logs, null, selectedGradeId)
}

function handleClicks(evt){
    var activeElement = chart.getElementsAtEventForMode(evt, 'nearest', { intersect: true }, true);
    var index = activeElement[0].index+1;
    changeLogs(logs, index, document.getElementById('selectBox').value);
    //console.log('element', activeElement);
    //console.log('index', index);
}

//chooseGrade(1)
//changeLogs(logs, null, 0)

handleGradeChange(true)

console.log(chart)