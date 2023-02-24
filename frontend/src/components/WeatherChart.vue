<template>
    <div>
        <canvas ref="chart" height="300"></canvas>
    </div>
</template>

<script>

import axios from 'axios';
import Chart from 'chart.js/auto';
export default {

  data() {
    return {
      weatherData: {},
      temp_array:[],
      label_array:[],
      forecase:{},
      response:{}
    };
  },
  mounted() {
    this.getWeatherData();
    this.renderChart();


  },
  methods: {
    getWeatherData() {
      const apiKey = 'acc07b8b4d7847eeb14174720232302';
      const lat=12.8379119;
      const lon=80.1316818;
      const apiUrl = `http://api.weatherapi.com/v1/forecast.json?key=acc07b8b4d7847eeb14174720232302&q=chennai&days=4&aqi=no&alerts=no`;

      axios.get(apiUrl)
        .then(response => {
          this.weatherData = response.data;
          localStorage.setItem("weatherData", JSON.stringify(response.data));
          console.log(this.weatherData.forecast.forecastday[0])    
          
        })
        .catch(error => {
          console.log(error);
        });
    },
    renderChart() {
    this.response=JSON.parse(localStorage.getItem("weatherData"))
     for(let i =6;i<=17;i++){
            this.temp_array.push(Math.floor(Math.random() * (6) + 21))
            this.label_array.push(i+':00')
          }
      console.log("datat chart",this.response)
          
      const ctx = this.$refs.chart.getContext('2d');
      new Chart(ctx, {
        type: 'bar',
        data: {
          labels: this.label_array,
          datasets: [
            {
              label: 'Temparature',
              
              data: this.temp_array,
              backgroundColor: 'rgba(255, 99, 132, 0.2)',
              borderColor: 'rgba(255, 99, 132, 1)',
              borderWidth: 1,
              hoverBackgroundColor: 'rgba(255, 99, 132, 0.4)',
              hoverBorderColor: 'rgba(255, 99, 132, 1)',
            },
          ],
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          scales: {
            yAxes: [
              {
                ticks: {
                  beginAtZero: true,
                },
              },
            ],
          },
        },
      });
    },
  }
}
</script>