import logo from './phisecurelogo.png';
import { NavLink } from "react-router-dom";

function Header() {
    return (
      <>
      <header>
        <nav className="nav">
          <img src={logo} alt={"logo"} className="nav-logo" />
          <ul className="nav-items">
            <li>
              <NavLink to="/Home">Home</NavLink>
            </li>
            <li>
              <NavLink to="/Contact">Contact</NavLink>
            </li>
            <li>
              <NavLink to="/Login">Login</NavLink>
            </li>
          </ul>
        </nav>
      </header>
      </>
    )
  };

  export default Header;