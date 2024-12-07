import { Link } from 'react-router-dom';
import  SidebarComponent from './components/Sidebar.js'
import Dashboard from './components/AdminDash.js';

function Admin() {
    return (
      <div>
          <SidebarComponent />
          <Dashboard />
      </div>
    );
  }

  export default Admin
