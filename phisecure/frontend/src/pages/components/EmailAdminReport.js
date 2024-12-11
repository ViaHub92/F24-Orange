import React, { useState, useEffect } from 'react';
import axios from 'axios';

const EmailAdminReport = () => {
  const [emailReport, setEmailReport] = useState(null);
  const [loading, setLoading] = useState(true);

  const fetchEmailReport = async () => {
    try {
      const response = await axios.get('/admin_dashboard/email_total_report');
      setEmailReport(response.data);
    } catch (error) {
      console.error('Error fetching email report:', error);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchEmailReport();
  }, []);

  if (loading) return <div>Loading...</div>;

  return (
    <div>
      
      <p>Total Emails Sent: {emailReport["Total Emails"]}</p>

    </div>
  );
};

export default EmailAdminReport;
