import React, { useState, useEffect } from "react";
import axios from "axios";
import { Bar } from "react-chartjs-2";
import { Chart as ChartJS, CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend } from "chart.js";

ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend);

const InstructorPerformance = () => {
  const [courses, setCourses] = useState([]);
  const [courseId, setCourseId] = useState(null);
  const [performanceData, setPerformanceData] = useState([]);
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

  // Fetch the performance data whenever a course is selected
  useEffect(() => {
    const fetchPerformanceData = async () => {
      if (!courseId) return; // Don't fetch if no course is selected

      try {
        const response = await axios.get(`instructor_dashboard/get_class_performance_data/${courseId}`);
        setPerformanceData(response.data);
        setError(null);
      } catch (err) {
        setError("Error fetching performance data");
        setPerformanceData([]);
      }
    };

    fetchPerformanceData();
  }, [courseId]); // Trigger when courseId changes

  const handleCourseChange = (e) => {
    setCourseId(e.target.value); // Update courseId when user selects a course
  };

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
        backgroundColor: "rgba(245, 221, 39, 1)",
      },
      {
        label: "Total Links Clicked",
        data: performanceData.map((student) => student.total_links_clicked),
        backgroundColor: "rgba(245, 39, 39, 1)",
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
      {error && <p style={{ color: "red" }}>{error}</p>}
      
      <div>
        <label htmlFor="course-select"></label>
        <select id="course-select" onChange={handleCourseChange} value={courseId}>
          <option value="">--Choose a Course--</option>
          {courses.map((course) => (
            <option key={course.id} value={course.id}>
              {course.course_name}
            </option>
          ))}
        </select>
      </div>

      {performanceData.length > 0 ? (
        <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start" }}>
          <div style={{ width: "45%" }}>
            <Bar data={chartData} options={chartOptions} />
          </div>
        </div>
      ) : courseId ? (
        <p>No performance data available for this course.</p>
      ) : (
        <p>Please select a course to view performance data.</p>
      )}
    </div>
  );
};

export default InstructorPerformance;
