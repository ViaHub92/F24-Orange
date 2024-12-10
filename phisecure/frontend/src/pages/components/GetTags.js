import React, { useState, useEffect } from 'react';
import axios from 'axios';

const GetTags = () => {
  const [tags, setTags] = useState([]);
  const [showTags, setShowTags] = useState(false);

  useEffect(() => {
    const fetchTags = async () => {
      try {
        const response = await axios.get('admin_dashboard/get_tags');
        console.log(response.data);
        setTags(response.data);
      } catch (error) {
        console.error('Error fetching tags:', error);
        setTags([]);
      }
    };

    fetchTags();

  }, []);

  return (
    <div>
      <button onClick={() => setShowTags(!showTags)}>
        {showTags ? 'Hide Tags' : 'Show Tags'}
      </button>

      {showTags && (
        <div>
          <h5>Tags:</h5>
          <ul>
            {tags.map((tag, index) => (
              <li key={index}>{tag}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};

export default GetTags;
