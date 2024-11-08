import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import { Helmet } from 'react-helmet';
import { FaEnvelope } from "react-icons/fa";
import { GoPersonFill } from "react-icons/go";
import { FaCog } from "react-icons/fa";
import 'w3-css/w3.css';
import FetchPerformance from './FetchPerformance';

const SidebarComponent = () => {
  const [studentName, setStudentName] = useState("Student");

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
          <Link to="/inbox" className="w3-bar-item w3-button w3-padding">
            <i className="fa fa-user-shield"></i> Inbox
          </Link>
          <Link to="/reports" className="w3-bar-item w3-button w3-padding">
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

        {/* Reports Section */}
        <div className="w3-container">
          <h5>Reports</h5>
          <table className="w3-table w3-striped w3-bordered w3-border w3-hoverable w3-white">
            <thead>
              <tr>
                <th>Report Title</th>
                <th>Date</th>
                <th>Status</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>Feedback</td>
                <td>Oct 21, 2024</td>
                <td>Reviewed</td>
              </tr>
              <tr>
                <td>Results</td>
                <td>Oct 19, 2024</td>
                <td>Pending</td>
              </tr>
            </tbody>
          </table>
        </div>
        <hr />

        {/* Email Section */}
        <div className="w3-container">
          <h5>Email Inbox</h5>
          <ul className="w3-ul w3-card-4 w3-white">
            <li className="w3-padding-16">
              <span className="w3-large">Subject</span><br />
              <span className="w3-opacity">From: johnsmith@example.com</span>
            </li>
            <li className="w3-padding-16">
              <span className="w3-large">Subject:</span><br />
              <span className="w3-opacity">From: janesmith@example.com</span>
            </li>
          </ul>

          <Link to="/inbox">
            <button className="w3-button w3-dark-grey">
              View All Emails <i className="fa fa-arrow-right" />
            </button>
          </Link>
        </div>
        <hr />

        {/* Notifications Section */}
        <div className="w3-container">
          <h5>Notifications</h5>
          <ul className="w3-ul w3-card-4 w3-white">
            <li className="w3-padding-16">
              <i className="fa fa-bell w3-text-red"></i> New grades available for review.
            </li>
            <li className="w3-padding-16">
              <i className="fa fa-bell w3-text-green"></i> Your report has been approved.
            </li>
          </ul>
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
