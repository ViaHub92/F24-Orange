import React, { useState, useEffect } from "react";
import axios from "axios";

const FillTargetList = ({ courseId }) => {
  const [courses, setCourses] = useState([]);
  const [selectedCourse, setSelectedCourse] = useState("");
  const [message, setMessage] = useState("");
  const instructorId = localStorage.getItem('instructor_id');

  // Fetch the list of courses available for the instructor
  useEffect(() => {
    const fetchCourses = async () => {
      try {
        const response = await axios.get(`/course/list_courses/${instructorId}`);
        setCourses(response.data);
      } catch (error) {
        console.error("Error fetching courses:", error);
      }
    };
    fetchCourses();
  }, []);

  const handleSubmit = async () => {
    try {
      const response = await axios.post(`/peer_phishing/fill-target-list/${selectedCourse}`);
      setMessage(response.data.message);
    } catch (error) {
      console.error("Error filling target list:", error);
      setMessage("Error: Unable to populate target list.");
    }
  };

  return (
    <div>
      <h5>Fill Target List for Selected Course</h5>
      <div>
        <select
          value={selectedCourse}
          onChange={(e) => setSelectedCourse(e.target.value)}
        >
          <option value="">Select a course</option>
          {courses.map((course) => (
            <option key={course.id} value={course.id}>
              {course.course_name}
            </option>
          ))}
        </select>
        <button onClick={handleSubmit} disabled={!selectedCourse}>
          Populate Target List
        </button>
      </div>
      {message && <p style={{ marginTop: '10px', color: 'green' }}>{message}</p>}
    </div>
  );
};

export default FillTargetList;
