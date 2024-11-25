// CourseList.js
import React, { useState } from 'react';
import axios from 'axios';
import DeleteCourseForm from './DeleteCourseForm';

const CourseList = () => {
  const [courses, setCourses] = useState([]);
  const [showCourses, setShowCourses] = useState(false);

  const fetchCourses = async () => {
    if (showCourses) {
      // Hide courses if currently visible
      setShowCourses(false);
    } else {
      try {
        // Fetch courses if not already shown
        const response = await axios.get('course/list_courses');
        setCourses(response.data);
        setShowCourses(true);
      } catch (error) {
        console.error('Error fetching courses:', error);
        setCourses([]);
        setShowCourses(false);
      }
    }
  };

  return (
    <div className="w3-container">
      <h5>List All Courses</h5>
      <button
        className="w3-button w3-green"
        onClick={fetchCourses}
        style={{ marginBottom: '10px' }}
      >
        {showCourses ? 'Hide Courses' : 'Show Courses'}
      </button>
      {showCourses && (
        <div>
          {courses.length > 0 ? (
            <>
              <h6>Available Courses:</h6>
              <ul>
                {courses.map((course) => (
                  <li key={course.id}>
                    {course.course_name} (Instructor ID: {course.instructor_id}){' '}
                    <DeleteCourseForm
                      courseId={course.id}
                      courseName={course.course_name}
                      onDeleteSuccess={() => setCourses((prevCourses) => prevCourses.filter(c => c.id !== course.id))}
                    />
                  </li>
                ))}
              </ul>
            </>
          ) : (
            <p>No courses available.</p>
          )}
        </div>
      )}
    </div>
  );
};

export default CourseList;
