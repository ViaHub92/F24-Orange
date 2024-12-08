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
import PhishingAttackInstructor from './PhishingAttackInstructor';
import Logout from './Logout';
import FillTargetList from './FillTargetList';

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
          <Logout />  
        </div>
      </nav>

      <main className="w3-main" style={{ marginLeft: '300px', marginTop: '43px' }}>
  <header className="w3-container" style={{ paddingTop: '18px' }}>
    <h5><b><i className="fa fa-dashboard"></i> Instructor Dashboard</b></h5>
  </header>

  {/* Main Layout */}
  <div className="dashboard-container">
    {/* Row 1: Create Course and List Courses */}
    <div className="dashboard-row">
      <div className="dashboard-item">
        <h5>Create Course</h5>
        <CreateCourseForm />
      </div>
      <div className="dashboard-item">
        <h5>My Courses</h5>
        <CourseList courses={courses} />
      </div>
    </div>

    {/* Row 2: Phishing Attack and Leave Feedback */}
    <div className="dashboard-row">
      <div className="dashboard-item">
        <h5>Phishing Attack</h5>
        <PhishingAttackInstructor />
      </div>
      <div className="dashboard-item">
        <h5>Leave Feedback</h5>
        <LeaveFeedback studentId={selectedStudentId} />
      </div>
    </div>

{/* Row 3: Target List */}
<div className="dashboard-row">
  <div className="dashboard-item">
    <h5></h5>
    <FillTargetList courseId={courseId} />

  </div>
</div>







    {/* Row 4: Class Performance */}
    <div className="dashboard-row single-item">
      <div className="dashboard-item">
        <h5>Class Performance Report</h5>
        <InstructorPerformance courseId={courseId} />
      </div>
    </div>
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
