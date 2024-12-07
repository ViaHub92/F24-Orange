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
import GetTags from './GetTags'
import GetMajors from './GetMajors'

const AdminDash = () => {
    const [studentName, setStudentName] = useState("Admin");
    const [courses, setCourses] = useState([]);
    const [showCourses, setShowCourses] = useState(false);
    const adminId = localStorage.getItem('admin_id');

  useEffect(() => {
    const fetchAdminData = async () => {
      try {
        const response = await axios.get(`/account/get_admin/${adminId}`);
        const adminData = response.data;
        setStudentName(adminData.first_name);
        setShowCourses(true);
      } catch (error) {
        console.error("Error fetching admin data:", error);
        setShowCourses(false);
      }
    };
    fetchAdminData();
  }, [adminId]);
  const Id = localStorage.getItem('admin_id');
  const [selectedAdminId, setSelectedAdminId] = useState("");
  
  const handleCourseIdChange = (e) => {
    const value = e.target.value;
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

function Admin() {
  return (
    <div>
      <Helmet>
        <title>Phisecure - Admin Dashboard</title>
      </Helmet>

      {/* Sidebar */}
      <nav className="w3-sidebar w3-collapse w3-white w3-animate-left always-open" id="mySidebar">
        <div className="w3-container w3-row">
          <div className="w3-col s8 w3-bar">
            <span>Welcome, <strong>TEMP</strong></span><br />
            <FaEnvelope />
            <a> </a>
            <GoPersonFill />
            <a> </a>
            <FaCog />
          </div>
        </div>
        <hr />
        <div className="w3-container">
          <h5>Admin Dashboard</h5>
        </div>
        <div className="w3-bar-block">
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
        <h5>Courses</h5>
        <CourseList courses={courses} />
      </div>
    </div>

    {/* Row 2: Tags and Majors */}
    <div className="dashboard-row">
      <div className="dashboard-item">
        <h5>Get Tags</h5>
        <GetTags />
      </div>
      <div className="dashboard-item">
        <h5>Get Majors</h5>
        <GetMajors />
      </div>
    </div>

    {/*Row 3: Analytics*/}
    <div className="dashboard-row">
      <div className="dashboard-item">
        <h5>Email Report</h5>
      </div>
      <div className="dashboard-item">
        <h5>Student Report</h5>
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
};

export default AdminDash;
