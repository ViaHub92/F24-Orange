//Mail.js
import React, { useState } from 'react';
import EmailList from './components/EmailList';
import FetchInbox from './components/FetchInbox';
import EmailDetailsByIndex from './components/FetchFirstInbox';


function Mail() {
  const [selectedEmail, setSelectedEmail] = useState(null);
  const emailIndex = 0;

  const emails = [
    { id: 1, subject: '1st', body: 'Placeholder', from: <EmailDetailsByIndex emailIndex={emailIndex} /> },
    { id: 2, subject: '2nd', body: 'Placeholder' },
    { id: 3, subject: '3rd', body: 'Placeholder' },
  ];

  const handleEmailSelect = (email) => {
    setSelectedEmail(email);
  };

  return (
    <div className="app">
      <EmailList emails={emails} onEmailSelect={handleEmailSelect} />
      {selectedEmail && <EmailDetailsByIndex emailIndex={emailIndex} email={selectedEmail} />}
  
    </div>
  );
};

export default Mail;
