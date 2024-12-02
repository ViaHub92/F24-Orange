import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

function Login() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch('/account/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, password }),
      });

      const data = await response.json();
      if (response.ok) {
        localStorage.setItem('user_id', data.user_id);
        localStorage.setItem('role', data.role);

        if (data.role === 'Student') {
          localStorage.setItem('student_id', data.user_id);
          navigate('/Dashboard');
        } else if (data.role === 'Instructor') {
          localStorage.setItem('instructor_id', data.user_id);
          navigate('/DashboardInstructor');
        }
      } else {
        setError(data.message || 'Invalid login credentials');
      }
    } catch (err) {
      console.error('Login failed:', err);
      setError('An error occurred. Please try again.');
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
          <h2>Login</h2>
          {error && <p style={{ color: 'red' }}>{error}</p>}
          <form onSubmit={handleLogin}>
            <div className="input-group">
              <label htmlFor="username">Username</label>
              <input
                type="text"
                id="username"
                name="username"
                required
                value={username}
                onChange={(e) => setUsername(e.target.value)}
              />
            </div>
            <div className="input-group">
              <label htmlFor="password">Password</label>
              <input
                type="password"
                id="password"
                name="password"
                required
                value={password}
                onChange={(e) => setPassword(e.target.value)}
              />
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
