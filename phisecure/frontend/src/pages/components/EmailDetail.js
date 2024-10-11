import React from 'react';

const EmailDetail = ({ email }) => {
  return (
    <div className="email-detail">
      <h2>{email.subject}</h2>
      <p>{email.body}</p>
    </div>
  );
};

export default EmailDetail;
