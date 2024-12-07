import { Chart } from "react-google-charts";
import React, { useState } from 'react';

export const data = [
  ["Name", "Class ID", "Approved"],
  ["Barnes, Ethan", { v: 54631, f: "54631" }, true],
  ["Engaro, Meat", { v: 8000, f: "8000" }, false],
  ["Milhouse, Tricky", { v: 54631, f: "54631" }, true],
  ["Wrong, Hany", { v: 54631, f: "54631" }, true],
];

export const options = {
  title: "Peer Phishing",
  curveType: "function",
  legend: { position: "bottom" },
  pageSize: 5,
};

function DropdownMenu() {
  const [isOpen, setIsOpen] = useState(false);

  const toggleDropdown = () => {
    setIsOpen(!isOpen);
  };

  return (
    <div>
      <button onClick={toggleDropdown} className="dropdown-button">
        Select Option
      </button>

      {isOpen && (
        <ul className="dropdown-menu">
          <li className="dropdown-item">Option 1</li>
          <li className="dropdown-item">Option 2</li>
          <li className="dropdown-item">Option 3</li>
        </ul>
      )}
    </div>
  );
}

export function PeerPhishing() {
  return (
    <div>
        <meta charSet="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Phisecure - Contact</title>
        <link rel="stylesheet" href="styles.css" />
        {/* Main Content */}
        <main>
        <section className="section">
            <h2>Peer-to-Peer Phishing</h2>
            <Chart
            chartType="Table"
            width="100%"
            height="400px"
            data={data}
            options={options}
            />
            <input type="submit" value="Select"></input>
        </section>
        </main>
        {/* Footer */}
        <footer>
        <p>© 2024 Phisecure. All rights reserved.</p>
        </footer>
    </div>
  )
}
