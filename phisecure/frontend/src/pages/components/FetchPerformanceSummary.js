import React, { useState, useEffect } from "react";
import { Pie } from "react-chartjs-2"; 
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from 'chart.js'; 
import '../../styles.css';  
import { Mosaic } from "react-loading-indicators"

ChartJS.register(ArcElement, Tooltip, Legend);

function FetchPerformanceSummary() {
  const [data, setData] = useState([]);

  useEffect(() => {
    const studentId = localStorage.getItem('student_id');

    fetch(`performance/summary/${studentId}`)
      .then(res => res.json())
      .then(data => {
        setData(data);
        console.log(data);
      })
      .catch(error => console.error("Error fetching data: ", error));
  }, []);

  const chartData = {
    labels: ['Opened', 'Replied', 'Links Clicked'],
    datasets: [
      {
        label: 'Performance Summary',
        data: [
          data.total_opened,
          data.total_replied,
          data.total_links_clicked
        ],
        backgroundColor: [
          'rgba(75, 192, 192, 0.6)', // Opened
          'rgba(255, 159, 64, 0.6)', // Replied
          'rgba(255, 99, 132, 0.6)'  // Links Clicked
        ],
        borderColor: [
          'rgba(75, 192, 192, 1)',
          'rgba(255, 159, 64, 1)',
          'rgba(255, 99, 132, 1)'
        ],
        borderWidth: 1
      }
    ]
  };

  const options = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: {
        position: 'top',
      },
    },
    aspectRatio: 1,
  };

const totalActions = data.total_opened + data.total_replied + data.total_links_clicked;
const maxRiskScore = 300; 
const currentRiskScore = 
  (data.total_opened * -15) + 
  (data.total_replied * 50) + 
  (data.total_links_clicked * 100);


const riskPercentage = Math.max(0, Math.min((currentRiskScore / maxRiskScore) * 100, 100));

let riskColor = 'green';

if (riskPercentage > 66) {
  riskColor = 'red'; // High risk
} else if (riskPercentage > 33) {
  riskColor = 'yellow'; // Medium risk
}



  return (
    <div className="performance-summary">
      {data.length === 0 ? (
        <p><Mosaic color="#231D6C" size="small" text="" textColor="" /></p>
      ) : (
        <div>
          <h3>Performance Summary</h3>
          <div style={{ width: '300px', height: '300px' }}>
            <Pie data={chartData} options={options} />
          </div>
          <h4>Risk Meter</h4>
          <div style={{ width: '100%', height: '20px', backgroundColor: '#e0e0e0', borderRadius: '10px' }}>
            <div
              style={{
                height: '100%',
                width: `${riskPercentage}%`,
                backgroundColor: riskColor,
                borderRadius: '10px',
                transition: 'width 0.3s ease-in-out'
              }}
            />
          </div>
          <p style={{ textAlign: 'center', marginTop: '10px' }}>
            Risk Level: {Math.round(riskPercentage)}% 
            <span style={{ color: riskColor, fontWeight: 'bold' }}> ({riskColor.toUpperCase()})</span>
          </p>
        </div>
      )}
    </div>
  );
}

export default FetchPerformanceSummary;