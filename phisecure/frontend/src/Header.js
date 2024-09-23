import logo from './phisecurelogo.png';

function Header() {
    return (
      <header>
        <nav className="nav">
          <img src={logo} alt={"logo"} className="nav-logo" />
          <ul className="nav-items">
            <li>Home</li>
            <li>About</li>
            <li>Services</li>
            <li>Contact</li>
            <li>Login</li>
            <li>Dashboard</li>
          </ul>
        </nav>
      </header>
    )
  };

  export default Header;