//Mail.js
import React, { useState } from 'react';
import EmailList from './components/EmailList';
import Inbox from './components/FetchFirstInbox';
import FetchSubject from './components/FetchSubject';
import FetchID from './components/FetchID';
import MarkPhish from './components/MarkPhish';


function Mail() {
  const [selectedEmail, setSelectedEmail] = useState(null);

  const emails = [
    { id: 4, subject: <FetchSubject />, body: <Mail /> },
    { id: 2, subject: 'Follow Up Question', body: 'Placeholder' },
    { id: 3, subject: 'Free Money', body: 'Placeholder' },
  ];

  const handleEmailSelect = (email) => {
    setSelectedEmail(email);
  };

  return (
    <div className="app">
      {/* Email List Component, passing the emails array and handler for selection */}
      <EmailList emails={emails} onEmailSelect={handleEmailSelect} />
      
      {/* If an email is selected, show the Inbox or other components */}
      {selectedEmail && (
        <div>
          <h2>Email Details</h2>
          <h3>Subject: {selectedEmail.subject}</h3>
          <p>Body: {selectedEmail.body}</p>

          {/* Fetch additional email info or actions (like MarkPhish) */}
          <FetchID emailId={selectedEmail.id} />
          <MarkPhish emailId={selectedEmail.id} />
        </div>
      )}
    </div>
  );
}

export default Mail;
