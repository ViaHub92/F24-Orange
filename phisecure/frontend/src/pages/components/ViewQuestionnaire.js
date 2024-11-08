import React, { useState, useEffect } from "react";



const ViewQuestionnaire = () => { 
    const [data, setData] = useState([]);

    useEffect(() => {
        fetch("/questionnaire/2")
          .then(res => res.json())
          .then(data => {
            setData(data);
            console.log(data);
          })
          .catch(error => console.error("Error fetching data: ", error));
      }, []);
 
      return (
        <div>
          <h1>{data.name}</h1>
          <p>{data.description}</p>
          {data.questions && data.questions.length > 0 ? (
            data.questions.map((question, i) => (
              <div key={i}>
                <p>Question: {question.question_text}</p>
                {question.options && question.options.length > 0 && (
                  <ul>
                  {question.options.map((option, j) => (
                    <li key={j}>
                      <label>
                        <input
                          type="radio"
                          name={`question-${i}`}
                          value={option.option_text}
                        />
                        {option.option_text}
                      </label>
                    </li>
                  ))}
                </ul>
              )}
            </div>
          ))
        ) : (
          <p>No questions available</p>
        )}
      </div>
    );
    
}
    export default ViewQuestionnaire;