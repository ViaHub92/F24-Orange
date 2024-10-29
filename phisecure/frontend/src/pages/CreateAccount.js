import React, { useState } from 'react';

function CreateAccount() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [firstname, setFirstname] = useState('');
  const [lastname, setLastname] = useState('');
  const [email, setEmail] = useState('');
  const [message, setMessage] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
        const response = await fetch('/account/create_student', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ username, password, firstname, lastname, email }),
        });

        if (response.ok) {
            const result = await response.json();
            setMessage(result.message);
        } else {
            const errorResult = await response.json();
            setMessage(errorResult.error);
        }
    } catch (error) {
        setMessage('Error creating user');
    }
};

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
              <form onSubmit={handleSubmit}>
                <div className="input-group">
                <label htmlFor="username">Username</label>
                  <input
                    type="text"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                    required
                  />
                </div>
                <div className="input-group">
                <label htmlFor="password">Password</label>
                  <input
                    type="password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    required
                  />
                </div>
                <div className="input-group">
                <label htmlFor="firstname">First Name</label>
                  <input
                    type="text"
                    value={firstname}
                    onChange={(e) => setFirstname(e.target.value)}
                    required
                  />
                </div>
                <div className="input-group">
                <label htmlFor="lastname">Last Name</label>
                  <input
                    type="text"
                    value={lastname}
                    onChange={(e) => setLastname(e.target.value)}
                    required
                  />
                </div>
                <div className="input-group">
                <label htmlFor="email">Email</label>
                  <input
                    type="email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    required
                  />
                </div>                
                <button type="submit" className="login-button">Submit</button>
              </form>
              {message && <p>{message}</p>}
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