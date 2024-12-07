import React, { useState } from 'react';
import axios from 'axios';
import DeleteCourseForm from './DeleteCourseForm';

const GetTags = () => {
  const [tags, setTags] = useState([]);
  const [showTags, setShowTags] = useState(false);

  const fetchTags = async () => {
    if (showTags) {
      setShowTags(false);
    } else {
      try {
        const response = await axios.get('admin_dashboard/get_tags');
        setTags(response.data);
        setShowTags(true);
      } catch (error) {
        console.error('Error fetching tags:', error);
        setTags([]);
        setShowTags(false);
      }
    }
  };
};

export default GetTags;