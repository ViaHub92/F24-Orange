import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import { Helmet } from 'react-helmet';
import { FaEnvelope } from "react-icons/fa";
import { GoPersonFill } from "react-icons/go";
import { FaCog } from "react-icons/fa";
import 'w3-css/w3.css';
import FetchPerformanceSummary from './FetchPerformanceSummary';
import FetchPerformanceDetailed from './FetchPerformanceDetailed';

const InstructorDashboard = () => {
  const [studentName, setStudentName] = useState("Instructor");

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

        {/* Manage Students Section */}
        <div className="w3-container">
          <h5>Manage Students</h5>
          <button className="w3-button w3-green">Add Student</button>
          <button className="w3-button w3-red">Remove Student</button>
          <button className="w3-button w3-yellow">Modify Student</button>
        </div>
        <hr />

        {/* Customized Phishing Attacks Section */}
        <div className="w3-container">
          <h5>Customized Phishing Attacks</h5>
          <p>Design phishing emails to simulate real-world scenarios for students.</p>
          <textarea className="w3-input" placeholder="Enter custom phishing email content here..."></textarea>
          <button className="w3-button w3-blue" style={{ marginTop: '10px' }}>Save Attack Template</button>
        </div>
        <hr />

        {/* Student Interaction Monitoring Section */}
        <div className="w3-container">
          <h5>Student Interaction Monitoring</h5>
          <p>Click details to view interaction summary or individual actions taken by students.</p>
        </div>
        <hr />

        {/* Grade Overview Section */}
        <div className="w3-container">
          <h5>Grade Overview</h5>
          <table className="w3-table w3-bordered w3-striped">
            <tr><th>Student Name</th><th>Grade</th></tr>
            <tr><td>Student A</td><td>A</td></tr>
            <tr><td>Student B</td><td>B</td></tr>
          </table>
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
