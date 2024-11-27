import React, { useState, useEffect } from 'react';
import axios from 'axios';

function CreateAccount() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [firstname, setFirstname] = useState('');
  const [lastname, setLastname] = useState('');
  const [email, setEmail] = useState('');
  const [courseId, setCourseId] = useState(''); 
  const [courses, setCourses] = useState([]); 
  const [message, setMessage] = useState('');
  const [accountType, setAccountType] = useState('student'); 

  // Fetch available courses when the component mounts
  useEffect(() => {
    const fetchCourses = async () => {
      try {
        const response = await axios.get('/course/list_courses'); 
        setCourses(response.data);
      } catch (error) {
        console.error('Error fetching courses:', error);
        setCourses([]); 
      }
    };

    if (accountType === 'student') {
      fetchCourses();
    }
  }, [accountType]); // Re-fetch courses if account type changes

  const handleSubmit = async (e) => {
    e.preventDefault();

    const accountData = {
      username,
      password,
      first_name: firstname,
      last_name: lastname,
      email,
      course_id: accountType === 'student' ? courseId : undefined, 
    };

    const endpoint =
      accountType === 'student' ? '/account/create_student' : '/account/create_instructor';

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

            {/* Course Selection (Only for Student) */}
            {accountType === 'student' && (
              <div className="input-group">
                <label htmlFor="course">Select a Course</label>
                <select
                  id="course"
                  value={courseId}
                  onChange={(e) => setCourseId(e.target.value)}
                  required
                >
                  <option value="" disabled>
                    Choose a course
                  </option>
                  {courses.map((course) => (
                    <option key={course.id} value={course.id}>
                      {course.course_name}
                    </option>
                  ))}
                </select>
              </div>
            )}

            <button type="submit" className="login-button">
              Submit
            </button>
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
