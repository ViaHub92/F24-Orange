import React from 'react';

const Sidebar = () => {
  return (
    <div className="sidebar">
      <h2>Folders</h2>
      <ul role="list">
        <li>Inbox</li>
        <li>Sent</li>
        <li>Drafts</li>
      </ul>
    </div>
  );
};

export default Sidebar;