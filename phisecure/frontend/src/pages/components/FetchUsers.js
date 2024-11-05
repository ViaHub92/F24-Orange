import React, { useState, useEffect } from "react";

function FetchAllUsers() {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch("/account/list_students")
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
        <p>Waiting...</p>
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

export default FetchAllUsers;
