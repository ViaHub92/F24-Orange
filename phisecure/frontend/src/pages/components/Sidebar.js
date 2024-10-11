import React from 'react';

const Sidebar = () => {
  return (
    <div className="sidebar">
      <h2>Folders</h2>
      <ul>
        <li>Inbox</li>
        <li>Sent</li>
        <li>Drafts</li>
        <li>Spam</li>
      </ul>
    </div>
  );
};

export default Sidebar;