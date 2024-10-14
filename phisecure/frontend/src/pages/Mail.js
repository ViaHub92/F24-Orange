//Mail.js
import React, { useState } from 'react';
import axios from 'axios';
import TestEMail from './email_templates/testemail';
import Sidebar from './components/Sidebar';
import EmailList from './components/EmailList';
import EmailDetail from './components/EmailDetail';


function Mail() {
  const [selectedEmail, setSelectedEmail] = useState(null);

  const emails = [
    { id: 1, subject: 'Not Spam', body: 'Placeholder' },
    { id: 2, subject: 'Phisecure', body: 'Placeholder' },
    { id: 3, subject: 'Not Spam', body: 'Placeholder' },
  ];

  const handleEmailSelect = (email) => {
    setSelectedEmail(email);
  };

  return (
    <div className="app">

      <Sidebar />  
      <EmailList emails={emails} onEmailSelect={handleEmailSelect} />
      {selectedEmail && <EmailDetail email={selectedEmail} />}
  
    </div>
  );
};

export default Mail;
