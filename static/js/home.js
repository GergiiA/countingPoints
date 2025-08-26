var canvas=document.getElementById('chart');

const labels = xValues;
const data = {
  labels: labels,
  datasets: [
    {
      label: 'Dataset 1',
      data: yValues,
      borderColor: '#000000',
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
    responsive: true,
    plugins: {
      legend: {
        position: 'top',
      },
      title: {
        display: false,
        text: 'Chart.js Bar Chart'
      },
      legend: {
        display: false
      }
    }
  },
};

chart=new Chart(canvas, config)
