// src/ScrollableList.js
import React from 'react';
import './ScrollableList.css'; // Import the CSS file for styling

const ScrollableList = ({ items }) => {
  return (
    <div className="scrollable-list">
      {items.map((item, index) => (
        <div key={index} className="list-item">
          {item}
        </div>
      ))}
    </div>
  );
};

export default ScrollableList;
