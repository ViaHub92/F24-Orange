import { Link } from 'react-router-dom';

function Admin() {
    return (
      <div>
        <main>
          <style dangerouslySetInnerHTML={{__html: "\n    li{margin-bottom: 20px; font-weight: bold;}\n    " }} />
          <div className="container">
            <p style={{textAlign: 'center', fontWeight: 'bold'}}>Hello Admin [INSERT NAME HERE]</p>
            <ul style={{textAlign: 'center', listStyle: 'none'}}>
              <li><Link to='/UserManagement'>User Management</Link></li> 
              <li><Link to='/PhishingAssesment'>Phishing Assessment</Link></li>
              <li><Link to='/Dataanalytics'>Data Analytics</Link></li>
              <li><Link to='/SystemAnalytics'>System Analytics</Link></li>
            </ul>
          </div>
        </main>
        {/* Footer */}
        <footer>
          <p>© 2024 Phisecure. All rights reserved.</p>
        </footer>
      </div>
    );
  }

  export default Admin