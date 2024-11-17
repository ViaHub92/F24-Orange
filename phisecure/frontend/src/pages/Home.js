import { Link } from 'react-router-dom';

export default function Home() {
      return (
        <div>
          <meta charSet="UTF-8" />
          <meta name="viewport" content="width=device-width, initial-scale=1.0" />
          <title>Phisecure - Home</title>
          <link rel="stylesheet" href="styles.css" />
          <main>
            <section className="section">
              <h2>Welcome to Phisecure</h2>
              <p>Learn cybersecurity through interactive lessons and hands-on practice.</p>
              <h3>Site Map (For Protoype Demo)</h3>
              <span></span>
              <ul>
                <li><Link to='/About'>About</Link></li>
                <li><Link to='/Admin'>Admin</Link></li>
                <li><Link to='/Contact'>Contact</Link></li>
                <li><Link to='/CreateAccount'>Create Account</Link></li>
                <li><Link to='/Dashboard'>Student Dashboard</Link></li>
                <li><Link to='/DashboardInstructor'>Instructor Dashboard</Link></li>
                <li><Link to='/Login'>Login</Link></li>
                <li><Link to='/GmailClone'>Email</Link></li>
                <li><Link to='/Services'>Services</Link></li>
                <li><Link to='/Questionnaire'>Questionnaire</Link></li>                
                      
              </ul>
            </section>
          </main>
          {/* Footer */}
          <footer>
            <p>© 2024 Phisecure. All rights reserved.</p>
          </footer>
        </div>
      );
    }