//Mail.js
import React, { useState } from 'react';
import EmailList from './components/EmailList';
import FetchInbox from './components/FetchInbox';


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

      <EmailList emails={emails} onEmailSelect={handleEmailSelect} />
      {selectedEmail && <FetchInbox email={selectedEmail} />}
  
    </div>
  );
};

export default Mail;
