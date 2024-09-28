import { Chart } from "react-google-charts";

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
        </section>
        </main>
        {/* Footer */}
        <footer>
        <p>© 2024 Phisecure. All rights reserved.</p>
        </footer>
    </div>
  )
}
