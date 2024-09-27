function Login() {
    return (
    <div>
        <meta charSet="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
          <title>Phisecure - Login</title>
          <link rel="stylesheet" href="styles.css" />
          {/* Main Content */}
          <main>
            <section className="section">
              <h2>Login</h2>
              <form action="login.php" method="post">
                <div className="input-group">
                  <label htmlFor="username">Username</label>
                  <input type="text" id="username" name="username" required />
                </div>
                <div className="input-group">
                  <label htmlFor="password">Password</label>
                  <input type="password" id="password" name="password" required />
                </div>
                <button type="submit" className="login-button">Login</button>
              </form>
            </section>
          </main>
          {/* Footer */}
          <footer>
            <p>© 2024 Phisecure. All rights reserved.</p>
          </footer>
        </div>
      );
    }

    export default Login;