import React, { useState } from 'react';

function CreateAccount() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [firstname, setFirstname] = useState('');
  const [lastname, setLastname] = useState('');
  const [email, setEmail] = useState('');
  const [message, setMessage] = useState('');
  const [accountType, setAccountType] = useState('student'); // Default to 'student'

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    const accountData = {
      username,
      password,
      first_name: firstname,
      last_name: lastname,
      email,
    };

    const endpoint = accountType === 'student' ? '/account/create_student' : '/account/create_instructor';

    try {
      const response = await fetch(endpoint, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(accountData),
      });

      const result = await response.json();
      if (response.ok) {
        setMessage(result.message);
      } else {
        setMessage(result.message || 'Error creating account');
      }
    } catch (error) {
      setMessage('Error creating user');
    }
  };

  return (
    <div className="create-account-page">
      <meta charSet="UTF-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      <title>Phisecure - Create Account</title>
      <link rel="stylesheet" href="styles.css" />

      <main>
        <section className="section-create">
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
            
            {/* Account Type Selection */}
            <div className="input-group">
              <label>Account Type</label>
              <div>
                <label>
                  <input
                    type="radio"
                    value="student"
                    checked={accountType === 'student'}
                    onChange={() => setAccountType('student')}
                  />
                  Student
                </label>
                <label>
                  <input
                    type="radio"
                    value="instructor"
                    checked={accountType === 'instructor'}
                    onChange={() => setAccountType('instructor')}
                  />
                  Instructor
                </label>
              </div>
            </div>

            <button type="submit" className="login-button">Submit</button>
          </form>
          {message && <p>{message}</p>}
        </section>
      </main>

      <footer>
        <p>© 2024 Phisecure. All rights reserved.</p>
      </footer>
    </div>
  );
}

export default CreateAccount;
