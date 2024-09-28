function CreateAccount() {
    return (
    <div>
        <meta charSet="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
          <title>Phisecure - Login</title>
          <link rel="stylesheet" href="styles.css" />
          {/* Main Content */}
          <main>
            <section className="section">
              <h2>Create Account</h2>
              <form action="login.php" method="post">
                <div className="input-group">
                  <label htmlFor="username">Username</label>
                  <input type="text" id="username" name="username" required />
                </div>
                <div className="input-group">
                  <label htmlFor="password">Password</label>
                  <input type="password" id="password" name="password" required />
                </div>
                <div className="input-group">
                  <label htmlFor="firstname">First Name</label>
                  <input type="firstname" id="firstname" name="firstname" required />
                </div>
                <div className="input-group">
                  <label htmlFor="lastname">Last Name</label>
                  <input type="lastname" id="lastname" name="lastname" required />
                </div>
                <div className="input-group">
                  <label htmlFor="email">Email</label>
                  <input type="email" id="email" name="email" required />
                </div>                
                <button type="submit" className="login-button">Submit</button>
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

    export default CreateAccount;