<template>
  <div>
      <div class="container" style="margin-top:7vh; margin-bottom:7vh width:100%">
        <div class="row">
          <div class="col-6">
            <div style="display:flex; justify-content:flex-start">
              <h4>DAILY DATA</h4>
            </div>
            <div >
              <canvas  ref="chart3" width="500"  height="400"></canvas>
            </div>
          </div>
          <div class="col-6">
            <div style="display:flex; justify-content:flex-start">
              <h4>WEEKLY DATA</h4>
            </div>
              
              <div >
                <canvas  ref="chart1" width="500"  height="400"></canvas>
              </div>
          </div>
          
         
         
        </div>
        <div class="row">
          <div class="col-6">
            <div style="display:flex; justify-content:flex-start">
              <h4>MONTHLY DATA</h4>
            </div>
            <div >
              <canvas  ref="chart2" width="500"  height="400"></canvas>
            </div>
          </div>
          <div class="col-6">
            <div style="display:flex; justify-content:flex-start">
              <h4>YEARLY DATA</h4>
            </div>
            <div >
              <canvas  ref="chart4" width="500"  height="400"></canvas>
            </div>
          </div>
        </div>


      </div>
        
        
       
        
        
        
       
    
    
  </div>
</template>

<script>
import Chart from 'chart.js/auto';

export default {

  data(){
    return{
      chart1:10,
      chart2:0,
      chart3:0,
      chart4:0,
    }
  },
  name: 'BarChart',
  mounted() {
    this.renderChart1();
    this.renderChart2();
    this.renderChart3();
    this.renderChart4();
  },
  methods: {
    


    renderChart1() {
      const ctx = this.$refs.chart1.getContext('2d');
      new Chart(ctx, {
        type: 'bar',
        data: {
          labels: ['Monday', 'Tuesday', 'Wednesday', 'thursday', 'Friday', 'Saturday', 'Sunday'],
          datasets: [
            {
              label: 'Power Generated Weekly',
              
              data: [120, 150, 180, 90, 200, 130, 160],
              backgroundColor: 'rgba(255, 99, 132, 0.2)',
              borderColor: 'rgba(255, 99, 132, 1)',
              borderWidth: 1,
              hoverBackgroundColor: 'rgba(255, 99, 132, 0.4)',
              hoverBorderColor: 'rgba(255, 99, 132, 1)',
            },
          ],
        },
        options: {
          responsive: false,
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
    renderChart2() {
      const ctx = this.$refs.chart2.getContext('2d');
      new Chart(ctx, {
        type: 'bar',
        data: {
          labels: ['January', 'Febuary', 'March', 'April', 'May', 'June', 'July','August','September','October','November','December'],
          datasets: [
            {
              label: 'Power Generated Monthly',
              
              data: [120, 150, 180, 90, 200, 130, 160,100,140,120,130,120],
              backgroundColor: 'rgba(255, 99, 132, 0.2)',
              borderColor: 'rgba(255, 99, 132, 1)',
              borderWidth: 1,
              hoverBackgroundColor: 'rgba(255, 99, 132, 0.4)',
              hoverBorderColor: 'rgba(255, 99, 132, 1)',
            },
          ],
        },
        options: {
          responsive: false,
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
    renderChart3() {
      const ctx = this.$refs.chart3.getContext('2d');
      this.chart=new Chart(ctx, {
        type: 'bar',
        data: {
          labels: ['06:00','07:00','08:00','09:00','10:00','11:00','12:00','13:00','14:00','15:00','16:00','17:00'],
          datasets: [
            {
              label: 'Power Generated',
              
              data: [0.7, 0.78, 0.81, 0.94, 1.03, 1.23, 1.5,1.4,1.37,1.21,0.9,0.5],
              backgroundColor: 'rgba(255, 99, 132, 0.2)',
              borderColor: 'rgba(255, 99, 132, 1)',
              borderWidth: 1,
              hoverBackgroundColor: 'rgba(255, 99, 132, 0.4)',
              hoverBorderColor: 'rgba(255, 99, 132, 1)',
            },
          ],
        },
        options: {
          responsive: false,
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
    renderChart4() {
      const ctx = this.$refs.chart4.getContext('2d');
      this.chart=new Chart(ctx, {
        type: 'bar',
        data: {
          labels:['2023','2024','2025','2026','2027'],
          datasets: [
            {
              label: 'Power Generated',
              
              data: [123],
              backgroundColor: 'rgba(255, 99, 132, 0.2)',
              borderColor: 'rgba(255, 99, 132, 1)',
              borderWidth: 1,
              hoverBackgroundColor: 'rgba(255, 99, 132, 0.4)',
              hoverBorderColor: 'rgba(255, 99, 132, 1)',
            },
          ],
        },
        options: {
          responsive: false,
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
  },
};
</script>

<style scoped>
canvas {
  max-width: 100%;
}
.button_container{
 display: flex;
 justify-content: space-evenly;
}
</style>
