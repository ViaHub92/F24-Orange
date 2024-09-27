export default function Home() {
      return (
        <div>
          <meta charSet="UTF-8" />
          <meta name="viewport" content="width=device-width, initial-scale=1.0" />
          <title>Phisecure - Home</title>
          <link rel="stylesheet" href="styles.css" />
          {/* Navigation Bar */}
          <header>
            <nav className="navbar">
              <div className="logo">
                <h1>Phisecure</h1>
              </div>
              <ul className="nav-links">
                <li><a href="home.html">Home</a></li>
                <li><a href="about.html">About</a></li>
                <li><a href="services.html">Services</a></li>
                <li><a href="contact.html">Contact</a></li>
                <li><a href="login.html">Login</a></li>
                <li><a href="dashboard.html">Dashboard</a></li>
              </ul>
            </nav>
          </header>
          {/* Main Content */}
          <main>
            <section className="section">
              <h2>Welcome to Phisecure</h2>
              <p>Learn cybersecurity through interactive lessons and hands-on practice.</p>
            </section>
          </main>
          {/* Footer */}
          <footer>
            <p>© 2024 Phisecure. All rights reserved.</p>
          </footer>
        </div>
      );
    }