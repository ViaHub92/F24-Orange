import React, { useState } from 'react';
import axios from 'axios';

const CreateCourseForm = () => {
  const [courseName, setCourseName] = useState('');
  const [instructorId, setInstructorId] = useState('');
  const [message, setMessage] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!courseName || !instructorId) {
      setMessage('Please fill out all fields.');
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
        setInstructorId('');
      }
    } catch (error) {
      setMessage(error.response?.data?.message || 'Error creating course.');
    }
  };

  return (
    <div className="create-course-form">
      <h3>Create a New Course</h3>
      {message && <p>{message}</p>}
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="courseName">Course Name:</label>
          <input
            type="text"
            id="courseName"
            value={courseName}
            onChange={(e) => setCourseName(e.target.value)}
            className="w3-input"
          />
        </div>
        <div className="form-group">
          <label htmlFor="instructorId">Instructor ID:</label>
          <input
            type="text"
            id="instructorId"
            value={instructorId}
            onChange={(e) => setInstructorId(e.target.value)}
            className="w3-input"
          />
        </div>
        <button type="submit" className="w3-button w3-blue">
          Create Course
        </button>
      </form>
    </div>
  );
};

export default CreateCourseForm;
