const REQUEST_BASE_URL = 'http://127.0.0.1:5000'

const score_url = `${REQUEST_BASE_URL}/score/current-score`

const fetchScore = async () => {
  let response = await fetch(score_url)
  let data = await response.json()
  return data
}

const fetched_data = await fetchScore()

const backgroundColors = [
  'rgba(255, 99, 132, 0.2)',
  'rgba(54, 162, 235, 0.2)',
  'rgba(255, 206, 86, 0.2)',
  'rgba(75, 192, 192, 0.2)',
  'rgba(153, 102, 255, 0.2)',
  'rgba(255, 159, 64, 0.2)'
]

const borderColors = [
  'rgba(255, 99, 132, 1)',
  'rgba(54, 162, 235, 1)',
  'rgba(255, 206, 86, 1)',
  'rgba(75, 192, 192, 1)',
  'rgba(153, 102, 255, 1)',
  'rgba(255, 159, 64, 1)'
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
      backgroundColor: backgroundColors[element.id % backgroundColors.length],
      borderColor: borderColors[element.id % borderColors.length]
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
  options: {}
};

const chart = new Chart(
  document.getElementById('scoreboard-chart'),
  config
);
