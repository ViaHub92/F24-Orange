import React, { useState } from 'react';
import axios from 'axios';
import DeleteCourseForm from './DeleteCourseForm';

const GetTags = () => {
  const [tags, setMajors] = useState([]);
  const [showMajors, setShowMajors] = useState(false);

  const fetchTags = async () => {
    if (showMajors) {
      setShowMajors(false);
    } else {
      try {
        const response = await axios.get('admin_dashboard/get_majors');
        setMajors(response.data);
        setShowMajors(true);
      } catch (error) {
        console.error('Error fetching majors:', error);
        setMajors([]);
        setShowMajors(false);
      }
    }
  };
};

export default GetTags;