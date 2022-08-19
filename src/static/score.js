const REQUEST_BASE_URL = 'http://127.0.0.1:5000'

const score_url = `${REQUEST_BASE_URL}/score/current-score`

const fetchScore = async () => {
  let response = await fetch(score_url)
  let data = await response.json()
  return data
}

const fetched_data = await fetchScore()

const colors = [
  'rgb(255, 99, 132)',
  'rgb(255, 159, 64)',
  'rgb(255, 205, 86)',
  'rgb(75, 192, 192)',
  'rgb(54, 162, 235)',
  'rgb(153, 102, 255)',
  'rgb(231,233,237)'
]

const labels = [
  '01',
  '02',
  '03',
  '04',
  '05',
  '06',
  '07',
  '08',
  '09',
  '10',
  '11',
  '12',
  '13',
  '14',
  '15',
  '16',
  '17',
  '18',
  '19',
  '20',
  '21',
  '22',
  '23',
  '24',
  '25',
  '26',
  '27',
  '28',
  '29',
  '30',
  '31',
];

let final_datasets = []

fetched_data.data.forEach(element => {
  final_datasets.push(
    {
      label: element.label,
      data: element.data,
      backgroundColor: colors[element.id % colors.length],
      borderColor: colors[element.id % colors.length],
    }
  )
});

const data = {
  labels: labels, 
  datasets: final_datasets
}

const config = {
  type: 'line',
  data: data,
  options: {
    plugins: {
      legend: {
        labels: {
          color: 'white'
        }
      }
    },
    scales: {
      y: {
        min: 0,
        suggestedMax: 20,
        grid: {
          display: false,
          color: '#D8DEE9'
        },
        ticks: {
          backdropColor: 'white',
          display: true, 
          color: '#D8DEE9'
        },
      },
      x: {
        grid: {
          color: '#D8DEE9',
          drawBorder: false
        },
        ticks: {
          backdropColor: 'white',
          color: '#D8DEE9',
          textStrokeColor: 'D8DEE9'
        }
      }
    },
    tooltips: {
      mode: 'index'
    },
  },
};

const chart = new Chart(
  document.getElementById('scoreboard-chart'),
  config
);
