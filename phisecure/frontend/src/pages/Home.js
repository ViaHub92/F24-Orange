import { Link } from 'react-router-dom';

export default function Home() {
      return (
        <div>
          <meta charSet="UTF-8" />
          <meta name="viewport" content="width=device-width, initial-scale=1.0" />
          <title>Phisecure - Home</title>
          <link rel="stylesheet" href="styles.css" />



        {/* Welcome Section */}
      <main className="hero">
        <div className="hero-content">
          <h2>Welcome to Phisecure</h2>
          <p>
            Learn cybersecurity through interactive lessons and hands-on practice.
          </p>
          <Link to="/CreateAccount" className="cta-button">
            Get Started
          </Link>
        </div>
      </main>


      

 {/* Site Map Section */}
 <section className="section">
        <div className="container">
          <h3>Site Map (For Prototype Demo)</h3>
          <div className="site-map">
            <Link to="/About" className="site-map-card">About</Link>
            <Link to="/Admin" className="site-map-card">Admin</Link>
            <Link to="/Contact" className="site-map-card">Contact</Link>
            <Link to="/CreateAccount" className="site-map-card">Create Account</Link>
            <Link to="/Dashboard" className="site-map-card">Student Dashboard</Link>
            <Link to="/DashboardInstructor" className="site-map-card">Instructor Dashboard</Link>
            <Link to="/Login" className="site-map-card">Login</Link>
            <Link to="/GmailClone" className="site-map-card">Email</Link>
            <Link to="/Services" className="site-map-card">Services</Link>
            <Link to="/ViewQuestionnaire" className="site-map-card">Questionnaire</Link>
          </div>
        </div>
      </section>

     
    </div>
  );
}