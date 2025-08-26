var canvas=document.getElementById('chart');

const labels = xValues;
const data = {
  labels: labels,
  datasets: [
    {
      label: 'Dataset 1',
      data: yValues,
      borderColor: ' #000000',
      backgroundColor: barColors
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
      }
    }
  },
};

chart=new Chart(canvas, config)
