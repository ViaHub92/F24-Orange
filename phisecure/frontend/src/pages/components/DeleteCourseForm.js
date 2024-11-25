import React from 'react';
import axios from 'axios';

const DeleteCourseForm = ({ courseId, courseName, onDeleteSuccess }) => {
  const handleDelete = () => {
    console.log(`Deleting course: ${courseName} (ID: ${courseId})`);
    axios.delete(`/course/delete_course/${courseId}`).then(() => {
     if (onDeleteSuccess) onDeleteSuccess(courseId);
         });
    if (onDeleteSuccess) {
      onDeleteSuccess(courseId);
    }
  };

  return (
    <button onClick={handleDelete} className="w3-button w3-red">
      Delete {courseName}
    </button>
  );
};

export default DeleteCourseForm;
