import React, { useState } from 'react';
import axios from 'axios';
import DeleteCourseForm from './DeleteCourseForm';

const CourseList = () => {
  const [courses, setCourses] = useState([]);
  const [showCourses, setShowCourses] = useState(false);

  const fetchCourses = async () => {
    if (showCourses) {
      setShowCourses(false);
    } else {
      try {
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
        style={{ marginBottom: '20px' }}
      >
        {showCourses ? 'Hide Courses' : 'Show Courses'}
      </button>
      {showCourses && (
        <div className="courses-grid">
          {courses.length > 0 ? (
            <>
              <h6>Available Courses:</h6>
              <div className="grid-container">
                {courses.map((course) => (
                  <div key={course.id} className="grid-item">
                    <div className="w3-card-4">
                      <header className="w3-container w3-blue">
                        <h5>{course.course_name}</h5>
                      </header>
                      <div className="w3-container">
                        <DeleteCourseForm
                          courseId={course.id}
                          courseName={course.course_name}
                          onDeleteSuccess={() =>
                            setCourses((prevCourses) =>
                              prevCourses.filter((c) => c.id !== course.id)
                            )
                          }
                        />
                      </div>
                    </div>
                  </div>
                ))}
              </div>
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
