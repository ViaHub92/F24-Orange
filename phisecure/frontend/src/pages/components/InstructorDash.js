import React, { useState, useEffect } from 'react'; 
import { Link } from 'react-router-dom';
import { Helmet } from 'react-helmet';
import { FaEnvelope } from "react-icons/fa";
import { GoPersonFill } from "react-icons/go";
import { FaCog } from "react-icons/fa";
import 'w3-css/w3.css';
import InstructorPerformance from './InstructorPerformance';
import CreateCourseForm from './CreateCourseForm';
import axios from 'axios';
import DeleteCourseForm from './DeleteCourseForm';
import CourseList from './CourseList';
import LeaveFeedback from './LeaveFeedback';

const InstructorDashboard = () => {
  const [studentName, setStudentName] = useState("Instructor");
  const [courseId, setCourseId] = useState("");
  const [courses, setCourses] = useState([]);
  const [showCourses, setShowCourses] = useState(false);
  const instructorId = localStorage.getItem('instructor_id');

  useEffect(() => {
    const fetchInstructorData = async () => {
      try {
        const response = await axios.get(`/account/get_instructor/${instructorId}`);
        const instructorData = response.data;
        setStudentName(instructorData.first_name);
        setCourses(instructorData.courses || []);
        setShowCourses(true);
      } catch (error) {
        console.error("Error fetching instructor data:", error);
        setShowCourses(false);
      }
    };

    fetchInstructorData();
  }, [instructorId]);
  const studentId = localStorage.getItem('student_id');
  const [selectedStudentId, setSelectedStudentId] = useState("");
  
  const handleCourseIdChange = (e) => {
    const value = e.target.value;

    // Allow only numbers or an empty string
    if (/^\d*$/.test(value)) {
      setCourseId(value);
    }
  };



  const fetchCourses = async () => {
    try {
      const response = await axios.get('course/list_courses'); 
      setCourses(response.data);
      setShowCourses(true);
    } catch (error) {
      console.error("Error fetching courses:", error);
      setCourses([]);
      setShowCourses(false);
    }
  };

  // Function to handle a successful delete operation
  const handleDeleteSuccess = (deletedCourseId) => {
    setCourses((prevCourses) => prevCourses.filter(course => course.id !== deletedCourseId));
  };

  return (
    <div>
      <Helmet>
        <title>Phisecure - Instructor Dashboard</title>
      </Helmet>

      {/* Sidebar */}
      <nav className="w3-sidebar w3-collapse w3-white w3-animate-left always-open" id="mySidebar">
        <div className="w3-container w3-row">
          <div className="w3-col s8 w3-bar">
            <span>Welcome, <strong>{studentName}</strong></span><br />
            <FaEnvelope />
            <a> </a>
            <GoPersonFill />
            <a> </a>
            <FaCog />
          </div>
        </div>
        <hr />
        <div className="w3-container">
          <h5>Instructor Dashboard</h5>
        </div>
        <div className="w3-bar-block">
          <Link to="/overview" className="w3-bar-item w3-button w3-padding">
            <i className="fa fa-users-cog"></i> Overview
          </Link>
          <Link to="/Inbox" className="w3-bar-item w3-button w3-padding">
            <i className="fa fa-user-shield"></i> Prototype Inbox
          </Link>
          <Link to="/ReportsInstructor" className="w3-bar-item w3-button w3-padding">
            <i className="fa fa-chart-line"></i> Reports
          </Link>
          <Link to="/notifications" className="w3-bar-item w3-button w3-padding">
            <i className="fa fa-server"></i> Notifications
          </Link>
          <Link to="/settings" className="w3-bar-item w3-button w3-padding">
            <i className="fa fa-cog"></i> Settings
          </Link>
        </div>
      </nav>

      {/* Main Content */}
      <main className="w3-main" style={{ marginLeft: '300px', marginTop: '43px' }}>
        <header className="w3-container" style={{ paddingTop: '18px' }}>
          <h5><b><i className="fa fa-dashboard"></i> Instructor Dashboard</b></h5>
        </header>

        {/* Create Course Section */}
        <div className="w3-container">
          <h5>Create a Course</h5>
          <CreateCourseForm />
        </div>
        <hr />

        {/* My Courses Section */}
        <div>
          <h3>My Courses</h3>
          <div>
            {courses.map((course) => (
              <div key={course.id} className="course-item w3-container w3-border-bottom">
                <p>{course.course_name}</p>
                <DeleteCourseForm
                  courseId={course.id}
                  courseName={course.course_name}
                  onDeleteSuccess={handleDeleteSuccess}
                />
              </div>
            ))}
          </div>
        </div>
            {/* My Courses Section */}
             <CourseList /> 
       

       
        <hr />

     {/* Feedback Section for a Specific Phishing Email */}
<div className="w3-container">
  <LeaveFeedback studentId={selectedStudentId} />
  </div>



      
        {/* Student Interaction Monitoring */}
        <div className="w3-container course-section">
          <h5>Student Interaction Monitoring</h5>
          <p>Monitor students' performance by selecting the course and viewing the reports below.</p>

          {/* Course ID Selector */}
          <div className="course-id-section">
            <label htmlFor="courseId" className="course-label">Select Course:</label>
            <input
              type="text"
              id="courseId"
              value={courseId}
              onChange={handleCourseIdChange}
              className="w3-input course-input"
              placeholder="Enter Course ID"
              style={{ marginBottom: '10px' }}
            />
          </div>

          {/* Display students for the selected course */}
          <InstructorPerformance courseId={courseId} />
        </div>
      </main>

      {/* Footer */}
      <footer className="w3-container w3-padding-16 w3-center">
        <p>&copy; 2024 Phisecure. All rights reserved.</p>
      </footer>
    </div>
  );
};

export default InstructorDashboard;
