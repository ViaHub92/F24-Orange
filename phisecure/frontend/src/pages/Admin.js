import React from 'react';
import { Link } from 'react-router-dom';
import SidebarComponent from './components/Sidebar.js';  // Import the Sidebar component
import AdminDash from './components/AdminDash.js';  // Import AdminDash (the main dashboard component)

function OldAdmin() {
  return (
    <div>
      {/* Sidebar Component */}
      <SidebarComponent />

      {/* Admin Dashboard Component */}
      <AdminDash />
    </div>
  );
}

export default OldAdmin;