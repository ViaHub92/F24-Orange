import React from 'react';
import {Link, useNavigate } from 'react-router-dom';

const Logout = () => {
  const navigate = useNavigate();

  const handleLogout = async () => {
    try {
      const response = await fetch('/account/logout', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
      });

      if (response.ok) {
        localStorage.clear(); // Clear local storage
        navigate('/login'); // Redirect to the login page
      } else {
        console.error('Logout failed');
      }
    } catch (err) {
      console.error('Logout failed:', err);
    }
  };

  return (
    <Link to="/login" className="w3-bar-item w3-button w3-padding" onClick={handleLogout}>
      <i className="fa fa-sign-out"></i> Logout
    </Link>
  );
};

export default Logout;