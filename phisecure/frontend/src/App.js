// Filename - App.js
//https://www.geeksforgeeks.org/how-to-connect-reactjs-with-flask-api/
 
// Importing modules
/*
import React, { useState, useEffect } from "react";
 
function App() {

    const [data, setData] = useState([{}])

    useEffect(() => {
        fetch("/account/list_users").then(
            res => res.json()        
        ).then(
            data => {
                setData(data)
                console.log(data)
            }
        )
    }, [])
    return (
        <div>
            {(typeof data.members === 'undefined') ?  (
                <p>loading...</p>
            ) : (
                data.members.map((member, i) => (
                    <p key={i}>{member}</p>
                ))
            )}

        </div>
    )
}

export default App;
*/
import React, { useState, useEffect } from "react";

function App() {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch("/account/list_users")
      .then(res => res.json())
      .then(data => {
        setData(data);
        console.log(data);
      })
      .catch(error => console.error("Error fetching data: ", error));
  }, []);

  return (
    <div>
      {data.length === 0 ? (
        <p>Loading...</p>
      ) : (
        data.map((user, i) => (
          <div key={i}>
            <p>Username: {user.username}</p>
            <p>Email: {user.email}</p>
            <p>First Name: {user.first_name}</p>
            <p>Last Name: {user.last_name}</p>
          </div>
        ))
      )}
    </div>
  );
}

export default App;