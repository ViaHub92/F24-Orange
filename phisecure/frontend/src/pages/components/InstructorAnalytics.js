import React, { useState, useEffect } from "react";
import axios from "axios";
import { Bar } from "react-chartjs-2";
import { Chart as ChartJS, CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend } from "chart.js";

ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend);

const InstructorAnalytics = () => {
  const [courses, setCourses] = useState([]);
  const [courseId, setCourseId] = useState(null);
  const [analyticsData, setAnalyticsData] = useState([]);
  const [selectedRate, setSelectedRate] = useState("");
  const [topN, setTopN] = useState(5);
  const [error, setError] = useState(null);
  const instructorId = localStorage.getItem('instructor_id');

  // Fetch the list of courses when the component mounts
  useEffect(() => {
    const fetchCourses = async () => {
      try {
        const response = await axios.get(`/course/list_courses/${instructorId}`);
        setCourses(response.data); // Set the course list
      } catch (err) {
        setError("Error fetching courses");
      }
    };

    fetchCourses();
  }, []);

  // Fetch the analytics data whenever a course is selected
  useEffect(() => {
    const fetchAnalyticsData = async () => {
      if (!courseId) return; // Don't fetch if no course is selected

      try {
        const response = await axios.get(`/instructor_dashboard/analytics/${courseId}`);
        setAnalyticsData(response.data);
        setError(null);
      } catch (err) {
        setError("Error fetching analytics data");
        setAnalyticsData([]);
      }
    };

    fetchAnalyticsData();
  }, [courseId]); // Trigger when courseId changes

  const handleCourseChange = (e) => {
    setCourseId(e.target.value); // Update courseId when user selects a course
  };

  const handleRateChange = (e) => {
    setSelectedRate(e.target.value); // Update selectedRate when user selects a rate
  };

  const handleTopNChange = (e) => {
    setTopN(parseInt(e.target.value)); // Update topN when user selects the number of top templates
  };

  const normalizedData = analyticsData.map((item) => {
    const totalEmails = item.total_phishing_emails;
    return {
      template_name: item.template_name,
      open_rate: (item.total_opened / totalEmails) * 100,
      click_rate: (item.total_links_clicked / totalEmails) * 100,
      reply_rate: (item.total_replied / totalEmails) * 100,
    };
  });

  const sortedData = [...normalizedData].sort((a, b) => b[selectedRate] - a[selectedRate]).slice(0, topN);

  const rateColors = {
    open_rate: "rgba(54, 162, 235, 0.6)",
    click_rate: "rgba(75, 192, 192, 0.6)",
    reply_rate: "rgba(255, 99, 132, 0.6)",
  };

  const chartData = {
    labels: sortedData.map((item) => item.template_name),
    datasets: [
      {
        label: selectedRate.replace("_", " ").toUpperCase(),
        data: sortedData.map((item) => item[selectedRate]),
        backgroundColor: rateColors[selectedRate],
      },
    ],
  };

  const chartOptions = {
    responsive: true,
    plugins: {
      title: {
        display: true,
        text: "Template Interaction Rates",
        font: {
          size: 20,
        },
      },
      tooltip: {
        bodyFont: {
          size: 16,
        },
      },
      legend: {
        position: 'top',
      },
    },
    scales: {
      x: {
        ticks: {
          font: {
            size: 14,
          },
        },
      },
      y: {
        ticks: {
          font: {
            size: 16,
          },
          beginAtZero: true,
          max: 100,
          callback: function(value) {
            return value + "%";
          }
        },
      },
    },
  };

  return (
    <div>
      <h5>Analytics Report</h5>
      <div>
        <label htmlFor="course-select">Select Course: </label>
        <select id="course-select" onChange={handleCourseChange} value={courseId}>
          <option value="">--Choose a Course--</option>
          {courses.map((course) => (
            <option key={course.id} value={course.id}>
              {course.course_name}
            </option>
          ))}
        </select>
      </div>
      <div>
        <label htmlFor="rate-select">Select Rate: </label>
        <select id="rate-select" onChange={handleRateChange} value={selectedRate}>
          <option value="">--Choose Rate--</option>
          <option value="open_rate">Open Rate</option>
          <option value="click_rate">Click Rate</option>
          <option value="reply_rate">Reply Rate</option>
        </select>
      </div>
      <div>
        <label htmlFor="top-n-select">Top Performing Templates: </label>
        <select id="top-n-select" onChange={handleTopNChange} value={topN}>
          <option value="">--Choose top---</option>
          <option value="5">Top 5</option>
          <option value="10">Top 10</option>
          <option value="15">Top 15</option>
        </select>
      </div>

      {analyticsData.length > 0 && selectedRate ? (
        <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start" }}>
          <div style={{ width: "45%" }}>
            <Bar data={chartData} options={chartOptions} />
          </div>
        </div>
      ) : courseId && selectedRate ? (
        <p>No analytics data available for this course.</p>
      ) : (
        <p>Please select a course and rate to view analytics data.</p>
      )}
    </div>
  );
};

export default InstructorAnalytics;