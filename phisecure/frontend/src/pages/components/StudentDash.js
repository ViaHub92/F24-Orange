import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { Helmet } from 'react-helmet';
import { FaEnvelope } from "react-icons/fa";
import { GoPersonFill } from "react-icons/go";
import { FaCog } from "react-icons/fa";
import 'w3-css/w3.css';
import FetchPerformanceSummary from './FetchPerformanceSummary';
import FetchPerformanceDetailed from './FetchPerformanceDetailed';
import axios from "axios";

const SidebarComponent = () => {
  const [studentName, setStudentName] = useState("Loading...");
  const [courses, setCourses] = useState([]);
  const studentId = localStorage.getItem('student_id');
  useEffect(() => {
    if (studentId) {
        axios.get(`account/get_student/${studentId}`)
            .then(response => {
                const { first_name } = response.data;
                setStudentName(first_name);
            })
            .catch(error => {
                console.error("Error fetching student data:", error);
                setStudentName("Unknown Student");
            });

    

    } else {
        setStudentName("Student ID Missing");
    }
}, [studentId]);
  return (
    <div>
      <Helmet>
        <title>Phisecure - Student Dashboard</title>
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
          <h5>Student Dashboard</h5>
        </div>
        <div className="w3-bar-block">
          <Link to="/overview" className="w3-bar-item w3-button w3-padding">
            <i className="fa fa-users-cog"></i> Overview
          </Link>
          <Link to="/GmailClone" className="w3-bar-item w3-button w3-padding">
            <i className="fa fa-user-shield"></i> Prototype Inbox
          </Link>
          <Link to="/ReportsStudents" className="w3-bar-item w3-button w3-padding">
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
          <h5><b><i className="fa fa-dashboard"></i> Student Dashboard</b></h5>
        </header>

        {/* Overall Performance*/}
        <div className="w3-container">
          <h5>Overall Performance</h5>
          <table className="w3-table w3-striped w3-bordered w3-border w3-hoverable w3-white">
            <thead>
              <tr>
                <th>Performance Summary</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><FetchPerformanceSummary /></td>
              </tr>
              <tr>
              
              </tr>
            </tbody>
          </table>
        </div>
        <hr />

        {/* Reports Section */}
        <div className="w3-container">
          <h5>Phishing Email Feedback</h5>
          <table className="w3-table w3-striped w3-bordered w3-border w3-hoverable w3-white">
            <thead>
              <tr>
                <th>Interactions</th>
                <th>Email Title</th>
                <th>Red Flags</th>
                <th>Instructor Feedback</th>
              </tr>
            </thead>
            <tbody>
              
              <FetchPerformanceDetailed />
              
            </tbody>
          </table>
        </div>
        <hr />

      </main>

      {/* Footer */}
      <footer className="w3-container w3-padding-16 w3-center">
        <p>&copy; 2024 Phisecure. All rights reserved.</p>
      </footer>
    </div>
  );
};

export default SidebarComponent;
