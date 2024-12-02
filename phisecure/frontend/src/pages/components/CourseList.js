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
        style={{ marginBottom: '20px' }}
      >
        {showCourses ? 'Hide Courses' : 'Show Courses'}
      </button>
      {showCourses && (
        <div className="w3-row-padding" style={{ marginTop: '20px' }}>
          {courses.length > 0 ? (
            <>
              <h6>Available Courses:</h6>
              <div className="w3-row">
                {courses.map((course) => (
                  <div
                    key={course.id}
                    className="w3-col s12 m6 l4"
                    style={{ marginBottom: '15px' }}
                  >
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
