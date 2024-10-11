import React from 'react';

const EmailList = ({ emails, onEmailSelect }) => {
  return (
    <div className="email-list">
      <h2>Emails</h2>
      <ul>
        {emails.map((email) => (
          <li key={email.id} onClick={() => onEmailSelect(email)}>
            {email.subject}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default EmailList;
