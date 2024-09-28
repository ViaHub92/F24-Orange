import { Link } from 'react-router-dom';

export default function Dashboard() {
      return (
        <div>
          <meta charSet="UTF-8" />
          <meta name="viewport" content="width=device-width, initial-scale=1.0" />
          <title>Phisecure- Student Dashboard</title>
          <link rel="stylesheet" href="styles.css" />
          <div className="dashboard">
            {/* Sidebar Navigation */}
            <aside className="sidebar">
              <ul>
              </ul>
            </aside>
            {/* Main Content */}
            <div className="main-content">
              {/* Inbox Section */}
              <section id="inbox" className="section">
                <h2>Inbox</h2>
                <div className="emails">
                  <p>No new emails.</p>
                </div>
              </section>
              {/* Notifications Section */}
              <section id="notifications" className="section hidden">
                <h2>Notifications</h2>
                <div className="notifications">
                  <p>You have no new notifications.</p>
                </div>
              </section>
              {/* Reports Section */}
              <section id="reports" className="section hidden">
                <h2><Link to='/ReportsStudents'>Reports</Link></h2>
                <div className="reports">
                </div>
              </section>
              {/* Peer Phishing */}
              <section id="peerphishing" className="section hidden">
                <h2><Link to='/PeerPhishing'>Peer Phishing</Link></h2>
                <div className="feedback">
                  <p>No feedback available.</p>
                </div>
              </section>
            </div>
          </div>
        </div>
      );
    }