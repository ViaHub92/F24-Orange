import React, { useState, useEffect } from 'react';
import axios from 'axios';

const AdminStudentComparison = () => {
  const [studentComparisonData, setStudentComparisonData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null); // To capture any error in fetching data

  const fetchStudentComparisonReport = async () => {
    try {
      const response = await axios.get('/admin_dashboard/student_comparison_report');
      if (response.data) {
        setStudentComparisonData(response.data);
      }
    } catch (error) {
      console.error('Error fetching student comparison report:', error);
      setError('Failed to load comparison data. Please try again later.');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchStudentComparisonReport();
  }, []);

  if (loading) return <div>Loading...</div>;

  return (
    <div>
      <h5>Student Comparison Report</h5>
      {error && <div style={{ color: 'red' }}>{error}</div>}
      {studentComparisonData ? (
        <ul>
          {Object.entries(studentComparisonData).map(([tag, percentage]) => (
            <li key={tag}>
              <strong>{tag}:</strong> {percentage}%
            </li>
          ))}
        </ul>
      ) : (
        <p>No data available</p>
      )}
    </div>
  );
};

export default AdminStudentComparison;
