import logo from './phisecurelogo.png';
import { NavLink } from "react-router-dom";

function Header() {
    return (
      <>
      <header>
        <nav className="navbar">
          <div className="logo">
            <img src={logo} alt="Phisecure Logo" className="nav-logo" />
            <h1>Phisecure</h1>
          </div>
          <ul className="nav-links">
            <li><NavLink to="/Home">Home</NavLink></li>
            <li><NavLink to="/About">About</NavLink></li>
            <li><NavLink to="/CreateAccount">Create Account</NavLink></li>
            <li><NavLink to="/Questionnaire">Questionnaire</NavLink></li>
            <li><NavLink to="/Login">Login</NavLink></li>
            <li><NavLink to="/Dashboard">Dashboard</NavLink></li>
            <li><NavLink to="/ReportsStudents">Reports</NavLink></li>
            <li><NavLink to="/Mail">Inbox</NavLink></li>
            
          </ul>
        </nav>
        
        {/* Inline Styling for Header */}
        <style>{`
          header {
            background-color: #231D6C;
            color: white;
            padding: 20px 0;
            text-align: center;
          }
          .logo {
            display: flex;
            align-items: center;
          }
          .logo h1 {
            font-size: 1.5rem;
            margin-left: 10px;
          }
          .nav-logo {
            width: 40px;
            height: 40px;
          }
          .nav-links {
            list-style-type: none;
            display: flex;
            gap: 15px;
          }
          .nav-links li a {
            color: white;
            text-decoration: none;
            font-size: 1rem;
          }
          .nav-links li a:hover {
            text-decoration: underline;
          }
        `}</style>
      </header>
      </>
    )
  };


  export default Header;