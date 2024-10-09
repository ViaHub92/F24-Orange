//Mail.js
import React, { useState } from 'react';
import axios from 'axios';
import TestEMail from './email_templates/testemail';

const Mail = () => {
  const [email, setEmail] = useState('');
  const [message, setMessage] = useState('');

  const handleSendEmail = async () => {
    try {
      const response = await axios.post('/api/send-email', { email, template: TestEMail });
      setMessage('Email sent successfully!');
    } catch (error) {
      setMessage('Failed to send email. Please try again.');
    }
  };

  return (
    <div>
      <h2>Send Email</h2>
      <input
        type="email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        placeholder="Enter your email"
      />
      <button onClick={handleSendEmail}>Send Email</button>
      {message && <p>{message}</p>}
    </div>
  );
};

export default Mail;
