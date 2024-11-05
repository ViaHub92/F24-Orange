import React, { useState } from 'react';

function CreateQuestionnaire() {
  const [name, setName] = useState('');
  const [description, setDescription] = useState('');
  const [error, setError] = useState('');
  const [success, setSuccess] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setSuccess('');
    
    const questionnaireData = {
      name,
      description
    };

    try {
      const response = await fetch('http://localhost:5000/questionnaire', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(questionnaireData)
      });

      if (response.ok) {
        const data = await response.json();
        setSuccess('Questionnaire created successfully!');
        console.log(data);
      } else {
        setError('Error creating questionnaire');
      }
    } catch (err) {
      setError('Error creating questionnaire');
      console.error(err);
    }
  };

  return (
    <div>
      <h2>Create a New Questionnaire</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Name:</label>
          <input
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
            required
          />
        </div>
        <div>
          <label>Description:</label>
          <input
            type="text"
            value={description}
            onChange={(e) => setDescription(e.target.value)}
          />
        </div>
        <button type="submit">Create Questionnaire</button>
      </form>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      {success && <p style={{ color: 'green' }}>{success}</p>}
    </div>
  );
}

export default CreateQuestionnaire;
