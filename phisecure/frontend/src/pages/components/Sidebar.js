import React, { useState } from 'react';
import { Helmet } from 'react-helmet';
import { FaEnvelope } from "react-icons/fa";
import { GoPersonFill } from "react-icons/go";
import { FaCog } from "react-icons/fa";
import 'w3-css/w3.css';

const SidebarComponent = () => {
    return (
      <div>
      {/* Sidebar */}
      <div className="w3-sidebar w3-collapse w3-white w3-animate-left always-open" id="mySidebar">
          <div className="w3-container w3-row">
              <div className="w3-col s8 w3-bar">
                  <span>Welcome, <strong>Admin</strong></span><br />
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
              <a href="usermanagement.html" className="w3-bar-item w3-button w3-padding">
                  <i className="fa fa-users-cog"></i> Manage Users
              </a>
              <a href="phishingassessment.html" className="w3-bar-item w3-button w3-padding">
                  <i className="fa fa-user-shield"></i> Phishing Assessments
              </a>
              <a href="dataanalytics.html" className="w3-bar-item w3-button w3-padding">
                  <i className="fa fa-chart-line"></i> Data Analytics
              </a>
              <a href="systemanalytics.html" className="w3-bar-item w3-button w3-padding">
                  <i className="fa fa-server"></i> System Analytics
              </a>
              <a href="#" className="w3-bar-item w3-button w3-padding">
                  <i className="fa fa-cog"></i> Settings
              </a>
          </div>
      </div>

      {/* Main Content */}
      <div className="w3-main" style={{ marginLeft: '300px', marginTop: '43px' }}>
          <header className="w3-container" style={{ paddingTop: '18px' }}>
              <h5><b><i className="fa fa-dashboard"></i> Admin Dashboard</b></h5>
          </header>

          {/* Your other content */}
          <div className="w3-container">
              <h5>Manage Users</h5>
              <p>View, add, and manage user accounts.</p>
          </div>
          <hr />
          <div className="w3-container">
              <h5>Phishing Assessments</h5>
              <p>Configure and review phishing simulation results.</p>
          </div>
          {/* Other sections... */}
      </div>

      {/* Footer */}
      <footer>
          <p>&copy; 2024 Phisecure. All rights reserved.</p>
      </footer>
  </div>
);
};

export default SidebarComponent;
