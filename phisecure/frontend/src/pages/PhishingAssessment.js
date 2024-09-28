import { Link } from 'react-router-dom';

export default function PhishingAssessment() {
      return (
        <div>
          <meta charSet="UTF-8" />
          <meta name="viewport" content="width=device-width, initial-scale=1.0" />
          <title>Phisecure - About</title>
          <link rel="stylesheet" href="styles.css" />
          <style dangerouslySetInnerHTML={{__html: "\n    " }} />
          <main>
            <style dangerouslySetInnerHTML={{__html: "\n    li{margin-bottom: 20px; font-weight: bold;}\n    " }} />
            <div className="container">
              <p style={{textAlign: 'center', fontWeight: 'bold'}}>Hello Admin [INSERT NAME HERE]</p>
              <p style={{textAlign: 'center', fontWeight: 'bold'}}><Link to='/Admin'>Return to Admin Home</Link></p>
            </div>
          </main>
          {/* Footer */}
          <footer>
            <p>© 2024 Phisecure. All rights reserved.</p>
          </footer>
        </div>
      );
    }
