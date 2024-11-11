import React from 'react';

const EmailList = ({ emails, onEmailSelect }) => {
  return (
    <div className="email-list">
      <h2>Demo Prototype Emails</h2>
      <ul>
        {emails.map((email) => (
          <li
            key={email.id}
            onClick={() => onEmailSelect(email)}
            style={{ display: 'flex', justifyContent: 'space-between' }} // Flex for inline display
          >
            <span style={{ display: 'inline' }}>{email.subject}</span>
            <span style={{ display: 'inline', marginLeft: '10px' }}>{email.from}</span>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default EmailList;
