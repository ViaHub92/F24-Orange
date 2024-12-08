import React, { useState } from 'react';
import axios from 'axios';

const CreateCourseForm = ({ onCourseCreated }) => {
  const [courseName, setCourseName] = useState('');
  const [message, setMessage] = useState('');
  const instructorId = localStorage.getItem('instructor_id');

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!courseName || !instructorId) {
      setMessage('Please fill out all fields and ensure you are logged in.');
      return;
    }

    try {
      const response = await axios.post('course/create_course', {
        course_name: courseName,
        instructor_id: instructorId,
      });

      if (response.status === 201) {
        setMessage('Course created successfully!');
        setCourseName('');
        if (onCourseCreated) onCourseCreated();
      }
    } catch (error) {
      setMessage(error.response?.data?.message || 'Error creating course.');
    }
  };

  return (
    <div className="w3-card w3-padding w3-margin-bottom">
      <h4 className="w3-text-blue">Create a New Course</h4>
      {message && <p className={`w3-text-${message.includes('successfully') ? 'green' : 'red'}`}>{message}</p>}
      <form onSubmit={handleSubmit}>
        <div className="w3-margin-bottom">
          <label htmlFor="courseName" className="w3-text-gray">Course Name:</label>
          <input
            type="text"
            id="courseName"
            value={courseName}
            onChange={(e) => setCourseName(e.target.value)}
            className="w3-input w3-border"
            placeholder="Enter course name"
          />
        </div>
        <button type="submit" className="w3-button w3-green w3-round">
          Create Course
        </button>
      </form>
    </div>
  );
};

export default CreateCourseForm;
