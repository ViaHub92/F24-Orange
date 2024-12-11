import React, { useState, useEffect } from 'react';
import axios from 'axios';

const AdminPhishingTemplates = () => {
  const [templates, setTemplates] = useState([]);
  const [loading, setLoading] = useState(true);
  const [selectedTemplate, setSelectedTemplate] = useState(null);

  const fetchPhishingTemplates = async () => {
    try {
      const response = await axios.get('/admin_dashboard/get_phishing_templates');
      setTemplates(response.data);
      console.log('Fetched templates:', response.data); // Log fetched templates
    } catch (error) {
      console.error('Error fetching phishing templates:', error);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchPhishingTemplates();
  }, []);

  if (loading) return <div>Loading...</div>;

  const handleSelectChange = (e) => {
    const selectedId = e.target.value;
    console.log("Selected ID:", selectedId); // Log the selected ID

    // Convert selectedId to a number before comparing
    const template = templates.find((t) => t.id === Number(selectedId)); 
    console.log("Template found:", template); // Log the found template

    setSelectedTemplate(template);
  };

  return (
    <div>

      {/* Dropdown to select phishing template */}
      <select onChange={handleSelectChange} defaultValue="">
        <option value="" disabled>Select a template</option>
        {templates.map((template) => (
          <option key={template.id} value={template.id}>
            {template.name}
          </option>
        ))}
      </select>

      {/* Display template details if one is selected */}
      {selectedTemplate ? (
        <div>
          <h6>Template Details:</h6>
          <p><strong>Category:</strong> {selectedTemplate.category}</p>
          <p><strong>Difficulty Level:</strong> {selectedTemplate["difficulty level"]}</p>
          <p><strong>Sender Template:</strong> {selectedTemplate["sender template"]}</p>
          <p><strong>Subject Template:</strong> {selectedTemplate["subject template"]}</p>
          <p><strong>Body Template:</strong> {selectedTemplate["body template"]}</p>
          <p><strong>Link:</strong> {selectedTemplate.link}</p>
          <p><strong>Red Flags:</strong> {selectedTemplate["red flag(s)"]}</p>
        </div>
      ) : (
        <p>Select a template to see details.</p>
      )}
    </div>
  );
};

export default AdminPhishingTemplates;
