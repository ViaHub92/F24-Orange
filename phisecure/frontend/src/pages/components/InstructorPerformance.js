import React, { useState, useEffect } from "react";
import axios from "axios";
import { Bar } from "react-chartjs-2";
import { Chart as ChartJS, CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend } from "chart.js";

ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend);

const InstructorPerformance = ({ courseId }) => {
  const [performanceData, setPerformanceData] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchPerformanceData = async () => {
      try {
        const response = await axios.post(
          `instructor_dashboard/get_class_performance_data/${courseId}`
        );
        setPerformanceData(response.data); 
        setError(null); 
      } catch (err) {
        setError(err.response?.data?.message || "Error fetching data");
        setPerformanceData([]); 
      }
    };

    if (courseId) {
      fetchPerformanceData();
    }
  }, [courseId]);

  const chartData = {
    labels: performanceData.map((student) => student.student_name),
    datasets: [
      {
        label: "Total Opened",
        data: performanceData.map((student) => student.total_opened),
        backgroundColor: "rgba(54, 162, 235, 0.6)",
      },
      {
        label: "Total Replied",
        data: performanceData.map((student) => student.total_replied),
        backgroundColor: "rgba(255, 99, 132, 0.6)",
      },
      {
        label: "Total Links Clicked",
        data: performanceData.map((student) => student.total_links_clicked),
        backgroundColor: "rgba(75, 192, 192, 0.6)",
      },
    ],
  };

  const chartOptions = {
    responsive: true,
    plugins: {
      title: {
        display: true,
        text: "Class Performance Overview",
        font: {
          size: 20, 
        },
      },
      tooltip: {
        bodyFont: {
          size: 16, 
        },
      },
    },
    scales: {
      y: {
        min: 0,      
        max: 20,     
        ticks: {
          font: {
            size: 16,  
          },
        },
      },
      x: {
        ticks: {
          font: {
            size: 14,  
          },
        },
      },
    },
  };

  return (
    <div>
      <h2>Class Performance Report</h2>
      {error ? (
        <p style={{ color: "red" }}>{error}</p>
      ) : performanceData.length > 0 ? (
        <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start" }}>
          {/* Chart container */}
          <div style={{ width: "45%" }}>
            <Bar data={chartData} options={chartOptions} />
          </div>
          


          
          
        </div>
      ) : (
        <p>No data available.</p>
      )}
    </div>
  );
};

export default InstructorPerformance;
